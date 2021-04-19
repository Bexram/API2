from docxtpl import DocxTemplate
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
import users, clients, tasks
import datetime
from rest_framework.response import Response
import os
import subprocess
from PyPDF2 import PdfFileMerger

def getQuarterStart(dt=datetime.date.today()):
    return datetime.date(dt.year, (dt.month - 1) // 3 * 3 + 1, 1)


def getQuarterEnd(dt=datetime.date.today()):
    nextQtYr = dt.year + (1 if dt.month > 9 else 0)
    nextQtFirstMo = (dt.month - 1) // 3 * 3 + 4
    nextQtFirstMo = 1 if nextQtFirstMo == 13 else nextQtFirstMo
    nextQtFirstDy = datetime.date(nextQtYr, nextQtFirstMo, 1)
    return nextQtFirstDy - datetime.timedelta(days=1)


class RepList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.QReport.objects.all()
    serializer_class = serializers.ReportSerializer

class RepDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.QReport.objects.all()
    serializer_class = serializers.ReportSerializer

class GetRepList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,format=None):
        queryset = models.QReport.objects.all()
        serializer_class = serializers.ReportSerializer
        return Response(serializer.data)

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None



#работа с сформированными отчетами
class GetReadyRepList(APIView):
    permission_classes = [IsAuthenticated]
    def get(request, self, format=None):
        queryset = models.ReadyReport.objects.all()
        serializer = serializers.GetReportSerializer(queryset, many=True)
        return Response(serializer.data)

class ReadyRepDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.ReadyReport.objects.all()
    serializer_class = serializers.ReportSerializer

class PrintReadyRep(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format=None):
        path = './files/media/generated_doc.docx'
        output = "./files/media/output.pdf"
        data = models.ReadyReport.objects.get(id=pk)
        new = models.ReadyReport(
            clientobj=data.clientobj,
            contact_man=data.contact_man,
            userprof=data.userprof,
            name=data.name,
            works=data.works,
            project=data.project,
            dateproj=data.dateproj,
            results=data.results,
        )
        new.save()
        ConstructDoc(data, path, output)
        return Response('/media/output.pdf')


def ConstructDoc(data,docpath,pdfpath):
    doc = DocxTemplate(os.path.abspath('reports/template.docx'))
    context = {'works': data.works,
               'object': data.clientobj.object_name,
               'adress': data.clientobj.object_adress,
               'start': getQuarterStart(data.rep_published).strftime("%d.%m.%Y"),
               'end': getQuarterEnd(data.rep_published).strftime("%d.%m.%Y"),
               'pos': data.userprof.position,
               'fio': data.userprof.last_name + ' ' + data.userprof.first_name[
                                                      :1] + '. ' + data.userprof.thirdname[:1] + '. ',
               'company_pos': data.contact_man.position,
               'company_fio': data.contact_man.FIO,
               'results': data.results
               }
    doc.render(context)
    doc.save(docpath)
    env = os.environ.copy()
    env['HOME'] = '/tmp'

    p = subprocess.Popen(["unoconv", "-f", "pdf", "-o", pdfpath,
                          docpath], env=env)
    out, err = p.communicate()

def merger(files,output):
    merger = PdfFileMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write(output)
    merger.close()



class GenerateReport(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        data = models.QReport.objects.filter(auto_generate=True)
        docpath='./files/media/generated_doc.docx'
        output="./files/media/output.pdf"
        for report in enumerate(data):
            new=models.ReadyReport(
                clientobj=report[1].clientobj,
                contact_man=report[1].contact_man,
                userprof=report[1].userprof,
                name=report[1].name,
                works=report[1].works,
                project=report[1].project,
                dateproj=report[1].dateproj,
                results=report[1].results,
                            )
            new.save()
            ConstructDoc(report[1],docpath,'./files/media/file'+str(report[0])+'.pdf')
        if data.count() > 1:
            pdfFiles = []
            for filename in os.listdir('./files/media'):
                if filename.endswith('.pdf'):
                    pdfFiles.append('./files/media/'+filename)
            merger(pdfFiles,output)
            for file in pdfFiles:
                os.remove(file)
            return Response('/media/output.pdf')
        if data.count() == 1:
            return Response('/media/file0.pdf')
        if data.count() == 0:
            return Response('null')

class GenerateOneReport(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format=None):
        path='./files/media/generated_doc.docx'
        output="./files/media/output.pdf"
        data = models.QReport.objects.get(id=pk)
        new=models.ReadyReport(
                clientobj=data.clientobj,
                contact_man=data.contact_man,
                userprof=data.userprof,
                name=data.name,
                works=data.works,
                project=data.project,
                dateproj=data.dateproj,
                results=data.results,
                            )
        new.save()
        ConstructDoc(data,path,output)
        return Response('/media/output.pdf')
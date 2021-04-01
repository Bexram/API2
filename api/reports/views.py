from docxtpl import DocxTemplate
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
import users, clients, tasks, api
import datetime
from docxcompose.composer import Composer
from docx import Document as Document_compose
from django.http import FileResponse
import os
import subprocess


def getQuarterStart(dt=datetime.date.today()):
    return datetime.date(dt.year, (dt.month - 1) // 3 * 3 + 1, 1)


def getQuarterEnd(dt=datetime.date.today()):
    nextQtYr = dt.year + (1 if dt.month > 9 else 0)
    nextQtFirstMo = (dt.month - 1) // 3 * 3 + 4
    nextQtFirstMo = 1 if nextQtFirstMo == 13 else nextQtFirstMo
    nextQtFirstDy = datetime.date(nextQtYr, nextQtFirstMo, 1)
    return nextQtFirstDy - datetime.timedelta(days=1)


class RepList(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.QReport.objects.all()
    serializer_class = serializers.ReportSerializer


class RepDetailList(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.QReport.objects.all()
    serializer_class = serializers.ReportSerializer


def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    p._p = p._element = None

class GetRepList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(request, self, format=None):
        queryset = models.QReport.objects.all()
        serializer = serializers.GetReportSerializer(queryset, many=True)
        return Response(serializer.data)

def ConstructDoc(data,name):
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
    doc.save(name)

class GenerateReport(APIView):
    def get(self, request, format=None):
        data = models.QReport.objects.filter(auto_generate=True)
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
            if report[0] == 0:
                ConstructDoc(report[1],'generated_doc.docx')
            else:
                ConstructDoc(report[1],'generated_doc1.docx')
                master = Document_compose("generated_doc.docx")
                composer = Composer(master)
                # filename_second_docx is the name of the second docx file
                doc2 = Document_compose("generated_doc1.docx")
                # append the doc2 into the master using composer.append function
                composer.append(doc2)
                # Save the combined docx with a name
                composer.save("generated_doc.docx")

        short_report = open("generated_doc.docx", 'rb')
        return FileResponse(short_report)
        # response = HttpResponse(FileWrapper(short_report), content_type='application/msword')
        # response['Content-Disposition'] = 'attachment; filename= "reports.docx"'
        # return response

class GenerateOneReport(APIView):
    def get(self, request, pk, format=None):
        path='./files/media/generated_doc.docx'
        output="./files/media/report.pdf"
        data = models.QReport.objects.get(id=pk)
        print(data)
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
        ConstructDoc(data,path)
        # a_url = "https://s3.pdfconvertonline.com:443/convert/p9.php"
        # a_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
        #              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        #              "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate",
        #              "Content-Type": "multipart/form-data; boundary=---------------------------326089013215643646281334313309",
        #              "Origin": "https://www.pdfconvertonline.com", "DNT": "1", "Connection": "close",
        #              "Referer": "https://www.pdfconvertonline.com/docx-to-pdf-online.html",
        #              "Upgrade-Insecure-Requests": "1"}
        #
        # file = open(path, "rb")
        #
        # Input_file = file.read()
        # a = Input_file.decode('latin-1').encode("utf-8")
        # l = str(a, 'UTF-8')
        # a_data = "-----------------------------326089013215643646281334313309\r\nContent-Disposition: form-data; name=\"localfile\"; filename=\"generated_doc.docx\"\r\nContent-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document\r\n\r\n" + l + "\r\n-----------------------------326089013215643646281334313309\r\nContent-Disposition: form-data; name=\"filetype\"\r\n\r\nPDF\r\n-----------------------------326089013215643646281334313309\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n1\r\n-----------------------------326089013215643646281334313309\r\nContent-Disposition: form-data; name=\"source\"\r\n\r\nWEENYSOFT\r\n-----------------------------326089013215643646281334313309\r\nContent-Disposition: form-data; name=\"cengine\"\r\n\r\n2\r\n-----------------------------326089013215643646281334313309--\r\n"
        # r = requests.post(a_url, headers=a_headers, data=a_data)
        # result = re.search("value.*.pdf", r.text)
        env = os.environ.copy()
        env['HOME'] = '/tmp'

        #p = subprocess.Popen(["unoconv", "-f", "pdf", "-o",output,
        #                      path], env=env)
        #out, err = p.communicate()

        return FileResponse(open(output, 'rb'))
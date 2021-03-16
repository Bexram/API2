from wsgiref.util import FileWrapper
from django.http import HttpResponse
import os
from docxtpl import DocxTemplate
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models,serializers
import users,clients,tasks
import datetime

def getQuarterStart(dt=datetime.date.today()):
    return datetime.date(dt.year, (dt.month - 1) // 3 * 3 + 1, 1)

def getQuarterEnd(dt=datetime.date.today()):
    nextQtYr = dt.year + (1 if dt.month>9 else 0)
    nextQtFirstMo = (dt.month - 1) // 3 * 3 + 4
    nextQtFirstMo = 1 if nextQtFirstMo==13 else nextQtFirstMo
    nextQtFirstDy = datetime.date(nextQtYr, nextQtFirstMo, 1)
    return nextQtFirstDy - datetime.timedelta(days=1)

class RepList(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = models.QReport.objects.all()
    serializer_class = serializers.ReportSerializer


class RepDetailList(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = [IsAuthenticated]
    queryset = models.QReport.objects.all()
    serializer_class = serializers.ReportSerializer

class GetRepList(APIView):
   # permission_classes = [IsAuthenticated]
    def get(request, self, format=None):
        queryset = models.QReport.objects.all()
        serializer = serializers.GetReportSerializer(queryset, many=True)
        return Response(serializer.data)

class GenerateReport(APIView):
    def get(self,request,pk,format=None):
        data = models.QReport.objects.get(id=pk)
        doc = DocxTemplate(os.path.abspath('reports/template.docx'))
        context = {'works': data.works,
                   'object': data.clientobj.object_name,
                   'adress': data.clientobj.object_adress,
                   'start': getQuarterStart(data.rep_published).strftime("%d.%m.%Y"),
                   'end': getQuarterEnd(data.rep_published).strftime("%d.%m.%Y"),
                   'pos': data.userprof.position,
                   'fio': data.userprof.last_name + ' ' + data.userprof.first_name[:1] + '. ' + data.userprof.thirdname[:1] + '. ',
                   'company_pos': data.contact_man.position,
                   'company_fio': data.contact_man.FIO,
                   'results': data.results
                   }
        doc.render(context)
        doc.save("generated_doc.docx")
        short_report = open("generated_doc.docx", 'rb')
        response = HttpResponse(FileWrapper(short_report), content_type='application/docx')
        return response
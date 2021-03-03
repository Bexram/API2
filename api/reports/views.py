from django.shortcuts import render
import os
from docxtpl import DocxTemplate
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models,serializers
import users,clients,tasks

def createrep(data):
            # empl=users.models.UserProfile.objects.get(id=request.data.__getitem__('employer'))
            # cl=clients.models.clients.objects.get(id=request.data.__getitem__('client'))
            # obj = clients.models.clientobj.objects.get(id=request.data.__getitem__('object'))
            # contact = clients.models.contact_man.objects.get(id=request.data.__getitem__('contact'))
            # contracts=clients.models.object_contracts.objects.filter(clientobj=obj)
            # works=[]
            # worksstr=''
            # for el in contracts:
            #     works=tasks.models.Task.objects.filter(contract=el).filter(task_compl__range=[request.data.__getitem__('start'),request.data.__getitem__('end')])
            #     for task in works:
            #         worksstr=worksstr+', '+task.Task_name
            # worksstr=worksstr[2:]

            doc = DocxTemplate(os.path.abspath('reports/template.docx'))
            context = {'works': data.works,
                       'object':data.object_name,
                       'adress':data.object_adress,
                       'start':data.__getitem__('start'),
                       'end':data.__getitem__('end'),
                       'pos':data.position,
                       'fio':data.last_name+' '+data.first_name[:1]+'. '+data.thirdname[:1]+'. ',
                       'company_pos':data.contact_position,
                       'company_fio':data.FIO,
                       }
            doc.render(context)
            doc.save("generated_doc.docx")
            return Response(status=status.HTTP_201_CREATED)

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

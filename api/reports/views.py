from django.shortcuts import render
import os
from docxtpl import DocxTemplate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import users,clients,tasks

class Report(APIView):

    def post(self, request):
            empl=users.models.UserProfile.objects.get(id=request.data.__getitem__('employer'))
            cl=clients.models.clients.objects.get(id=request.data.__getitem__('client'))
            obj = clients.models.clientobj.objects.get(id=request.data.__getitem__('object'))
            contact = clients.models.contact_man.objects.get(id=request.data.__getitem__('contact'))
            contracts=clients.models.object_contracts.objects.filter(clientobj=obj)
            works=[]
            for el in contracts:
                works.append(tasks.models.Task.objects.filter(contract=el).filter(task_compl__range=[request.data.__getitem__('start'),request.data.__getitem__('end')]))
            print(works[0][0].Task_name)
            doc = DocxTemplate(os.path.abspath('reports/template.docx'))
            context = {'works': "works",
                       'object':obj.object_name,
                       'adress':obj.object_adress,
                       'start':request.data.__getitem__('start'),
                       'end':request.data.__getitem__('end'),
                       }
            doc.render(context)
            doc.save("generated_doc.docx")
            return Response(status=status.HTTP_201_CREATED)


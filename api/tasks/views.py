import calendar
from users.models import auth
from clients.models import object_contracts
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bs4 import BeautifulSoup
import requests
import datetime
import json
from . import serializers
from . import models


class TaskGetAllList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, format=None):
        queryset = models.Task.objects.all()
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskGetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = models.Task.objects.filter(userprof=request.user)
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)

class MissTaskGetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = models.Task.objects.filter(userprof=request.user).filter(task_compl__lte=datetime.datetime.now()).filter(task_status=0)
        print(queryset)
        serializer = serializers.TaskGetSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class STaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask.objects.all()
    serializer_class = serializers.StaskSerializer


class STaskDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask.objects.all()
    serializer_class = serializers.StaskSerializer


class GetSTaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.Stask.objects.filter(Task=pk)
        serializer = serializers.StaskSerializer(queryset, many=True)
        return Response(serializer.data)


class GetFoto(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.Stask_foto.objects.filter(Stask=pk)
        serializer = serializers.StaskFotoSerializer(queryset, many=True)
        return Response(serializer.data)


class SFotoTaskList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask_foto.objects.all()
    serializer_class = serializers.StaskFotoSerializer


class STaskFotoDetailList(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Stask_foto.objects.all()
    serializer_class = serializers.StaskFotoSerializer


class GetReglamList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, pk, format=None):
        queryset = models.Reglament.objects.filter(cat=pk)
        serializer = serializers.ReglamentSerializer(queryset, many=True)
        return Response(serializer.data)


class GetReglamCatList(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, format=None):
        queryset = models.Reglament_cat.objects.all()
        serializer = serializers.ReglamCatSerializer(queryset, many=True)
        return Response(serializer.data)


class GetHd(APIView):
    permission_classes = [IsAuthenticated]

    def get(request, self, format=None):
        nowyear = datetime.datetime.now().year
        startyear = int(nowyear) - 5
        holydays = []
        holydaysp = []
        while startyear < nowyear + 5:
            url = 'https://calendar.yoip.ru/' + str(startyear) + '-calendar.html'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'lxml')
            year = soup.find_all('div', class_='col-6 col-sm-6 col-md-4 text-center')
            monthnumb = 1
            for month in year:
                for tag in month.find_all('td', class_='_hd warning'):
                    holydays.append(str(startyear) + '-' + str(monthnumb) + '-' + tag.text)
                for tag in month.find_all('td', class_='_hd warning tt-hd'):
                    holydaysp.append(str(startyear) + '-' + str(monthnumb) + '-' + tag.text)
                monthnumb = monthnumb + 1
            startyear = startyear + 1
        weekends = {'wd': holydays}
        hd = {'hd': holydaysp}
        return Response(json.dumps(weekends) + json.dumps(hd))


class TransferGetList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = models.trasfer_task.objects.filter(to_user=request.user)
        serializer = serializers.GetTranferSerializer(queryset, many=True)
        return Response(serializer.data)


class TransferList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.trasfer_task.objects.all()
    serializer_class = serializers.TranferSerializer


class TransferDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.trasfer_task.objects.all()
    serializer_class = serializers.TranferSerializer


class CompleteTaskTransfer(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        queryset = models.trasfer_task.objects.get(id=pk)
        models.Task.objects.filter(id=queryset.Task.id).update(userprof=queryset.to_user)
        models.trasfer_task.objects.filter(id=queryset.id).delete()
        return Response(status=status.HTTP_200_OK)


class DismissTaskTransfer(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        models.trasfer_task.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)


class AddReglam(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer_class = serializers.AddReglam(request.data, many=False)
        reglament = models.Reglament.objects.filter(cat=serializer_class.data['reglamcat'])
        days_in_month = lambda dt: calendar.monthrange(dt.year, dt.month)[1]
        today = datetime.date.today()
        contract = object_contracts.objects.get(id=serializer_class.data['contract'])
        for work in reglament:
            reglam_cat = models.Reglament_cat.objects.get(id=serializer_class.data['reglamcat'])
            next_startdate = today.replace(day=1) + datetime.timedelta(days_in_month(today))
            today = datetime.datetime.now()
            if (work.Task_period == 3):
                for month in range(12):
                    task = models.Task(Task_name=reglam_cat,
                                       userprof=auth.objects.get(id=serializer_class.data['userprof']),
                                       Task_other=work.Task_name, task_compl=next_startdate, contract=contract)
                    task.save()
                    next_startdate = next_startdate.replace(day=1) + datetime.timedelta(days_in_month(next_startdate))
            if (work.Task_period == 4):
                if (today.month <= 2):
                    next_startdate = datetime.datetime.strptime(str(today.year) + '-02-01', '%Y-%m-%d')
                    task = models.Task(Task_name=reglam_cat,
                                       userprof=auth.objects.get(id=serializer_class.data['userprof']),
                                       Task_other=work.Task_name, task_compl=next_startdate, contract=contract)
                    task.save()
                    next_startdate = datetime.datetime.strptime(str(today.year) + '-08-01', '%Y-%m-%d')
                    task = models.Task(Task_name=reglam_cat,
                                       userprof=auth.objects.get(id=serializer_class.data['userprof']),
                                       Task_other=work.Task_name, task_compl=next_startdate, contract=contract)
                    task.save()
                else:
                    next_startdate = datetime.datetime.strptime(str(today.year) + '-08-01', '%Y-%m-%d')
                    task = models.Task(Task_name=reglam_cat,
                                       userprof=auth.objects.get(id=serializer_class.data['userprof']),
                                       Task_other=work.Task_name, task_compl=next_startdate, contract=contract)
                    task.save()
                for year in range(4):
                    next_startdate = datetime.datetime.strptime(str(today.year + year) + '-02-01', '%Y-%m-%d')
                    task = models.Task(Task_name=reglam_cat,
                                       userprof=auth.objects.get(id=serializer_class.data['userprof']),
                                       Task_other=work.Task_name, task_compl=next_startdate, contract=contract)
                    task.save()
                    next_startdate = datetime.datetime.strptime(str(today.year + year) + '-08-01', '%Y-%m-%d')
                    task = models.Task(Task_name=reglam_cat,
                                       userprof=auth.objects.get(id=serializer_class.data['userprof']),
                                       Task_other=work.Task_name, task_compl=next_startdate, contract=contract)
                    task.save()

            if (work.Task_period == 5):
                next_startdate = datetime.datetime.strptime(str(today.year) + '-12-01', '%Y-%m-%d')
                for year in range(5):
                    task = models.Task(Task_name=reglam_cat,
                                       userprof=auth.objects.get(id=serializer_class.data['userprof']),
                                       Task_other=work.Task_name, task_compl=next_startdate, contract=contract)
                    task.save()
                    next_startdate = datetime.datetime.strptime(str(today.year + year) + '-12-01', '%Y-%m-%d')
        return Response(status=status.HTTP_200_OK)

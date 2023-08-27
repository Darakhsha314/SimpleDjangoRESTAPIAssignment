from rest_framework import generics
from .models import Tasklist
from .serializers import TaskListsSerializer


# Tasklist views will be created here.

# titleTask class is different than other class because this wil get a query parameter as per description
class Title(generics.ListCreateAPIView):
    serializer_class = TaskListsSerializer

    # Query set is the data which will come from the database.

    def get_queryset(self):
        queryset = Tasklist.objects.all()
        taskdata = self.request.get('taskdata')
        return queryset


# descriptionTask class

class Description(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListsSerializer
    queryset = Tasklist.objects.all()


# duedateTask class

class Duedate(generics.ListCreateAPIView):
    serializer_class = TaskListsSerializer
    queryset = Tasklist.objects.all()


# statusTask class

class Status(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListsSerializer
    queryset = Tasklist.objects.all()

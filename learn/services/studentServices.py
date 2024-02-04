from django.http import JsonResponse
from ..models import Student
from ..serializers import StudentSerialzer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST','PUT'])
def getAllStudents(request):
   print(type(request))
   if request.method == "GET":
    students = Student.objects.all()
    serializer = StudentSerialzer(students,many = True)
    return Response({'students':serializer.data})
   elif request.method == "POST":
     serializer = StudentSerialzer(data=request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def getStudent(request,id):
   try:
    student = Student.objects.get(pk = id)
   except Student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method == "GET":
      serializer = StudentSerialzer(student)
      return Response(serializer.data,status=status.HTTP_200_OK)
   elif request.method == "PUT":
      serializer = StudentSerialzer(student,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(status=status.HTTP_400_BAD_REQUEST)
   elif request.method == "DELETE":
     student.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
      
     
  
  
       
     


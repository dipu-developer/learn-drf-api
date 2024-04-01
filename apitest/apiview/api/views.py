from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializer import StudentSerializer
from api.models import Student
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@api_view(['GET','PUT','POST','DELETE'])
def studentApi(request):
            
        if request.method == 'GET':
            # id = request.GET.get('id')
            id = request.query_params.get('id')
            if id is None:
                try:
                    students = Student.objects.all()  # Retrieve all student data
                    serializer = StudentSerializer(students, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return Response("somethidg", status=status.HTTP_404_NOT_FOUND)

            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Student not found with the provided id.", status=status.HTTP_404_NOT_FOUND)

        if request.method == 'POST':
            if not request.data:
                return Response("No data provided", status=status.HTTP_400_BAD_REQUEST)
            serializer = StudentSerializer(data= request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            if serializer.is_valid():
                serializer.save()
                return Response("data add",status=status.HTTP_201_CREATED)
            return Response(serializer.error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # try:
            #     serializer = StudentSerializer(data=request.data)
            #     serializer.is_valid(raise_exception=True)  # Raise exception if serializer is not valid
            #     serializer.save()
            #     return Response("Data added", status=status.HTTP_201_CREATED)
            # except Exception as e:  # Catch any exception
            #     return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            try:
                id = request.data.get('id')
                if id is None:
                    return Response("Please provide 'id' field in the request data.", status=status.HTTP_400_BAD_REQUEST)
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response("Data updated", status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response("Student not found with the provided id.", status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            try:
                id = request.data.get('id')
                if id is None:
                    return Response("Please provide 'id' field in the request data.", status=status.HTTP_400_BAD_REQUEST)
                student = Student.objects.get(id=id)
                student.delete()
                return Response("Data deleted", status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response("Student not found with the provided id.", status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
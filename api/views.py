from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializer import StudentSerializer


@api_view(['GET','POST','PUT','DELETE'])

def student_operations(request, pk=None):
    if request.method == 'GET':
        if pk:
            try:
                student = Student.objects.get(id=pk)
                serializedData = StudentSerializer(student).data
                return Response(serializedData, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'error:Student Not Found'}, status = status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializedData = StudentSerializer(students,many = True).data
            return Response(serializedData, status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT' and pk:
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({"Error : Student Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE' and pk:
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({"Error:Student Not Found"},status = status.HTTP_404_NOT_FOUND)
        
        student.delete()
        return Response({"Student deleted successfully"}, status=status.HTTP_200_OK)
    
    return Response({"Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)










































# @api_view(['GET'])
# def get_students(request):
    
#     students = Student.objects.all()
#     serializedData = StudentSerializer(students, many=True).data
#     return Response(serializedData)

# @api_view(['POST'])
# def create_students(request):
#     data = request.data
#     serializer = StudentSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update_student(request, pk):
#     try:
#         student = Student.objects.get(id=pk)
#     except Student.DoesNotExist:
#         return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer = StudentSerializer(student, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_student(request, pk):
#     try:
#         student = Student.objects.get(id=pk)
#     except Student.DoesNotExist:
#         return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     student.delete()
#     return Response({'message': 'Student deleted successfully'}, status=status.HTTP_200_OK)


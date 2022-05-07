from os import set_inheritable, stat
from django.shortcuts import render,get_list_or_404, get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from algorithms.serializers import ProblemListSerializer, SolutionListSerializer, SolutionSerializer, TypeSerializer,ProblemSerializer
from .models import Type, Problem, Solution


# Create your views here.
@api_view(['GET','POST'])
def problem_list(request):
    if request.method == 'GET':
        problems = get_list_or_404(Problem)
        serializer = ProblemListSerializer(problems, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProblemSerializer(data=request.data)
        #type = TypeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )

@api_view(['GET','DELETE','PUT'])
def problem_detail(request,problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    if request.method == "GET":
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)
    elif request.method =="PUT":
        serializer = ProblemSerializer(problem, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        problem.delete()
        data = {
            'delete' : f'문제 {problem_pk}번이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def solution_list(request):
    if request.method == "GET":
        solutions = get_list_or_404(Solution)
        serializer = SolutionListSerializer(solutions, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def solution_create(request, problem_pk):
    problem = get_object_or_404(Problem, pk=problem_pk)
    serializer = SolutionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(problem=problem)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def problem_create(request):
    problem = Problem()
    print('################')
    print(request.data)
    problem.title = request.data['title']
    problem.content = request.data['content']
    problem.save()
    # problem.types.set(request.data['types'])
    # if request.data['types']

    # type = get_object_or_404(Type, pk=request.data['types'])
    # if problem.types.filter(pk=request.data['types']).exists():
    #     pass
    # else:
    #     type = TypeSerializer()
    #     problem.types.add(type)\
    types = Type.objects.all()
    data = request.data['types']
    if not types.filter(content=data).exists():
        type = Type()
        type.content = data
        type.save()
    problem.types.add(types.get(content=data).pk)
    

    serializer = ProblemSerializer(problem)
    return Response(serializer.data)
    



# @api_view(['GET','POST'])
# def problem_create(request, type_pk):
#     type = get_object_or_404(Type, pk=type_pk)
#     serializer = ProblemListSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(type=type)
#         return Response(serializer.data, status=status.HTTP_201_CREATED )
        

# @api_view(['POST'])
# def register(request, type_pk, problem_pk):
#     type = get_object_or_404(Type, pk=type_pk)
#     problem = get_object_or_404(Problem, pk=problem_pk)
#     problem.types.add(type)
#     serializer = ProblemSerializer(problem)




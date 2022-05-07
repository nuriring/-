from rest_framework import serializers
from .models import Type, Problem, Solution


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class ProblemListSerializer(serializers.ModelSerializer):
    #types = TypeSerializer(many=True,read_only=True)
    class Meta:
        model = Problem
        fields = '__all__'

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'
        read_only_fields =('problem',)
        
class ProblemSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, read_only=True)
    # type_count = serializers.IntegerField(source='type_set.count',read_only=True)
    solution_set = SolutionSerializer(many=True, read_only=True)
    solution_count = serializers.IntegerField(source='solution_set.count',read_only=True)

    class Meta:
        model = Problem
        fields ='__all__'


class SolutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields ='__all__'

    

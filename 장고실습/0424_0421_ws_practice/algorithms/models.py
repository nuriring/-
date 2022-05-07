from django.db import models

class Type(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content

class Problem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    types = models.ManyToManyField(Type, related_name='problems')

    def __str__(self):
        return self.title
# # Create your models here.
#     problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
#     #problems = models.ManyToManyField(Problem, related_name='types')



    

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    hint = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.hint
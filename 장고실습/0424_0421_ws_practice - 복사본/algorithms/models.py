from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # type = models.ForeignKey(Type, related_name='problems')

    def __str__(self):
        return self.title
# Create your models here.
class Type(models.Model):
    content = models.CharField(max_length=100)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    #problems = models.ManyToManyField(Problem, related_name='types')
    def __str__(self):
        return self.content



    

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    hint = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.hint
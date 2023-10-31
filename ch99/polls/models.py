from django.db import models

class Question(models.Model):
    Question_test = models.CharField(max_length = 200)
    pub_date = models.DateField("date_bulicshed")
    def __str__(self):
        return self.Question_text
    
class Choice(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_Text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Choice_Text
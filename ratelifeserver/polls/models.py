from django.db import models

# Create your models here.


class Question(models.Model):
	question_id = models.AutoField(primary_key = True)
	question_text = models.CharField(max_length=500)
	votes = models.IntegerField(default=0)
	bestAnswer = models.CharField(max_length=50, default='')
	bestVotes = models.IntegerField(default=0)

	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_text = models.CharField(max_length=100)
	answer_id = models.AutoField(primary_key = True) #add self incrementing default 
	votes = models.IntegerField(default=0)
	origin_id = models.IntegerField() #question_id for this answer
	def __str__(self):
		return self.answer_text


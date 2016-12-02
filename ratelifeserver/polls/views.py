from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question, Answer


def index(request):
	questions_list = Question.objects.order_by('votes')[:5]
    #return render(request, 'polls/home.html')
	output = '</br>'.join([str(a) for a in questions_list])
	return HttpResponse(output)

def answer(request, my_question_id):
	my_question= Question.objects.filter(question_id=my_question_id)
	answers_list = Answer.objects.filter(question=my_question) #order_by('votes')
	context= {'all_answers': answers_list}
	return render (request, 'polls/answersPage.html', context)

def questions(request):
	questions_list = Question.objects.all().order_by('votes')
	context= {'all_questions': questions_list}
	return render (request, 'polls/home.html', context)
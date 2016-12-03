from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Question, Answer
from .forms import answerForm, questionForm
from django.conf import settings
import numpy as np

def answer(request, my_question_id):
    my_question= Question.objects.filter(question_id=my_question_id)
    answers_list = Answer.objects.filter(origin_id=my_question_id).order_by('votes')
    newAnswerForm = answerForm(initial={'origin_id': my_question_id})
    context= {'all_answers': answers_list, "question": my_question, "form":newAnswerForm}
    return render (request, 'polls/answersPage.html', context)

def questions(request):
    questions_list = Question.objects.order_by('votes')
    newQuestionForm = questionForm(initial={'question_text': "Enter a new question"})
    context= {'all_questions': questions_list, 'form':newQuestionForm}
    for question in questions_list:
        if len(Answer.objects.filter(origin_id = question.question_id))>0:
            question.bestAnswer= Answer.objects.filter(origin_id = question.question_id).order_by('votes')[0].answer_text
            question.bestVotes = Answer.objects.filter(origin_id = question.question_id).order_by('votes')[0].votes
    context= {'all_questions': questions_list, 'form':newQuestionForm}
    return render (request, 'polls/home.html', context)

def update_answers(request):    
    if request.POST:
        newAnswerForm = answerForm(request.POST)
        my_question_id = newAnswerForm['origin_id'].value()
        my_question = Question.objects.filter(question_id=my_question_id)[0]   
        my_answer_text = newAnswerForm['answer_text'].value()
        votes = 0
        new_answer_obj = Answer(question = my_question, answer_text = my_answer_text, votes = votes, origin_id = my_question_id)
        new_answer_obj.save()
    return HttpResponseRedirect('/polls/'+my_question_id)

def update_questions(request):    
    if request.POST:
        newQuestionForm = questionForm(request.POST)
        my_question_text = newQuestionForm['question_text'].value()
        votes = 0
        new_question_obj = Question( question_text = my_question_text, votes = votes)
        new_question_obj.save()

    return HttpResponseRedirect('/polls/')

def vote(request):
	my_answer_id= request.POST.id  
	my_answer= Answer.objects.filter(answer_id=my_answer_id).votes=+1
	my_answer.save()
	return HttpResponseRedirect('/polls/'+request.POST.answer.origin_id)
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.questions, name='questionPage'),
    url(r'answersPage.html/', views.answer, name='answer'),
    url(r'^(?P<my_question_id>[0-9]+)', views.answer, name='answer'),
    url(r'update_answers', views.update_answers, name= 'update_answers'),
    url(r'update_questions', views.update_questions, name= 'update_questions'),
    url(r'vote', views.vote, name= 'vote'),
]


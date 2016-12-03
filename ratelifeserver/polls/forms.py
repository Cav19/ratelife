from django import forms
from .models import Answer, Question

class answerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['answer_id', 'votes']
        fields = [ 'origin_id', 'answer_text']

class questionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
from django import forms
from .models import Question, Answer

class QuestForm(forms.ModelForm):
    class Meta:
        model = Question

        fields = [
            'topic',
            'the_question',
            'image',
            'question_type',
            'status',
        ]
        
    def clean_topic(self):
        topic = self.cleaned_data.get('topic')
            
        if topic and len(topic) < 10:
                raise forms.ValidationError(
                'Topic must contain at least 10 characters'
            )
        return topic
        
    def clean_the_question(self):
        the_question = self.cleaned_data.get('the_question')

        if the_question and len(the_question) < 10:
            raise forms.ValidationError(
                'Questions must contain at least 10 characters'
            )
        return the_question
    
    def clean_question_type(self):
        question_type = self.cleaned_data.get('question_type')

        if not question_type:
            raise forms.ValidationError(
                'Wrong question type, kindly select the correct question type!'
            )
        return question_type

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer

        fields = [
            'answer'
        ]

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')

        if answer and len(answer) < 10:
            raise forms.ValidationError(
                'Answer must contain at least 10 characters'
            )
        return answer
        

    
from django import forms
from django.forms.widgets import RadioSelect


class QuestionForm(forms.Form):
    """
    Form for displaying one question at a time.
    Checks the type of question and displays content accordingly.
    e.g : If mcq type question, displays radiobuttons as options
    and if one word answer, displays textbox.
    """
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self._q_id = question.id
        self._mcq = False
        if question.get_answers_list():
            self._mcq = True
            choice_list = [x for x in question.get_answers_list()]
            self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)
        else:
            self.fields["answer"] = forms.CharField()
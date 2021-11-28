from django import forms

class NameForm(forms.Form):
    videolistname = forms.CharField(label='清單名稱', max_length=100)
from django import forms

class ChatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lines'].widget = forms.HiddenInput()

    txt = forms.CharField(label='入力欄')
    lines = forms.CharField()


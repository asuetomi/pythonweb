from django import forms

class ChatForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lines'].widget = forms.HiddenInput()
        self.fields['mode'].widget = forms.HiddenInput()
        self.fields['prompt'].widget = forms.HiddenInput()

    txt = forms.CharField(label='')
    lines = forms.CharField()
    mode = forms.CharField()
    prompt = forms.CharField()


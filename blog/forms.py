from django import forms


class EntryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    is_published = forms.BooleanField(label='Published', required=False)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

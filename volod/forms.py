from django import forms

class MyFrom(forms.Form):
    title = forms.CharField(max_length=32, label='', widget=forms.TextInput(attrs={'class': 'test-class', 'placeholder': 'Name'}))
    content =forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'test-class', 'placeholder': 'Name'}))
    content1 =forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'test-class', 'placeholder': 'Name'}))
    content2 =forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'test-class', 'placeholder': 'Name'}))
    content3 =forms.IntegerField(label='', widget=forms.Textarea(attrs={'class': 'test-class-big', 'placeholder': 'Tell us about the car needing service(s)'}))
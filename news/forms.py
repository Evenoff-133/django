from django import forms


class CommentForm(forms.Form):
    comment = forms.Textarea()
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField()
from django import forms

class ReviewForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    rate = forms.IntegerField(min_value=0, max_value=5)

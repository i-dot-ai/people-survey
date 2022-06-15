from django import forms


class Group1Form(forms.Form):
    b01 = forms.IntegerField(required=False)
    b02 = forms.IntegerField(required=False)
    b03 = forms.IntegerField(required=False)
    b04 = forms.IntegerField(required=False)
    b05 = forms.IntegerField(required=False)


class Group2Form(forms.Form):
    b06 = forms.IntegerField(required=False)
    b07 = forms.IntegerField(required=False)

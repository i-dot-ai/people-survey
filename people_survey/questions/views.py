from django.shortcuts import render

from . import forms

forms_mapping = {
    "1": forms.Group1Form,
    "2": forms.Group2Form,
}


def question_view(request):
    param = request.GET["form"]
    form = forms_mapping.get(param)
    return render(
        request,
        template_name="questions/question.html",
        context={"form": form},
    )

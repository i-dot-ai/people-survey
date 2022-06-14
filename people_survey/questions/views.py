from django.shortcuts import render

def question_view(request):
    return render(
        request,
        template_name="questions/question.html",
        context={},
    )
    

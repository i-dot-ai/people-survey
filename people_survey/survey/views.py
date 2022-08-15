from django.shortcuts import render


def index_view(request):
    return render(
        request,
        template_name="survey/index.html",
        context={"request": request},
    )

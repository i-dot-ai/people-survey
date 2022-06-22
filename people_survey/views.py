from django.shortcuts import render


def index_view(request):
    return render(
        request,
        template_name="index.html",
        context={},
    )


def page_view(request, page_num):
    return render(
        request,
        template_name=f"page{page_num}.html",
        context={},
    )

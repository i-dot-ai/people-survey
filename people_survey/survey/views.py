from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from ninja import NinjaAPI

from .models import Survey, Answer
from .schemas import SurveySchema, AnswerSchema

api = NinjaAPI()


@require_http_methods(["GET"])
def index_view(request):
    return render(
        request,
        template_name="index.html",
        context={"request": request},
    )


@require_http_methods(["GET"])
def builder_view(request):
    return render(
        request,
        template_name="builder.html",
        context={"request": request},
    )


@require_http_methods(["GET"])
def survey_view(request):
    return render(
        request,
        template_name="survey.html",
        context={"request": request},
    )


@api.post("/survey")
def api_builder_post(request, data: SurveySchema):
    return

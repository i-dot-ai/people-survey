from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from ninja import NinjaAPI

from .models import Answer, Survey
from .schemas import AnswerSchema, SurveySchema

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


@api.get("/survey")
def api_builder_get(request):
    if Survey.objects.count():
        survey = Survey.objects.get(1).data
    else:
        survey = None
    return survey


@api.post("/survey")
def api_builder_post(request, data: SurveySchema):
    survey = Survey.objects.update_or_create(id=1, data=str(data.data))
    return None


@api.get("/answer")
def api_answer_get(request):
    if Answer.objects.count():
        answer = Answer.objects.first().data
    else:
        answer = None
    return answer


@api.post("/answer")
def api_answer_post(request, data: AnswerSchema):
    answer = Answer.objects.update_or_create(data=str(data.data))
    return None

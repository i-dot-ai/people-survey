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
def homepage_view(request):
    return render(
        request,
        template_name="homepage.html",
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


@api.get("/survey", response=SurveySchema)
def api_builder_get(request):
    user = request.user
    if Survey.objects.filter(user=user).count():
        survey = Survey.objects.filter(user=user).first().data
    else:
        survey = None
    return survey


@api.post("/survey", response=SurveySchema)
def api_builder_post(request, data: SurveySchema):
    user = request.user
    survey, created = Survey.objects.update_or_create(user=user, data=str(data.data))
    return survey


@api.get("/answer", response=AnswerSchema)
def api_answer_get(request):
    user = request.user
    if Answer.objects.filter(user=user).count():
        answer = Answer.objects.filter(user=user).first().data
    else:
        answer = None
    return answer


@api.post("/answer", response=AnswerSchema)
def api_answer_post(request, data: AnswerSchema):
    user = request.user
    answer, created = Answer.objects.update_or_create(user=user, data=str(data.data))
    return answer

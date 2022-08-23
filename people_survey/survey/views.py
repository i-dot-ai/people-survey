from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from ninja import NinjaAPI

from . import models
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


def get_item(model, user):
    if not user.is_authenticated:
        user = None
    if model.objects.filter(user=user).count():
        item = model.objects.filter(user=user).first()
    else:
        item = {'data': None}
    return item


@api.get("/survey", response=SurveySchema)
def api_builder_get(request):
    survey = get_item(models.Survey, request.user)
    return survey


@api.post("/survey", response=SurveySchema)
def api_builder_post(request, data: SurveySchema):
    user = request.user
    survey, created = Survey.objects.update_or_create(user=user, data=str(data.data))
    return survey


@api.get("/answer", response=AnswerSchema)
def api_answer_get(request):
    answer = get_item(models.Answer, request.user)
    return answer


@api.post("/answer", response=AnswerSchema)
def api_answer_post(request, data: AnswerSchema):
    user = request.user
    answer, created = Answer.objects.update_or_create(user=user, data=str(data.data))
    return answer

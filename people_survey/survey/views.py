import yaml
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from ninja import NinjaAPI

from . import models
from .schemas import ResultSchema, SurveySchema


with (settings.BASE_DIR / "questions.yaml").open() as f:
    questions_data = yaml.safe_load(f)

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
        item = model.objects.filter(user=user).order_by('id').first()
    else:
        item = {'data': None}
    return item


def save_item(model, user, data):
    if not user.is_authenticated:
        user = None
    if model.objects.filter(user=user).count():
        item = model.objects.filter(user=user).order_by('id').first()
    else:
        item = model(user=user)
    item.data = data
    item.save()
    return item


@api.get("/survey", response=SurveySchema)
def api_builder_get(request):
    survey = get_item(models.Survey, request.user)
    return survey


@api.post("/survey", response=SurveySchema)
def api_builder_post(request, data: SurveySchema):
    survey = save_item(models.Survey, request.user, data.data)
    return survey


@api.get("/result", response=ResultSchema)
def api_result_get(request):
    result = get_item(models.Result, request.user)
    return result


@api.post("/result", response=ResultSchema)
def api_result_post(request, data: ResultSchema):
    result = save_item(models.Result, request.user, data.data)
    return result


def questions_view(request, page_num=1):
    if request.method == "GET":
        section = questions_data[page_num-1]
        return render(
            request,
            template_name="questions.html",
            context={"request": request, 'section': section},
        )
    elif request.method == "POST":
        if page_num >= len(questions_data):
            return redirect("finished")
        else:
            next_page_num = page_num + 1
            return redirect("questions",  page_num=next_page_num)


def finished_view(request):
    return render(
        request,
        template_name="finished.html",
        context={"request": request},
    )

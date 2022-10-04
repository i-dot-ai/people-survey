import yaml
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from people_survey.survey.models import Result

with (settings.BASE_DIR / "questions.yaml").open() as f:
    questions_data = yaml.safe_load(f)


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


def get_item(model, user):
    if not user.is_authenticated:
        user = None
    if model.objects.filter(user=user).count():
        item = model.objects.filter(user=user).order_by("id").first()
    else:
        item = {"data": None}
    return item


def save_item(model, user, data, update=False):
    if not user.is_authenticated:
        user = None
    if model.objects.filter(user=user).count():
        item = model.objects.filter(user=user).order_by("id").first()
    else:
        item = model(user=user)
    if not update:
        item.data = data
    else:
        data_update = item.data
        if not data_update:
            data_update = {}
        for k, v in data.items():
            if k != "csrfmiddlewaretoken":
                data_update[k] = v
        item.data = data_update
    item.save()
    return item


def add_existing_responses(section_data, existing_results):
    questions_with_responses = []
    for question in section_data["questions"]:
        question_id = question["id"]
        val = existing_results.get(question_id)
        try:
            val = int(val)
        except (ValueError, TypeError):
            pass
        question["existing_value"] = val
        questions_with_responses.append(question)

    updated_section_data = {}
    for k, v in section_data.items():
        if k != "questions":
            updated_section_data[k] = v
        else:
            updated_section_data["questions"] = questions_with_responses
    return updated_section_data


def questions_view(request, page_num=1):
    user = request.user
    if request.method == "GET":
        existing_results = get_item(Result, user)
        if existing_results.data:
            existing_results = existing_results.data
        else:
            existing_results = {}
        section = questions_data[page_num - 1]
        updated_section_data = add_existing_responses(
            section_data=section, existing_results=existing_results
        )
        print(updated_section_data)
        return render(
            request,
            template_name="questions.html",
            context={"request": request, "section": updated_section_data},
        )
    elif request.method == "POST":
        data = request.POST
        save_item(Result, user=user, data=data, update=True)
        if page_num >= len(questions_data):
            return redirect("finished")
        else:
            next_page_num = page_num + 1
            return redirect("questions", page_num=next_page_num)


def finished_view(request):
    return render(
        request,
        template_name="finished.html",
        context={"request": request},
    )

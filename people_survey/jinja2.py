import govuk_frontend_jinja
import jinja2
from django.templatetags.static import static
from django.urls import reverse



from jinja2 import ChoiceLoader, PackageLoader, PrefixLoader


def environment(**options):
    extra_options = dict(
        loader = ChoiceLoader(
            [
                options['loader'],
                PrefixLoader({"govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja")}),
            ]
        )

    )
    env = jinja2.Environment(
        **{
            **options,
            **extra_options,
        }
    )
    env.globals.update(
        {
            "static": static,
            "url": reverse,
        }
    )
    return env

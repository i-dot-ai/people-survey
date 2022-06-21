import govuk_frontend_jinja
import jinja2
from django.templatetags.static import static
from django.urls import reverse


def environment(**options):
    extra_options = dict(
        autoescape=jinja2.select_autoescape(("html", "htm", "xml", "xhtml", "njk")),
        extensions=[govuk_frontend_jinja.templates.NunjucksExtension],
        undefined=govuk_frontend_jinja.templates.NunjucksUndefined,
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

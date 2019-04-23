from django import template
from django.utils.safestring import mark_safe
from pwd_front.models import Page, Slider, Blurb

register = template.Library()


# Template tags

@register.simple_tag
def paragraph(slug=''):
    """
    This inclusion template tag dispatches paragraphs in a page.

    A ``slug`` page must be given as argument.

    If more than one paragraph is returned, they're ordered following
    position parameter.

    :param slug: web page slug.
    :return: html string
    """
    if slug:
        try:
            page = Page.objects.get(slug=slug)
            html = ''
            for p in page.paragraphs.filter(is_active=True):
                html = html + p.content
            return mark_safe(html)

        except Page.DoesNotExist:
            return f"<Internal error: Slug '{slug}' doesn't exist, check " \
                "template tag 'paragraph' on this template."

    return "<Internal error: missing slug argument in template tag " \
           "'paragraph'.>"


@register.inclusion_tag('pwd_front/_parts/blurb.html', takes_context=False)
def blurbs(slug=''):
    """
    This inclusion template tag dispatches blurbs.

    If a page ``slug`` is given as argument. If the page exists and is
    related to active blurbs, they're displayed.

    If no argument is provided, all active blurbs are displayed.

    A blurb is composed of an icon from Linear Awesome, a title and
    a description.

    :param slug: web page slug.
    :return: html string
    """
    if slug:
        try:
            page = Page.objects.get(slug=slug)
            return {'bs': page.blurbs.filter(is_active=True)}
        except Page.DoesNotExist:
            return {}
    else:
        try:
            bs = Blurb.objects.filter(is_active=True)
        except Page.DoesNotExist:
            return {}
        return {'bs': bs}


@register.inclusion_tag('pwd_front/_parts/slider.html', takes_context=False)
def slider():
    """
    This inclusion template tag includes a slider.

    It takes all active slides.
    """
    try:
        slides = Slider.objects.filter(is_active=True)
        return {'slides': slides}
    except Slider.DoesNotExist:
        return {}


@register.inclusion_tag('pwd_front/_parts/analytics.html')
def ga_analytics(ga_analytics):
    """
    This inclusion template tag includes Google analytics in base
    template.
    """
    return {'analytics': ga_analytics}


# Filters

@register.filter
def headify(value):
    if len(value) > 3:
        c1, c2 = value[0:2], value[2:]
        v = f'{c1}</span>{c2}'.upper()
        return mark_safe(v)

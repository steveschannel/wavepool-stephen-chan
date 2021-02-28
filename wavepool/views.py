from django.template import loader
from django.http import HttpResponse

from wavepool.models import NewsPost
from wavepool.code_exercise_defs import code_exercise_defs, code_review_defs, code_design_defs
from django.conf import settings


def front_page(request):
    """ View for the site's front page
        Returns all available newsposts, formatted like:
            cover_story: the newsposts with is_cover_story = True
            top_stories: the 3 most recent newsposts that are not cover story
            archive: the rest of the newsposts, sorted by most recent
    """
    template = loader.get_template('wavepool/frontpage.html')
    # this is to place the cover story within its proper location. However, is cover story MUST be unique. Alternatively .filter(is_cover_story=True).get()
    try:
        cover_story = NewsPost.objects.get(is_cover_story=True)
    except:
        # Non-ideal behavior, but return random story for cover story in case cover story does not exist
        cover_story = NewsPost.objects.order_by('?').first()
    top_stories = NewsPost.objects.filter(
        is_cover_story=False).order_by('-publish_date')[:3]
    other_stories = NewsPost.objects.filter(
        is_cover_story=False).order_by('-publish_date')[3:]

    context = {
        'cover_story': cover_story,
        'top_stories': top_stories,
        'archive': other_stories,
    }

    return HttpResponse(template.render(context, request))


def newspost_detail(request, newspost_id=None):
    template = loader.get_template('wavepool/newspost.html')
    # newspost = NewsPost.objects.get(pk=newspost_id)
    newspost = NewsPost.objects.all().first()
    context = {
        'newspost': newspost
    }

    return HttpResponse(template.render(context, request))


def instructions(request):
    template = loader.get_template('wavepool/instructions.html')

    context = {
        'code_exercise_defs': code_exercise_defs,
        'code_design_defs': code_design_defs,
        'code_review_defs': code_review_defs,
        'show_senior_exercises': settings.SENIOR_USER,
    }
    return HttpResponse(template.render(context, request))

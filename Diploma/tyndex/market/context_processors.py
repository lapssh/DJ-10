from market.models import Section, Category


def menu_items(request):
    context = {'menu': Section.objects.prefetch_related('categories').all()}

    return context

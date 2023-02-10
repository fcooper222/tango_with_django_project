import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

django.setup()
from rango.models import Category, Page


def populate():

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/', 'views': 100},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/', 'views': 300},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/', 'views': 50}]

    django_pages = [{'title': 'Official Django Tutorial',
                     'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 120},
                    {'title': 'Django Rocks',
                     'url': 'http://www.djangorocks.com/', 'views': 110},
                    {'title': 'How to Tango with Django',
                     'url': 'http://www.tangowithdjango.com/', 'views': 30}]

    django_pages = [{'title': 'Official Django Tutorial',
                     'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 120},
                    {'title': 'Django Rocks',
                     'url': 'http://www.djangorocks.com/', 'views': 110},
                    {'title': 'How to Tango with Django',
                     'url': 'http://www.tangowithdjango.com/', 'views': 30}]
    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/', 'views': 50},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org', 'views': 50}]
    cats = {'Python': {'pages': python_pages, 'likes': 2, 'views': 10},
            'Django': {'pages': django_pages, 'likes': 20, 'views': 80},
            'Other Frameworks': {'pages': other_pages, 'likes': 6, 'views': 50}}

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["likes"],cat_data["views"])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'],p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name,likes,views):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

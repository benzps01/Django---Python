from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

posts = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "content": "Python is a high-level programming language that supports multiple programming paradigms."
    },
    {
        "id": 2,
        "title": "Getting Started with Django",
        "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design."
    },
    {
        "id": 3,
        "title": "REST API with Django",
        "content": "Django REST Framework (DRF) is a powerful toolkit for building Web APIs in Django."
    },
    {
        "id": 4,
        "title": "Understanding Python Data Structures",
        "content": "Python supports several built-in data structures, such as lists, tuples, sets, and dictionaries."
    }
]

# Create your views here.
def home(request):
    return render(request,'posts/home.html', {"posts":posts, 'username':'benson'})


def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request, 'posts/post.html', {'post_dict': post_dict})
    else:
        raise Http404()
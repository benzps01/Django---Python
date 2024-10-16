from django.shortcuts import render
from django.http import HttpResponse

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
    html = ""
    for post in posts:
        html += f'''
            <div>
                <h1>{post['id']} - {post['title']}</h1>
                <p>{post['content']}</p>
            </div>
'''
    return HttpResponse(html)
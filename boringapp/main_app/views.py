from django.shortcuts import render
from main_app.models import blog_post


# Create your views here.

def homepage(request):

    my_dict=blog_post.objects.all()

    return render(request, 'main.html',{'my_dict':my_dict})


def blogpost(request,article_id):

    my_dict=blog_post.objects.get(id=article_id)
    return render(request, 'blogpost.html',{'my_dict':my_dict})
  
from django.contrib.auth import login
from django.shortcuts import render
from django.template import loader

from posts.models import Login
from django.http import HttpResponse

def html_view(request):
    main_page_data = Login.objects.order_by('position')
    context = {
        'main_page_data': main_page_data
    }

    template = '../static/../templates/html/../html/hair.html'
    return render(request, template, context=context)


def css_view(request):
    return render(request, '../static/css/styles.css')

def login_view(request):
    login_v = Login.objects.all()
    return render(request, '../templates/html/login.html', context={"login":login})

def post_change_view(request, post_id):
    post = Login.objects.get(id=post_id)
    return render(request, "../templates/html/hair.html", context={'login':login})



#
# class Home (TemplateView):
#     template_name = 'index.html'
#
#     def get_context_data(self, request):
#         ctx = {}
#         return render(request, self.template_name, ctx)


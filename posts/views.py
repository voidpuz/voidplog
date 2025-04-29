from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from posts.models import Post


# def hello_world(request):
#     posts = Post.objects.all().order_by("-created_at")
#     return render(
#         request=request, 
#         template_name="posts/hello.html", 
#         context = {
#             "posts": posts
#         }
#     )


class HelloWorldView(TemplateView):
    template_name = "posts/hello.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(">>> Context", context)
        context["posts"] = Post.objects.all().order_by("-created_at")
        print(">>>", context)
        return context
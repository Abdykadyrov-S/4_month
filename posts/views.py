from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from posts.models import Post, Comment
from django.views import generic
from django.urls import reverse_lazy
from posts.forms import CommentForms, PostForms
import datetime

class IndexView(generic.ListView):
    model = Post
    context_object_name = "posts"
    extra_context = {"title": "Главная страница"}
    template_name = "posts/index.html"


class POstDetailView(generic.DetailView):
    model = Post
    context_object_name = "posts"   
    template_name = "posts/post_detail.html" 
    extra_context = {"form": CommentForms()}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = CommentForms()
    #     return context


    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForms(request.POST)

        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()

        return redirect("post-detail", pk)

    # def post(self, request, pk):
    #     post = Post.objects.get(pk=pk)
    #     name = request.POST.get("name", None)
    #     text = request.POST.get("text", None)

    #     if name and text:
    #         comment = Comment.objects.create(name=name, text=text, post=post)
    #         comment.save()
    #     return redirect("post-detail", pk)


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"  
    form_class = PostForms
    success_url = reverse_lazy("main-page")



class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("main-page")


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    form_class = PostForms
    success_url = reverse_lazy("main-page")




def time(request):
    tim = datetime.datetime.now()
    return HttpResponse(tim)

def goodbye(request):
    return HttpResponse("Goodbye!")


# def index(request):
#     posts = Post.objects.all()
#     context = {
#         "title": "Главная страница",
#         "posts": posts
#     }
#     return render(request, "index.html", context)

# def get_post(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         raise Http404("Такого поста нет")
#     return render(request, "post_detail.html", {"post": post})

# def about(request):
#     context = {
#         "title": "О нас"
#     }
#     return render(request, "about.html", context )

class About(generic.TemplateView):
    template_name = "posts/about.html"
    extra_context = {"title": "О нас"}



# def contacts(request):
#     context = {
#         "title": "Контакты"
#     }
#     return render(request, "contacts.html", context )

class Contacts(generic.TemplateView):
    template_name = "posts/contacts.html"
    extra_context = {"title": "Контакты"}
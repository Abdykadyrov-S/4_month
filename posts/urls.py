from django.urls import path
from posts.views import time, goodbye, IndexView, POstDetailView,PostUpdateView, PostCreateView,PostDeleteView, About, Contacts

urlpatterns = [
    path('', IndexView.as_view(), name="main-page"),
    path('time/', time, name="time"),
    path('goodbye/', goodbye, name="goodbye"),
    path('about/', About.as_view(), name="about-page"),
    path('contacts/', Contacts.as_view(), name="contacts"),
    path("post/<int:pk>/", POstDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),
    path("post/update/<int:pk>", PostUpdateView.as_view(), name="post-update"),
]


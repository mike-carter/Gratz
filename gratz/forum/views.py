from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Post, Comment

# Create your views here.


class HomepageView(generic.ListView):
    """ Displays Forum Homepage """
    template_name = 'forum/homepage.html'
    context_object_name = 'most_recent_posts'

    def get_queryset(self):
        return Post.objects.order_by('-date_posted')[:20]


class PostDetailView(generic.DetailView):
    """ Displays the post content along with comments. """
    model = Post
    template_name = 'forum/post_details.html'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    """ Displays form used to create new posts """
    model = Post
    fields = ['title', 'text']
    template_name = 'forum/post_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.date_posted = timezone.now()
        return super().form_valid(form)


class CommentView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = ['text']
    template_name = 'forum/comment_create.html'

    def form_valid(self, form):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)

        comment = form.instance
        comment.owner = self.request.user
        comment.date_posted = timezone.now()
        comment.post = post

        # go back to the post details page if successful
        self.success_url = reverse('forum:post_detail',  args=(post_id,))
        return super().form_valid(form)

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from .models import Post
import random
# Create your views here.
def post_list(request):
    POSTS_ON_PAGES = 3
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:5]
    all_posts = get_list_or_404(Post, published_date__lte=timezone.now())
    num_pages = int(len(all_posts)/POSTS_ON_PAGES)+1 #количество страниц
    pages = range(1, num_pages+1)
    posts = all_posts[:POSTS_ON_PAGES]
    random_post = random.choice(posts)
    content = {'posts':posts, 'random_post':random_post, 'pages':pages}
    return render(request, 'portfolio/index.html', content)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'portfolio/post_detail.html', {'post': post})
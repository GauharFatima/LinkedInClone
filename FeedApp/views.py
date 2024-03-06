from AccountsApp.models import MyUser
from ProfileApp.models import Profile
from PostsApp.models import Post
from django.shortcuts import render, get_object_or_404


def feed_view(request):
    posts = Post.objects.all().order_by('-created_at')

    # Fetch the current user's profile from the session
    myuser_id = request.session.get('myuser_id')
    if myuser_id:
        myuser = get_object_or_404(MyUser, id=myuser_id)
        profile = myuser.profile
    else:
        myuser = None
        profile = None

    return render(request, 'FeedApp/feed.html', {'posts': posts, 'myuser': myuser, 'profile': profile})

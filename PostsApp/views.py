from django.core.paginator import Paginator
from django.db.models import F
from .models import Post, Like, Comments
from django.http import JsonResponse
from AccountsApp.models import MyUser
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from ProfileApp.models import Profile
from django.urls import reverse_lazy


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'PostsApp/list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        myuser_id = request.session.get('myuser_id')

        if not myuser_id:
            messages.error(request, 'User session not found.')
            return redirect('login')  # Adjust with your login view's name
        try:
            myuser_instance = MyUser.objects.get(id=myuser_id)
            profile = Profile.objects.get(user=myuser_instance)
        except (MyUser.DoesNotExist, Profile.DoesNotExist):
            messages.error(
                request, 'Profile not found. Please complete your profile first.')
            return redirect('complete_profile')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.profile = profile
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'PostsApp/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myuser_id = request.session.get('myuser_id')
            if not myuser_id:
                messages.error(request, 'User session not found.')
                return redirect('login')

            myuser_instance = MyUser.objects.get(id=myuser_id)
            try:
                user_profile = Profile.objects.get(user=myuser_instance)
            except Profile.DoesNotExist:
                messages.error(
                    request, 'Profile not found. Please complete your profile first.')
                # Redirect to profile creation view
                return redirect('complete_profile')

            # Set the profile on the form instance
            post = form.save(commit=False)
            post.profile = user_profile
            post.save()

            # Redirect to the post's detail view or another success URL
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'PostsApp/create.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'PostsApp/update.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse_lazy('posts:post_list'))
    return render(request, 'PostsApp/delete.html', {'post': post})


# like feature view


def toggle_like(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        myuser_id = request.session.get('myuser_id')

        if not myuser_id:
            return JsonResponse({'error': 'Authentication required'}, status=403)
        # Fetch the profile using the myuser_id from session
        profile = get_object_or_404(Profile, user_id=myuser_id)
        # Use the profile to toggle the like
        like, created = Like.objects.get_or_create(post=post, profile=profile)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        like_count = Post.objects.filter(id=post.id).annotate(
            like_count=F('likes__id')).count()

        return JsonResponse({
            'liked': liked,
            'like_count': like_count
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


# comment view
def submit_comment(request, pk):
    if request.method == 'POST':
        myuser_id = request.session.get('myuser_id')
        if not myuser_id:
            return JsonResponse({'error': 'Authentication required'}, status=403)

        profile = get_object_or_404(Profile, user_id=myuser_id)
        post = get_object_or_404(Post, pk=pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.profile = profile
            comment.save()

            # Optionally, return some information about the new comment
            return JsonResponse({
                'message': 'Comment added successfully',
                'content': comment.content,
                'author': comment.profile.user.first_name,
                'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    # Handle invalid form or request method
    return JsonResponse({'error': 'Invalid request'}, status=400)



def get_comments(request, pk):
    comments = Comments.objects.filter(post_id=pk).order_by('-created_at')
    paginator = Paginator(comments, 3)  # Show 5 comments per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    comments_data = list(page_obj.object_list.values(
        'id', 'content', 'profile__user__first_name', 'created_at'))
    return JsonResponse({
        'message': 'No Comment Added',
        'comments': comments_data,
        'has_next': page_obj.has_next(),
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    })
    # comments_data = [{'content': comment.content, 'author': comment.profile.user.first_name} for comment in page_obj]
    # return JsonResponse({'comments': comments_data})
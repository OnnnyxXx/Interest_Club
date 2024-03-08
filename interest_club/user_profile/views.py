from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, PostForm
from .models import Post


@login_required
def profile(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    else:
        form = ProfileForm(instance=profile, user=user)

    context = {'form': form}
    return render(request, 'user_profile/settings_profile.html', context)


def User_View(request):
    profile = request.user.profile
    posts = Post.objects.filter(post_author=request.user).order_by("-created_at")

    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_home')

    context = {'form': form,
               "posts": posts

               }

    return render(request, 'user_profile/home_user.html', context)


def user_profile(request, id):
    user = get_object_or_404(User, id=id)
    profile = user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_home')

    context = {'form': form, 'profile': profile}

    return render(request, 'user_profile/user_profile.html', context)


@login_required
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.post_author = request.user
        post.save()
        return redirect('user_home')

    context = {'form': form}
    return render(request, 'user_profile/create_post.html', context)

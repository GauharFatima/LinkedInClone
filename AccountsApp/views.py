from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib.auth import logout
from .forms import SignUpForm, LogInForm


# Create your views here.


def createUser(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('feed')
        # return redirect('ProfileApp:profile_test')

    return render(request, 'AccountsApp/signup.html', {'form': form})


# def feedsView(request):
#     return render(request, 'AccountsApp/home.html', {})


def existingUser(request):
    form = LogInForm()
    if request.method == 'GET':
        return render(request, 'AccountsApp/login.html', {'form': form})

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = MyUser.objects.get(email=email)  # returns user object

            if (password == user.password):
                # print(user.first_name)
                # Store MyUser's ID in session
                request.session['myuser_id'] = user.id
                # print(request.session)
                return redirect('feed')
            else:
                return render(request, 'AccountsApp/login.html', {'messages': 'Incorrect Password'})
        except MyUser.DoesNotExist:
            return render(request, 'AccountsApp/signup.html', {'messages': 'Email does not exist,Create new Account'})

    return render(request, 'AccountsApp/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    request.session.flush()  # This clears all session data
    # print(request.session.flush())
    return redirect('login')

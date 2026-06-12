from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import User
from .forms import SignupForm, LoginForm
from django.utils import timezone
from .decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == "POST":
        form = SignupForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            user = form.save(commit=False)

            user.password = make_password(
                form.cleaned_data['password']
            )

            user.save()

            messages.success(
                request,
                "Account created successfully"
            )

            return redirect('login')

    else:
        form = SignupForm()

    return render(
        request,
        'sign_up.html',
        {'form': form}
    )

def login(request):
    if request.method == 'POST':
        form = LoginForm(
            request.POST
        )

        if form.is_valid():
            email= form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)

                if check_password(password, user.password):
                    request.session['user_id'] = user.pk
                    request.session['username'] = user.username
                    request.session['full_name'] = user.full_name 

                    user.last_login = timezone.now()
                    user.save()

                    messages.success(
                        request, 'Login succesful'
                    )
                    return redirect('dashboard')
                else:
                    messages.error(
                        request, 'Incorrect password, Kindly input the correct password'
                    )
            except User.DoesNotExist:
                messages.error(
                    request, '404 User not Found'
                )
    else:
        form = LoginForm()
    context = {
            'form': form
        }
    return render(request, 'login.html', context)

@login_required
def user_details(request):
    user = get_object_or_404(User, id=request.session.get('user_id'))
    
    context = {
        'user':user
    }
    return render(request, 'user_details.html', context)

@login_required
def update_user_details(request):
    user = get_object_or_404(User, id=request.session.get('user_id'))
   
    form = SignupForm(
        request.POST or None,
        request.FILES or None,
        instance=user
    )

    if request.method =='POST':
        if form.is_valid():
            form.save()

            messages.success(
                request, 'User details updated successfully'
            )
            return redirect ('user_details')
    context = {
        'form':form
    }
    return render(request, 'update_user_details.html', context)

def logout(request):
    request.session.flush()

    messages.success(
        request, 'Account logout successfully'
    )
    return redirect('login')

@login_required
def delete_user(request):
    user = get_object_or_404(User, id=request.session.get('user_id'))

    if request.method == "POST":
        user.delete()
        request.session.flush()

        messages.success(
            request, 'Account Deleted Successful'
        )
        return redirect('sign_up')
    context = {
        'user':user
    }
    return render(request, 'delete_user.html', context)




                    
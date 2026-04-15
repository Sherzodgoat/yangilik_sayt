from django.shortcuts import render, redirect
from django.views import View

from account.forms import EditProfileForm, EditUserForm, SignupForm
from account.models import Profile
from django.contrib.auth.decorators import login_required


def logout_request_view(request):

    return render(request, 'registration/logged_out.html')

@login_required
def user_profile_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    context = {
        'user': user,
        'profile': profile,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, 'registration/profile.html', context)



# class UserLoginView(View):
#
#     def get(self,request):
#         login_form = LoginForm()
#         return render(request,'registration/login.html', context={'form':login_form})
#
#     def post(self,request):
#         # print(request.POST)
#         login_form = LoginForm()
#         print(login_form)
#         # username = request.POST['username']
#         # password = request.POST['password']
#
#         return HttpResponse('Login bo\'ldingiz')


class ProfileView(View):
    def get(self, request):
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email

        context = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }
        return render(request, 'registration/edit_profile.html', context)


class EditProfileView(View):
    def get(self, request):
        user = request.user
        profile_form = EditProfileForm(instance=user)
        user_form = EditUserForm(instance=user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'registration/edit_profile.html', context)

    def post(self, request):
        user = request.user

        profile_form = EditProfileForm(request.POST, request.FILES, instance=user.profile)
        user_form = EditUserForm(request.POST, instance=user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }

        return render(request, 'registration/edit_profile.html', context)



class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            return redirect("login")

        return render(request, 'registration/signup.html', {'form': form})


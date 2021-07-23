from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib import messages 

from pokemon.forms.auth import SignUpForm, LogInForm

class RegisterView(generic.CreateView):
    template_name = 'auth/signup.html'
    model = get_user_model()
    form_class = SignUpForm

    def get_success_url(self) -> str:
        return reverse('home')

    def post(self, request, *args: str, **kwargs):
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            post = super().post(request, *args, **kwargs)
            post.status_code = 400
            return post
        messages.add_message(request, messages.SUCCESS, "Sign Up successfully")
        return super().post(request, *args, **kwargs)


class LogInView(generic.View):

    def get(self, request):
        context = {}
        form = LogInForm(request.POST)
        context['form'] = form
        return render(request, 'auth/login.html', context)

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            print(user)
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'auth/login.html', status=401, context=context)
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "Log In successfully")
        return redirect('home')

class LogOutView(generic.View):
    
    def get(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, "Logout successfully")
        return redirect('home')
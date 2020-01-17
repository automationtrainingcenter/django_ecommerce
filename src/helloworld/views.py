from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from helloworld.forms import ContactForm, LoginForm, RegistrationForm

User = get_user_model()

# Create your views here.


def home_page(request):
    context = {
        'title': 'Home Page',
        'content': 'Hello world, welcome to Home page'
    }
    if request.user.is_authenticated():
        context['premium_content'] = 'Premium Content'
    return render(request, 'helloworld/hello_world.html', context=context)


def about_page(request):
    context = {
        'title': 'About Page',
        'content': 'This is a basic ecommerce site'
    }
    return render(request, 'helloworld/hello_world.html', context=context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact Page',
        'content': 'Contact us using the following form',
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'helloworld/contact_page.html', context=context)


# user login
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user)
            return redirect('helloworld:home')
        else:
            print('error')

    return render(request, "auth/login.html", context=context)


def register_page(request):
    form = RegistrationForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        data = form.cleaned_data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        User.objects.create_user(username, email, password)
        return redirect('helloworld:login')
    return render(request, 'auth/register.html', context=context)

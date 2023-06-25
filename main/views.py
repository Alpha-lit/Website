from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import ContactForm, RegistrationForm
from django.views.generic import FormView, TemplateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# def Home_Page(request):

#     return render(request, "index.html", {})

def About_Page(request):
    
    return render(request, "about.html", {})

def Services_Page(request):
        
    return render(request, "service.html", {})

 
def Terms_Page(request):

    return render(request, 'terms.html', {})


def Privacy_Page(request):

    return render(request, 'privacy.html', {})


class HomeView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')
    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
# @method_decorator(login_required(login_url='login'), name='dispatch') 
class ServicesView(FormView):
    template_name = 'service.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')
    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

      
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')
    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
        
  
class ContactSuccessView(TemplateView):
    template_name = 'success.html'

# @login_required(login_url='login')   
def Details_Page(request):

    return render(request, "single.html", {})


#Account creation
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user:
                # Log in the user
                login(request, user)
                # Redirect to the home page
                return redirect('Home')
            
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form= RegistrationForm()

    return render(request, 'registration.html', {'form': form})

def login_user(request):
    error_message= ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log in the user
            login(request, user)
            return redirect('Home')  # Replace 'dashboard' with the desired redirect URL after login
        else:
            # Handle invalid credentials
            error_message = 'Invalid username or password. Please try again.'

    return render(request, 'login.html', {'error_message': error_message})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
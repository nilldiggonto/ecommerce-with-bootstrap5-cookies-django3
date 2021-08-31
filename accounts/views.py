from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def registrationView(request):
    
    template_name = 'accounts/register.html'

    if request.method == 'POST':
        username = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():

            return render(request,template_name,{'valid':False})
        else:
            user = User.objects.create(first_name=fname,last_name=lname,username=username,email=username,is_active=True)
            user.set_password(password)
            # user.active=False
            user.save()
            ### SENDING EMAIL FOR VERIFICATION
            # current_site = str(get_current_site(request).domain)
            # print(current_site)
            # mail_subject = 'Activate your newsCarrier account.'
            # message = render_to_string('acc_active_email.html', {
            #     'first_name': user.first_name,
                
            #     'last_name':user.last_name,
            #     'domain': current_site,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            # print(message)
            # plain_message = strip_tags(message)

            # to_email = username
            # email = EmailMessage(
            #             mail_subject, plain_message, to=[to_email]
            # )
            # # email.attach_alternative(message, 'text/html')
            # email.send()
            # request.session['vmsg'] = True

            return redirect('auth-login')
    
    return render(request,template_name,{'valid':True})



def loginView(request):
    template_name = 'accounts/login.html'
    a = ''
    if request.user.is_authenticated:
        return redirect('dashboard-home')
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username,is_active=False):
            a = 'ask antu to verify. will automate later'

        # print(username,password)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home-page')
        else:
            a = 'please register sir'

    return render(request,template_name,context={'a':a})



@login_required
def logoutView(request):
    user = logout(request)
    return redirect('home-page')
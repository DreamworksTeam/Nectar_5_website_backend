from django.shortcuts import render, redirect
from .forms import Support_Form, Contact_Form, Get_Started_Form
from .models import Support
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string


# Create your views here.
# home page
def index(request):
    return render(request, 'website/index.html', {})


# At a glance page
def at_a_glance(request):
    context = {'At_a_glance': 'active'}
    return render(request, 'website/at-a-glance.html', context)

# How it works Page
def how_it_works(request):
    context = {'how_it_works': 'active'}
    return render(request, 'website/how-it-works.html', context)

# Features page
def features(request):
    context = {'features': 'active'}
    return render(request, 'website/features.html', context)

def send_html_email(to_list, subject, template_name, context, sender = settings.EMAIL_HOST_USER):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()


# support page
def support(request):
    if request.method == 'POST':
        support_form = Support_Form(request.POST)
        # check if form is valid
        if support_form.is_valid():
            full_name = support_form.cleaned_data['full_name']
            phone_no = support_form.cleaned_data['phone']
            user_email = support_form.cleaned_data['email']
            problem = support_form.cleaned_data['problem']
            complaint = support_form.cleaned_data['complaint']

            # print the data
            print(full_name)
            print(phone_no)
            print(user_email)
            print(problem)
            print(complaint)

            # problem & context of complaint
            email = [user_email]
            title = 'Nectar 5 Support:- {}'.format(problem)
            sender = settings.EMAIL_HOST_USER
            our_email = [settings.EMAIL_HOST_USER]

            context = {
                'full_name': full_name,
                'phone_no': phone_no,
                'complaint': complaint,
                'user_email': user_email,
                'problem': problem
            }

            try:

                # send email to the person and self
                send_html_email(email, title, 'support_email.html', context, sender)
                send_html_email(our_email, title, 'support_email_self.html', context, sender)

                # send success message
                 # support_form.save()
                support_form.save()
                # on submit message
                messages.success(request, 'Thank you for contacting Support, One of our support agents will contact you shortly.')
                # return redirect

            except Exception as e:
                print(e)
                messages.error(request, 'Oops! Something went wrong')

           
            return redirect('support')
            

    else:

        support_form = Support_Form()
    context = {
        'support': 'active',
        'support_form': support_form,
    
    }
    return render(request, 'website/support.html', context)

# contact us page
def contact_us(request):
    if request.method == 'POST':
        contact_form = Contact_Form(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            # success message
            messages.success(request, 'Thanks for contacting us! We will be in touch with you shortly.')
            return redirect('contact-us')

    else:

        contact_form = Contact_Form()
    context = {
        'contact_us': 'active',
        'contact_form': contact_form, 
    }
    return render(request, 'website/contact_us.html', context)

# faq page
def faq(request):
    context  ={
        'faq': 'active'
    }
    return render(request, 'website/faq.html',  context)


# get started page
def get_started(request):
    if request.method == 'POST':
        # assign the values from post request to form
        get_started_form = Get_Started_Form(request.POST)
        # check if form is valid
        if get_started_form.is_valid():
            # retrieve data from form
            organization = get_started_form.cleaned_data['organization']
            user_email = get_started_form.cleaned_data['email']
            phone = get_started_form.cleaned_data['phone']
            location = get_started_form.cleaned_data['location']
            entry = get_started_form.cleaned_data['entry']

            # send email details
            email = [settings.EMAIL_HOST_USER]
            title = 'New Survey Request From - {}'.format(organization)
            sender = settings.EMAIL_HOST_USER

            # context
            context = {
                'organization': organization,
                'user_email': user_email,
                'phone': phone,
                'location': location,
                'entry': entry,
            }

            # send email
            try:
                send_html_email(email, title, 'get-started-email.html', context, sender)

            except Exception as e:
                print(e)


            # save form in db
            get_started_form.save()
            messages.success(request, 'Thank you for your request to join our mobile work force. We will contact you soon')
            return redirect('get-started')


    else:

        get_started_form = Get_Started_Form()

    context = {
        'get_started_form': get_started_form,
    }

    return render(request, 'website/get-started.html', context)












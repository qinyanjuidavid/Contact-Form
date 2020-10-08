from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError
from myapp.forms import ContactForm,FeedbackForm
from myapp.models import Feedback
from django.contrib import messages
from django.conf import settings



def ContactView(request):
    if request.method=="GET":
        form=ContactForm()
    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            from_email=form.cleaned_data['from_email']
            message=form.cleaned_data['message']
            try:
                send_mail(subject,message,from_email,['tabibuhospital.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
    context={
    'form':form
    }
    return render(request,'myapp/contact.html',context)
def FeedbackView(request):
    form= FeedbackForm()
    if request.method=="POST":
        form= FeedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            sender=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            message=f"By {name},\n{message}"
            try:
                send_mail(subject,message,sender,['tabibuhospital.com'])
                form.save()
                messages.info(request,'Feedback was successfully submitted!')
            except BadHeaderError:
                messages.danger(request,'Invalid header found!')
                return HttpResponseRedirect("/feedback/")
            return HttpResponseRedirect('/feedback/')
        else:
            form= FeedbackForm()
    context={
    'form':form
    }
    return render(request,'myapp/feedback.html',context)

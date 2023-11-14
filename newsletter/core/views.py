from django.shortcuts import render
from .forms import SubscriberForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def index(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():

            subscriber = form.save()

            context = {'email': subscriber.email}
            email_content = render_to_string('core/subcription_thank_you.html', context)

            email_subject = 'Thank you for Subscribing'
            recipient_list = [subscriber.email]
            from_email = settings.EMAIL_HOST_USER

            send_mail(
                email_subject,
                '',
                from_email,
                recipient_list,
                html_message=email_content,
                fail_silently=False
            )

            return render(request, 'core/thank_you.html', context)
        
    else:
        form = SubscriberForm()
    return render(request, 'core/index.html', {'form': form})
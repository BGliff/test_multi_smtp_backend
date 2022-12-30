from django.shortcuts import render
from django_multi_mail_backend import send_mail

# Create your views here.
from test_multi_smtp_backend import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def send_email(request):
    backend = settings.SMTP_KEY
    try:
        send_mail(
            subject='this is test email',
            message='this is test email',
            from_email=None,
            recipient_list=['putinevgeniy@gmail.com'],
            use_backend=backend,
            fail_silently=False
        )
    except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, template_name=None)
    return Response({"message": "ok"}, status=status.HTTP_200_OK, template_name=None)

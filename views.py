import io
import sys
from .models import Alert
from .models import Stacks
from weasyprint import HTML
from django.http import FileResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.shortcuts import render, redirect
from django.template.loader import get_template

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serial import AlertSerial, StacksSerial


############################################Pour les alertes
@api_view(['GET'])
def getData(request):
    items = Alert.objects.all()
    serialer = AlertSerial(items, many=True)
    return Response(serialer.data)

@api_view(['POST'])
def addAlert(request):
    serialer = AlertSerial(data=resquest.data)
    if serialer.is_valid():
        serializer.save()
    return Response()
###############################################Fin pour les alertes

################################################Debut pour la descrition
@api_view(['GET'])
def getDataDescription(request):
    items = Stacks.objects.all()
    serialer = StacksSerial(items, many=True)
    return Response(serialer.data)

@api_view(['POST'])
def addDescription(request):
    serialer = StacksSerial(data=resquest.data)
    if serialer.is_valid():
        serializer.save()
    return Response()
################################################fin pour la description


def salutation(request):
	stack_afficher = Stacks.objects.all()
	alert_afficher = Alert.objects.all()
	return render(request, 
        'rapport/base_repport.html', 
        {'stack_afficher':stack_afficher, 'alert_afficher':alert_afficher})

def makepdf(html):
    """Generate a PDF file from a string of HTML."""
    htmldoc = HTML(string=html, base_url="")
    return htmldoc.write_pdf()


def genererpdf(request):
    stack_afficher = Stacks.objects.all()
    alert_afficher = Alert.objects.all()
    template_path = 'rapport/pdf_report.html'
    context = {'stack_afficher': stack_afficher, 'alert_afficher': alert_afficher}
    template = get_template(template_path)
    html = template.render(context)
    pdf = makepdf(html)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="monRapportwatchman.pdf"'
    return response

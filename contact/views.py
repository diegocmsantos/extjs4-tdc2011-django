# -*- coding: utf-8 -*-

from django.db import transaction
from django.http import HttpResponse
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response, get_object_or_404
from django.utils.translation import gettext as __
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from models import Contact

from django.core import serializers
import simplejson as json

def view(request):
    page = int(request.GET.get('page', 0))
    start = int(request.GET.get('start', 0))
    limit = int(request.GET.get('limit', 0))
    total_contacts = Contact.objects.all().count()
    contacts = Contact.objects.all()[start:limit*page]
    list = []
    for contact in contacts:
        list.append(model_to_dict(contact, fields=[field.name for field in contact._meta.fields]))
    context = {
        'total': total_contacts,
        'data': list,
        'success': True
    }
    return HttpResponse(json.dumps(context), mimetype="application/json")

def create(request):
    list = []
    if request.POST:
        data = json.loads(request.POST.keys()[0])
        contact = Contact.objects.latest('id')
        contact.id = contact.id + 1
        contact.name = data['data']['name']
        contact.phone = data['data']['phone']
        contact.email = data['data']['email']
        contact.save()
        list.append(model_to_dict(contact, fields=[field.name for field in contact._meta.fields]))
    context = {
        'total': list.__len__(),
        'data': list,
        'success': True
    }
    return HttpResponse(json.dumps(context), mimetype="application/json")

def update(request):
    json_data = json.loads(request.POST.keys()[0])
    contact = get_object_or_404(Contact, pk=json_data['data']['id'])
    contact.email = json_data['data']['email']
    contact.name = json_data['data']['name']
    contact.phone = json_data['data']['phone']
    contact.save()
    list = []
    list.append(model_to_dict(contact, fields=[field.name for field in contact._meta.fields]))
    context = {
        'total': list.__len__(),
        'data': list,
        'success': True
    }
    return HttpResponse(json.dumps(context), mimetype="application/json")

def delete(request):
    json_data = json.loads(request.POST.keys()[0])
    contact = get_object_or_404(Contact, pk=json_data['data']['id'])
    contact.delete()
    context = {
        'success': True
    }
    return HttpResponse(json.dumps(context), mimetype="application/json")
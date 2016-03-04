# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response

def index(request):
    output = _(u"首页.")
    return render_to_response('index.html', locals())


from django.shortcuts import render_to_response, render
from django.template import RequestContext


def h404(request):
    return render(request, 'home/404_custom.html', {})


def h500(request):
    response = render_to_response('home/404_custom.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
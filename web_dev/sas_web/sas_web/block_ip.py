from django.shortcuts import render
from startpage.models import Banned


class BlockedIpMiddleware(object):

    def process_request(self, request):
        if get_client_ip(request) in [b.ip_address for b in
                                      Banned.objects.all()]:
            return render(request, 'startpage/bann.html')
        return None


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

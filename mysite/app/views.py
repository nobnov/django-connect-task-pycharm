from django.http import HttpResponse
from django.shortcuts import redirect
from urllib.parse import urlencode


# Create your views here.
def index(request):
    return HttpResponse("<br><a href="'redirect_path/'">リダイレクト</a>")


def redirect_path(request):
    post_number = "3"
    post_value = "test"
    redirect_url = redirect("redirect page", value_int=post_number, value_str=post_value)
    parameters = urlencode({"param1": "情報1", "param2": "情報2"})
    url = f"{redirect_url['Location']}?{parameters}"
    return redirect(url)


def redirect_page(request, value_int, value_str):
    param1 = request.GET.get("param1")
    param2 = request.GET.get("param2")
    return HttpResponse(f"POST: {value_int}, {value_str} <br>GET: {param1}, {param2}")

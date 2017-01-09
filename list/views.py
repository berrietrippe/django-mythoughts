from django.shortcuts import render, get_object_or_404
from .models import Quote
from django.utils import timezone
from .forms import addThoughtForm
from django.db import models
from django.http import HttpResponseRedirect
from .serializers import QuoteSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
def quote_list(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = addThoughtForm(request.POST)
            if form.is_valid():
                # user = User(request.user)
                b = Quote(author=request.user, text=request.POST.get("text", ""))
                b.save()
            return HttpResponseRedirect("#")
        else:
            quotes = Quote.objects.filter(
            added_date__lte=timezone.now()).order_by('-added_date')

            return render(request, 'list/quote_list.html', {'quotes': quotes})
    else:
        return HttpResponseRedirect("/login")


def quote_detail(request, pk):
        quote = get_object_or_404(Quote, pk=pk)
        return render(request, 'list/quote_detail.html', {'quote': quote})

def quote_delete(request, pk):
    Quote.objects.filter(pk=pk).delete()
    return HttpResponseRedirect("../../../")

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_quotes(request):
    if request.method == 'GET':
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_single_quote(request, pk):
    try:
        quote = Quote.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuoteSerializer(quote)
        return Response(serializer.data)


from rest_framework import generics

from App.renderers import Child
from .models import Identity ##file se import karne ke liye dot
from .serializers import IdentitySerializer
from django.shortcuts import render
# for Identity
class IdentityList(generics.ListCreateAPIView):
    queryset=Identity.objects.all()
    serializer_class=IdentitySerializer
    renderer_classes=(Child,)
class IdentityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Identity.objects.all()
    serializer_class=IdentitySerializer
    renderer_classes=(Child,)

#method for displaying form
def displayForm(request):
    if request.method=="POST": #form me jab tag method="post"
        first=request.POST['a'] #a hold the value of input,comes from url
        last=request.POST['b']#b hold the value of input,comes fom url
        obj=Identity(first_name=first,last_name=last) #passiong captured value to model,
        print("RES",obj)#jo model return kar raha h wah print karega .eg last name
        obj.save() #saving

    
    return render(request,"App/index.html")
    #POST /forms?csrfmiddlewaretoken=TEv833oCMPcpfUbWnz4QgnF94K4MWvxCrMJbIHDor7WBjfU8H17OcAIDyQWTrAPn&a=hello&b=world HTTP/1.1" 200 in url
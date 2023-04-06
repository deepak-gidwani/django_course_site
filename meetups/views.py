from django.shortcuts import render
from .models import *
from .forms import *
from django.views import View
from django.shortcuts import redirect
from django.http import HttpResponse
# from django.http import Http404

# from django.http import HttpResponse
# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request,'meetups/index.html',{
        'meetups':meetups,
    })

# def meetup_details(request,meetup_slug):
#     try:
#         selected_meetup = Meetup.objects.get(slug=meetup_slug)
#         registeration_form = RegisterationForm()
#         return render(request,'meetups/meetup-details.html',{
#             'meetup_found':True,
#             'meetup':selected_meetup,
#             'form':RegisterationForm
#         })
#     except Exception as exc:
#         return render(request,'meetups/meetup-details.html',{
#             'meetup_found':False,
#         })
#         # raise Http404()

class Meetup_details(View):
    def get(self,request,meetup_slug):
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        registeration_form = RegisterationForm()
        return render(request,'meetups/meetup-details.html',{
            'meetup_found':True,
            'meetup':selected_meetup,
            'form':registeration_form
        })
    def post(self,request,meetup_slug):
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        # return redirect('../')
        registeration_form = RegisterationForm(request.POST)
        if registeration_form.is_valid():
            user_email = registeration_form.cleaned_data['email']
            participant , _ = Participant.objects.get_or_create(email=user_email)  # it returns a tuple of participant and was_created
            selected_meetup.participants.add(participant) 
            return redirect('confirm-registeration')
        else:
            # print(registeration_form.is_valid())
            return render(request,'meetups/meetup-details.html',{
            'meetup_found':True,
            'meetup':selected_meetup,
            'form':registeration_form
        })

def confirm_registeration(request):
    return render(request,'meetups/registeration-success.html')
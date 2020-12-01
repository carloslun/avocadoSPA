from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from services.models import Service
from clients.models import Client
from contact.forms import ContactForm
from social.models import Social
from django.urls import reverse

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["services_list"] = Service.objects.all()
        context["clients_list"] = Client.objects.all()
        context["social_list"] = Social.objects.all()
        # context["form"] = form;
        return context


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST);
        if form.is_valid():
            form.save()
            return redirect(reverse('core:index')+'?ok')
            # var = form['name']
            # import pdb
            # pdb.set_trace()
            

        else:
            # import pdb
            # pdb.set_trace()
            return redirect(reverse('core:index')+'?notok')
            # return render(request, 'core/index.html', {'form':form})
            


    return redirect('/')
        
        


        # form.name = 
   
   
    
    


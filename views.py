# views.py

# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from .models import GeeksModel

# class GeeksCreate(CreateView):
#     model = GeeksModel
#     fields = ['title', 'description']
#     template_name = 'geeksmodel_form.html'  # Adjust the template name based on your preference

#     # Optionally, you can specify a success URL after the form submission
#     success_url = '/success/'  # Adjust the success URL based on your requirements

#listview
# views.py

# from django.views.generic.list import ListView
# from .models import GeeksModel

# class GeeksList(ListView):
#     model = GeeksModel
#     template_name = 'geeksmodel_list.html'  # Adjust the template name based on your preference

#     # Optionally, you can specify the context variable name for the list of objects (optional)
#     context_object_name = 'geeks_list'
#detailview
# views.py

# from django.views.generic.detail import DetailView
# from .models import GeeksModel

# class GeeksDetailView(DetailView):
#     model = GeeksModel
#     template_name = 'geeksmodel_detail.html'  # Adjust the template name based on your preference
#     context_object_name = 'geeks_model'

#updateview
# views.py

from django.views.generic.edit import UpdateView
from .models import GeeksModel

class GeeksUpdateView(UpdateView):
    model = GeeksModel
    fields = ["title", "description"]
    template_name = 'geeksmodel_update.html'  # Adjust the template name based on your preference
    success_url = '/updateview/'  # Adjust the success URL based on your requirements

from django.shortcuts import render
from hostelapp.models import *
from .forms import *


# Create your views here.

def create_block(request):
    create_block_form = Block_form()
    if request.method == 'POST':
        create_block_form = Block_form(request.POST)
        if create_block_form.is_valid():
            create_block_form.save()

    context = {'form_table': create_block_form}
    return render(request, 'cheif_warden/create_block_page.html', context)

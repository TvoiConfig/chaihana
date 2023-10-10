from django.shortcuts import render
from .forms import RecordForm

def index(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()

    return render(request, 'main/index.html', {'form': form})
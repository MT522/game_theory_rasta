from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddScoreForm
from .models import Group
from django.contrib import messages

# Create your views here.
def homepage_view(request):
    #groups1 = Group.objects.all().filter(gender='F').order_by('-score')
    #groups2 = Group.objects.all().filter(gender='M').order_by('-score')
    #return render(request, 'standings.html', {'groups1': groups1, 'groups2': groups2})
    return render(request, 'home.html')

def addScore_view(request):
    if request.method == 'POST':
        form = AddScoreForm(request.POST)
        if form.is_valid():
            group_id = form.cleaned_data['id']
            score_increment = form.cleaned_data['score']

            group = get_object_or_404(Group, id=group_id)
            group.score += score_increment
            group.save()

            messages.success(request, 'Score updated successfully!')
            return redirect('homepage')
    else:
        form = AddScoreForm()
    return render(request, 'addscore.html', {'form': form})

def standings_view(request):
    #groups1 = Group.objects.all().filter(gender='F').order_by('-score')
    #groups2 = Group.objects.all().filter(gender='M').order_by('-score')
    groups = Group.objects.all().order_by('-score')
    #return render(request, 'standings.html', {'groups1': groups1, 'groups2': groups2})
    return render(request, 'standings.html', {'groups': groups})

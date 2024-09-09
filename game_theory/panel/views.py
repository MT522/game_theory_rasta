from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddScoreForm, AddNumberForm
from .models import Group
from authenticator.models import GTUser
from django.contrib import messages
from math import exp

# Create your views here.
def homepage_view(request):
    #user = request.user
    #groups1 = Group.objects.all().filter(gender='F').order_by('-score')
    #groups2 = Group.objects.all().filter(gender='M').order_by('-score')
    #return render(request, 'standings.html', {'groups1': groups1, 'groups2': groups2, 'user': user})
    return render(request, 'home.html')

def theory_view(request):
    return render(request, 'theory.html')

def addScore_view(request):
    user = request.user

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
    return render(request, 'addscore.html', {'form': form, 'user': user})

def standings_view(request):
    user = request.user
    groups1 = Group.objects.all().filter(gender='F').order_by('-score')
    groups2 = Group.objects.all().filter(gender='M').order_by('-score')
    #groups = Group.objects.all().order_by('-score')
    return render(request, 'standings.html', {'groups1': groups1, 'groups2': groups2, 'user': user})
    #return render(request, 'standings.html', {'groups': groups})

def number_view(request):
    user = request.user

    if request.method == 'POST':
        form = AddNumberForm(request.POST, request=request)
        if form.is_valid():
            group_id = form.cleaned_data['id']
            number1 = form.cleaned_data['number1']
            number2 = form.cleaned_data['number2']
            number3 = form.cleaned_data['number3']

            group = get_object_or_404(Group, id=group_id)
            group.number1 = number1
            group.number2 = number2
            group.number3 = number3
            group.save()

            messages.success(request, 'Numbers submitted successfully!')
            return redirect('homepage')
    else:
        form = AddNumberForm(request=request)
    return render(request, 'addnumber.html', {'form': form, 'user': user})

def plot_group_data(request):
    groups = Group.objects.all()
    all_values = []

    for group in groups:
        if group.number1 != None:
            all_values.append(group.number1)
        if group.number2 != None:
            all_values.append(group.number2)
        if group.number3 != None:
            all_values.append(group.number3)

    mean_value = sum(all_values) / len(all_values) if all_values else 0

    context = {
        'all_values': all_values,
        'mean_value': mean_value*2/3,
    }
    return render(request, 'plot_group_data.html', context)

def commit_game_score():
    groups = Group.objects.all()
    all_values = []

    for group in groups:
        if group.number1 != None:
            all_values.append(group.number1)
        if group.number2 != None:
            all_values.append(group.number2)
        if group.number3 != None:
            all_values.append(group.number3)

    mean_value = sum(all_values) / len(all_values) * 2 / 3 if all_values else 0
    
    for group in groups:
        scores = []
        if group.number1 != None:
            scores.append(1/exp(abs(mean_value - group.number1)/50)*1000/1.5/3)
        if group.number2 != None:
            scores.append(1/exp(abs(mean_value - group.number2)/50)*1000/1.5/3)
        if group.number3 != None:
            scores.append(1/exp(abs(mean_value - group.number3)/50)*1000/1.5/3)

        group.score += sum(scores)/3
        print(f"Group {group.id} got {sum(scores)/3} This round!")
        group.save()








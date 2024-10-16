from django.shortcuts import get_object_or_404, redirect, render

from meetings.forms import MeetingForm
from meetings.models import Meeting, Room

def meetings_list_view(request):

    meetings = Meeting.objects.all()  # Get all meetings

    return render(request, 'meetings.html', {'meetings': meetings, })

def detail(request, id):

    meeting = get_object_or_404(Meeting, id=id)  

    return render(request, "details.html", {"meeting": meeting})

def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde le meeting si le formulaire est valide
            return redirect('list')  # Redirige vers une liste de meetings ou une autre page après ajout
    else:
        form = MeetingForm()

    return render(request, 'new.html', {'form': form})

def   Room_list_view(request):

    room = Room.objects.all()  # Get all meetings

    return render(request, 'room.html', {'room': room, })

def room(request, id):

    room = get_object_or_404(Room, id=id)  

    return render(request, "room.html", {"room": room})
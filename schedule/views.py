from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Meeting
from .forms import MeetingForm


@login_required
def schedule_home(request):
    meetings = Meeting.objects.order_by('date', 'time')
    upcoming = Meeting.objects.filter(date__gte=now().date()).order_by('date')
    return render(request, 'schedule/schedule_home.html', {
        'meetings': meetings,
        'upcoming': upcoming,
    })


@login_required
def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule:schedule_home')
    else:
        form = MeetingForm()
    return render(request, 'schedule/create_meeting.html', {'form': form})


@login_required
def delete_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    meeting.delete()
    return redirect('schedule:schedule_home')
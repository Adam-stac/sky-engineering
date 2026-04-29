from django.shortcuts import render
from core.models import EngineeringTeam

def team_list(request):
    teams = EngineeringTeam.objects.all()
    return render(request, "teams/team_list.html", {"teams": teams})
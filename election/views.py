from django.shortcuts import render, redirect
from .models import Candidate, Vote
from django.db.models import Count

def index(request, username):
    candidates = Candidate.objects.all()
    
    has_voted = Vote.objects.filter(voter_name=username).exists()
    
    my_vote = Vote.objects.filter(voter_name=username).first()

    results = Candidate.objects.annotate(total_votes=Count('vote'))
    
    return render(request, 'election/index.html', {
        'username': username,
        'candidates': candidates,
        'has_voted': has_voted,
        'my_vote': my_vote,
        'results': results
    })

def cast_vote(request, username, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    if not Vote.objects.filter(voter_name=username).exists():
        Vote.objects.create(candidate=candidate, voter_name=username)
    return redirect('index', username=username)
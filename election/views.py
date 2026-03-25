from django.shortcuts import render, redirect
from .models import Candidate, Vote
from django.db.models import Count

def index(request):
    
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    candidates = Candidate.objects.all()
    
    
    has_voted = Vote.objects.filter(session_id=session_key).exists()
   
    results = Candidate.objects.annotate(total_votes=Count('vote'))
    
    context = {
        'candidates': candidates,
        'has_voted': has_voted,
        'results': results
    }
    return render(request, 'election/index.html', context)

def cast_vote(request, candidate_id):
    session_key = request.session.session_key
    candidate = Candidate.objects.get(id=candidate_id)
   
    if not Vote.objects.filter(session_id=session_key).exists():
        Vote.objects.create(candidate=candidate, session_id=session_key)
        
    return redirect('index')
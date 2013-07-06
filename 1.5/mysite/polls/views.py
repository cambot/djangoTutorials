from django.http import HttpResponse

def index(request):
	return HttpResponse("Poll Index")

def detail(request, poll_id):
	return HttpResponse("details of poll %s" % poll_id)

def results(request, poll_id):
	return HttpResponse("results for poll %s" % poll_id)

def vote(request, poll_id):
	return HttpResponse("vote on poll %s" % poll_id)

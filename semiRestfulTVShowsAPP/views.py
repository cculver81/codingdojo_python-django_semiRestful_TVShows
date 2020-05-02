from django.shortcuts import render, redirect
from .models import Show
from time import strftime

def index(request):
    return redirect('/shows')

# code for shows.html template
def shows(request):
    context = {
        'allShows' : Show.objects.all()
    }  
    return render(request, 'shows.html', context)


# code for newShow.html template
def newShow(request):
    return render(request, 'newShow.html')

def createShow(request):
    pTitle = request.POST['title']
    # print(pTitle)
    pNetwork = request.POST['network']
    # print(pNetwork)
    pReleaseDate = request.POST['releaseDate']
    # print(pReleaseDate)
    pDescription = request.POST['description']
    # print(pDescription)

    Show.objects.create(title = pTitle,network = pNetwork, releaseDate = pReleaseDate, description = pDescription)
    return redirect('/shows/new')

# code for editShow.html template
def editShow(request, showID):
    S = Show.objects.get(id = showID)
   
    context = {
        'id' : S.id,
        'title' : S.title,
        'network' : S.network,
        'releaseDate' : S.releaseDate.strftime('%Y-%m-%d'),
        'description' : S.description
    }
    # print(context)
    return render(request, 'editShow.html', context)

def updateShow(request, showID):
    print('It ran at least.')
    
    pTitle = request.POST['title']
    pNetwork = request.POST['network']
    pReleaseDate = request.POST['releaseDate']
    pDescription = request.POST['description']

    # print(pTitle)
    # print(pNetwork)
    # print(pReleaseDate)
    # print(pDescription)

    S = Show.objects.get(id = showID)
    S.title = pTitle
    S.network = pNetwork
    S.releaseDate = pReleaseDate
    S.description = pDescription
    S.save()
    return redirect('/shows/' + str(showID) + '/edit')

# code for tvShow.html template
def tvShow(request, showID):
    S = Show.objects.get(id = showID)
   
    context = {
        'id' : S.id,
        'title' : S.title,
        'network' : S.network,
        'releaseDate' : S.releaseDate.strftime('%Y-%m-%d'),
        'description' : S.description,
        'lastUpdated' : S.updated_at.strftime('%B %d, %Y %I:%M %p')
    }
    # print(context)
    return render(request, 'tvShow.html', context)

# code to DELETE a Show Record
def deleteShow(request, showID):
    S = Show.objects.get(id = showID)
    S.delete()
    return redirect('/shows')

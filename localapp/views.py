# from rest_framework import generics
from django.shortcuts import render,redirect
from .models import *
# from .serializers import LocationSerializer, ItemSerializer
from storage.settings import db


def fetch_data_anime(doc_ID='ame3'):
    
    anime = db.collection('anime')
    anime_data = anime.document(doc_ID).get().to_dict()
    # print(anime_data)
    hastags=anime_data['hastags']
    name=anime_data['name'].get().to_dict()['name']
    image_url=anime_data['image_url']
    watch_urls=anime_data['watch_urls'].get().to_dict()
    description=anime_data['description']
    # print(watch_urls)
    return hastags, name, watch_urls,image_url,description

def index(request):

    hastags, name,watch_urls,image_url,description = fetch_data_anime()
    watch_urls=[watch_urls['url1'],watch_urls['url2']]
    params = {
        'name': name,
        'hashtags': hastags,
        'image_url': image_url,
        'description': description,
        'watch_urls': watch_urls
    }

    # print(params)
    return render(request, 'homepage.html', params)


def add_anime(request):
    if request.method == 'POST':
        name = request.POST.get('anime_name')
        image = request.POST.get('image_url')
        watch_url1 = request.POST.get('watch_url1')
        watch_url2 = request.POST.get('watch_url2')
        # trailer_url1 = request.POST.get('trailer_url1')
        # trailer_url2 = request.POST.get('trailer_url2')
        description = request.POST.get('description')
        hashtags = request.POST.get('hashtag')




        animename,count=create_animename(name)
        watch_urls={
            'url1':watch_url1,
            'url2':watch_url2
        }
        web_urls=create_web_url(watch_urls,count)
        data={
            'name':animename,
            'image_url':image,
            'watch_urls':web_urls,
            'description':description,
            'hastags':hashtags
            }
        print(f">>>>>>>>>>>>>>>>>>>---------{count}")

        anime= db.collection('anime').document(f'ame{count}')
        anime.set(data)
        print('Anime Created')

        request.session.flush()
        return redirect('index')
    return render(request, 'add_anime.html')
    


def create_animename(anime_name):
    count=0
    with open('./series.json', 'r') as f:
        data = f.read()
    
    # Process the data
    data = data.split('+')
    animeno = f"ame{data.count('@')}"
    count=data.count('@')
    # Write the new data to the file
    with open('./series.json', 'a') as f:
        f.write('@+')
    
    # Create the new anime name in Firestore
    anime_doc = db.collection('AnimeName').document(animeno)
    
    anime_doc.set({
        'name': anime_name
    })

    print('Anime Name Created')
    print(f">>>>>>>>>>>>>>>>>>>---------{count}")
    return anime_doc,count




def create_web_url(web_url_data,count):
    print(f">>>>>>>>>>>>>>>>>>>---------{count}")

    url_location= db.collection('url_location').document(f'ame{count}')
    url_location.set(web_url_data)

    print('url_location Created')

    return url_location





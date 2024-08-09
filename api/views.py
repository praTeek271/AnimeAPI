from django.http import JsonResponse,HttpResponse

from localapp.views import fetch_data_anime
import json




def apiindex(request,doc_ID='np14FaSKyK9DiLzMoYV9'):
    hastags, name,watch_urls,image_url,description = fetch_data_anime(doc_ID=doc_ID)
    watch_urls=[watch_urls['url1'],watch_urls['url2']]

    http_temp={
        "name": name,
        "image_url": image_url,
        "description": description,
        "watch_urls": [watch_urls[0],watch_urls[1]],
            }

    return HttpResponse(json.dumps(http_temp), content_type="application/json")
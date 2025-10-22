from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Place

# def main_page(request):
    # return HttpResponse("""
    # <h1>Карта интересных мест Москвы</h1>
    # <p>Backend для интерактивной карты активного отдыха</p>
    # <p><em>Проект</em></p>
    # """)
    # 
    
def show_map(request):
    return HttpResponse("""
    <h1>Moscow Discovery API</h1>
    <p>Backend работает</p>
    <p>Доступные endpoints:</p>
    <ul>
        <li><a href="/places/geojson/">/places/geojson/</a> - GeoJSON всех мест</li>
        <li><a href="/places/1/">/places/1/</a> - детали места (id=1)</li>
        <li><a href="/admin/">/admin/</a> - админка</li>
    </ul>
    """)
def places_geojson(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point", 
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"/places/{place.id}/"
            }
        }
        features.append(feature)
    
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    return JsonResponse(geojson, safe=False)
def place_details(request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        
        response_data = {
            "title": place.title,
            "imgs": [image.image.url for image in place.images.all()],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lng": place.lng,
                "lat": place.lat
            }
        }
        
        return JsonResponse(response_data, safe=False)
        
    except Place.DoesNotExist:
        return JsonResponse({"error": "Place not found"}, status=404)
    
    
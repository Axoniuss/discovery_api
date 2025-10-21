from django.http import HttpResponse

def main_page(request):
    return HttpResponse("""
    <h1>Карта интересных мест Москвы</h1>
    <p>Backend для интерактивной карты активного отдыха</p>
    <p><em>Проект для Артёма</em></p>
    """)
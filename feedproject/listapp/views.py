from django.shortcuts import render
from listapp.forms import NasaForm
import requests


def home(request):

    if request.method == 'POST':

        form = NasaForm(request.POST)

        if form.is_valid():
            response = requests.get(
                f'https://api.nasa.gov/neo/rest/v1/feed?start_date={form.cleaned_data["start"]}&end_date={form.cleaned_data["end"]}&detailed=true&api_key=DEMO_KEY')
            nasa_data = response.json()

            return render(request, 'listapp/home.html', {
                'element_count': nasa_data['element_count'],
                'near_earth_objects': nasa_data['near_earth_objects'][form.cleaned_data["start"].strftime('%Y-%m-%d')],
                'form': form,
            })

        else:

            return render(request, 'listapp/home.html', {'form': form, })

    else:

        form = NasaForm()

        return render(request, 'listapp/home.html', {
            'form': form,
        })

from django.shortcuts import render, redirect
from listapp.forms import NasaForm
import requests
import re

DATE_FORMAT = r"[1-2]\d{3}-[0-1][0-2]-[0-3][0-9]"


def home(request):

    if request.method == 'POST':

        form = NasaForm(request.POST)

        if form.is_valid():
            response = requests.get(
                f'https://api.nasa.gov/neo/rest/v1/feed?start_date={form.cleaned_data["start"]}&end_date={form.cleaned_data["end"]}&detailed=true&api_key=DEMO_KEY')
            nasa_data = response.json()
            start_date = form.cleaned_data["start"].strftime('%Y-%m-%d')
            end_date = form.cleaned_data["end"].strftime('%Y-%m-%d')

            return render(request, 'listapp/home.html', {
                'element_count': nasa_data['element_count'],
                'near_earth_objects': nasa_data['near_earth_objects'][start_date],
                'form': form,
                'start_date': start_date,
                'end_date': end_date,
            })

        else:

            return render(request, 'listapp/home.html', {'form': form, })

    else:

        form = NasaForm()

        return render(request, 'listapp/home.html', {
            'form': form,
        })


def list(request, start_date, end_date):

    if (re.match(DATE_FORMAT, start_date) and
        re.match(DATE_FORMAT, end_date) and
            (start_date <= end_date)):

        form = NasaForm()

        response = requests.get(
            f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&detailed=true&api_key=DEMO_KEY')
        nasa_data = response.json()

        return render(request, 'listapp/home.html', {
            'element_count': nasa_data['element_count'],
            'near_earth_objects': nasa_data['near_earth_objects'][start_date],
            'form': form,
            'start_date': start_date,
            'end_date': end_date,
        })

    else:

        return redirect('/second')


def object_detail(request, id, start_date, end_date):

    response = requests.get(
        f'https://api.nasa.gov/neo/rest/v1/neo/{id}?api_key=DEMO_KEY')
    object_data = response.json()

    return render(request, 'listapp/object_detail.html', {
        'id': id,
        'object_data': object_data,
        'start_date': start_date,
        'end_date': end_date,
    })

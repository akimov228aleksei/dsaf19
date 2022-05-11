from django.shortcuts import render
from .models import Points


def point(request):
    # Function that displays map
    return render(request, 'index.html')


def save_point(request):
    # Function that saves coordinates in DB
    coordinates = request.GET.get('coordinates')
    if coordinates:
        # Convert string coordinates to list
        coordinates = coordinates[7:-1].replace(' ', '').split(',')

        point = Points(point=f'Point({coordinates[0]} {coordinates[1]})')
        point.save()
        return render(request, 'points_list.html')
    else:
        points = Points.objects.all()
        return render(request, 'points_list.html', {'points': points})
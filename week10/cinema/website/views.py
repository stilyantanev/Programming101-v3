from django.shortcuts import render
from .models import Movie, Projection, Reservation
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    projections = {movie: movie.projection_set.all() for movie in movies}
    all_projections = Projection.objects.all()
    reservations = {projection: projection.reservation_set.all() for projection in all_projections}
    return render(request, "index.html", locals())


def about(request):
    return render(request, "about.html")


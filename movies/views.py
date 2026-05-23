from django.contrib.auth.models import User
from .models import Movie, ViewHistory
from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie, ViewHistory
from django.contrib.auth.models import User

@login_required
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect('/')

    users = User.objects.all()

    movies = Movie.objects.all()

    histories = ViewHistory.objects.all().order_by('-watched_at')

    total_users = users.count()

    total_movies = movies.count()

    total_views = histories.count()

    context = {

        'users': users,

        'movies': movies,

        'histories': histories,

        'total_users': total_users,

        'total_movies': total_movies,

        'total_views': total_views,
    }

    return render(
        request,
        'movies/dashboard.html',
        context
    )

@login_required
def delete_user(request, pk):

    if not request.user.is_superuser:
        return redirect('/')

    user = User.objects.get(id=pk)

    if user.is_superuser:
        return redirect('/dashboard/')

    user.delete()

    return redirect('/dashboard/')

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies/home.html',
                  {'movies': movies})


def movie_detail(request, pk):

    movie = Movie.objects.get(id=pk)

    if request.user.is_authenticated:

        ViewHistory.objects.create(
            user=request.user,
            movie=movie
        )

    return render(
        request,
        'movies/movie_detail.html',
        {'movie': movie}
    )


@login_required
def upload_movie(request):

    if request.method == 'POST':
        form = MovieForm(request.POST,
                         request.FILES)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.uploaded_by = request.user
            movie.save()

            return redirect('home')

    else:
        form = MovieForm()

    return render(request,
                  'movies/upload_movie.html',
                  {'form': form})

@login_required
def edit_movie(request, pk):

    if not request.user.is_superuser:
        return redirect('/')

    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':

        movie.title = request.POST['title']
        movie.description = request.POST['description']

        if 'thumbnail' in request.FILES:
            movie.thumbnail = request.FILES['thumbnail']

        if 'video' in request.FILES:
            movie.video = request.FILES['video']

        movie.save()

        return redirect('/')

    return render(
        request,
        'movies/edit_movie.html',
        {'movie': movie}
    )


@login_required
def delete_movie(request, pk):

    if not request.user.is_superuser:
        return redirect('/')

    movie = get_object_or_404(Movie, pk=pk)

    movie.delete()

    return redirect('/')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from firstapp_var_music.dao import temp_data
from firstapp_var_music.forms import LoginForm, RegisterForm
def index(request):
    return render(request, "index.html")


def search_music(request, mname, artist_name=""):
    if mname:
        music_name = mname
    else:
        music_name = request.GET.get("music_name")

    musics = []
    if music_name:
        music_name = music_name.lower()
        artist_name = artist_name.lower()
        for artist, data in temp_data["music"]["artists"].items():
            if artist_name and artist_name not in artist:
                continue
            for song in data["top_songs"]:

                if music_name in song.lower():
                    musics.append({
                        "artist": data["name"],
                        "song": song,
                        "genre": data["genre"],
                    })

    return TemplateResponse(request, "music.html",
                            {"music": musics})


# def register(request):
#     register_form = RegisterForm()
#     return TemplateResponse(request, "register.html", {"form": register_form})

def login(request):
    return redirect("/")
    # login_form = LoginForm()
    # return TemplateResponse(request, "login.html", {"form": login_form})

def contacts(request):
    show_phone = request.GET.get("show_phone")
    return render(request, "contacts.html", {"show_phone": show_phone})

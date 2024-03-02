from django.shortcuts import render

from .models import Menu


def index(request):
    return render(
        request, 'menu/menu_list.html', {'menu_list': Menu.objects.all()}
    )


def draw_menu(request, path):
    list_path = path.split('/')
    return render(
        request, 'menu/menu_list.html',
        {'menu_name': list_path[0], 'menu_point': list_path[-1]})

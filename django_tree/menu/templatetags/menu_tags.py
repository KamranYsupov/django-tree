from django.core.exceptions import ObjectDoesNotExist
from django.template import Library

from menu.models import MenuPoint

register = Library()


@register.inclusion_tag('menu/detail_menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):
    def get_menu(menu_item: str = None, list_menu: list = None):
        if menu_item is None:
            menu = list(points.filter(parent=None))
        else:
            menu = list(points.filter(parent__name=menu_item))
        try:
            menu.insert(menu.index(list_menu[0].parent) + 1, list_menu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(points.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_menu(list_menu=menu)
        except ObjectDoesNotExist:
            return menu

    points = MenuPoint.objects.filter(menu__name=menu_name)
    return {'menu': get_menu() if menu_name == menu_item else get_menu(menu_item)}
# @register.inclusion_tag('menu/detail_menu.html')
# def draw_menu(menu_name=None, menu_point=None):
#     points = MenuPoint.objects.filter(menu__name=menu_name)
#
#     def get_menu(menu_point_name=None, list_menu=None):
#         menu = ''
#         if menu_point is None:
#             menu = list(points.filter(parent=None))
#         else:
#             menu = list(points.filter(parent__name=menu_point_name))
#
#         try:
#             menu.insert(menu.index(list_menu[0].parent) + 1, list_menu)
#         except (IndexError, TypeError):
#             pass
#         try:
#             return get_menu(points.get(name=menu_point_name).parent.name, menu)
#         except AttributeError:
#             return get_menu(list_menu=menu)
#         except ObjectDoesNotExist:
#             return menu
#
#     return {'menu': get_menu() if menu_name == menu_point else get_menu(menu_point)}

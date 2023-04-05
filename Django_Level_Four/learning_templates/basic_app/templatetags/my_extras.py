from django import template

register = template.Library()

# Cortamos/quitamos la palabra que le pasamos a arg del string value

# Lo que se hace con un decorator es reasignar la funcion
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg, '')
# Lo que esta entre '' sera el nombre cuando lo llamemos desde el html

#register.filter('cut', cut)

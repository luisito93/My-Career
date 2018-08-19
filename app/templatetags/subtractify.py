from django import template
register = template.Library() 

@register.simple_tag(takes_context=True)
def subtractify(context, obj1, obj2):
    newval = int(obj2) - int(obj1)
    return int(newval)
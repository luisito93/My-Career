from django import template
register = template.Library()

@register.simple_tag(takes_context = True)
def career_level(context, experience_from,experience_to):
    exp = int(experience_to) - int(experience_from)
    if exp == 0:
        return 'Internship'
    if exp <= 1:
        return 'Entry Level'
    if exp <= 2:
        return 'Associate'
    if exp <= 5:
        return 'Mid-Senior level'
    if exp <= 10:
        return 'Director'
    if exp >= 15:
        return 'Executive'
    

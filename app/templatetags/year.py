import datetime
from django import template
register = template.Library() 

@register.simple_tag(takes_context=True)
def year(context, job_to):
    now = datetime.datetime.now()
    if now.year == job_to:
        return "Present"
    else:
        return job_to
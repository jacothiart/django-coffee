from django import template
from django.forms import RadioSelect, CheckboxInput, CheckboxSelectMultiple

register = template.Library()

@register.simple_tag(takes_context=True)
def detect_radio(context, field):
    if isinstance(field.field.widget, RadioSelect):
        context['is_radio'] = True
    else:
        context['is_radio'] = False
    
    return ''
    
@register.simple_tag(takes_context=True)
def detect_checkbox(context, field):
    widget = field.field.widget
    
    if isinstance(widget, CheckboxInput) or isinstance(widget, CheckboxSelectMultiple):
        context['is_checkbox'] = True
    else:
        context['is_checkbox'] = False
    
    return ''
    
    
@register.inclusion_tag('coffee/partial/form.html')
def render_form(form):
    return {'form': form}
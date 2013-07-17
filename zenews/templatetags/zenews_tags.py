from django.db.models import get_model
from django import template

register = template.Library()

# get latest content,format: get_latest_content [app.model] [number] as [varname]
@register.tag(name='get_latest_content')
def do_latest_content(parser, token):
    bits = token.split_contents()
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' tag tags exactly four arguments")
    model_args = bits[1].split('.')

    if len(model_args) !=2:
        raise template.TemplateSyntaxError("First argument to 'get_latest_content' must be an 'application name'.'model name' string")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("'get_latest_content' tag got an invalid model: %s" % bits[1])
    return LatestContentNode(model, bits[2], bits[4])

class LatestContentNode(template.Node):
    def __init__(self, model, num, varname):
        self.model = model
        self.num = num
        self.varname = varname

    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

# get all tuples in a given model,format: get_all_tuples [app.model] as [varname]
@register.tag(name='get_all_tuples')
def do_all_tuples(parser, token):
    bits = token.split_contents()
    if len(bits) != 4:
        raise template.TemplateSyntaxError("'get_latest_content' tag tags exactly three arguments")
    model_args = bits[1].split('.')

    if len(model_args) !=2:
        raise template.TemplateSyntaxError("First argument to 'get_all_tuples' must be an 'application name'.'model name' string")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("'get_all_tuples' tag got an invalid model: %s" % bits[1])
    return AllTuplesNode(model, bits[3])

class AllTuplesNode(template.Node):
    def __init__(self, model, varname):
        self.model = model
        self.varname = varname
    def render(self, context):
        context[self.varname] = self.model._default_manager.all().order_by('id')
        return ''

# get the content of a given category,format: get_category_content [app.model] ['category'] [number] as [varname]
@register.tag(name='get_category_content')
def do_category_content(parser, token):
    bits = token.split_contents()
    if len(bits) != 6:
        raise template.TemplateSyntaxError("'get_category_content' tag tags exactly five arguments")
    model_args = bits[1].split('.')

    if len(model_args) !=2:
        raise template.TemplateSyntaxError("First argument to 'get_category_content' must be an 'application name'.'model name' string")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("'get_category_content' tag got an invalid model: %s" % bits[1])
    
    format_string = bits[2]
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"',"'")):
        raise template.TemplateSyntaxError, "%r tag's second argument 'category' must be in quotes" % bits[0]
    
    return CategoryContentNode(model, format_string[1:-1], bits[3], bits[5])

class CategoryContentNode(template.Node):
    def __init__(self, model, cat, num, varname):
        self.model = model
        self.cat = cat
        self.num = num
        self.varname = varname

    def render(self, context):
        context[self.varname] = self.model._default_manager.filter(categories__slug=self.cat).order_by('-pub_date')[:self.num]
        return ''


from django.db.models import get_model
from django import template

# get latest content,format: get_latest_content [app.model] [number] as [varname]
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
        context[self.varname] = self.model._default_manager.all()
        return ''

# get distinct months when records are published in a given model,format: get_archive_month [app.model] as [varname]
def do_archive_month(parser, token):
    bits = token.split_contents()
    if len(bits) != 4:
        raise template.TemplateSyntaxError("'get_latest_content' tag tags exactly three arguments")
    model_args = bits[1].split('.')
    if len(model_args) !=2:
        raise template.TemplateSyntaxError("First argument to 'get_archive_month' must be an 'application name'.'model name' string")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("'get_archive_month' tag got an invalid model: %s" % bits[1])
    return ArchiveMonthNode(model, bits[3])
class ArchiveMonthNode(template.Node):
    def __init__(self, model, varname):
        self.model = model
        self.varname = varname
    def render(self, context):
        context[self.varname] = self.model._default_manager.dates('pub_date','month')
        return ''

register = template.Library()
register.tag('get_latest_content', do_latest_content)
register.tag('get_all_tuples', do_all_tuples)
register.tag('get_archive_month', do_archive_month)


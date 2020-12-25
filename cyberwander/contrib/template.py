"""
前后端分离之后，后端模板日渐式微
现在多数用于一些模板消息场景
"""

from jinja2 import Template


def render_template(tmpl, **kwargs):
    template = Template(tmpl)
    return template.render(**kwargs)

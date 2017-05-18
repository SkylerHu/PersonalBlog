# -*- coding: utf8 -*-
# refer these following links
# http://mistune.readthedocs.org/en/latest/
# http://daringfireball.net/projects/markdown/syntax#link
import copy
import re

import mistune

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from utils.file_util import get_full_path


_link = re.compile(
    r'(?<!!)\[('
    r'(?:\[[^^\]]*\]|[^\[\]]|\](?=[^\[]*\]))*'
    r')\]\('
    r'''\s*<?([\s\S]*?)>?(?:\s+['"]([\s\S]*?)['"])?\s*'''
    r'\)'
)
_gm_video_link = re.compile(
    r'!!'
    r'\('
    r'([\s\S]+?)'
    r'\)'
)
_image_link = re.compile(
    r'!\[('
    r'(?:\[[^^\]]*\]|[^\[\]]|\](?=[^\[]*\]))*'
    r')\]\('
    r'''\s*<?([\s\S]*?)>?(?:\s+['"]([\s\S]*?)['"])?\s*'''
    r'\)'
)

_iframe = re.compile(
    r'<iframe.*?</iframe>'
)


def strip_markdown_links(md_txt, keep_image=False):
    """strip markdown link and image."""
    striped = _link.sub('', md_txt)
    if keep_image:
        return striped

    striped = _image_link.sub('', striped)
    striped = _iframe.sub('', striped)
    return striped


class SkylerRenderer(mistune.Renderer):
    def image(self, src, title, text):
        src = get_full_path(src)
        return '<img src="{}" alt="{}" title="{}" />'.format(src, title, text)

    def block_code(self, code, lang):
        if lang:
            try:
                lexer = get_lexer_by_name(lang, stripall=True)
                formatter = HtmlFormatter()
                return highlight(code, lexer, formatter)
            except:
                pass
        return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)


def markdown_to_html(content):
    renderer = SkylerRenderer()
    md = mistune.Markdown(renderer=renderer)
    return md(content)

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = []
        if content:
            self.contents.append(content)

    def append(self, new_content):
        self.contents.append(new_content)


    def render(self, out_file):
        out_file.write(self._open_tag())
        out_file.write("\n")
        for content in self.contents:   
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
                out_file.write("\n")
        out_file.write(self._close_tag())
        out_file.write("\n")

    def _open_tag(self):
        open_tag = ["<{}".format(self.tag)]
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        open_tag.append(">")
        return "".join(open_tag)

    def _close_tag(self):
        return "</{}>\n".format(self.tag)



class OneLineTag(Element):
    def render(self, out_file):
        for content in self.contents:
            out_file.write("<{}>".format(self.tag)) #removed newline
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content) #removed newline from Element
            out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class SelfClosingTag(Element):
    def __init__(self, content=None, **kwargs):
        if content is not None:
            raise TypeError("SelfClosingTag cannot contain any content")
        super().__init__(content=content, **kwargs)
    
    def render(self, out_file):
        tag = self._open_tag()[:-1] + " />\n"
        out_file.write(tag)

    def append(self, *args):
        raise TypeError("You cannot add content to SelfClosingTag")


class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

class Head(Element):
    tag = "head"

class Title(OneLineTag):
    tag = "title"

class Ul(Element):
    tag = "ul"

class List(Element):
    tag = "li"

class Anchor(Element):
    tag = "a"


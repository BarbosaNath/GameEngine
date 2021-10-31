import pygame
import utils
import text as Text


class DebugLog:
    def __init__(self, default_font=Text.arial[16], size=(200,200), font_color='#FFFFFF'):
        self.lines = list()
        self.default_font = default_font
        self.space = default_font.get_linesize()
        self.canvas = pygame.Surface(size)
        self.canvas_size = size
        self.updated = True
        self.font_color = font_color
        # lines = [
        #          {'text': 'texto1', 'font': font, 'fixed': True},
        #          {'text': 'texto2', 'font': font}
        #         ]

        # color codes: $#000$text$

    def add_line(self, text, fixed=False, font=None, id=None):
        if font is None: font = self.default_font

        self.lines.append({'text':text,'font':font,'fixed':fixed,'id':id})

        self.updated = True

    def edit_line(self, id, what, value):
        line = next((sub for sub in self.lines if sub['id'] == id), None)
        self.lines[self.lines.index(line)][what] = value
        self.updated=True

    def render(self):
        if self.lines == []: return
        if self.updated:
            self.canvas.fill((0x00000000))

            height = 0
            reversed_height = self.canvas_size[1]-self.lines[0]['font'].get_linesize()

            for line in self.lines:
                if line['fixed']:
                    color = self.font_color
                    width = 0
                    for text in line['text'].split('$'):
                        if list(text) != []:
                            if list(text)[0] == '#':
                                color = utils.hex(text)
                                continue
                        Text.render(line['font'], text, color, (width, height), self.canvas)
                        width += line['font'].size(text)[0]
                    height += line['font'].get_linesize()

            for line in reversed(self.lines):
                if line['fixed']: continue
                if reversed_height <= height: break
                color = self.font_color
                width = 0
                for text in line['text'].split('$'):
                    if list(text) != []:
                        if list(text)[0] == '#':
                            color = utils.hex(text)
                            continue
                    Text.render(line['font'], text, color, (width, reversed_height), self.canvas)
                    width += line['font'].size(text)[0]
                reversed_height -= line['font'].get_linesize()
            self.updated = False


debugLog = DebugLog()
debugLog.render()

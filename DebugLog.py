import pygame
import text as Text


class DebugLog:
    def __init__(self, default_font=Text.arial[32]):
        self.lines = list()
        self.default_font = default_font
        self.updated = True
        # lines = [
        #          {'text': 'texto1', 'font': font}
        #          {'text': 'texto2', 'font': font}
        #         ]

    def add_line(self, text, font=None, color=(255,255,255)):
        if font is not None:
            self.lines.append({'text': text, 'font': font             , 'color': color})
        else:
            self.lines.append({'text': text, 'font': self.default_font, 'color': color})
        self.updated = True

    def edit_line(self, which, what, value):
        self.lines[which][what] = value
        self.updated = True

    def render(self, canvas, position):
        if self.updated:
            for i, line in enumerate(self.lines):
                Text.render(line['font'], line['text'], line['color'], (position[0],position[1]*(i+1)), canvas)
            self.updated = False

debugLog = DebugLog()

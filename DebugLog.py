import pygame
import utils
import text as Text


class DebugLog:
    def __init__(self, default_font=Text.arial[16], size=(200,200), font_color='#FFFFFF', max=100):
        self.lines = list()
        self.default_font = default_font
        self.canvas = pygame.Surface(size, pygame.SRCALPHA)
        # self.canvas.set_colorkey((0,0,0))
        self.canvas_size = size
        self.updated = True
        self.font_color = font_color
        self.max = max

        # lines = [
        #          {'text': 'texto1', 'font': font, 'fixed': True},
        #          {'text': 'texto2', 'font': font}
        #         ]
        # color codes: $#000$text$


    def add_line(self, text, fixed=False, font=None, id=None):
        if font is None: font = self.default_font
        self.lines.append({'text':text,'font':font,'fixed':fixed,'id':id})
        self.updated = True

        first_not_fixed = 0
        if len(self.lines) > self.max:
            for line in self.lines:
                if self.lines[first_not_fixed]['fixed'] == False and\
                    self.lines[first_not_fixed]['id'] is None:
                    del self.lines[first_not_fixed]
                    break
                first_not_fixed += 1

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


        first_not_fixed = 0
        if len(self.lines) > self.max:
            for line in self.lines:
                if self.lines[first_not_fixed]['fixed'] == False and\
                    self.lines[first_not_fixed]['id'] is None:
                    del self.lines[first_not_fixed]
                    break
                first_not_fixed += 1


debugLog = DebugLog(max=10)
debugLog.render()

acc     = '$#A3F$'
acc2    = '$#3AF$'
white   = '$#AA0$'

def log_var(varname, var):
    return f'{acc}{varname}{white}: {var}'
def log_vars(varname1, var1, varname2, var2):
    return f'{acc}{varname1}{white}: {var1}   {acc2}|{acc}   {varname2}{white}: {var2}'

from abc import ABC, abstractmethod
from tkinter import Canvas
from svgwrite import Drawing


class Draw(ABC):
    @abstractmethod
    def draw_oval(self):
        pass

    @abstractmethod
    def draw_rectangle(self):
        pass
    
    @abstractmethod
    def draw_polygon(self):
        pass


class SVGDraw(Draw):
    def draw_oval(x, y, radius, color, outline, stroke, svg_file: Drawing):
        svg_file.add(svg_file.circle(
            center = (x, y),
            r = radius,
            fill=color,
            stroke=outline,
            stroke_width=stroke
        ))
        svg_file.save()

    def draw_rectangle(x, y, width, height, color, outline, stroke, svg_file: Drawing):
        svg_file.add(svg_file.rect(
            insert = (x, y),
            size = (width, height),
            fill=color,
            stroke=outline,
            stroke_width=stroke
        ))
        svg_file.save()
    
    def draw_polygon(pts, color, outline, stroke, svg_file: Drawing):
        svg_file.add(svg_file.polygon(
            points=pts,
            fill=color,
            stroke=outline,
            stroke_width=stroke
        ))
        svg_file.save()

class TKDraw(Draw):
    def draw_oval(x, y, radius, color, outline, stroke, canvas: Canvas):
        canvas.create_oval(x - radius, y - radius,
                           x + radius, y + radius,
                           fill=color,
                           outline=outline,
                           width=stroke)

    def draw_rectangle(x, y, width, height, color, outline, stroke, canvas: Canvas):
        canvas.create_rectangle(x, 
                                y,
                                x + width,
                                y + height,
                                fill=color,
                                outline=outline,
                                width=stroke)
    
    def draw_polygon(pts, color, outline, stroke, canvas: Canvas):
        canvas.create_polygon(*pts, fill=color, outline=outline, width=stroke)
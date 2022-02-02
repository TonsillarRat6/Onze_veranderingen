from shape import Shape
from tkinter import Canvas
from draw import SVGDraw, TKDraw
from svgwrite import Drawing


class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int, color: str, outline: str, stroke: str):
        self.x: int = x
        self.y: int = y
        self.radius: int = radius
        self.color: str = color
        self.outline: str = outline
        self.stroke: str = stroke
        super().__init__()

    def draw(self, canvas: Canvas, svg_file: Drawing):
        SVGDraw.draw_oval(self.x, self.y, self.radius, self.color, self.outline, self.stroke, svg_file)
        TKDraw.draw_oval(self.x, self.y, self.radius, self.color, self.outline, self.stroke, canvas)
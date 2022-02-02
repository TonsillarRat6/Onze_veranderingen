from shape import Shape
from tkinter import Canvas
from draw import TKDraw, SVGDraw
from svgwrite import Drawing


class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, color: str, outline: str, stroke: str):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.color: str = color
        self.outline: str = outline
        self.stroke: str = stroke
        super().__init__()

    def draw(self, canvas: Canvas, svg_file: Drawing):
        print(svg_file)
        SVGDraw.draw_rectangle(self.x, self.y, self.width, self.height, self.color, self.outline, self.stroke, svg_file)
        TKDraw.draw_rectangle(self.x, self.y, self.width, self.height, self.color, self.outline, self.stroke, canvas)
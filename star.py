from shape import Shape
import math
from tkinter import Canvas
from draw import TKDraw, SVGDraw
from svgwrite import Drawing


class Star(Shape):

    def __init__(self, x: int, y: int, width: int, height: int, pts: int, color: str, outline: str, stroke: str):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.pts: int = pts
        self.color: str = color
        self.outline: str = outline
        self.stroke: str = stroke
        super().__init__()

    def get_pts_list(self):
        numPoints = self.pts
        pts = []
        rx = self.width / 2 
        ry = self.height / 2 
        cx = self.x + rx 
        cy = self.y + ry 
        theta = -math.pi / 2 
        dtheta = 4 * math.pi / numPoints

        for i in range(0, numPoints + 1):
            pts.append(
                int(round(cx + rx * math.cos(theta)))) 
            pts.append(
                int(round(cy + ry * math.sin(theta)))
            )
            theta += dtheta
        return pts
    
    def adapt_pts(self):
        temp = iter(self.get_pts_list())
        return zip(temp, temp)

    def draw(self, canvas: Canvas, svg_file: Drawing):
        SVGDraw.draw_polygon(self.adapt_pts(), self.color, self.outline, self.stroke, svg_file)
        TKDraw.draw_polygon(self.get_pts_list(), self.color, self.outline, self.stroke, canvas)
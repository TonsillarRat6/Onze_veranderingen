from abc import ABC, abstractmethod
from tkinter import Canvas
from urllib.request import AbstractHTTPHandler


class Shape(ABC):

    @abstractmethod
    def draw(self, canvas: Canvas):
        pass
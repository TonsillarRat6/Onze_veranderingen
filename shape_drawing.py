from tkinter import Tk, Canvas, Frame, Menu, BOTH, filedialog
from shape_parser import Parser
import svgwrite
import os # Verwijder dit


class ShapeDrawing(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.widgets()
        self.shapes = []
        self.svg_name = 'svg.svg'
        self.svgFile = svgwrite.Drawing(self.svg_name)

    def widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Clear", command=self.onClear)
        fileMenu.add_command(label="Export", command=self.onExport)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.master.title("Shape Drawing")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

    def onOpen(self):
        file = filedialog.askopenfilename(title="Select file")

        if not file:
            return

        parser = Parser()
        self.shapes = parser.parse_shapes(file)

        if os.path.exists(self.svg_name): # Verwijder dit
            os.remove(self.svg_name) # Verwijder dit
        self.canvas.delete("all")
        for shape in self.shapes:
            shape.draw(self.canvas, self.svgFile)
        os.startfile(self.svg_name) # Verwijder dit

    def onClear(self):
        self.canvas.delete("all")
        self.shapes = []

    def onExport(self):
        print("To do.")

    def onExit(self):
        self.quit()


def main():
    root = Tk()
    root.title("Shape Drawing")
    root.geometry("400x250+300+300")
    app = ShapeDrawing(root)

    root.mainloop()


if __name__ == '__main__':
    main()
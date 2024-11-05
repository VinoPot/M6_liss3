import tkinter as tk
from PIL import Image, ImageDraw, ImageTk


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("холст")

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.default_bg_color = "#FFFFFF"
        self.canvas.configure(bg=self.default_bg_color)

        self.bg_color = self.default_bg_color
        self.fill_color = "#FFFFFF"
        self.border_color = "#000000"

        self.create_widgets()

    def create_widgets(self):
        # Поле для ввода цвета фона
        self.bg_color_entry = tk.Entry(self.root)
        self.bg_color_entry.insert(0, self.default_bg_color)
        self.bg_color_entry.pack()

        change_bg_button = tk.Button(self.root, text="Изменить цвет фона", command=self.change_bg_color)
        change_bg_button.pack()

        # Метка и поле для ввода цвета заливки
        fill_color_label = tk.Label(self.root, text="Цвет заливки:")
        fill_color_label.pack()

        self.fill_color_entry = tk.Entry(self.root)
        self.fill_color_entry.insert(0, self.fill_color)
        self.fill_color_entry.pack()

        # Метка и поле для ввода цвета обводки
        border_color_label = tk.Label(self.root, text="Цвет обводки:")
        border_color_label.pack()

        self.border_color_entry = tk.Entry(self.root)
        self.border_color_entry.insert(0, self.border_color)
        self.border_color_entry.pack()

        circle_button = tk.Button(self.root, text="Окружность", command=self.draw_circle)
        circle_button.pack()

        triangle_button = tk.Button(self.root, text="Треугольник", command=self.draw_triangle)
        triangle_button.pack()

        square_button = tk.Button(self.root, text="Квадрат", command=self.draw_square)
        square_button.pack()

        clear_button = tk.Button(self.root, text="Очистить", command=self.clear_canvas)
        clear_button.pack()

    def change_bg_color(self):
        self.bg_color = self.bg_color_entry.get()
        self.canvas.configure(bg=self.bg_color)

    def update_colors(self):
        # Обновляем цвета заливки и обводки на основе введенных значений
        self.fill_color = self.fill_color_entry.get()
        self.border_color = self.border_color_entry.get()

    def draw_circle(self):
        self.update_colors()
        self.canvas.create_oval(100, 100, 300, 300, fill=self.fill_color, outline=self.border_color, width=2)

    def draw_triangle(self):
        self.update_colors()
        self.canvas.create_polygon(200, 100, 100, 300, 300, 300, fill=self.fill_color, outline=self.border_color,
                                   width=2)

    def draw_square(self):
        self.update_colors()
        self.canvas.create_rectangle(100, 100, 300, 300, fill=self.fill_color, outline=self.border_color, width=2)

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
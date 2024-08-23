import tkinter as tk
from tkinter import ttk
from main_2 import *


def on_click_solver_button_handler():
    try:
        arr = [int(x) for x in input_array.get().split(",")]
        k = int(input_k_number.get())

        result = rotate_and_reverse(arr, k)

        output_result_label.config(text=f"Результат: {result}")

    except ValueError as e:
        output_result_label.config(text=f"Ошибка: {e}")


root = tk.Tk()
root.title("Вот это поворот-разворот-переворот")

root.geometry("300x250+900+400")

input_array_label = ttk.Label(root, text="Введите массив (через запятую):")
input_array_label.pack()

input_array = ttk.Entry(root)
input_array.pack()

input_k_number_label = ttk.Label(root, text="Введите значение k:")
input_k_number_label.pack()

input_k_number = ttk.Entry(root)
input_k_number.pack()

solver_button = ttk.Button(root, text="Выполнить", command=on_click_solver_button_handler)
solver_button.pack()

output_result_label = ttk.Label(root, text="")
output_result_label.pack()

root.mainloop()
import tkinter as tk
from tkinter import ttk
from main_3 import *

class App:
    def __init__(self, root= tk.Tk()):
        self.__root_window = root
        self.__input_array_entry = None
        self.__solver_button = None
        self.__output_result_label = None
        self.__config_window()
        self.__build_main()

    def run(self):
        self.__root_window.mainloop()

    def __config_window(self):
        self.__root_window.title("Туда-сюда если четный")
        self.__root_window.geometry("500x100+900+400")
        self.__root_window.resizable(False, False)

    def __build_main(self):
        main_frame = ttk.Frame(self.__root_window)

        self.input_array_label = ttk.Label(master=main_frame, text="Введите массив (через запятую):")
        self.input_array_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.__input_array_entry = ttk.Entry(master=main_frame)
        self.__input_array_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.__solver_button = ttk.Button(master=main_frame, text="Выполнить", command=self.on_click_solver_button_handler)
        self.__solver_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.__output_result_label = ttk.Label(master=main_frame, text="")
        self.__output_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        main_frame.pack()

    def on_click_solver_button_handler(self):
        try:
            arr = [int(x) for x in self.__input_array_entry.get().split(",")]

            result = reverse_even_elements(arr)

            self.__output_result_label.config(text=f"Результат: {result}")

        except ValueError as e:
            self.__output_result_label.config(text=f"Ошибка: {e}")


if __name__ == "__main__":
    app = App()
    app.run()

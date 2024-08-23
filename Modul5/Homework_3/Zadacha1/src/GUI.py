import tkinter as tk
from tkinter import ttk
from main_1 import *




class App:
    def __init__(self, root=tk.Tk()):
        self.__root_window = root
        self.__input_array_entry = None
        self.__input_start_entry = None
        self.__input_end_entry = None
        self.__solver_button = None
        self.output_result_label = None
        self.__config_window()
        self.__build_main()

    def run(self):
        self.__root_window.mainloop()

    def __config_window(self):
        self.__root_window.title("Поиск максималочки")
        self.__root_window.geometry("800x200+900+400")
        self.__root_window.resizable(False, False)

    def __build_main(self):
        main_frame = ttk.Frame(self.__root_window)

        self.input_array_label = ttk.Label(master=main_frame, text="Введите массив (через запятую):")
        self.__input_array_entry = ttk.Entry(master=main_frame)

        self.input_start_label = ttk.Label(master=main_frame, text="Введите начальный индекс:")
        self.__input_start_entry = ttk.Entry(master=main_frame)

        self.input_end_label = ttk.Label(master=main_frame, text="Введите конечный индекс:")
        self.__input_end_entry = ttk.Entry(master=main_frame)

        self.__solver_button = ttk.Button(master=main_frame, text="Найти максимум", command=self.on_click_solver_button_handler)

        self.output_result_label = ttk.Label(master=main_frame, text="")

        self.input_array_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.__input_array_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.input_start_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.__input_start_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.input_end_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.__input_end_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.__solver_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.output_result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        main_frame.pack()

    def on_click_solver_button_handler(self):
        try:
            arr = [int(x) for x in self.__input_array_entry.get().split(",")]
            start = int(self.__input_start_entry.get())
            end = int(self.__input_end_entry.get())

            max_element, max_index_relative, max_index_absolute = max_in_range(arr, start, end)

            self.output_result_label.config(text=f"Максимальный элемент: {max_element}\nОтносительный индекс: {max_index_relative}\nАбсолютный индекс: {max_index_absolute}")

        except ValueError as e:
            self.output_result_label.config(text=f"Ошибка: {e}")



if __name__ == "__main__":
    app = App()
    app.run()








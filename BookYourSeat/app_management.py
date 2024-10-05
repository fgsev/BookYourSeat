from buttons import SeatButton, VIPSeatButton
import tkinter as tk

class AppManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("BookYourSeat")
        self.root.geometry("1200x700")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=240, height=140)

        self.info_frame = tk.Frame(self.root, bg='lightgray', width=200, height=700)
        self.info_frame.place(relx=0.8, rely=0.5, anchor='center')

        self.info_label = tk.Label(self.info_frame, text="Wybierz miejsce, aby zobaczyć szczegóły", font=("Arial", 12), bg='lightgray')
        self.info_label.pack(pady=20)

        self.reset_button = tk.Button(self.root, text="Resetuj bilety", command=self.reset_tickets)
        self.reset_button.place(relx=0.05, rely=0.95, anchor='sw')

        for i in range(5):
            self.main_frame.grid_columnconfigure(i, weight=1)
        for j in range(5):
            self.main_frame.grid_rowconfigure(j, weight=1)

        self.create_seats()
        self.create_legend()

    def create_seats(self):
        self.seat_buttons = []
        for row in range(5):
            for column in range(5):
                if row == 0:
                    button = VIPSeatButton(self.main_frame, row, column, width=6, height=3)
                else:
                    button = SeatButton(self.main_frame, row, column, width=6, height=3)
                button.grid(row=row, column=column, sticky='nsew')
                self.seat_buttons.append(button)

    def create_legend(self):
        legend_frame = tk.Frame(self.root)
        legend_frame.place(relx=0.95, rely=0.95, anchor='se')

        tk.Label(legend_frame, text="Legenda:", font=("Arial", 10)).grid(row=0, column=0, sticky='w')

        self.draw_square(legend_frame, "green", 1)
        tk.Label(legend_frame, text=" Wolne miejsca", font=("Arial", 10)).grid(row=1, column=1, sticky='w')

        self.draw_square(legend_frame, "gold", 2)
        tk.Label(legend_frame, text=" Miejsca VIP", font=("Arial", 10)).grid(row=2, column=1, sticky='w')

        self.draw_square(legend_frame, "darkorange", 3)
        tk.Label(legend_frame, text=" Zajęte miejsca VIP", font=("Arial", 10)).grid(row=3, column=1, sticky='w')

        self.draw_square(legend_frame, "red", 4)
        tk.Label(legend_frame, text=" Miejsca zajęte", font=("Arial", 10)).grid(row=4, column=1, sticky='w')

    def draw_square(self, frame, color, row):
        square_size = 15
        canvas = tk.Canvas(frame, width=square_size, height=square_size, bg=color, highlightthickness=0)
        canvas.grid(row=row, column=0, sticky='w')

    def reset_tickets(self):
        for button in self.seat_buttons:
            if button.reserved:
                button.change_reservation_status()  # Resetuj status rezerwacji
        self.info_label.config(text="Wybierz miejsce, aby zobaczyć szczegóły")

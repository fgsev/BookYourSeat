from buttons import SeatButton, VIPSeatButton
import tkinter as tk

class AppManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("BookYourSeat")
        self.root.geometry("1200x700")
        self.root.configure(bg='#2C2F33')  # Ciemne tło aplikacji

        self.total_cost = 0

        # Główna ramka na miejsca siedzące
        self.main_frame = tk.Frame(self.root, bg='#23272A', bd=2, relief='flat')
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=300, height=200)

        # Ramka na informacje
        self.info_frame = tk.Frame(self.root, bg='#99AAB5', width=200, height=700)
        self.info_frame.place(relx=0.8, rely=0.5, anchor='center')

        self.info_label = tk.Label(self.info_frame, text="Wybierz miejsce, aby zobaczyć szczegóły", font=("Arial", 12), bg='#99AAB5', fg='white')
        self.info_label.pack(pady=20)

        self.total_label = tk.Label(self.info_frame, text="Łączny koszt: $0", font=("Arial", 12), bg='#99AAB5', fg='white')
        self.total_label.pack(pady=10)

        # Przycisk resetu
        self.reset_button = tk.Button(self.root, text="Resetuj bilety", command=self.reset_tickets, bg='#7289DA', fg='white', font=("Arial", 12), relief='flat')
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
                    button = VIPSeatButton(self.main_frame, row, column, self.update_info_label, self.update_total_cost, width=6, height=3)
                else:
                    button = SeatButton(self.main_frame, row, column, self.update_info_label, self.update_total_cost, width=6, height=3)
                button.grid(row=row, column=column, sticky='nsew', padx=5, pady=5)  # Dystans dla estetyki
                self.seat_buttons.append(button)

    def create_legend(self):
        legend_frame = tk.Frame(self.root, bg='#2C2F33', bd=2, relief='flat')
        legend_frame.place(relx=0.95, rely=0.95, anchor='se')

        tk.Label(legend_frame, text="Legenda:", font=("Arial", 10, 'bold'), bg='#2C2F33', fg='white').grid(row=0, column=0, sticky='w')

        self.draw_square(legend_frame, "green", 1)
        tk.Label(legend_frame, text=" Wolne miejsca ($25)", font=("Arial", 10), bg='#2C2F33', fg='white').grid(row=1, column=1, sticky='w')

        self.draw_square(legend_frame, "gold", 2)
        tk.Label(legend_frame, text=" Miejsca VIP ($40)", font=("Arial", 10), bg='#2C2F33', fg='white').grid(row=2, column=1, sticky='w')

        self.draw_square(legend_frame, "darkorange", 3)
        tk.Label(legend_frame, text=" Zajęte miejsca VIP", font=("Arial", 10), bg='#2C2F33', fg='white').grid(row=3, column=1, sticky='w')

        self.draw_square(legend_frame, "red", 4)
        tk.Label(legend_frame, text=" Miejsca zajęte", font=("Arial", 10), bg='#2C2F33', fg='white').grid(row=4, column=1, sticky='w')

    def draw_square(self, frame, color, row):
        square_size = 15
        canvas = tk.Canvas(frame, width=square_size, height=square_size, bg=color, highlightthickness=0)
        canvas.grid(row=row, column=0, sticky='w')

    def reset_tickets(self):
        for button in self.seat_buttons:
            if button.reserved:
                button.change_reservation_status()
        self.total_cost = 0
        self.total_label.config(text="Łączny koszt: $0")
        self.info_label.config(text="Wybierz miejsce, aby zobaczyć szczegóły")

    def update_info_label(self, message):
        self.info_label.config(text=message)

    def update_total_cost(self, amount):
        self.total_cost += amount
        self.total_label.config(text=f"Łączny koszt: ${self.total_cost}")

class SeatButton(tk.Button):
    def __init__(self, master, row, column, update_info_callback, update_total_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.row = row
        self.column = column
        self.reserved = False
        self.update_info_callback = update_info_callback
        self.update_total_callback = update_total_callback
        self.config(bg="green", command=self.change_reservation_status, relief='flat', font=("Arial", 12))

    def change_reservation_status(self):
        if not self.reserved:
            self.config(bg="red")
            self.reserved = True
            self.update_info_callback(f"Miejsce zajęte: {self.row}, {self.column} - Cena: $25")
            self.update_total_callback(25)
        else:
            self.config(bg="green")
            self.reserved = False
            self.update_info_callback("Wybierz miejsce, aby zobaczyć szczegóły")
            self.update_total_callback(-25)

    def __str__(self):
        return f"Seat at row {self.row}, column {self.column}, reserved: {self.reserved}"

class VIPSeatButton(SeatButton):
    def __init__(self, master, row, column, update_info_callback, update_total_callback, **kwargs):
        super().__init__(master, row, column, update_info_callback, update_total_callback, **kwargs)
        self.config(bg="gold", relief='flat', font=("Arial", 12))

    def change_reservation_status(self):
        if not self.reserved:
            self.config(bg="darkorange")
            self.reserved = True
            self.update_info_callback(f"Miejsce VIP zajęte: {self.row}, {self.column} - Cena: $40")
            self.update_total_callback(40)
        else:
            self.config(bg="gold")
            self.reserved = False
            self.update_info_callback("Wybierz miejsce, aby zobaczyć szczegóły")
            self.update_total_callback(-40)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppManagement(root)
    root.mainloop()

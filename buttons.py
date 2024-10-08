import tkinter as tk

class SeatButton(tk.Button):
    def __init__(self, master, row, column, update_info_callback, update_total_callback, **kwargs):
        super().__init__(master, **kwargs)
        self.row = row
        self.column = column
        self.reserved = False
        self.update_info_callback = update_info_callback
        self.update_total_callback = update_total_callback
        self.config(bg="green", command=self.change_reservation_status)

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
        self.config(bg="gold")

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

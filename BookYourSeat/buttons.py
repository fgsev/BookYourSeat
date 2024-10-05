import tkinter as tk

class SeatButton(tk.Button):
    def __init__(self, master, row, column, **kwargs):
        super().__init__(master, **kwargs)
        self.row = row
        self.column = column
        self.reserved = False
        self.config(bg="green", command=self.change_reservation_status)

    def change_reservation_status(self):
        if not self.reserved:
            self.config(bg="red")
            self.reserved = True
        else:
            self.config(bg="green")
            self.reserved = False

    def __str__(self):
        return f"Seat at row {self.row}, column {self.column}, reserved: {self.reserved}"


class VIPSeatButton(SeatButton):
    def __init__(self, master, row, column, **kwargs):
        super().__init__(master, row, column, **kwargs)
        self.config(bg="gold")

    def change_reservation_status(self):
        if not self.reserved:
            self.config(bg="darkorange")
            self.reserved = True
        else:
            self.config(bg="gold")
            self.reserved = False

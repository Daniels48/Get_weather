from tkinter import Label, Tk, Entry, Button
from tkinter.ttk import Combobox

window = Tk()
window.geometry("800x300")
window.title("Приложение для поиска квартир на Avito")


font_subtitle = ("Arial Bold", 18)
subTitle_text = "Заполните данные для поиска квартир"
lbl_subtitle = Label(window, text=subTitle_text, font=font_subtitle)
lbl_subtitle.grid(row=0, column=0, columnspan=3)


font_city = ("Arial Bold", 14)
city_text = "Введите город: "
lbl_city = Label(window, text=city_text, font=font_city)
lbl_city.grid(row=2, column=0)
input_city = Entry(window, width=40)
input_city.grid(row=2, column=1)


font_room = ("Arial Bold", 14)
room_text = "Колличество комнат: "
lbl_room = Label(window, text=room_text, font=font_room)
lbl_room.grid(row=3, column=0)
count_rooms = Combobox(window)
count_rooms["values"] = (1, 2, 3, 4, 5, 6)
count_rooms.current(0)
count_rooms.grid(row=3, column=1)


def clicked():
    pass


button_ = Button(window, text="Показать", command=clicked)
button_.grid(column=0, row=4)


window.mainloop()
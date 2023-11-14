from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

def LeftClickButton(event):
    c = CurrencyRates()
    base_currency = textbox_base_currency.get().upper()
    destination_currency = textbox_dest_currency.get().upper()
    amount = float(textbox_amount.get())
    amount_result = c.convert(base_currency, destination_currency, amount)
    label_result_amount.configure(text=amount_result)
    label_result_dest_currency.configure(text=destination_currency)

main_window = Tk()
main_window.config(width=300,height=200)
main_window.title("เครื่องมือแปลงสกุลเงิน")

label_base_currency = Label(main_window, text="ค่าเงินที่ต้องกาารแลกเปลี่ยน : ")
label_base_currency.grid(row=0,column=0)

textbox_base_currency = Entry(main_window)
textbox_base_currency.grid(row=0,column=1)

label_dest_currency = Label(main_window, text="แลกเปลี่ยนเป็นค่าเงิน : ")
label_dest_currency.grid(row=1,column=0)

textbox_dest_currency = Entry(main_window)
textbox_dest_currency.grid(row=1,column=1)

label_amount = Label(main_window, text="จำนวนเงิน : ")
label_amount.grid(row=2,column=0)

textbox_amount = Entry(main_window)
textbox_amount.grid(row=2,column=1)

calculate_button = Button(main_window, text="คำนวณ")
calculate_button.bind('<Button-1>',LeftClickButton)
calculate_button.grid(row=3,column=1)

label_result = Label(main_window, text="ผลลัพธ์ คือ ")
label_result.grid(row=4,column=0)

label_result_amount = Label(main_window ,text=" ")
label_result_amount.grid(row=4,column=1)

label_result_dest_currency = Label(main_window, text=" ")
label_result_dest_currency.grid(row=4,column=2)

main_window.mainloop()


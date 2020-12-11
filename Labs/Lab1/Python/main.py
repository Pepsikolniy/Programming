from tkinter import *
import json
import requests

#Функция, запрашивающая значение температуры у сервера
def reload_data(event=None):
	try:
		response = requests.get('http://localhost:3000/raw').content.decode("utf8")
		forecast_j = json.loads(response)

		desc.config(text=str(forecast_j["description"]))
		temp.config(text=str(round(forecast_j["temp"])) + "°C")
	except requests.exceptions.ConnectionError:
		pass

root = Tk()
root.title("Погода")
root.pack_propagate(0)
root.bind("<Button-1>", reload_data)
root.geometry("200x250")

top_frame =    Frame(root, bg="yellow")
middle_frame = Frame(root, bg="white")
bottom_frame = Frame(root, bg="yellow")

top_frame.pack(fill=X)
middle_frame.pack(expand=True, fill=BOTH)
bottom_frame.pack(side=BOTTOM, fill=X)

city = Label(top_frame, font=("Times New Roman", 12), text="Симферополь", bg="yellow")
desc = Label(top_frame, font=("Times New Roman", 12), bg="yellow")
temp = Label(middle_frame, font=("Times New Roman", 48), bg="white")

city.pack(pady=0)
desc.pack(pady=0)
temp.pack(expand=True)

reload_data()
root.mainloop()

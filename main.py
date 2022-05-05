import tkinter as tk
import requests
import time

def weather(canvas):
    city = place.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=9bf220b034f99dcba2f9bdf4b3583a4f"

    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    min_temp = int(json_data["main"]["temp_min"] - 273.15)
    max_temp = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind_speed = json_data["wind"]["speed"]
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data["sys"]["sunrise"] + 19800))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data["sys"]["sunset"] + 19800))

    display1 = f"condition - {condition} \n temp - {temp}°C\n"
    display2 = f"min - {min_temp}°C\n max - {max_temp}°C\n pressure - {pressure} psi\n humidty - {humidity} g/kg\n wind_speed - {wind_speed} m/s\n sunrise - {sunrise}\n sunset - {sunset}"

    label1.config(text = display1)
    label2.config(text = display2)




canvas = tk.Tk()
canvas.geometry("600x600")
canvas.title("Weather Forecasting")

place = tk.Entry(canvas, font = ("poppins", 25, "bold"))
place.pack(pady = 20)
place.focus()
place.bind('<Return>', weather)

label1 = tk.Label(canvas, font = ("poppins", 35, "bold"))
label1.pack()

label2 = tk.Label(canvas, font = ("poppins", 15, "bold"))
label2.pack()

canvas.mainloop()

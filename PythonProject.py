import tkinter as tk
import requests
from datetime import datetime

def getWeather(canvas):
    api_key = 'b532756daae24621694af153d1932475'
    location = textField.get()  
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
    api_data = requests.get(complete_api_link).json()

    temp_city = int(api_data['main']['temp'] - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    final_info = "Weather Stats for : \n {}   ||   {}".format(location.upper(), date_time)
    final_data = "\n" + weather_desc + "\n" + str(temp_city) + "degree"
    final_data2 = "\n" + "Current Humidity: " + str(hmdt) + "%" + "\n" + "Current Wind speed: " + str(wind_spd) + "kmph"
    label3.config(text = final_info)
    label1.config(text = final_data)
    label2.config(text = final_data2)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("Century Schoolbook",15,"bold")
t = ("Century Schoolbook",25,"bold")
k = ("californian FB",35,"bold italic")

textField = tk.Entry(canvas, justify='center', width=20, font = k)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()
label3 = tk.Label(canvas, font = k)
label3.pack()
canvas.mainloop()

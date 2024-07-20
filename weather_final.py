from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
import os

# Create the main window
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    try:
        location = geolocator.geocode(city)
        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER")

            api_key = "aa7140ee2321cdb54be3bb768a866850"  
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=aa7140ee2321cdb54be3bb768a866850&units=metric"
            
            response = requests.get(weather_url)
            data = response.json()

            # Debugging output
            print(f"Weather API URL: {weather_url}")
            print(f"Weather API Response Status Code: {response.status_code}")
            print(f"Weather API Response Data: {data}")

            if response.status_code == 200:
                wind = data["wind"]["speed"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"]
                pressure = data["main"]["pressure"]
                temp = data["main"]["temp"]
                condition = data["weather"][0]["main"]

                # Update weather information labels
                w1.config(text=f"{wind} m/s")
                w2.config(text=f"{humidity}%")
                w3.config(text=description.capitalize())
                w4.config(text=f"{pressure} hPa")
                t.config(text=f"{temp}°C")
                c.config(text=f"{condition} | FEELS LIKE {temp}°C")
            else:
                error_message = data.get("message", "Unknown error")
                messagebox.showerror("Error", f"Weather API Error: {error_message}")
        else:
            messagebox.showerror("Error", "City not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"Unable to retrieve data: {e}")

# Ensure the correct file path for the images
script_dir = os.path.dirname(os.path.abspath(__file__))

# Main search image
main_image_path = os.path.join(script_dir, "whether_changes", "search.png")
try:
    Search_image = PhotoImage(file=main_image_path)
    myimage = Label(root, image=Search_image)
    myimage.place(x=20, y=20)
except Exception as e:
    messagebox.showerror("Error", f"Unable to load main image: {e}")

# Search icon image
icon_image_path = os.path.join(script_dir, "whether_changes", "search_icon.png")
try:
    Search_icon = PhotoImage(file=icon_image_path)
    myimage_icon = Button(root, image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
    myimage_icon.place(x=400, y=34)
except Exception as e:
    messagebox.showerror("Error", f"Unable to load search icon image: {e}")

# Logo image
logo_image_path = os.path.join(script_dir, "whether_changes", "logo.png")
try:
    Logo_image = PhotoImage(file=logo_image_path)
    logo = Label(root, image=Logo_image)
    logo.place(x=150, y=100)
except Exception as e:
    messagebox.showerror("Error", f"Unable to load logo image: {e}")

# Frame image
frame_image_path = os.path.join(script_dir, "whether_changes", "box.png")
try:
    Frame_image = PhotoImage(file=frame_image_path)
    frame_myimage = Label(root, image=Frame_image)
    frame_myimage.pack(padx=5, pady=5, side=BOTTOM)
except Exception as e:
    messagebox.showerror("Error", f"Unable to load frame image: {e}")

# Create and place the text field
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

# Labels for displaying time and weather information
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)

clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Add labels for weather information with blue background color
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Placeholder labels for weather information
w1 = Label(root, text=". . .", font=("arial", 20, "bold"), bg="#1ab5ef")
w1.place(x=120, y=430)

w2 = Label(root, text=". . .", font=("arial", 20, "bold"), bg="#1ab5ef")
w2.place(x=250, y=430)

w3 = Label(root, text=". . .", font=("arial", 20, "bold"), bg="#1ab5ef")
w3.place(x=430, y=430)

w4 = Label(root, text=". . .", font=("arial", 20, "bold"), bg="#1ab5ef")
w4.place(x=650, y=430)

# Temperature and condition labels aligned horizontally
t = Label(root, text=". . .", font=("arial", 20, "bold"), bg="#1ab5ef")
t.place(x=500, y=250)  # Adjusted position to align towards right

c = Label(root, text=". . .", font=("arial", 20, "bold"), bg="#1ab5ef")
c.place(x=500, y=150)  # Adjusted position to align horizontally with temperature

# Start the main event loop
root.mainloop()

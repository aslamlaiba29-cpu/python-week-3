import tkinter as tk


def c_to_f():
   c = float(entry.get())
   f = (c * 9 / 5) + 32
   result_label.config(text="Fahrenheit: " + str(f))


def f_to_c():
   f = float(entry.get())
   c = (f - 32) * 5 / 9
   result_label.config(text="Celsius: " + str(c))


window = tk.Tk()
window.title("Temperature Converter")

label = tk.Label(window, text="Enter Temperature:")
label.pack()

entry = tk.Entry(window)
entry.pack()

btn1 = tk.Button(window, text="Celsius to Fahrenheit", command=c_to_f)
btn1.pack()

btn2 = tk.Button(window, text="Fahrenheit to Celsius", command=f_to_c)
btn2.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
import tkinter as tk

window = tk.Tk()
window.title("Simple Form")

name_label = tk.Label(window, text="Name")
email_label = tk.Label(window, text="Email")

name_entry = tk.Entry(window)
email_entry = tk.Entry(window)

submit_btn = tk.Button(window, text="Submit")

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)

email_label.grid(row=1, column=0)
email_entry.grid(row=1, column=1)

submit_btn.grid(row=2, column=1)

window.mainloop()
import tkinter as tk


def login():
   if (entry_userName.get() == "admin") & (entry_password.get() == "admin"):
       print("login Successfull")
   else:
       label_status.config(text="Login Failed", bg="red")
import tkinter as tk

# Function for login button
def login():
   username = user_entry.get()
   password = pass_entry.get()

   if username == "admin" and password == "1234":
       login_window.destroy()
       open_dashboard()
   else:
       status_label.config(text="Login Failed", bg="red")

# Dashboard window
def open_dashboard():
   dashboard = tk.Tk()
   dashboard.title("Dashboard")
   dashboard.geometry("300x200")

   label = tk.Label(dashboard, text="Welcome to Dashboard")
   label.pack(pady=50)

   dashboard.mainloop()

# Login window
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("300x200")

user_label = tk.Label(login_window, text="Username")
user_label.pack()

user_entry = tk.Entry(login_window)
user_entry.pack()

pass_label = tk.Label(login_window, text="Password")
pass_label.pack()

pass_entry = tk.Entry(login_window, show="*")
pass_entry.pack()

login_btn = tk.Button(login_window, text="Login", command=login)
login_btn.pack(pady=10)

status_label = tk.Label(login_window, text="")
status_label.pack()

login_window.mainloop()
#Final

import mysql.connector
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.simpledialog as sd


# Create a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="OPEN",
    database="e_library"
)

attemptCnt = 0

# Functions
def submitData():
    global attemptCnt
    attemptCnt += 1
    if attemptCnt > 3:
        mb.showerror("Login Failed", "You have exceeded your login attempts.")
    else:
        nameVal = name_entry.get()
        passwordVal = password_entry.get()
        cardIDVal = card_id_entry.get()

        try:
            cursor = db_connection.cursor()

            query = "SELECT * FROM Users WHERE username = %s AND password = %s AND CARD_ID = %s"
            values = (nameVal, passwordVal, cardIDVal)
            cursor.execute(query, values)

            result = cursor.fetchall()

            if result:
                mb.showinfo("Login Successful", "Welcome, " + result[0][1])
                import admin
                admin.root.update()
                admin.root.mainloop()
            else:
                mb.showerror("Login Failed", "Invalid credentials. Please try again")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

def registerUser():
    nameVal = name_entry.get()
    passwordVal = password_entry.get()
    mobileVal = mobile_entry.get()
    cardIDVal = card_id_entry.get()

    try:
        cursor = db_connection.cursor()

        query = "INSERT INTO Users (username, password, mobile, CARD_ID) VALUES (%s, %s, %s, %s)"
        values = (nameVal, passwordVal,mobileVal, cardIDVal)
        cursor.execute(query, values)
        db_connection.commit()

        mb.showinfo("Registration Successful", "User registered successfully!")
    except mysql.connector.Error as err:
        mb.showerror("Registration Failed", f"Error: {err}")
    finally:
        cursor.close()

rt = tk.Tk()
rt.geometry("400x450")
rt.title("Login Form")

checkValue = IntVar

Label(rt, text="Login to E-Library", font="ar 15 bold", bg='SteelBlue', fg='White').grid(ipadx=120, row=0, column=1, columnspan=3, sticky=N, pady=20)

frame_grid = tk.Frame(rt)

name = Label(rt, text="Name", font="Georgia 10")
name.grid(row=3, column=1, pady=10)

name_entry = Entry(rt)
name_entry.grid(row=3, column=2, ipadx=20, pady=10)

password = Label(rt, text="Password", font="Georgia 10")
password.grid(row=5, column=1, pady=10)

password_entry = Entry(rt, show="*")
password_entry.grid(row=5, column=2, ipadx=20, pady=10)


mobile = Label(rt, text="Mobile", font="Georgia 10")
mobile.grid(row=7, column=1, pady=10)

mobile_entry = Entry(rt)
mobile_entry.grid(row=7, column=2, ipadx=20, pady=10)


CardID = Label(rt, text="Card-ID", font="Georgia 10")
CardID.grid(row=9, column=1, pady=10)

card_id_entry = Entry(rt)
card_id_entry.grid(row=9, column=2, ipadx=20, pady=10)

checkbtn = Checkbutton(text="Remember me", variable=checkValue)
checkbtn.grid(row=11, column=2, ipadx=7, pady=10, sticky=W)

login_btn = Button(rt, text="Login", command=submitData)
login_btn.grid(row=12, column=2, ipadx=30, pady=10, sticky=W, columnspan= 3)

regBtn = Button(rt, text="Not registered? Create Your Account.", font="ar 7", command=registerUser)
regBtn.grid(row=13, column=2, sticky=W)

rt.mainloop()

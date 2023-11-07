import tkinter as tk
import mysql.connector

def search_books():
    search_query = search_text.get("1.0", "end-1c")  # Get the text content of the Text widget
    # Query the database to retrieve book results based on the search_query
    # You can modify the SQL query to search by title, author, genre, ISBN, etc.
    query = "SELECT BK_NAME, AUTHOR_NAME FROM Library WHERE BK_NAME LIKE %s OR AUTHOR_NAME LIKE %s"
    values = (f"%{search_query}%", f"%{search_query}%")
    cursor.execute(query, values)

    # Fetch all matching book results
    book_results = cursor.fetchall()

    # Populate the listbox with book results
    book_listbox.delete(0, tk.END)
    for book in book_results:
        book_listbox.insert(tk.END, f"{book[0]} by {book[1]}")

root = tk.Tk()
root.title("Library User Panel")
root.geometry("800x600")

# Initialize the database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="OPEN",
    database="e_library"
)
cursor = conn.cursor()

# Create and configure widgets
search_text = tk.Text(root, font=('Times New Roman', 12), width=30, height=1)
search_text.place(x=8, y=33)

# Create a "Search" button
search_button = tk.Button(root, text="Search", font=('Gill Sans MT', 13), width=10, command=search_books)
search_button.place(x=350, y=32, height=30)

# Create a listbox to display book results
book_listbox = tk.Listbox(root, font=("Arial", 12), width=45, height=10)
book_listbox.place(x=8, y=75)

root.mainloop()




# # Importing all necessary modules

# from tkinter import *
# import tkinter.ttk as ttk
# import tkinter.messagebox as mb
# import tkinter.simpledialog as sd

# def books_issued():
#     #Code for issued books from the Library database
#     pass
# # Variables
# lf_bg = 'LightSkyBlue'  # Left Frame Background Color
# rtf_bg = 'DeepSkyBlue'  # Right Top Frame Background Color
# rbf_bg = 'DodgerBlue'  # Right Bottom Frame Background Color
# btn_hlb_bg = 'SteelBlue'  # Background color for Head Labels and Buttons

# lbl_font = ('Georgia', 13)  # Font for all labels
# entry_font = ('Times New Roman', 12)  # Font for all Entry widgets
# btn_font = ('Gill Sans MT', 13)

# # Initializing the main GUI window
# root = Tk()
# root.title('E-Library')
# root.geometry('1010x530')
# root.resizable(0, 0)

# Label(root, text='E - LIBRARY (User)', font=("Noto Sans CJK TC", 15, 'bold'), bg=btn_hlb_bg, fg='White').pack(side=TOP, fill=X)

# # StringVars
# bk_status = StringVar()
# bk_name = StringVar()
# bk_id = StringVar()
# author_name = StringVar()
# card_id = StringVar()

# # Frames
# left_frame = Frame(root, bg=lf_bg)
# left_frame.place(x=0, y=30, relwidth=0.3, relheight=0.96)

# RT_frame = Frame(root, bg=rtf_bg)
# RT_frame.place(relx=0.3, y=30, relheight=0.2, relwidth=0.7)

# RB_frame = Frame(root)
# RB_frame.place(relx=0.3, rely=0.24, relheight=0.785, relwidth=0.7)

# # Left Frame
# Label(left_frame, text='Book Name', bg=lf_bg, font=lbl_font).place(x=98, y=25)
# Entry(left_frame, width=25, font=entry_font, text=bk_name).place(x=45, y=55)

# Label(left_frame, text='Book ID', bg=lf_bg, font=lbl_font).place(x=110, y=105)
# bk_id_entry = Entry(left_frame, width=25, font=entry_font, text=bk_id)
# bk_id_entry.place(x=45, y=135)

# Label(left_frame, text='Author Name', bg=lf_bg, font=lbl_font).place(x=90, y=185)
# Entry(left_frame, width=25, font=entry_font, text=author_name).place(x=45, y=215)

# Label(left_frame, text='Status of the Book', bg=lf_bg, font=lbl_font).place(x=75, y=265)
# dd = OptionMenu(left_frame, bk_status, *['Available', 'Issued'])
# dd.configure(font=entry_font, width=12)
# dd.place(x=75, y=300)

# # submit = Button(left_frame, text='Add new record', font=btn_font, bg=btn_hlb_bg, width=20, command=add_record)
# # submit.place(x=50, y=375)

# # clear = Button(left_frame, text='Clear fields', font=btn_font, bg=btn_hlb_bg, width=20, command=clear_fields)
# # clear.place(x=50, y=435)

# # Right Top Frame
# Text(RT_frame, font=btn_font, bg='White', width=37).place(x=8, y=33, height=30)
# Button(RT_frame, text='Search', font=btn_font, bg=btn_hlb_bg, width=10).place(x=350, y=32, height=30)
# # Button(RT_frame, text='Update book details', font=btn_font, bg=btn_hlb_bg, width=17,
# #        command=update_record).place(x=348, y=30)


# # Right Bottom Frame
# Label(RB_frame, text='BOOKS Issued', bg=rbf_bg, font=("Noto Sans CJK TC", 15, 'bold')).pack(side=TOP, fill=X)

# tree = ttk.Treeview(RB_frame, selectmode=BROWSE, columns=('Book Name', 'Book ID', 'Author', 'Status', 'Due Date'))

# XScrollbar = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
# YScrollbar = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
# XScrollbar.pack(side=BOTTOM, fill=X)
# YScrollbar.pack(side=RIGHT, fill=Y)

# tree.config(xscrollcommand=XScrollbar.set, yscrollcommand=YScrollbar.set)

# tree.heading('Book Name', text='Book Name', anchor=CENTER)
# tree.heading('Book ID', text='Book ID', anchor=CENTER)
# tree.heading('Author', text='Author', anchor=CENTER)
# tree.heading('Status', text='Status of the Book', anchor=CENTER)
# tree.heading('Due Date', text='Card ID of the Issuer', anchor=CENTER)

# tree.column('#0', width=0, stretch=NO)
# tree.column('#1', width=225, stretch=NO)
# tree.column('#2', width=70, stretch=NO)
# tree.column('#3', width=150, stretch=NO)
# tree.column('#4', width=105, stretch=NO)
# tree.column('#5', width=132, stretch=NO)

# style = ttk.Style()
# style.configure("Treeview",
#                     foreground="black",
#                     rowheight=20,
#                     fieldbackground="yellow"
#                     )
# style.map('Treeview',
#               background=[('selected', 'orange')])

# tree.place(y=30, x=0, relheight=0.9, relwidth=1)


# # Finalizing the window
# root.update()
# root.mainloop()

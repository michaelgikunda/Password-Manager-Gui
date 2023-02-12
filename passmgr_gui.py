#Aim is create a nice gui for the CLI password manager created earlier and import its fucntionality
#Package use intended custom tkinter

from customtkinter import *
import customtkinter

#Main WIndow
root = customtkinter.CTk()
root.geometry("400x400")
root.config(bg="black")
root.title("Password Manager")
root.attributes("-alpha", 0.9)

#Centering window
def win_center():
    width =400
    height = 400

    screen_width = root. winfo_screenwidth()
    screen_height  = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' %(width, height, x, y))
win_center()

#Destroys The 2 Buttons and changes window name
def new_window(title_value):
    store_button.destroy()
    retrive_button.destroy()

    root.title(title_value)

#destroy compnents to give illusion of going back
def destroy_components():
    root.title("Password Manager")
    try:
        retrive_label.destroy()
        retrive_entry.destroy()
        return_button.destroy()
    except:
        password_label.destroy()
        password_entry.destroy()
        service_label.destroy()
        return_button.destroy()
        service_entry.destroy()

#Return to main window
def return_function():
    global return_button
    def perform():
        main()
        destroy_components()
        
    return_button  =  customtkinter.CTkButton(root, text="Back", bg_color="black", fg_color="white", text_color="black", command=perform, width=20)
    return_button.pack(pady=10)

#Retrive Function
def retrive_function():
    global retrive_label
    global retrive_entry
    new_window("Retrive")

    #Using inheritance to impliment functionality of passmanager class
    def get_password(event):
        import passmanager
        m = passmanager.get_password(retrive_entry.get())

        retrive_entry.delete(0, END)
        retrive_label.configure(text=m)
    
    retrive_label  = customtkinter.CTkLabel(root, text="Enter Service Name", font=("zector", 20), bg_color="black")
    retrive_label.pack(pady=100)

    retrive_entry = customtkinter.CTkEntry(root, bg_color="black")
    retrive_entry.pack(pady=5)

    return_function()

    root.bind('<Return>', get_password)

#Store Function
def store_function():
    global service_entry, service_label, password_entry, password_label
    new_window("Store")

    #Using inheritance to impliment functionality of passmanager class
    def set_password(event):
        import passmanager
        m = passmanager.store_password(service_entry.get(), password_entry.get())

        service_entry.delete(0, END)
        password_entry.delete(0, END)
        service_label.configure(text="Sucess")
        password_label.configure(text="Sucess")
    
    service_label  = customtkinter.CTkLabel(root, text="Enter Service Name", font=("zector", 20), bg_color="black")
    service_label.pack(pady=50)

    service_entry = customtkinter.CTkEntry(root, bg_color="black")
    service_entry.pack(pady=5)

    password_label  = customtkinter.CTkLabel(root, text="Enter Password", font=("zector", 20), bg_color="black")
    password_label.pack(pady=30)

    password_entry = customtkinter.CTkEntry(root, bg_color="black")
    password_entry.pack(pady=5)

    return_function()

    root.bind('<Return>', set_password)

#Buttons
def main():
    global retrive_button
    global store_button
    
    retrive_button = customtkinter.CTkButton(root, text="Retrive",text_color = "black", bg_color="black", fg_color="white", height=80, font=("zector", 20), command=retrive_function)
    retrive_button.pack(pady=80)

    store_button = customtkinter.CTkButton(root, text="Store",text_color = "black", bg_color="black", fg_color="white", height=80, font=("zector", 20), command=store_function)
    store_button.pack(pady=10)

main()

root.mainloop()
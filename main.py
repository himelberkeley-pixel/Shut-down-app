from tkinter import *
import os

# -------------------------------
# Define system control functions
# -------------------------------

def restart():
    os.system("shutdown /r /t 1")  # Restart immediately

def restart_time():
    os.system("shutdown /r /t 20")  # Restart after 20 seconds

def logout():
    os.system("shutdown -l")  # Log out user (correct command)

def shutdown():
    os.system("shutdown /s /t 1")  # Shutdown immediately


# -------------------------------
# GUI Setup
# -------------------------------

st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="blue")

# -------------------------------
# Buttons
# -------------------------------

r_button = Button(
    st, text="Restart",
    font=('Times New Roman', 20, 'bold'),
    relief=RAISED, cursor='plus', command=restart
)
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(
    st, text="Restart Time (20s)",
    font=('Times New Roman', 20, 'bold'),
    relief=RAISED, cursor='plus', command=restart_time
)
rt_button.place(x=150, y=160, height=50, width=200)

lg_button = Button(
    st, text="Log Out",
    font=('Times New Roman', 20, 'bold'),
    relief=RAISED, cursor='plus', command=logout
)
lg_button.place(x=150, y=260, height=50, width=200)

st_button = Button(
    st, text="Shut Down",
    font=('Times New Roman', 20, 'bold'),
    relief=RAISED, cursor='plus', command=shutdown
)
st_button.place(x=150, y=360, height=50, width=200)

# -------------------------------
# Run App
# -------------------------------

st.mainloop()

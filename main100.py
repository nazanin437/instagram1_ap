from tkinter import *
from tkinter import PhotoImage
from signup import SignUpWindow
from login import LoginWindow

def open_signup_window():
    SignUpWindow(window)

def open_login_window():
    LoginWindow(window)

window = Tk()
window.title("instagram")
window.geometry("900x500")
window.resizable(0, 0)

photo = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Desktop\my_p\instagram.png")
window.iconphoto(True, photo)

login_frame_chap = Frame(window, bg="white", width=450, height=500)
login_frame_chap.place(x=0, y=0)

lb_insta = Label(login_frame_chap, text="WELCOME TO INSTAGRAM", bg="white", font=("Helvetica", "18", 'bold'))
lb_insta.place(x=80, y=50)

lb_singup = Label(login_frame_chap, text="If you do not have an account, please register first.", bg="white", font=("Helvetica", "11"))
lb_singup.place(x=80, y=150)

photo_bt = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Pictures\AnyDesk\login01.png")
bot_lb = Label(login_frame_chap, image=photo_bt, border=0)
bot_lb.place(x=70, y=180)

lb_login_ = Label(login_frame_chap, text="If you have an account, log in to your account.", bg="white", font=("Helvetica", "11"))
lb_login_.place(x=80, y=230)

bot_2b = Label(login_frame_chap, image=photo_bt, border=0)
bot_2b.place(x=70, y=260)

Button_1 = Button(login_frame_chap, text="Sign Up", font=("Helvetica", "11", 'bold'), bg="#62449d", fg="white", border=0, height=1, width=28, activebackground="#62449d", activeforeground="#62449d", command=open_signup_window, cursor="hand2")
Button_1.place(x=85, y=190)

Button_2 = Button(login_frame_chap, text="Login", font=("Helvetica", "11", 'bold'), bg="#62449d", fg="white", border=0, height=1, width=28, activebackground="#62449d", activeforeground="#62449d", command=open_login_window, cursor="hand2")
Button_2.place(x=85, y=270)

login_frame_rast = Frame(window, bg="blue", width=450, height=500)
login_frame_rast.place(x=450, y=0)

bg_login = PhotoImage(file=r"C:\Users\Ofogh Rayaneh0211\Pictures\AnyDesk\login1.png")
bg_lb = Label(login_frame_rast, image=bg_login)
bg_lb.place(x=0, y=0)

window.mainloop()

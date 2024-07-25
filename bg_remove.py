from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from rembg import remove
import time

def open_file():
    global img,open_path, disp_img
    filetype = (("Image file", "*.png;*.jpg;.*jpeg"), ("All files", "*.*"))
    open_path = fd.askopenfilename(filetypes=filetype, title="Select Image")
    img = Image.open(open_path)
    # img = img.resize((300, 300), Image.LANCZOS)
    disp_img = ImageTk.PhotoImage(img)
    label_img.config(image=disp_img, bg="#005073")
    btn_remove = Button(frame3, text="Remove Background", padx=20, pady=5, bg="#005073", fg="white", activebackground="#005073", activeforeground="white", font=("Arial", 15), command=remove_bg)
    btn_remove.grid(row=1, column=1)

def remove_bg():
    global open_path, img, disp_img
    rem_bg = remove(img)
    save_path = fd.asksaveasfilename(defaultextension=".png", title="Save As")
    rem_bg.save(save_path)
    disp_img = ImageTk.PhotoImage(rem_bg)
    label_img.config(image=disp_img, bg="#005073")
    label_msg = Label(frame3, text="File Saved as PNG", font=("Arial", 15), bg="skyblue", fg="#005073")
    label_msg.grid(row=2, column=1, padx=10)
    label_msg.after(3000, label_msg.destroy)


if __name__ == '__main__':
    root = Tk()
    root.geometry('777x555')
    root.title("Bg Remover")
    root.config(bg="skyblue")

    frame1 = Frame(root, bg="skyblue")
    frame1.pack()

    frame2 = Frame(frame1, bg="skyblue")
    frame2.pack(fill=X, padx=10, pady=10)
    label_title = Label(frame2, text="Bg Remover", font=("Helvatica", 35, "bold"), bg="skyblue", fg="#005073")
    label_title.grid(padx=50, pady=30)

    frame3 =Frame(frame1, bg="skyblue")
    frame3.pack(pady=20)

    label_app = Label(frame3, text=f"Remove Image \nBackground \n using Bg Remover.", font=("Times", 40), bg="skyblue", fg="#005073")
    label_app.grid(row=0, column=0, padx=30)

    frame4 = Frame(frame1, bg="skyblue")
    frame4.pack()

    btn_start = Button(frame3, text="Get started", padx=20, pady=5, font=("Arial", 15), bg="#005073", fg="white", activebackground="#005073", activeforeground="white", command=open_file)
    btn_start.grid(row=1, column=0, pady=40)

    label_img = Label(frame3, text="", bg="skyblue")
    label_img.grid(row=0, column=1, padx=300)

    root.mainloop()

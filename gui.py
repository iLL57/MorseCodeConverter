from tkinter import *
from PIL import Image, ImageTk
from main import encode, decode


def resize_image(event):
    new_width = event.width
    new_height = event.height

    # Resize the image
    resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    new_background_image = ImageTk.PhotoImage(resized_image)

    # Update the canvas with the new image
    canvas.itemconfig(background, image=new_background_image)
    canvas.image = new_background_image  # Keep a reference to prevent garbage collection


def on_cypher_button_click():
    try:
        message = text.get("1.0", END).strip()
        if radio_state.get() == 1:
            result_message = encode(message)
        else:
            result_message = decode(message)
        result.delete("1.0", END)
        result.insert("1.0", result_message)
    except ValueError as e:
        result.delete("1.0", END)
        result.insert(END, str(e))


window = Tk()
window.title("Morse Code Encrypter")
window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

# Load the original image
original_image = Image.open("decode_img.png")

# Create a Canvas widget
canvas = Canvas(window, width=500, height=400)
canvas.grid(row=0, column=0, columnspan=3, rowspan=6, sticky='nsew')

# Create the initial background image
background_image = ImageTk.PhotoImage(original_image)
background = canvas.create_image(0, 0, anchor='nw', image=background_image)

# Bind the resize event to the resize_image function
window.bind("<Configure>", resize_image)

# Configure grid to have 3 columns and rows to stretch
for i in range(3):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)

# Label
msg_label = canvas.create_text(250, 50, text='Enter your message in the box below', font=('Open Sans', 26),
                               fill='white')

# Entry Window
text = Text(canvas, width=50, height=5)
text_window = canvas.create_window(250, 120, window=text)


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(canvas, text="Encrypt", value=1, variable=radio_state, command=radio_used, bg='#a38156')
radiobutton2 = Radiobutton(canvas, text="Decrypt", value=2, variable=radio_state, command=radio_used, bg='#a38156')
radiobutton1_window = canvas.create_window(200, 200, window=radiobutton1)
radiobutton2_window = canvas.create_window(300, 200, window=radiobutton2)

# Button
button = Button(canvas, text='Cypher Message', bg='#f0f0f0', command=on_cypher_button_click)
button_window = canvas.create_window(250, 250, window=button)

# Result Window
result = Text(canvas, width=50, height=5)
result_window = canvas.create_window(250, 325, window=result)

window.mainloop()

import customtkinter as ctk
from PIL import Image


def get_info_by_dork(dork, frame):
    if dork == "archivos tipo:":
        return [ctk.CTkEntry(master=frame)]
    elif dork == "que la url contenga:":
        return [ctk.CTkEntry(master=frame), ctk.CTkEntry(master=frame)]
    else:
        return []


def dork_change(name, frame_id, dork_info, frame, *args):
    print(name.get() + " " + str(frame_id))
    for elem in dork_info[frame_id]:
        elem.pack_forget()

    info = get_info_by_dork(name.get(), frame)
    for elem in info:
        elem.pack(side="left", padx="7 3")
    dork_info[frame_id] = info


def add_dork(input_frame, list_dorks, list_info, last_add):
    last_add.pack_forget()

    # start elements

    dork_frame = ctk.CTkFrame(master=input_frame)
    DORKS = [
        "Elige opción",
        "archivos tipo:",
        "que la url contenga:"
    ]
    inside_of_menu = ctk.StringVar()
    inside_of_menu.set(DORKS[0])
    dork_select = ctk.CTkOptionMenu(master=dork_frame, variable=inside_of_menu, values=DORKS,
                                    corner_radius=10)

    # elements logic

    list_dorks.append(dork_select)
    list_info.append([])
    dork_select.configure(
        command=lambda *args, inside=inside_of_menu, frame_id=list_dorks.index(dork_select), dork_info=list_info,
                       frame=dork_frame:
        dork_change(inside, frame_id, list_info, frame, *args))
    b_add = ctk.CTkButton(master=input_frame, text="+",
                          command=lambda: add_dork(input_frame, list_dorks, list_info, last_add))

    last_add = b_add

    # show elements

    dork_select.pack(side="left")
    dork_frame.pack(side="top", anchor='nw', pady="20")
    b_add.pack(side="left", padx="10 0")
    input_frame.pack(side="top", anchor='nw', padx="110", pady="70")


def main_loop():
    logo.pack_forget()
    b_inicio.pack_forget()
    list_dorks = []
    list_info = []
    add_button = ctk.CTkButton(master=window)
    input_frame = ctk.CTkFrame(master=window)
    add_dork(input_frame, list_dorks, list_info, add_button)
    print("init succesful")


# start menu

# describe window

window = ctk.CTk()
window.geometry("1280x700")
window.title("EasyDorks")
window.configure(bg='white')

# logo

master_frame = ctk.CTkFrame(master=)
img = ctk.CTkImage(
    light_image=Image.open("logo.png"),
    dark_image=Image.open("logo.png"),
    size=(400, 400))
logo = ctk.CTkLabel(window, text="", image=img)
logo.pack(pady="70 0")

# init CTkButton

b_inicio = ctk.CTkButton(master=window, text="INICIO", command=main_loop)
b_inicio.pack(pady="20 0")

# window.bind('<Configure>', )

window.mainloop()

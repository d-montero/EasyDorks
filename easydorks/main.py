import tkinter
import webbrowser

import customtkinter
import customtkinter as ctk
import dork_functions as df
import dork_history as dh
import dork_wiki as dw
from PIL import Image

# https://github.com/d-montero/EasyDorks
result = "https://www.google.com"


def clear_page():
    for widget in master_frame.winfo_children():
        widget.forget()


def chooseAppearanceMode():
    if ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("Dark")
    else:
        ctk.set_appearance_mode("Light")

def initializeSwitchVar():
    if ctk.get_appearance_mode() == "Light":
        return "off"
    else:
        return "on"


# do function

str_to_func = {
    "Elige una opción": df.nada,
    "Coincidencia exacta": df.searchInCoincidenceDork,
    "Sitio web": df.searchInSiteDork,
    "Tipo de archivo": df.fileTypeDork,
    "Contenido de la url": df.searchInurlDork,
    "Contenido del título": df.searchInTitleDork,
    "Contenido de la página": df.searchInTextDork,
    "Exclusión de los resultados": df.searchInExclusionDork
}


def combine_google_search_urls(urls, operator="AND"):
    combined_query = f"%20{operator}%20".join(urls)
    search_url = f"https://www.google.com/search?q={combined_query}"
    return search_url


def do_dorks(dorks, info, label):
    urls = []
    for dork_num in range(len(dorks)):
        info_in_dork = info[dork_num]
        if not info_in_dork:
            info_in_dork = "nada"
        else:
            info_in_dork = info_in_dork[0].get()
        print(info_in_dork)
        url = str_to_func[dorks[dork_num].get()](info_in_dork)[0]
        if url != "":
            print(url)
            urls.append(url)
    for i in range(len(urls)):
        urls[i] = urls[i][urls[i].index("q=") + len("q="):len(urls[i])]
    global result
    result = combine_google_search_urls(urls)
    print(result)
    label.configure(text=result)
    dh.writeLastFive(result)


# interfaces functions

def get_info_by_dork(dork, frame):
    if dork != "Elige una opción":
        return [ctk.CTkEntry(master=frame, border_color=("black","white"), border_width=2, corner_radius=10, fg_color=("white","black"))]
    else:
        return []


def dork_change(name, frame_id, dork_info, frame, last_add, *args):
    if name.get() != "Elige una opción":
        if frame_id == len(dork_info) - 1:
            last_add.pack(side="left", padx="10 0", pady=(0, 10))
    else:
        last_add.pack_forget()

    print(name.get() + " " + str(frame_id))
    for elem in dork_info[frame_id]:
        elem.pack_forget()

    info = get_info_by_dork(name.get(), frame)
    for elem in info:
        elem.pack(side="left", padx="7 3")
    dork_info[frame_id] = info


def add_dork(input_frame, list_dorks, list_info, last_add):
    last_add.pack_forget()
    optionMenu_Font = ctk.CTkFont(family="Helvetica", size=14)
    # start elements

    dork_frame = ctk.CTkFrame(master=input_frame, border_color=("white","black"), fg_color=("white","black"), bg_color=("white","black"),
                              border_width=2, corner_radius=10)
    dorks = [
        "Elige una opción",
        "Coincidencia exacta",
        "Sitio web",
        "Tipo de archivo",
        "Contenido de la url",
        "Contenido del título",
        "Contenido de la página",
        "Exclusión de los resultados"
    ]
    inside_of_menu = ctk.StringVar()
    inside_of_menu.set(dorks[0])
    dork_select = ctk.CTkOptionMenu(master=dork_frame, variable=inside_of_menu, values=dorks,
                                    corner_radius=10, fg_color=("white","black"), text_color=("black","white"), width=250, bg_color=("white","black"),
                                    button_color=("white","black"), button_hover_color=("yellow","purple"), dropdown_fg_color=("white","black"),
                                    dropdown_hover_color=("yellow","purple"), font=optionMenu_Font, dropdown_font=optionMenu_Font)

    # elements logic

    list_dorks.append(dork_select)
    list_info.append([])
    b_add = ctk.CTkButton(master=input_frame, text="+",
                          command=lambda: add_dork(input_frame, list_dorks, list_info, last_add),
                          width=400, fg_color=("white", "black"), hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, font=optionMenu_Font, text_color=("black", "white"))

    last_add = b_add
    dork_select.configure(
        command=lambda *args, inside=inside_of_menu, frame_id=list_dorks.index(dork_select), dork_info=list_info, frame=dork_frame, add=last_add:
        dork_change(inside, frame_id, list_info, frame, add, *args), button_color=("white","black"), text_color=("black","white"),
        bg_color=(("white","black")), button_hover_color=("yellow","purple"), corner_radius=10)
    # show elements

    dork_select.pack(side="left")
    dork_frame.pack(side="top", anchor="center", pady="20", padx="10")
    input_frame.pack(side="top", anchor="center", pady=(200, 0))

def main_loop():
    myButtonFont = ctk.CTkFont(family="Helvetica", size=14, weight="bold")

    clear_page()
    list_dorks = []
    list_info = []
    add_button = ctk.CTkButton(master=master_frame)
    input_frame = ctk.CTkFrame(master=master_frame, fg_color=("white","black"), border_color=("black","white"), border_width=2, corner_radius=10)


    home_button = ctk.CTkButton(master=master_frame, command=title_page, text="PÁGINA PRINCIPAL", fg_color=("white","black"),
                                hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), font=myButtonFont, )
    home_button.pack(anchor="n", side="left", padx=(0, 20), pady=30)


    us_button = ctk.CTkButton(master=master_frame, command=about_us, text="SOBRE NOSOTROS", fg_color=("white","black"),
                              hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), font=myButtonFont)
    us_button.pack(anchor="n", side="left", pady=30)


    moon.place(x=1044.5, y=27.5)
    switch.pack(side="right", anchor="n", pady=30, padx=(8, 0))
    sun.pack(side="right", anchor="n", pady=29, padx=(200, 0))

    moon.lift(switch)

    add_dork(input_frame, list_dorks, list_info, add_button)
    result_label = ctk.CTkLabel(master=master_frame, text=result, font=ctk.CTkFont(family="Helvetica", size=10, weight="bold"))
    result_label.pack(pady=(50, 80), anchor="center")
    do_button = ctk.CTkButton(master=master_frame,
                              command=lambda dorks=list_dorks, info=list_info, label=result_label: do_dorks(dorks, info,
                                                                                                            result_label),
                              text="OBTENER URL", fg_color=("white", "black"), hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black", "white"), font=myButtonFont)
    do_button.pack(anchor="s", side="left", padx=(0, 20))
    link = ctk.CTkButton(master=master_frame, text="BUSCAR", cursor="hand2", fg_color=("white", "black"), hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black", "white"), font=myButtonFont)
    link.pack(anchor="s", pady="20 0", side="left", padx=(0, 20))
    link.bind("<Button-1>", lambda e: webbrowser.open_new(result))
    history_button = ctk.CTkButton(master=master_frame, text="HISTORIAL", fg_color=("white", "black"), hover_color=("yellow","purple"), command=history, border_color=("black","white"), border_width=2, text_color=("black", "white"), font=myButtonFont)
    history_button.pack(anchor="s", pady="20 0", side="left")
    print("init succesful")

# title page creation


def title_page():
    clear_page()
    master_frame.forget()

    moon.place(x=600, y=27.5)
    switch.pack(side="right", anchor="n", pady=30, padx=(8, 0))
    sun.pack(side="right", anchor="n", pady=29)
    moon.lift(switch)

    logo.pack(pady=(70, 0), side="top", padx=(125, 0))

    b_inicio.pack(pady=(160, 30), side="left", anchor="center", padx=(153, 37))
    b_wiki.pack(pady=(160, 30), side="top", anchor="center")
    master_frame.pack()


# about us page creation

def about_us():
    clear_page()
    moon.place_forget()
    back_button = ctk.CTkButton(master=master_frame, command=main_loop, text="<", fg_color=("white","black"),
                                hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), font=myButtonFont, width=75)

    us = ctk.CTkLabel(master=master_frame, text="Aplicación creada por el grupo Agile Eagles\n\n"
                                                "Ingeniería de Software, del Grado en Ingeniería de la Ciberseguridad de la Universidad Rey Juan Carlos\n\n\n"
                                                "Correo de contacto --> contact@agileagles.com\n\n", font=("Helvetica", 24))
    us.pack(pady=175, side="bottom")

    back_button.pack(pady=30, side="left", padx=(30, 0))
    moon.place(x=1070, y=27.5)
    switch.pack(side="right", anchor="n", pady=30, padx=(8, 0))
    sun.pack(side="right", anchor="n", pady=29)
    moon.lift(switch)




# wiki

def wiki():
    wiki_window = ctk.CTk()
    ctk.set_appearance_mode("system")
    wiki_window.geometry("700x800")
    wiki_window.title("Wiki EasyDorks")
    wiki_window.configure(fg_color=("white","black"))
    wiki_window.mainloop()


# history

def history():
    clear_page()
    back_button = ctk.CTkButton(master=master_frame, command=main_loop, text="<", fg_color=("white","black"),
                                hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), width=75, font=myButtonFont)

    history = dh.readLastFive()
    length = len(history)
    for index, link in enumerate(history):
        reversed_index = length - 1 - index
        entry = ctk.CTkLabel(master=master_frame, text=str(reversed_index+1)+": "+link, text_color=("black", "white"), font=myButtonFont)
        entry.pack(pady=15, side="bottom")

    back_button.pack(pady=(30, 100), side="left", padx=(30, 0))

    moon.place(x=980, y=27.5)
    switch.pack(side="right", anchor="n", pady=(30, 100), padx=(8, 0))
    sun.pack(side="right", anchor="n", pady=(29, 101), padx=(800, 0))
    moon.lift(switch)




# init

window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.geometry("1280x700")
window.title("EasyDorks")
window.configure(fg_color=("white","black"))

# logo

master_frame = ctk.CTkFrame(master=window, fg_color=("white","black"))

myButtonFont = ctk.CTkFont(family="Helvetica", size=14, weight="bold")

img = ctk.CTkImage(
    light_image=Image.open("logo.png"),
    dark_image=Image.open("logo_dark.png"),
    size=(400, 400))
logo = ctk.CTkLabel(master=master_frame, text="", image=img)

# moon icon

image = ctk.CTkImage(
    light_image=Image.open("black_moon.png"),
    dark_image=Image.open("white_moon.png"),
    size=(12, 12))
moon = ctk.CTkLabel(master=master_frame, text="", image=image)

# sun icon

image2 = ctk.CTkImage(
    light_image=Image.open("black_sun.png"),
    dark_image=Image.open("white_sun.png"),
    size=(15, 15))
sun = ctk.CTkLabel(master=master_frame, text="", image=image2)

# switch appearance mode

switch_var = customtkinter.StringVar(value=initializeSwitchVar())
switch = customtkinter.CTkSwitch(master=master_frame, command=chooseAppearanceMode,
                                     variable=switch_var, onvalue="on", offvalue="off", text="", fg_color="white", button_color=("black", "white"), border_color=("black", "white"), border_width=2, progress_color="black", switch_width=45)

# start button

b_inicio = ctk.CTkButton(master=master_frame, text="INICIO", command=main_loop,
                         text_color=("black","white"), fg_color=("white","black"), border_color=("black","white"), bg_color=("white","black"),
                         border_width=2, hover_color=("yellow","purple"), font=myButtonFont)

b_wiki = ctk.CTkButton(master=master_frame, command=dw.wiki, text="WIKI",text_color=("black","white"), fg_color=("white","black"), border_color=("black","white"), bg_color=("white","black"),
                         border_width=2, hover_color=("yellow","purple"), font=myButtonFont)

title_page()

window.mainloop()

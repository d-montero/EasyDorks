import tkinter
import webbrowser

import customtkinter
import customtkinter as ctk
import dork_functions as df
import dork_history as dh
import dork_wiki as dw
from PIL import Image

# https://github.com/d-montero/EasyDorks
result = ""
global add_button, remove_button

def clearResult():
    global result
    result = ""

# init with google dorks

global dorksType
global dorksType_history

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

# dorks

dorks_Google = [
        "Elige una opción",
        "Coincidencia exacta",
        "Sitio web",
        "Tipo de archivo",
        "Contenido de la url",
        "Contenido del título",
        "Contenido de la página",
        "Exclusión de los resultados",
        "Contenido relacionado",
        "Preferencia de contenido",
        "Intervalo"
    ]

dorks_Shodan = [
    "Elige una opción",
    "Base de datos",
    "Puerto",
    "Sistema operativo",
    "Servidor web"
]

# do function

str_to_func_Google = {
    "Elige una opción": df.nada,
    "Coincidencia exacta": df.searchInCoincidenceDork,
    "Sitio web": df.searchInSiteDork,
    "Tipo de archivo": df.fileTypeDork,
    "Contenido de la url": df.searchInurlDork,
    "Contenido del título": df.searchInTitleDork,
    "Contenido de la página": df.searchInTextDork,
    "Exclusión de los resultados": df.searchInExclusionDork,
    "Contenido relacionado": df.serachRelated,
    "Preferencia de contenido": df.serachPrefer,
    "Intervalo": df.searchIntervalo
}

str_to_func_Shodan = {
    "Elige una opción": df.nada,
    "Base de datos": df.searchDatabase,
    "Puerto": df.searchPort,
    "Sistema operativo": df.specificOperatingSystem,
    "Servidor web": df.webServers
}




def combine_search_urls(urls, operator="AND"):
    combined_query_google = f"%20{operator}%20".join(urls)
    combined_query_shodan = f"%20".join(urls)
    if dorksType == 0:
        search_url = f"https://www.google.com/search?q={combined_query_google}"
    else:
        search_url = f"https://www.shodan.io/search?query={combined_query_shodan}"

    return search_url


def do_dorks(dorks, info, label):
    urls = []
    for dork_num in range(len(dorks)):
        info_in_dork = info[dork_num]
        if not info_in_dork:
            info_in_dork = "nada"
        else:
            info_list = []
            for i in info_in_dork:
                info_list.append(i.get())
        print(info_list)

        if dorksType == 0:
            url = str_to_func_Google[dorks[dork_num].get()](info_list)
        else:
            url = str_to_func_Shodan[dorks[dork_num].get()](info_list)

        if url != "":
            print(url)
            urls.append(url)
    for i in range(len(urls)):
        url = urls[i][0]
        if dorksType == 0:
            urls[i] = url[url.index("q=") + len("q="):len(url)]
        else:
            urls[i] = url[url.index("query=") + len("query="):len(url)]

    global result
    result = combine_search_urls(urls)
    print(result)
    label.configure(text=result)
    dh.writeLastFive(result)


# interfaces functions

def get_info_by_dork(dork, frame):
    if dork == "Intervalo":
        return [ctk.CTkEntry(master=frame, border_color=("black", "white"), border_width=2, corner_radius=10,
                             fg_color=("white", "black"), width=100),
                ctk.CTkEntry(master=frame, border_color=("black", "white"), border_width=2, corner_radius=10,
                             fg_color=("white", "black"), width=100)]
    elif dork != "Elige una opción":
        return [ctk.CTkEntry(master=frame, border_color=("black","white"), border_width=2, corner_radius=10, fg_color=("white","black"))]
    else:
        return []


def dork_change(name, frame_id, dork_info, frame, listDorks, *args):
    global add_button, remove_button
    add_button.pack_forget()
    remove_button.pack_forget()

    if name.get() != "Elige una opción":
        if frame_id == len(dork_info) - 1:
            add_button.pack(padx=10, pady=10, fill="x")

            if len(listDorks) >= 2:
                add_button.pack_forget()
                remove_button.pack_forget()
                add_button.pack(side="left", padx=10, pady=10)
                remove_button.pack(side="right", padx=10, pady=10)
            else:
                remove_button.pack_forget()
    else:

        add_button.pack_forget()
        remove_button.pack_forget()
        remove_subsequent_dorks(frame_id, listDorks, dork_info)

        if len(listDorks) > 1:
            remove_button.pack(padx=10, pady=10, fill="x")


    print(name.get() + " " + str(frame_id))
    for elem in dork_info[frame_id]:
        elem.pack_forget()

    info = get_info_by_dork(name.get(), frame)
    for elem in info:
        elem.pack(side="left", padx="7 3")
    dork_info[frame_id] = info



def add_dork(input_frame, list_dorks, list_info, dorksType):
    global add_button, remove_button
    add_button.pack_forget()
    remove_button.pack_forget()



    optionMenu_Font = ctk.CTkFont(family="Helvetica", size=14)

    inside_of_menu = ctk.StringVar()

    inside_of_menu.set(dorks_Google[0])

    dork_frame = ctk.CTkFrame(master=input_frame, border_color=("white", "black"), fg_color=("white", "black"),
                              bg_color=("white", "black"),
                              border_width=2, corner_radius=10)

    dork_select = ctk.CTkOptionMenu(master=dork_frame, variable=inside_of_menu, values=dorks_Google,
                                    corner_radius=10, fg_color=("white", "black"), text_color=("black", "white"),
                                    width=200, bg_color=("white", "black"),
                                    button_color=("white", "black"), button_hover_color=("yellow", "purple"),
                                    dropdown_fg_color=("white", "black"),
                                    dropdown_hover_color=("yellow", "purple"), font=optionMenu_Font,
                                    dropdown_font=optionMenu_Font)

    if dorksType == 0:
        inside_of_menu.set(dorks_Google[0])
        dork_select.configure(values=dorks_Google)
    else:
        inside_of_menu.set(dorks_Shodan[0])
        dork_select.configure(values=dorks_Shodan)

    # elements logic

    list_dorks.append(dork_select)
    list_info.append([])
    b_add = ctk.CTkButton(master=input_frame, text="", image=image_Add,
                          command=lambda: add_dork(input_frame, list_dorks, list_info, dorksType),
                          border_spacing=5, fg_color=("white", "black"), hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, font=optionMenu_Font, text_color=("black", "white"), width=175)
    remove_add = ctk.CTkButton(master=input_frame, text="", image=image_Remove,
                          command=lambda: remove_dork(list_dorks, list_info),
                          border_spacing=5, fg_color=("white", "black"), hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, font=optionMenu_Font, text_color=("black", "white"), width=175)


    add_button = b_add
    remove_button = remove_add
    dork_select.configure(
        command=lambda *args, inside=inside_of_menu, frame_id=list_dorks.index(dork_select), dork_info=list_info, frame=dork_frame, listDorks=list_dorks:
        dork_change(inside, frame_id, list_info, frame, listDorks, *args), button_color=("white","black"), text_color=("black","white"),
        bg_color=(("white","black")), button_hover_color=("yellow","purple"), corner_radius=10)
    # show elements

    dork_select.pack(side="left")
    dork_frame.pack(side="top", anchor="center", pady="20", padx="10")
    input_frame.pack(side="top", anchor="center", pady=(50, 0))
    if len(list_dorks) > 1:
        remove_button.pack(padx=10, pady=10, fill="x")


def remove_dork(list_dorks, list_info):
    global add_button, remove_button
    if list_dorks:
        last_dork = list_dorks.pop()
        last_dork.master.destroy()

        if list_info:
            last_info = list_info.pop()
            for widget in last_info:
                widget.destroy()
        if len(list_dorks) < 2:
            remove_button.pack_forget()
            add_button.pack_forget()
            add_button.pack(padx=10, pady=10, fill="x")
        else:
            add_button.pack_forget()
            remove_button.pack_forget()
            add_button.pack(side="left", padx=10, pady=10)
            remove_button.pack(side="right", padx=10, pady=10)


def remove_subsequent_dorks(start_index, list_dorks, list_info):
    global add_button, remove_button
    remove_button.pack_forget()
    add_button.pack_forget()

    while len(list_dorks) > start_index + 1:
        last_dork = list_dorks.pop()
        last_dork.master.destroy()

        if list_info:
            last_info = list_info.pop()
            for widget in last_info:
                widget.destroy()



def on_button_click_main():
    global dorksType
    if dorksType == 0:
        dorksType = 1
        text_buttonExchanger.set("GOOGLE")
    else:
        dorksType = 0
        text_buttonExchanger.set("SHODAN")

    main_loop()

def main_loop():
    global add_button, remove_button
    clearResult()

    text_var.set("ORDENAR POR BÚSQUEDA MÁS ANTIGUA")

    myButtonFont = ctk.CTkFont(family="Helvetica", size=14, weight="bold")

    clear_page()
    list_dorks = []
    list_info = []

    add_button = ctk.CTkButton(master=master_frame)
    remove_button = ctk.CTkButton(master=master_frame)
    input_frame = ctk.CTkFrame(master=master_frame, fg_color=("white", "black"), border_color=("black", "white"),
                               border_width=2, corner_radius=10)

    home_button = ctk.CTkButton(master=master_frame, command=title_page, text="PÁGINA PRINCIPAL", fg_color=("white","black"),
                                hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), font=myButtonFont)
    home_button.pack(anchor="n", side="left", padx=(0, 20), pady=30)


    us_button = ctk.CTkButton(master=master_frame, command=about_us, text="SOBRE NOSOTROS", fg_color=("white","black"),
                              hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), font=myButtonFont)
    us_button.pack(anchor="n", side="left", pady=30)


    moon.place(x=1044.5, y=27.5)
    switch.pack(side="right", anchor="n", pady=30, padx=(8, 0))
    sun.pack(side="right", anchor="n", pady=29, padx=(200, 0))

    moon.lift(switch)

    change_button = ctk.CTkButton(master=master_frame, command=on_button_click_main, textvariable=text_buttonExchanger, fg_color=("white","black"),
                                hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), font=myButtonFont, image=image_Arrows, compound="left", anchor="center")

    change_button.pack(pady=(150, 0), anchor="center")

    add_dork(input_frame, list_dorks, list_info, dorksType)
    result_label = ctk.CTkLabel(master=master_frame, text=result, font=ctk.CTkFont(family="Helvetica", size=8, weight="bold"))
    result_label.pack(pady=(35, 35), anchor="center")
    do_button = ctk.CTkButton(master=master_frame,
                              command=lambda dorks=list_dorks, info=list_info, label=result_label: do_dorks(dorks, info,
                                                                                                            result_label),
                              text="OBTENER URL", fg_color=("white", "black"), hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black", "white"), font=myButtonFont)
    do_button.pack(anchor="s", side="left", padx=(0, 20))
    link = ctk.CTkButton(master=master_frame, text="BUSCAR", cursor="hand2", fg_color=("white", "black"), hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black", "white"), font=myButtonFont)
    link.pack(anchor="s", pady="20 0", side="left", padx=(0, 20))
    link.bind("<Button-1>", lambda e: webbrowser.open_new(result))
    history_button = ctk.CTkButton(master=master_frame, text="HISTORIAL", fg_color=("white", "black"), hover_color=("yellow","purple"), command=lambda reverse=False: history(reverse), border_color=("black","white"), border_width=2, text_color=("black", "white"), font=myButtonFont)
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

def on_button_click_history(reverse):
    reverse = not reverse

    if reverse:
        text_var.set("ORDENAR POR BÚSQUEDA MÁS RECIENTE")
    else:
        text_var.set("ORDENAR POR BÚSQUEDA MÁS ANTIGUA")

    history(reverse)


def on_button_click_change(reverse):
    global dorksType_history
    if dorksType_history == 0:
        dorksType_history = 1
        text_buttonExchangerV2.set("GOOGLE")
    else:
        dorksType_history = 0
        text_buttonExchangerV2.set("SHODAN")

    history(reverse)


def history(reverse):
    clear_page()

    history_list_Google, history_list_Shodan = dh.readLastFive(reverse)

    if dorksType_history == 0:
        history_list = history_list_Google[:]
        name = "Google"
    else:
        history_list = history_list_Shodan[:]
        name = "Shodan"

    length = len(history_list)

    order_button = ctk.CTkButton(master=master_frame, command=lambda: on_button_click_history(reverse), textvariable=text_var,
                                 fg_color=("white", "black"),
                                 hover_color=("yellow", "purple"), border_color=("black", "white"), border_width=2,
                                 text_color=("black", "white"), width=75, font=myButtonFont, border_spacing=10)

    emptyHistory = ctk.CTkLabel(master=master_frame, text="El historial de "+name+" está vacío", font=myButtonFont)

    if length > 0:
        order_button.pack(side="bottom", pady=(50, 0))
    else:
        emptyHistory.pack(side="bottom", pady=(50, 0))

    back_button = ctk.CTkButton(master=master_frame, command=main_loop, text="<", fg_color=("white","black"),
                                hover_color=("yellow","purple"), border_color=("black","white"), border_width=2, text_color=("black","white"), width=75, font=myButtonFont)

    change_button = ctk.CTkButton(master=master_frame, command=lambda: on_button_click_change(reverse), textvariable=text_buttonExchangerV2,
                                  fg_color=("white", "black"),
                                  hover_color=("yellow", "purple"), border_color=("black", "white"), border_width=2,
                                  text_color=("black", "white"), font=myButtonFont, image=image_Arrows, compound="left",
                                  anchor="center")


    for i in range(length-1, -1, -1):
        entry = ctk.CTkLabel(master=master_frame, text=history_list[i], text_color=("black", "white"), font=myButtonFont)
        entry.pack(pady=15, side="bottom")


    change_button.pack(pady=(0, 50), anchor="center", side="bottom")

    back_button.pack(pady=(30, 75), side="left", padx=(30, 0))

    moon.place(x=980, y=27.5)
    switch.pack(side="right", anchor="n", pady=(30, 75), padx=(8, 0))
    sun.pack(side="right", anchor="n", pady=(29, 76), padx=(800, 0))
    moon.lift(switch)




# init

window = ctk.CTk()
ctk.set_appearance_mode("dark")
window.geometry("1280x700")
window.title("EasyDorks")
window.configure(fg_color=("white","black"))


# Sort Button Text

text_var = ctk.StringVar()
text_var.set("ORDENAR POR BÚSQUEDA MÁS ANTIGUA")

# Exchanger Shodan-Google Button

text_buttonExchanger = ctk.StringVar()
text_buttonExchanger.set("SHODAN")

# Exchanger Shodan-Google History Button

text_buttonExchangerV2 = ctk.StringVar()
text_buttonExchangerV2.set("SHODAN")

# test StringVar

test = ctk.StringVar()
test.set("Elige una opción")

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

# arrows icon

image_Arrows = ctk.CTkImage(
    light_image=Image.open("black_arrows.png"),
    dark_image=Image.open("white_arrows.png"),
    size=(17, 17)
)

# add icon

image_Add = ctk.CTkImage(
    light_image=Image.open("black_add.png"),
    dark_image=Image.open("white_add.png"),
    size=(15, 15)
)

# remove icon

image_Remove = ctk.CTkImage(
    light_image=Image.open("black_remove.png"),
    dark_image=Image.open("white_remove.png"),
    size=(15, 15)
)

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

# init with google dorks (0 = Google / 1 = Shodan)

dorksType = 0

# init with google history (0 = Google / 1 = Shodan)

dorksType_history = 0

title_page()

window.mainloop()



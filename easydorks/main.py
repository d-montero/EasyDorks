import webbrowser
import customtkinter as ctk
import dork_functions as df
from PIL import Image

# https://github.com/d-montero/EasyDorks
result = "https://www.google.com"


def clear_page():
    for widget in master_frame.winfo_children():
        widget.forget()


# do function

str_to_func = {
    "Elige opción": df.nada,
    "archivos tipo:": df.fileTypeDork,
    "que la url contenga:": df.searchInurlDork,
    "que la página contenga": df.searchInsiteDork
}

def combineGoogleSearchUrls(urls, operator="AND"):
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
    result = combineGoogleSearchUrls(urls)
    print(result)
    label.configure(text=result)


# interfaces functions

def get_info_by_dork(dork, frame):
    if dork != "Elige opción":
        return [ctk.CTkEntry(master=frame, border_color="black", border_width=2)]
    else:
        return []


def dork_change(name, frame_id, dork_info, frame, last_add, *args):
    if name.get() != "Elige opción":
        if frame_id == len(dork_info)-1:
            last_add.pack(side="left", padx="10 0")
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

    # start elements

    dork_frame = ctk.CTkFrame(master=input_frame, border_color="white", fg_color="white", bg_color="white", border_width=2)
    DORKS = [
        "Elige opción",
        "archivos tipo:",
        "que la url contenga:",
        "que la página contenga"
    ]
    inside_of_menu = ctk.StringVar()
    inside_of_menu.set(DORKS[0])
    dork_select = ctk.CTkOptionMenu(master=dork_frame, variable=inside_of_menu, values=DORKS,
                                    corner_radius=10, fg_color="white", text_color="black", width=250, bg_color="white", button_color="white", button_hover_color="yellow", dropdown_fg_color="white", dropdown_hover_color="yellow")
    # elements logic

    list_dorks.append(dork_select)
    list_info.append([])
    b_add = ctk.CTkButton(master=input_frame, text="+",
                          command=lambda: add_dork(input_frame, list_dorks, list_info, last_add), width=400, fg_color="black", hover_color="blue", border_color="black", border_width=2)

    last_add = b_add
    dork_select.configure(
        command=lambda *args, inside=inside_of_menu, frame_id=list_dorks.index(dork_select), dork_info=list_info,
                       frame=dork_frame, add=last_add:
        dork_change(inside, frame_id, list_info, frame, add, *args), button_color="white", text_color="black",
        bg_color="white", button_hover_color="yellow")
    # show elements

    dork_select.pack(side="left")
    dork_frame.pack(side="top", anchor='nw', pady="20", padx="10")
    input_frame.pack(side="top", anchor='nw', padx="110", pady="70")


def main_loop():
    clear_page()
    list_dorks = []
    list_info = []
    add_button = ctk.CTkButton(master=master_frame)
    input_frame = ctk.CTkFrame(master=master_frame, fg_color="white", border_color="black", border_width=2)
    home_button = ctk.CTkButton(master=master_frame, command=title_page, text="HOME", fg_color="white", hover_color="yellow", border_color="black", border_width=2, text_color="black")
    home_button.pack(anchor="nw")
    us_button = ctk.CTkButton(master=master_frame, command=about_us, text="ABOUT US", fg_color="white", hover_color="yellow", border_color="black", border_width=2, text_color="black")
    us_button.pack(anchor="nw")
    add_dork(input_frame, list_dorks, list_info, add_button)
    result_label = ctk.CTkLabel(master=master_frame, text=result)
    result_label.pack(pady="0 30")
    do_button = ctk.CTkButton(master=master_frame,
                              command=lambda dorks=list_dorks, info=list_info, label=result_label: do_dorks(dorks, info, result_label), text="DO", fg_color="black", hover_color="blue")
    do_button.pack(anchor="se")
    link = ctk.CTkButton(master=master_frame, text="SEARCH:", cursor="hand2", fg_color="black", hover_color="blue")
    link.pack(anchor="se", pady="20 0")
    link.bind("<Button-1>", lambda e: webbrowser.open_new(result))
    print("init succesful")


# title page creation


def title_page():
    clear_page()
    master_frame.forget()
    logo.pack(pady="70 0")
    b_inicio.pack(pady="180 0")
    b_wiki.pack()
    master_frame.pack()


# about us page creation

def about_us():
    clear_page()
    back_button = ctk.CTkButton(master=master_frame, command=main_loop, text="\u2770", fg_color="white",
                                hover_color="yellow", border_color="black", border_width=2, text_color="black")
    back_button.pack(pady=30)
    us = ctk.CTkLabel(master=master_frame, text="Programa realizado por el grupo Agile Eagles\n\n"
                                                "Ingeniería de Software en el grado de Ciberseguridad de la Universidad Rey Juan Carlos\n\n\n"
                                                "Correo de contacto:\tcontact@agileagles.com\n\n")
    us.pack(pady="200")


def wiki():
    wiki_window = ctk.CTk()
    ctk.set_appearance_mode("light")
    wiki_window.geometry("700x800")
    wiki_window.title("WIKI")
    wiki_window.configure(fg_color="cyan")
    wiki_window.mainloop()


# init

window = ctk.CTk()
ctk.set_appearance_mode("light")
window.geometry("1280x700")
window.title("EasyDorks")
window.configure(fg_color="white")

# logo

master_frame = ctk.CTkFrame(master=window, fg_color="white")

img = ctk.CTkImage(
    light_image=Image.open("logo.png"),
    dark_image=Image.open("logo.png"),
    size=(400, 400))
logo = ctk.CTkLabel(master=master_frame, text="", image=img)

# start button

b_inicio = ctk.CTkButton(master=master_frame, text="INICIO", command=main_loop,
                         text_color="black", fg_color="white", border_color="black", bg_color="white", border_width=2, hover_color="yellow")

b_wiki = ctk.CTkButton(master=master_frame, command=wiki, text="WIKI")

title_page()

window.mainloop()

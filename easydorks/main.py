import urllib.parse
import webbrowser
import customtkinter
import customtkinter as ctk
from PIL import Image

# dork functions

dorksFiletype = [
    "filetype:pdf",
    "filetype:doc",
    "filetype:txt",
    "filetype:jpg",
    "filetype:xls",
    "filetype:ppt",
    "filetype:html",
    "filetype:xml",
]

dorksInurl = [
    "inurl:"
]

dorksInsite = [
    "insite:"

]

dorksExtension = [
    "extension:json",
    "extension:xml",
    # Agrega más dorks personalizados según sea necesario
]


def fileTypeDork(file_type):
    results = []
    for dork in dorksFiletype:
        if dork.split(":")[1] == file_type:
            query = f"{dork} {file_type}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results


def searchInurlDork(keyword):
    results = []
    for dork in dorksInurl:
        query = f"{dork} {keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"  # Cadena segura para url escapando caracteres especiales que no deberian estar
        results.append(search_url)
    return results


def searchInsiteDork(keyword):
    results = []
    for dork in dorksInsite:
        query = f"{dork} {keyword}"
        encoded_query = urllib.parse.quote(query)
        search_url = f"https://www.google.com/search?q={encoded_query}"
        results.append(search_url)
    return results


def ExtensionDork(keyword):
    results = []
    for dork in dorksFiletype:
        if dork.split(":")[1] == keyword:
            query = f"{dork} {keyword}"
            encoded_query = urllib.parse.quote(query)
            search_url = f"https://www.google.com/search?q={encoded_query}"
            results.append(search_url)
    return results


def nada(n):
    return n
# do function

str_to_func = {
    "Elige opción": nada,
    "archivos tipo:": fileTypeDork,
    "que la url contenga:": searchInurlDork,
    "que la página contenga": searchInsiteDork
}


def do_dorks(dorks, info):
    for dork_num in range(len(dorks)):
        info_in_dork = info[dork_num][0].get()
        print(str_to_func[dorks[dork_num].get()](info_in_dork))


# interfaces functions

def get_info_by_dork(dork, frame):
    if dork != "Elige opción":
        return [ctk.CTkEntry(master=frame)]
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
        "que la url contenga:",
        "que la página contenga"
    ]
    inside_of_menu = ctk.StringVar()
    inside_of_menu.set(DORKS[0])
    dork_select = ctk.CTkOptionMenu(master=dork_frame, variable=inside_of_menu, values=DORKS,
                                    corner_radius=10, fg_color="white", )
    # elements logic

    list_dorks.append(dork_select)
    list_info.append([])
    dork_select.configure(
        command=lambda *args, inside=inside_of_menu, frame_id=list_dorks.index(dork_select), dork_info=list_info,
                       frame=dork_frame:
        dork_change(inside, frame_id, list_info, frame, *args))
    b_add = ctk.CTkButton(master=input_frame, text="+",
                          command=lambda: add_dork(input_frame, list_dorks, list_info, last_add), width=500)

    last_add = b_add

    # show elements

    dork_select.pack(side="left")
    dork_frame.pack(side="top", anchor='nw', pady="20")
    b_add.pack(side="left", padx="10 0")
    input_frame.pack(side="top", anchor='nw', padx="110", pady="70")


def main_loop():
    for widget in master_frame.winfo_children():
        widget.forget()
    list_dorks = []
    list_info = []
    add_button = ctk.CTkButton(master=master_frame)
    input_frame = ctk.CTkFrame(master=master_frame)
    home_button = ctk.CTkButton(master=master_frame, command=title_page, text="HOME")
    home_button.pack(anchor="nw")
    add_dork(input_frame, list_dorks, list_info, add_button)
    do_button = ctk.CTkButton(master=master_frame,
                              command=lambda dorks=list_dorks, info=list_info: do_dorks(dorks, info), text="DO")
    do_button.pack(anchor="se")
    link = ctk.CTkButton(master=master_frame, text="SEARCH:", cursor="hand2", fg_color="red")
    link.pack(anchor="se", pady="20 0")
    link.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.google.com"))
    print("init succesful")


def title_page():
    for widget in master_frame.winfo_children():
        widget.forget()
    master_frame.forget()
    logo.pack(pady="70 0")
    b_inicio.pack(pady="200 0")
    master_frame.pack()


# start menu
# describe window


window = ctk.CTk()
customtkinter.set_appearance_mode("light")
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

# init CTkButton

b_inicio = ctk.CTkButton(master=master_frame, text="INICIO", command=main_loop)
b_inicio.configure(text_color="black", fg_color="white", border_color="black", bg_color="white", border_width=2)

title_page()

window.mainloop()

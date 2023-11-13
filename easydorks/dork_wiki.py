import customtkinter as ctk
import json

already_open = False
wiki_window = None

def init():
    global wiki_window
    global already_open
    if not already_open:
        wiki_window = ctk.CTkToplevel(fg_color="blue")
        wiki_window.protocol("WM_DELETE_WINDOW", on_closing)
        wiki_window.geometry("700x800")
        wiki_frame = ctk.CTkScrollableFrame(master=wiki_window, width=600, height=700, fg_color="cyan")
        main_loop(wiki_frame)
        already_open = True


def on_closing():
    global wiki_window
    global already_open
    already_open = False
    wiki_window.destroy()


def wiki():
    global wiki_window
    init()
    wiki_window.after(50, wiki_window.focus)


def main_loop(wiki_frame):
    for widget in wiki_frame.winfo_children():
        widget.forget()
    wiki_frame.pack(pady=50)
    wiki_file = open('easydorks\wiki.json')
    wiki_data = json.load(wiki_file)

    for dork in wiki_data.keys():
        wiki_entry = ctk.CTkButton(master=wiki_frame, command=lambda info=wiki_data[dork], frame=wiki_frame: dork_page(info, frame), text=dork, fg_color="white",
                                   hover_color="yellow", border_color="black", border_width=2, text_color="black")
        wiki_entry.pack(pady=10)


def dork_page(dork_info, frame):
    for widget in frame.winfo_children():
        widget.forget()
    title = ctk.CTkLabel(master=frame, text=dork_info["nombre"], font=("Arial", 40))
    back_button = ctk.CTkButton(master=frame, command=lambda wiki_frame=frame: main_loop(frame), text="\u2770", fg_color="white",
                                hover_color="yellow", border_color="black", border_width=2, text_color="black")
    back_button.pack(pady=30)
    ejemplo = ctk.CTkLabel(master=frame, text="ejemplo: "+dork_info["ejemplo"], font=("Arial", 20))
    info = ctk.CTkLabel(master=frame, font=("Arial", 10), text=dork_info["info"], wraplength=400)
    title.pack(pady=20)
    ejemplo.pack(pady=10)
    info.pack()
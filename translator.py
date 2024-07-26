from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES as LANGUAGES

def get_language_code(language_name):
    for name, code in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None

def change(text="Type", src="English", dest="Tamil"):
    src_code = get_language_code(src)
    dest_code = get_language_code(dest)
    if not src_code or not dest_code:
        return "Invalid source or destination language"
    
    try:
        translation = GoogleTranslator(source=src_code, target=dest_code).translate(text)
        return translation
    except Exception as e:
        return f"Translation error: {e}"

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0, END).strip()
    if not msg:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, "Please enter text to translate.")
        return

    text_get = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, text_get)

root = Tk()
root.title("My Translator")
root.geometry("500x700")
root.config(bg="lightgreen")

# Main title
lab_txt = Label(root, text="My Translator", font=("Ubuntu", 30, "bold"), bg="lightgreen")
lab_txt.pack(pady=20)

# Frame for source text and controls
frame_source = Frame(root, bg="lightgreen")
frame_source.pack(fill=BOTH, expand=True, padx=10, pady=5)

# Source text label
lab_src_txt = Label(frame_source, text="Source Text", font=("Ubuntu", 18, "bold"), bg="lightgreen")
lab_src_txt.pack(anchor=W, pady=5)

# Source text box
sor_txt = Text(frame_source, font=("Ubuntu", 14, "bold"), wrap=WORD, height=8)
sor_txt.pack(fill=BOTH, expand=True, pady=5)

# Frame for controls (comboboxes and button)
frame_controls = Frame(root, bg="lightgreen")
frame_controls.pack(fill=BOTH, padx=10, pady=5)

# Source language combobox
comb_sor = ttk.Combobox(frame_controls, values=list(LANGUAGES.keys()))
comb_sor.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)
comb_sor.set("english")

# Translate button
button_change = Button(frame_controls, text="Translate", relief=RAISED, command=data)
button_change.pack(side=LEFT, padx=50, pady=50, expand=True, fill=X)

# Destination language combobox
comb_dest = ttk.Combobox(frame_controls, values=list(LANGUAGES.keys()))
comb_dest.pack(side=LEFT, padx=5, pady=5, expand=True, fill=X)
comb_dest.set("english")

# Frame for destination text
frame_dest = Frame(root, bg="lightgreen")
frame_dest.pack(fill=BOTH, expand=True, padx=10, pady=5)

# Destination text label
lab_dest_txt = Label(frame_dest, text="Destination Text", font=("Ubuntu", 18, "bold"), bg="lightgreen")
lab_dest_txt.pack(anchor=W, pady=5)

# Destination text box
dest_txt = Text(frame_dest, font=("Ubuntu", 14, "bold"), wrap=WORD, height=8)
dest_txt.pack(fill=BOTH, expand=True, pady=5)

root.mainloop()

import tkinter as tk
from googletrans import Translator
class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.input_text = tk.Text(self.root, height=10, width=40)
        self.input_text.pack(padx=10, pady=10)
        self.output_text = tk.Text(self.root, height=10, width=40)
        self.output_text.pack(padx=10, pady=10)
        self.from_language = tk.StringVar()
        self.from_language.set("English")
        self.from_language_menu = tk.OptionMenu(self.root, self.from_language, "English", "Spanish", "French", "German", "Italian", "Portuguese", "Chinese")
        self.from_language_menu.pack(padx=10, pady=10)
        self.to_language = tk.StringVar()
        self.to_language.set("Spanish")
        self.to_language_menu = tk.OptionMenu(self.root, self.to_language, "English", "Hindi", "French", "German", "Italian", "Portuguese", "Chinese")
        self.to_language_menu.pack(padx=10, pady=10)
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.pack(padx=10, pady=10)
    def translate_text(self):
        translator = Translator()
        input_text = self.input_text.get("1.0", "end-1c")
        from_language = self.from_language.get()
        to_language = self.to_language.get()
        result = translator.translate(input_text, src=from_language, dest=to_language)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", result.text)
if __name__ == "__main__":
    root = tk.Tk()
    translator = LanguageTranslator(root)
    root.mainloop()
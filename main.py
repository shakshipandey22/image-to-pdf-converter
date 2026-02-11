import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os


class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("400x600")

        self.image_paths = []
        self.output_pdf_name = tk.StringVar()

        self.initialize_ui()

    def initialize_ui(self):
        tk.Label(
            self.root,
            text="Image to PDF Converter",
            font=("Helvetica", 16, "bold")
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Select Images",
            command=self.select_images
        ).pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        tk.Label(self.root, text="Enter output PDF name:").pack()

        tk.Entry(
            self.root,
            textvariable=self.output_pdf_name,
            width=35,
            justify="center"
        ).pack(pady=5)

        tk.Button(
            self.root,
            text="Convert to PDF",
            command=self.convert_to_pdf
        ).pack(pady=20)

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
        )

        self.listbox.delete(0, tk.END)
        for path in self.image_paths:
            self.listbox.insert(tk.END, os.path.basename(path))

    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected")
            return

        pdf_name = self.output_pdf_name.get() or "output"
        pdf_path = pdf_name + ".pdf"

        images = []
        for path in self.image_paths:
            img = Image.open(path)
            if img.mode != "RGB":
                img = img.convert("RGB")
            images.append(img)

        #  THIS LINE ACTUALLY CREATES THE PDF
        images[0].save(
            pdf_path,
            save_all=True,
            append_images=images[1:]
        )

        messagebox.showinfo("Success", f"PDF created:\n{pdf_path}")


def main():
    root = tk.Tk()
    ImageToPDFConverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()

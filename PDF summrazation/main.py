import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, simpledialog, font
from tkinter import PhotoImage  # Import PhotoImage for handling images
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from pdfminer.high_level import extract_text
import requests
from io import BytesIO
from fpdf import FPDF  # Import FPDF for PDF generation

model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')

def pdf_to_text(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def summarize_text(text):
    preprocess_text = text.strip().replace("\n", " ")
    t5_prepared_text = "summarize: " + preprocess_text
    tokenized_text = tokenizer.encode(t5_prepared_text, return_tensors="pt").to(device)
    summary_ids = model.generate(tokenized_text,
                                 num_beams=4,
                                 no_repeat_ngram_size=2,
                                 min_length=30,
                                 max_length=100,
                                 early_stopping=True)
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output

def download_pdf(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BytesIO(response.content)
    except requests.RequestException as e:
        messagebox.showerror("Download Error", f"Failed to download PDF: {e}")
        return None

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if file_paths:
        summaries = [summarize_text(pdf_to_text(pdf_file)) for pdf_file in file_paths if
                     pdf_to_text(pdf_file) is not None]
        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, "\n\n".join(summaries))
        messagebox.showinfo("Completion", "Summarization completed!")
    else:
        messagebox.showinfo("No Files", "No PDF files were selected.")

def fetch_from_url():
    url = simpledialog.askstring("Enter URL", "Please enter the PDF URL:")
    if url:
        pdf_file = download_pdf(url)
        if pdf_file:
            summary = summarize_text(pdf_to_text(pdf_file))
            output_text.delete('1.0', tk.END)
            output_text.insert(tk.END, summary)
            messagebox.showinfo("Completion", "Summarization completed!")

def save_summary_as_pdf():
    text_to_save = output_text.get('1.0', tk.END)
    if not text_to_save.strip():
        messagebox.showerror("No Data", "There is no summary to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf = FPDF()
        pdf.add_page()

        # Calculate center position for logo and title
        logo_x = (pdf.w - 30) / 2  # Centering logo horizontally
        pdf.image("p.png", x=logo_x, y=10, w=30)
        pdf.ln(28)
        # Add header title centered
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "MGM's College Of Engineering", ln=True, align='C')

        # Add line separator
        pdf.set_line_width(0.5)
        pdf.line(10, 50, pdf.w - 10, 50)

        # Add summary text
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, text_to_save)

        pdf.output(file_path)

        messagebox.showinfo("Saved as PDF", "The summary has been saved as PDF!")

app = tk.Tk()
app.title("PDF Summarizer")
app.geometry("800x600")
app.config(bg="light blue")
customFont = font.Font(family="Helvetica", size=12)

btn_load = tk.Button(app, text="Load PDFs", command=select_files, font=customFont, bg="navy", fg="white", padx=10,
                     pady=5)
btn_load.pack(pady=10)

btn_fetch = tk.Button(app, text="Fetch PDF from URL", command=fetch_from_url, font=customFont, bg="navy", fg="white",
                      padx=10, pady=5)
btn_fetch.pack(pady=10)

btn_save_pdf = tk.Button(app, text="Save Summary as PDF", command=save_summary_as_pdf, font=customFont, bg="navy",
                         fg="white", padx=10, pady=5)
btn_save_pdf.pack(pady=10)

output_text = scrolledtext.ScrolledText(app, width=70, height=20, font=customFont, padx=10, pady=10, wrap=tk.WORD)
output_text.pack(pady=20)

app.mainloop()

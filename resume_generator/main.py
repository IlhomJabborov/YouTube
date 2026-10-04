from input_handler import collect_resume_data
from display import show_resume
from pdf_generator import generate_pdf
import questionary

def main():
    resume = collect_resume_data()
    show_resume(resume)

    save_pdf = questionary.confirm(
        "Resume'ni PDF fayl sifatida saqlaymizmi ?"
    ).ask()

    if save_pdf:
        generate_pdf(resume)

main()
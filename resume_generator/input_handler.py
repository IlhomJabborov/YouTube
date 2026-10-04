from rich.console import Console
from rich.panel import Panel
import questionary

from resume import Resume

console = Console()

def collect_resume_data():
    console.print(Panel(" Resume Generator", style="bold cyan"))

    name = questionary.text("Ismingiz : ").ask()
    email = questionary.text(" Email : ").ask()
    phone = questionary.text("Telefon raqam : ").ask()
    skills_input = questionary.text("Ko'nikmalar (vergul bilan) : ").ask()
    skills = [s.strip() for s in skills_input.split(",")]
    experience = questionary.text("Ish tajribasi (qisqacha) : ").ask()
    education = questionary.text("Ta'lim malumoti : ").ask()

    return Resume(
        name,
        email,
        phone,
        skills,
        experience,
        education
    )

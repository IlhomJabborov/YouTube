from rich.console import Console
from rich.table import Table

console = Console()

def show_resume(resume):
    table = Table(title="Sizning Resume'ingiz")

    #jadval ustunlari
    table.add_column("Bo'lim",style="cyan")
    table.add_column("Ma'lumot",style="white")

    #jadval qatorlari
    table.add_row("Ism",resume.name)
    table.add_row("Email",resume.email)
    table.add_row("Telefon",resume.phone)
    table.add_row("Ko'nikmalar",", ".join(resume.skills))
    table.add_row("Tajriba",resume.experience)
    table.add_row("Ta'lim",resume.education)

    console.print(table)

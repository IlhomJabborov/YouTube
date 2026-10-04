from fpdf import FPDF
from rich.console import Console

console = Console()

def generate_pdf(resume):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,resume.name,ln=True)

    pdf.set_font("Arial","B",12)
    pdf.cell(0,10,f"Email : {resume.email}",ln=True)
    pdf.cell(0,10,f"Telefon : {resume.phone}",ln=True)

    pdf.ln(5)

    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"Ko'nikmalar : ",ln=True)
    pdf.set_font("Arial","B",12)
    for skill in resume.skills:
        pdf.cell(0,8,f"- {skill}",ln=True)

    pdf.ln(3)
    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"Ish tajribasi : ",ln=True)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,8,resume.experience)

    pdf.ln(3)
    pdf.set_font("Arial","B",14)
    pdf.cell(0,10,"Ta'lim : ",ln=True)
    pdf.set_font("Arial","B",12)
    pdf.cell(0,8,resume.education)


    #Faylni saqlash
    pdf.output("resume.pdf")

    console.print(" resume.pdf yaratildi !", style="bold green")
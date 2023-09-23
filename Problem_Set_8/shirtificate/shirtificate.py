from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        self.cell(txt = "CS50 Shirtificate", align="C", center = True)
        pdf.image("shirtificate.png", x = "C", y = 50, w = 175)

    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.cell(0 , 200, txt = f"{name} took CS50", align="C", center = True)

name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
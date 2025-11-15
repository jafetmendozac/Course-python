from fpdf import FPDF


def main():
  name = input("Name: ")

  image_path = "./shirtificate.png"

  pdf = FPDF(orientation='P', format='A4')
  pdf.add_page()

  pdf.set_font("Arial", style="B", size=32)
  pdf.cell(0, 30, "CS50 Shirtificate", ln=True, align="C")

  pdf.image(image_path, x=10, y=60, w=190)

  pdf.set_font("Arial", "B", 24)
  pdf.set_text_color(255, 255, 255)
  pdf.set_xy(0, 120)
  pdf.cell(0, 20, f"{name} took CS50", align="C")

  pdf.output("shirtificate.pdf")

if __name__ == "__main__":
  main()
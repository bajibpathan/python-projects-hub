from fpdf import FPDF
import pandas as pd

# ------------------ CONSTANTS ------------------------
# Font and page configuration
FONT_FAMILY = "Times"
PAGE_FORMAT = "A4"

# Line layout configuration
LINE_START_X = 10
LINE_END_X = 200
LINE_START_Y = 20
LINE_GAP = 10
PAGE_HEIGHT_MM = 278


# ------------------------------- HELPERS -------------------------------
def generate_lines(pdf_obj, x_start, y_start, x_end, gap, page_height):
    """
    Draw horizontal lines across the page.

    Args:
        pdf_obj (FPDF): PDF object instance.
        x_start (int): Starting X coordinate.
        y_start (int): Starting Y coordinate.
        x_end (int): Ending X coordinate.
        gap (int): Space between each line.
        page_height (int): Maximum page height.
    """
    for y in range(y_start, page_height, gap):
        pdf_obj.line(x_start, y, x_end, y)


def set_header(pdf_obj, title):
    """
    Render the page header.

    Args:
        pdf_obj (FPDF): PDF object instance.
        title (str): Title text to display.
    """
    pdf_obj.set_font(family=FONT_FAMILY, style="B", size=24)
    pdf_obj.set_text_color(100, 100, 100)
    pdf_obj.cell(w=0, h=12, txt=title, align="L", ln=1)


def set_footer(pdf_obj, title, y_pos):
    """
    Render the page footer.

    Args:
        pdf_obj (FPDF): PDF object instance.
        title (str): Footer text.
        y_pos (int): Vertical position for the footer.
    """
    pdf_obj.ln(y_pos)
    pdf_obj.set_font(family=FONT_FAMILY, style="I", size=8)
    pdf_obj.set_text_color(100, 100, 100)
    pdf_obj.cell(w=0, h=12, txt=title, align="R")


def add_page_with_content(pdf_obj, title, show_header=True):
    """
    Add a new page with lines and optional header.

    Args:
        pdf_obj (FPDF): PDF object instance.
        title (str): Page title.
        show_header (bool): Whether to display the header.
    """
    pdf_obj.add_page()

    if show_header:
        set_header(pdf_obj, title)

    generate_lines(
        pdf_obj,
        LINE_START_X,
        LINE_START_Y,
        LINE_END_X,
        LINE_GAP,
        PAGE_HEIGHT_MM
    )

    set_footer(pdf_obj, title, 265)


# ------------------------------- MAIN FLOW -------------------------------
def main():
    """
    Main function to generate the PDF from topics.csv.
    """
    # Initialize PDF object
    pdf = FPDF(orientation="P", unit="mm", format=PAGE_FORMAT)
    pdf.set_auto_page_break(auto=False, margin=0)

    # Load CSV file
    df = pd.read_csv("topics.csv")

    # Loop through each topic and generate pages
    for index, row in df.iterrows():
        title = row["Topic"]
        pages = row["Pages"]

        # First page includes header
        add_page_with_content(pdf, title, show_header=True)

        # Remaining pages without header
        for _ in range(pages - 1):
            add_page_with_content(pdf, title, show_header=False)

    # Export PDF file
    pdf.output("output.pdf")


if __name__ == "__main__":
    main()
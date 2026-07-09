from playwright.sync_api import sync_playwright


class PDFMaker:

    def __init__(self):
        pass

    def create_pdf(self, html: str, output_pdf: str):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(html, wait_until="networkidle")
            page.pdf(
                path=output_pdf,
                format="A4",
                print_background=True,
                margin={
                    "top": "20px",
                    "bottom": "20px",
                    "left": "20px",
                    "right": "20px",
                },
            )
            browser.close()
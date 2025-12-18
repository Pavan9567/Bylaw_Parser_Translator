import pdfplumber
import re

# Valid section IDs: 1, 1.2, 2.2.1, 3.1.4.2
SECTION_ID_REGEX = re.compile(r'^\d{1,2}(\.\d{1,2}){0,3}$')

def is_obvious_table_row(line: str) -> bool:
    if "m²" in line or " m2" in line:
        return True
    if sum(c.isdigit() for c in line) >= 6:
        return True
    if line.count("  ") >= 4:
        return True
    return False

def extract_sections(pdf_path: str):
    sections = []
    current_section = None

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)

        for page_index, page in enumerate(pdf.pages):
            page_number = page_index + 1
            text = page.extract_text()

            if not text:
                continue

            for raw_line in text.split("\n"):
                line = raw_line.strip()

                if not line or is_obvious_table_row(line):
                    continue

                parts = line.split(" ", 1)

                # ---- PHASE 1: detect section id safely ----
                if len(parts) == 2 and SECTION_ID_REGEX.match(parts[0]):
                    section_id = parts[0]
                    title = parts[1].strip()
                    parent = ".".join(section_id.split(".")[:-1])

                    # Close previous section
                    if current_section:
                        current_section["section_end_page"] = page_number - 1
                        sections.append(current_section)

                    current_section = {
                        "parent_section": parent,
                        "section": section_id,
                        "section_title": title,
                        "section_body_text": "",
                        "section_start_page": page_number,
                        "section_end_page": None
                    }
                else:
                    if current_section:
                        current_section["section_body_text"] += line + "\n"

        # Close last section
        if current_section:
            current_section["section_end_page"] = total_pages
            sections.append(current_section)

    return {"sections": sections}
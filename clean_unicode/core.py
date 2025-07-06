def remove_unicode(text: str) -> str:
    """Remove all non-ASCII characters from a string."""
    return ''.join(char for char in text if ord(char) < 128)


def clean_text_file(input_path:str, output_path:str):
    """Clean a plain text file and wrute output to a new file."""
    with open(input_path, "r", encoding="utf-8") as infile:
        content = infile.read()
    cleaned = remove_unicode(content)
    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(cleaned)
    

def clean_docx_file(input_path: str, output_path: str):
    """Clean a Word (.docx) document and write output to a new file."""
    from docx import Document

    doc = Document(input_path)
    for para in doc.paragraphs:
        para.text = remove_unicode(para.text)
    doc.save(output_path)
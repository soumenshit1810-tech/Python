# save as create_project_pdf.py
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

def create_project_pdf(filename, metadata, sections):
    """
    filename: output pdf path e.g. 'project.pdf'
    metadata: dict with keys: title, author, guide, semester, dept, university, date
    sections: list of tuples (heading, text) in the order to appear
    """
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=60)
    styles = getSampleStyleSheet()
    story = []

    # Title page
    title_style = ParagraphStyle('TitleStyle', parent=styles['Title'], alignment=1, fontSize=20, spaceAfter=12)
    meta_style = ParagraphStyle('MetaStyle', parent=styles['Normal'], alignment=1, fontSize=11, leading=14)
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph(metadata.get('title',''), title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(f"Submitted by: <b>{metadata.get('author','')}</b>", meta_style))
    story.append(Paragraph(f"Department: {metadata.get('dept','')}", meta_style))
    story.append(Paragraph(f"Semester: {metadata.get('semester','')}", meta_style))
    story.append(Paragraph(f"Guide: {metadata.get('guide','')}", meta_style))
    story.append(Paragraph(f"{metadata.get('university','')}", meta_style))
    story.append(Spacer(1, 1.2*inch))
    story.append(Paragraph(f"Date: {metadata.get('date','')}", meta_style))
    story.append(PageBreak())

    # Content pages
    heading_style = ParagraphStyle('Heading', parent=styles['Heading2'], spaceAfter=6)
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=11, leading=15, spaceAfter=8)

    for heading, text in sections:
        story.append(Paragraph(heading, heading_style))
        # Allow newlines in text to create paragraphs
        for para in str(text).split('\n\n'):
            story.append(Paragraph(para.strip().replace('\n','<br />'), body_style))
        story.append(Spacer(1, 0.1*inch))

    doc.build(story)
    print(f"PDF created: {filename}")

# Example usage
if __name__ == "__main__":
    metadata = {
        'title': 'The Impact of Climate Change on Indigenous Rights: Legal and Constitutional Perspectives',
        'author': 'Priya D',
        'guide': 'Ms. Manisha Naskar',
        'semester': '3rd',
        'dept': 'Department of Law',
        'university': 'Brainware University',
        'date': 'November 2025'
    }
    sections = [
        ('Introduction', 'Climate change has emerged as one of the most critical global challenges...'),
        ('Research Questions', '1. How does climate change affect...\n\n2. What are the major legal provisions...'),
        ('Scope', 'The present study focuses on...'),
        ('Findings', '1. Indigenous communities are among the most vulnerable...\n\n2. Gap between legal recognition and enforcement...'),
        ('Suggestions', '1. Strengthen legal implementation...\n\n2. Inclusive policy-making...')
    ]
    create_project_pdf('project_report.pdf', metadata, sections)

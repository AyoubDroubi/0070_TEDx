from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def create_proposal():
    # File Path
    pdf_path = "TEDxZU_Final_Proposal.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Custom TED Styles
    ted_red = colors.Color(235/255, 0/255, 40/255) # #EB0028
    
    title_style = ParagraphStyle(
        'TEDTitle',
        parent=styles['Title'],
        fontSize=32,
        textColor=ted_red,
        spaceAfter=20,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'TEDSubtitle',
        parent=styles['Normal'],
        fontSize=18,
        textColor=colors.black,
        alignment=1, # Center
        spaceAfter=10
    )
    
    heading_style = ParagraphStyle(
        'TEDHeading',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=ted_red,
        spaceBefore=20,
        spaceAfter=15,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'TEDBody',
        parent=styles['Normal'],
        fontSize=12,
        leading=16,
        spaceAfter=12
    )

    # --- Page 1: Cover ---
    story.append(Spacer(1, 2.5*inch))
    story.append(Paragraph("TEDxZU: BEYOND Limits", title_style))
    story.append(Paragraph("Official Event Proposal 2026", subtitle_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Location: Zarqa University", subtitle_style))
    story.append(Paragraph("Amman, Jordan", subtitle_style))
    story.append(PageBreak())

    # --- Page 2: The Vision ---
    story.append(Paragraph("The Vision", heading_style))
    
    philosophy_text = """
    <b>The Philosophy: BEYOND Limits</b><br/>
    The limits we encounter are often not physical walls, but psychological, social, or technical boundaries we place around ourselves. 
    TEDxZU aims to redefine these boundaries through three core pillars:<br/>
    - <b>Beyond Self:</b> Overcoming the fear of failure and self-doubt.<br/>
    - <b>Beyond Tradition:</b> Innovating unfamiliar solutions in technology and society.<br/>
    - <b>Beyond Circumstances:</b> Creating and excelling despite hardships and challenges.<br/>
    <br/>
    We don't just talk about the impossible; we talk about the stage that comes <i>after</i> the impossible.
    """
    story.append(Paragraph(philosophy_text, body_style))
    
    impact_text = """
    <b>Impact on Zarqa Community</b><br/>
    As the first event of its kind at Zarqa University, TEDxZU serves as a personal 'business accelerator' for students and a hub for the local community. 
    It aims to:<br/>
    - Empower youth to showcase their talents.<br/>
    - Spread cutting-edge knowledge in Cyber Security, Humanities, and Self-Development.<br/>
    - Build a bridge between academia and the practical professional world.<br/>
    - Establish Zarqa as a center for creativity and innovation in Jordan.
    """
    story.append(Paragraph(impact_text, body_style))
    story.append(PageBreak())

    # --- Page 3: The Stage (Speakers) ---
    story.append(Paragraph("The Stage: Speaker Lineup", heading_style))
    
    speaker_data = [
        ["Speaker Name", "Role", "Talk Title"],
        ["Dr. Haiel Al-Khafajeh", "Dean of IT", "Beyond the Lecture Hall"],
        ["Dr. Mohammad Al-Juwaidi", "Head of Cyber Security", "Beyond the Screen"],
        ["Rawda Al-Ramahi", "Psychological Researcher", "Beyond Inner Walls"],
        ["Issa Assaf", "Motivational Speaker", "Beyond Negativity"],
        ["Ali Alwan", "Self-Development Speaker", "Beyond Hardship"],
        ["Dr. Amr Al-Madadha", "Communication Expert", "Beyond Silence"],
        ["Dania Al-Gharaibeh", "HR Specialist", "Beyond the Resume"],
        ["Dr. Assar", "Expert Speaker", "Beyond the Comfort Zone"],
        ["Roua Samara", "Inspirational Speaker", "Beyond Expectations"]
    ]
    
    table = Table(speaker_data, colWidths=[2*inch, 1.8*inch, 2.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), ted_red),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("<i>Note: All speakers have been selected for their unique ability to embody the 'BEYOND' mindset in their respective fields.</i>", body_style))
    story.append(PageBreak())

    # --- Page 4: The Host & Experience ---
    story.append(Paragraph("The Experience", heading_style))
    
    experience_text = """
    <b>The Host's Role</b><br/>
    The Host at TEDxZU is the 'Heartbeat of the Stage.' Their role is to bridge the gap between our local Zarqa context and the global TED standards. 
    They will guide the audience through the emotional and intellectual highs of the event, ensuring every attendee leaves with a 'BEYOND' mindset.
    <br/><br/>
    <b>Interactive Zones</b><br/>
    The event extends beyond the red circle with several immersive experience areas:<br/>
    - <b>Networking Zone:</b> A space for direct dialogue between speakers and attendees.<br/>
    - <b>Interactive Lab:</b> Live demonstrations of Cyber Security and AI applications.<br/>
    - <b>Art Performances:</b> Creative breaks that visualize the theme of crossing boundaries.<br/>
    - <b>The 'Best Version' Wall:</b> A participatory installation where guests share their own 'BEYOND' goals.
    """
    story.append(Paragraph(experience_text, body_style))
    
    # Final Footer-like text
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("<font color='#EB0028'><b>Ideas Worth Spreading.</b></font>", subtitle_style))

    # Build PDF
    doc.build(story)
    print(f"Proposal generated successfully: {pdf_path}")

if __name__ == "__main__":
    create_proposal()

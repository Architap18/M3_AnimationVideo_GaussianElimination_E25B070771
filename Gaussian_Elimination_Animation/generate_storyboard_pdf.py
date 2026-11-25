"""
Generate professional Storyboard PDF for Gaussian Elimination Educational Animation
"""
import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_storyboard(output_path="Gaussian_Elimination_Animation/storyboard.pdf"):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=landscape(letter),
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#FF7A00'),
        alignment=0
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#4A5260'),
        alignment=0
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#0B0D11'),
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#252B36')
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#13161C')
    )

    table_mono_style = ParagraphStyle(
        'TableMono',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#0B0D11')
    )

    elements = []

    # Title Banner
    elements.append(Paragraph("PROJECT STORYBOARD: GAUSSIAN ELIMINATION", title_style))
    elements.append(Paragraph("M3 Linear Algebra Internal Assessment • Futuristic AI Dashboard Animation • Total Duration: 05:42 (342.08s)", subtitle_style))
    elements.append(Spacer(1, 8))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#FF7A00'), spaceBefore=2, spaceAfter=10))

    # Visual Theme Summary
    elements.append(Paragraph("1. VISUAL THEME & DESIGN SPECIFICATIONS", h1_style))
    theme_text = """
    <b>Color Palette:</b> Background: Dark Charcoal (<code>#0B0D11</code>), Dashboard Panels: Near-Black (<code>#13161C</code>), Panel Borders: (<code>#252B36</code>), Accent Highlights: Futuristic Orange (<code>#FF7A00</code>), Verification Success: Emerald Green (<code>#00E676</code>), Normal Math: Crisp White (<code>#F4F6F8</code>), Supporting Telemetry: Slate Grey (<code>#8C96A5</code>).<br/>
    <b>Typography:</b> Monospace mathematical numerals (<code>Menlo/Courier</code>) for matrix alignment and coordinate vectors; modern sans-serif (<code>Helvetica Neue</code>) for UI telemetry.<br/>
    <b>Technical Layout:</b> Futuristic AI console featuring rounded dashboard cards, top status HUD bar, augmented dotted background grid, and progressive telemetry panels.
    """
    elements.append(Paragraph(theme_text, body_style))
    elements.append(Spacer(1, 10))

    # Scene Breakdown Table
    elements.append(Paragraph("2. SIX-SCENE CHOREOGRAPHY & STORYBOARD BREAKDOWN", h1_style))

    storyboard_data = [
        [
            Paragraph("Scene & Time", table_header_style),
            Paragraph("Phase Title", table_header_style),
            Paragraph("Narration Key Focus", table_header_style),
            Paragraph("Visual Layout & Dynamic Elements", table_header_style),
            Paragraph("Pedagogical Outcome", table_header_style)
        ],
        [
            Paragraph("<b>Scene 1</b><br/>0:00 - 0:57<br/>(57.0s)", table_cell_style),
            Paragraph("<b>The Hook</b><br/>(Start from Zero)", table_cell_style),
            Paragraph("Store problem: 1 Notebook + 1 Pen = ₹30; 2 Notebooks + 1 Pen = ₹50. Difference gives ₹20.", table_cell_style),
            Paragraph("Dark console HUD boots up. Left card shows store receipt; right card translates items into unknowns and algebraic equations.", table_cell_style),
            Paragraph("Grasp what unknowns and equations mean through everyday intuition.", table_cell_style)
        ],
        [
            Paragraph("<b>Scene 2</b><br/>0:57 - 2:05<br/>(68.6s)", table_cell_style),
            Paragraph("<b>The Basics</b><br/>(Foundations)", table_cell_style),
            Paragraph("3 unknowns x, y, z across 3 linear equations. Matrix extraction, pivot concept, 3 elementary row operations.", table_cell_style),
            Paragraph("Equation terms fade leaving coefficients in an Augmented Matrix [A | b]. Orange pulsing box introduces the pivot. Three operation cards slide in.", table_cell_style),
            Paragraph("Understand matrix notation and why row operations preserve true solutions.", table_cell_style)
        ],
        [
            Paragraph("<b>Scene 3</b><br/>2:05 - 2:39<br/>(33.6s)", table_cell_style),
            Paragraph("<b>Visual Intuition</b><br/>(3D Geometry)", table_cell_style),
            Paragraph("Each linear equation represents a 2D plane in 3D space. 3 planes intersect at a single unique point.", table_cell_style),
            Paragraph("3D coordinate space with 3 semi-transparent planes intersecting. Intersection line glows cyan; point (1, 2, 3) radiates orange with orbit camera.", table_cell_style),
            Paragraph("Visualize algebraic solutions as spatial geometric intersections.", table_cell_style)
        ],
        [
            Paragraph("<b>Scene 4</b><br/>2:39 - 4:31<br/>(112.1s)", table_cell_style),
            Paragraph("<b>Complete Solution</b><br/>(Worked Example)", table_cell_style),
            Paragraph("Solve system: R2→R2-2R1, R3→R3-R1, Swap R2↔R3, R3→R3+3R2. Row Echelon Form reached. Back-substitution: z=3, y=2, x=1.", table_cell_style),
            Paragraph("Dual dashboard: Live Matrix stage on left transforms visibly step by step; right card shows exact row calculations and back-substitution steps.", table_cell_style),
            Paragraph("Master full Gaussian Elimination execution without skipping any calculation.", table_cell_style)
        ],
        [
            Paragraph("<b>Scene 5</b><br/>4:31 - 5:12<br/>(41.0s)", table_cell_style),
            Paragraph("<b>Verification</b><br/>(Validation Suite)", table_cell_style),
            Paragraph("Substitute (1, 2, 3) into Equations 1, 2, and 3. All check out identically.", table_cell_style),
            Paragraph("3 test lanes illuminate in sequence with glowing emerald checkmarks (✓ CORRECT). System status shows 100% constraints satisfied.", table_cell_style),
            Paragraph("Confirm mathematical rigor and algebraic correctness.", table_cell_style)
        ],
        [
            Paragraph("<b>Scene 6</b><br/>5:12 - 5:42<br/>(29.6s)", table_cell_style),
            Paragraph("<b>Summary & Credits</b><br/>(Takeaways)", table_cell_style),
            Paragraph("3 Key Takeaways: 1. Augmented Matrix, 2. Row Operations (REF), 3. Back-Substitution.", table_cell_style),
            Paragraph("Summary cards slide in, followed by futuristic college credit plaque and academic disclosures. Smooth fade to black.", table_cell_style),
            Paragraph("Synthesize core linear algebra principles and conclude project.", table_cell_style)
        ]
    ]

    col_widths = [75, 95, 180, 240, 130]
    t = Table(storyboard_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0B0D11')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')])
    ]))

    elements.append(t)
    elements.append(Spacer(1, 10))

    # Page Break for Mathematical Verification Proof
    elements.append(PageBreak())

    elements.append(Paragraph("3. RIGOROUS MATHEMATICAL EXECUTION & DERIVATION PROOF", h1_style))
    math_proof = """
    <b>Original System of Equations:</b><br/>
    (1) &nbsp; <code>x + y + z = 6</code><br/>
    (2) &nbsp; <code>2x - y + z = 3</code><br/>
    (3) &nbsp; <code>x + 2y - z = 2</code><br/><br/>
    <b>Step 1: Augmented Matrix Setup</b><br/>
    <code>[ 1 &nbsp; 1 &nbsp; 1 | &nbsp;6 ]</code><br/>
    <code>[ 2 -1 &nbsp; 1 | &nbsp;3 ]</code><br/>
    <code>[ 1 &nbsp; 2 -1 | &nbsp;2 ]</code><br/><br/>
    <b>Step 2: Eliminate Column 1 below Pivot 1 (Row 1, Col 1 = 1)</b><br/>
    • <code>R2 → R2 - 2·R1</code>: &nbsp; [2, -1, 1 | 3] - 2·[1, 1, 1 | 6] = [0, -3, -1 | -9]<br/>
    • <code>R3 → R3 - R1</code>: &nbsp; [1, 2, -1 | 2] - [1, 1, 1 | 6] = [0, 1, -2 | -4]<br/><br/>
    <b>Step 3: Row Swap to Avoid Fractions</b><br/>
    • <code>R2 ↔ R3</code>: &nbsp; Row 2 becomes [0, 1, -2 | -4] (Pivot 2 = 1); Row 3 becomes [0, -3, -1 | -9]<br/><br/>
    <b>Step 4: Eliminate Column 2 below Pivot 2</b><br/>
    • <code>R3 → R3 + 3·R2</code>: &nbsp; [0, -3, -1 | -9] + 3·[0, 1, -2 | -4] = [0, 0, -7 | -21]<br/>
    • <i>Row Echelon Form (REF) Reached:</i> &nbsp; Third pivot = -7.<br/><br/>
    <b>Step 5, 6, 7: Back-Substitution</b><br/>
    • Row 3: <code>-7z = -21 ⇒ z = 3</code><br/>
    • Row 2: <code>y - 2(3) = -4 ⇒ y - 6 = -4 ⇒ y = 2</code><br/>
    • Row 1: <code>x + (2) + (3) = 6 ⇒ x + 5 = 6 ⇒ x = 1</code><br/><br/>
    <b>Final Solution Vector:</b> &nbsp; <code>[x, y, z]ᵀ = [1, 2, 3]ᵀ</code> (Verified in all 3 original equations).
    """
    elements.append(Paragraph(math_proof, body_style))

    doc.build(elements)
    print("Storyboard PDF successfully created at:", output_path)

if __name__ == "__main__":
    generate_storyboard()

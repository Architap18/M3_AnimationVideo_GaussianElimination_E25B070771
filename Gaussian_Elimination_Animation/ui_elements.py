"""
UI Elements and Theme for Futuristic AI Dashboard
Gaussian Elimination Educational Animation
"""
from manim import *
import numpy as np

# Theme Color Palette (Inspired by Reference Design)
BG_DARK = "#0B0D11"          # Deep charcoal / near black
PANEL_BG = "#13161C"         # Slightly lighter charcoal panel
PANEL_BORDER = "#252B36"     # Subtle panel border
PANEL_BORDER_ACCENT = "#3A4454"

ORANGE_ACCENT = "#FF7A00"    # Bright futuristic orange
ORANGE_GLOW = "#FF9E40"      # Softer orange for highlights
AMBER_SUBTLE = "#B35A00"

WHITE_TEXT = "#F4F6F8"       # Bright mathematical text
GREY_TEXT = "#8C96A5"        # Supporting info & muted text
GREY_DARK = "#4A5260"

GREEN_SUCCESS = "#00E676"    # Verification / Correct indicator
GREEN_BG = "#0D2E1F"
BLUE_CYAN = "#00D2FF"        # System telemetry / active indicator

FONT_MONO = "Menlo"          # Standard macOS futuristic monospace
FONT_SANS = "Helvetica Neue"  # Clean modern UI sans


class BackgroundGrid(VGroup):
    """Futuristic subtle background grid with corner crosshairs and tech dots."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Background rect
        bg = Rectangle(
            width=16, height=9,
            fill_color=BG_DARK,
            fill_opacity=1.0,
            stroke_width=0
        )
        self.add(bg)

        # Subtle grid dots
        dots = VGroup()
        for x in np.linspace(-7.0, 7.0, 15):
            for y in np.linspace(-4.0, 4.0, 9):
                dot = Dot(point=[x, y, 0], radius=0.02, color=GREY_DARK)
                dot.set_opacity(0.25)
                dots.add(dot)
        self.add(dots)

        # Tech corner accents
        corners = VGroup()
        for cx, cy in [(-6.8, 3.6), (6.8, 3.6), (-6.8, -3.6), (6.8, -3.6)]:
            cross_h = Line([cx - 0.15, cy, 0], [cx + 0.15, cy, 0], stroke_width=1.5, stroke_color=GREY_TEXT, stroke_opacity=0.4)
            cross_v = Line([cx, cy - 0.15, 0], [cx, cy + 0.15, 0], stroke_width=1.5, stroke_color=GREY_TEXT, stroke_opacity=0.4)
            corners.add(cross_h, cross_v)
        self.add(corners)


class TopHUD(VGroup):
    """Top navigation / status HUD bar."""
    def __init__(self, scene_number=1, total_scenes=6, scene_title="SYS.INIT", **kwargs):
        super().__init__(**kwargs)
        # Top line
        top_line = Line([-7.2, 3.5, 0], [7.2, 3.5, 0], stroke_width=1.0, stroke_color=PANEL_BORDER)
        
        # System title
        sys_label = Text("CORE // LINEAR ALGEBRA ENGINE", font=FONT_MONO, font_size=13, color=GREY_TEXT)
        sys_label.move_to([-4.8, 3.7, 0])

        # Pulse indicator dot
        pulse_dot = Dot(point=[-2.7, 3.7, 0], radius=0.06, color=ORANGE_ACCENT)
        pulse_ring = Circle(radius=0.12, stroke_color=ORANGE_ACCENT, stroke_width=1.0).move_to([-2.7, 3.7, 0])
        pulse_ring.set_opacity(0.6)

        mode_text = Text("GAUSSIAN_ELIMINATION", font=FONT_MONO, font_size=13, color=WHITE_TEXT)
        mode_text.move_to([-1.0, 3.7, 0])

        # Scene badge
        badge_bg = RoundedRectangle(corner_radius=0.1, width=2.4, height=0.35, fill_color=PANEL_BG, fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=1)
        badge_bg.move_to([5.8, 3.7, 0])
        scene_text = Text(f"PHASE 0{scene_number}/0{total_scenes} // {scene_title}", font=FONT_MONO, font_size=11, color=ORANGE_ACCENT)
        scene_text.move_to(badge_bg.get_center())

        self.add(top_line, sys_label, pulse_dot, pulse_ring, mode_text, badge_bg, scene_text)


class DashboardCard(VGroup):
    """Futuristic rounded card container with glowing border, title bar, and content area."""
    def __init__(self, width=6.0, height=4.5, title="MODULE", corner_radius=0.18, border_color=PANEL_BORDER, **kwargs):
        super().__init__(**kwargs)
        self.card_width = width
        self.card_height = height

        # Outer subtle glow / shadow border
        outer_border = RoundedRectangle(
            corner_radius=corner_radius,
            width=width + 0.04,
            height=height + 0.04,
            stroke_color=border_color,
            stroke_width=1.5,
            stroke_opacity=0.6,
            fill_opacity=0
        )

        # Main background
        self.bg = RoundedRectangle(
            corner_radius=corner_radius,
            width=width,
            height=height,
            fill_color=PANEL_BG,
            fill_opacity=0.92,
            stroke_color=border_color,
            stroke_width=1.0
        )

        # Header divider line
        header_y = height / 2 - 0.55
        self.divider = Line(
            [-width/2 + 0.2, header_y, 0],
            [width/2 - 0.2, header_y, 0],
            stroke_width=1.0,
            stroke_color=PANEL_BORDER
        )

        # Title text
        self.title_text = Text(title.upper(), font=FONT_MONO, font_size=13, color=ORANGE_ACCENT)
        self.title_text.move_to([-width/2 + 0.35 + self.title_text.width/2, header_y + 0.28, 0])

        # Header status light
        dot1 = Dot(point=[width/2 - 0.5, header_y + 0.28, 0], radius=0.04, color=GREY_DARK)
        dot2 = Dot(point=[width/2 - 0.3, header_y + 0.28, 0], radius=0.04, color=ORANGE_ACCENT)

        self.add(outer_border, self.bg, self.divider, self.title_text, dot1, dot2)


class MatrixGrid(VGroup):
    """High-contrast, perfectly aligned augmented matrix for Gaussian Elimination."""
    def __init__(self, data, pivots=None, highlight_row=None, font_size=20, h_buff=1.1, v_buff=0.75, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        pivots = pivots or []

        self.cells = []
        cell_mobjects = VGroup()

        # Compute dimensions
        total_w = (self.cols - 1) * h_buff
        total_h = (self.rows - 1) * v_buff

        for r in range(self.rows):
            row_cells = []
            for c in range(self.cols):
                val = data[r][c]
                val_str = str(val)
                # Check color
                is_pivot = (r, c) in pivots
                is_hi_row = highlight_row == r
                
                if is_pivot:
                    txt_color = ORANGE_ACCENT
                elif is_hi_row:
                    txt_color = WHITE_TEXT
                else:
                    txt_color = WHITE_TEXT if val != 0 else GREY_TEXT

                txt = Text(val_str, font=FONT_MONO, font_size=font_size, color=txt_color)
                x = -total_w / 2 + c * h_buff
                # Adjust for augmented separator column gap if 4 columns (3x3 + 1)
                if self.cols == 4 and c == 3:
                    x += 0.25
                elif self.cols == 4 and c < 3:
                    x -= 0.1

                y = total_h / 2 - r * v_buff
                txt.move_to([x, y, 0])

                if is_pivot:
                    # Add an orange rounded highlight box around pivot
                    pbox = RoundedRectangle(
                        corner_radius=0.08,
                        width=txt.width + 0.32,
                        height=txt.height + 0.22,
                        fill_color=ORANGE_ACCENT,
                        fill_opacity=0.22,
                        stroke_color=ORANGE_ACCENT,
                        stroke_width=1.5
                    ).move_to(txt.get_center())
                    cell_mobjects.add(pbox)

                cell_mobjects.add(txt)
                row_cells.append(txt)
            self.cells.append(row_cells)

        self.add(cell_mobjects)

        # Outer brackets
        bracket_pad_x = 0.35
        bracket_top = total_h / 2 + 0.4
        bracket_bot = -total_h / 2 - 0.4
        left_x = -total_w / 2 - bracket_pad_x
        right_x = total_w / 2 + (0.35 if self.cols == 4 else 0) + bracket_pad_x

        # Left bracket
        lb = VGroup(
            Line([left_x + 0.15, bracket_top, 0], [left_x, bracket_top, 0], stroke_width=2.5, stroke_color=WHITE_TEXT),
            Line([left_x, bracket_top, 0], [left_x, bracket_bot, 0], stroke_width=2.5, stroke_color=WHITE_TEXT),
            Line([left_x, bracket_bot, 0], [left_x + 0.15, bracket_bot, 0], stroke_width=2.5, stroke_color=WHITE_TEXT),
        )
        # Right bracket
        rb = VGroup(
            Line([right_x - 0.15, bracket_top, 0], [right_x, bracket_top, 0], stroke_width=2.5, stroke_color=WHITE_TEXT),
            Line([right_x, bracket_top, 0], [right_x, bracket_bot, 0], stroke_width=2.5, stroke_color=WHITE_TEXT),
            Line([right_x, bracket_bot, 0], [right_x - 0.15, bracket_bot, 0], stroke_width=2.5, stroke_color=WHITE_TEXT),
        )
        self.add(lb, rb)

        # Augmented vertical line if 4 columns
        if self.cols == 4:
            sep_x = -total_w / 2 + 2 * h_buff + 0.5 * h_buff + 0.08
            aug_line = DashedLine(
                [sep_x, bracket_top - 0.05, 0],
                [sep_x, bracket_bot + 0.05, 0],
                dash_length=0.1,
                dashed_ratio=0.6,
                stroke_width=1.5,
                stroke_color=GREY_TEXT
            )
            self.add(aug_line)


class OperationBadge(VGroup):
    """Badge indicating the elementary row operation."""
    def __init__(self, op_text="R2 → R2 - 2R1", font_size=14, **kwargs):
        super().__init__(**kwargs)
        txt = Text(op_text, font=FONT_MONO, font_size=font_size, color=WHITE_TEXT)
        bg = RoundedRectangle(
            corner_radius=0.1,
            width=txt.width + 0.4,
            height=txt.height + 0.25,
            fill_color="#201812",
            fill_opacity=0.95,
            stroke_color=ORANGE_ACCENT,
            stroke_width=1.2
        )
        self.add(bg, txt)

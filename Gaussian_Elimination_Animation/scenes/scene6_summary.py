"""
Scene 6: Summary and Credits (5:12.432 - 5:42.076, duration 29.644s)
Gaussian Elimination Animation
"""
from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_elements import *

class Scene6Summary(Scene):
    def construct(self):
        bg = BackgroundGrid()
        hud = TopHUD(scene_number=6, total_scenes=6, scene_title="SUMMARY & CREDITS")
        self.add(bg, hud)

        # 1. Three Key Takeaways (0.0s - 17.73s)
        card_sum = DashboardCard(width=11.2, height=5.2, title="KEY ARCHITECTURAL TAKEAWAYS")
        card_sum.move_to([0, -0.4, 0])

        t1 = VGroup(
            RoundedRectangle(corner_radius=0.1, width=10.0, height=0.9, fill_color="#181D26", fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=1),
            Text("1. AUGMENTED MATRIX REPRESENTATION", font=FONT_MONO, font_size=14, color=ORANGE_ACCENT),
            Text("Translate systems of equations into compact [ A | b ] numerical grids.", font=FONT_SANS, font_size=12, color=WHITE_TEXT)
        )
        t1[1].move_to(t1[0].get_center() + UP * 0.15 + LEFT * 1.0)
        t1[2].move_to(t1[0].get_center() + DOWN * 0.18 + LEFT * 0.7)
        t1.move_to(card_sum.get_center() + UP * 1.3)

        t2 = VGroup(
            RoundedRectangle(corner_radius=0.1, width=10.0, height=0.9, fill_color="#181D26", fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=1),
            Text("2. SYSTEMATIC ROW OPERATIONS (REF)", font=FONT_MONO, font_size=14, color=ORANGE_ACCENT),
            Text("Use pivots and elementary row operations to clear lower columns into triangular form.", font=FONT_SANS, font_size=12, color=WHITE_TEXT)
        )
        t2[1].move_to(t2[0].get_center() + UP * 0.15 + LEFT * 0.9)
        t2[2].move_to(t2[0].get_center() + DOWN * 0.18 + LEFT * 0.1)
        t2.move_to(card_sum.get_center() + UP * 0.25)

        t3 = VGroup(
            RoundedRectangle(corner_radius=0.1, width=10.0, height=0.9, fill_color="#181D26", fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=1),
            Text("3. BACK-SUBSTITUTION (BOTTOM TO TOP)", font=FONT_MONO, font_size=14, color=ORANGE_ACCENT),
            Text("Solve the bottom single variable first, then substitute upward for remaining unknowns.", font=FONT_SANS, font_size=12, color=WHITE_TEXT)
        )
        t3[1].move_to(t3[0].get_center() + UP * 0.15 + LEFT * 0.8)
        t3[2].move_to(t3[0].get_center() + DOWN * 0.18 + LEFT * 0.1)
        t3.move_to(card_sum.get_center() + DOWN * 0.8)

        self.play(FadeIn(card_sum), run_time=1.0) # 1.0s
        self.wait(1.95) # 2.95s
        self.play(FadeIn(t1, shift=UP * 0.2), run_time=1.8) # 4.75s
        self.wait(2.14) # 6.89s
        self.play(FadeIn(t2, shift=UP * 0.2), run_time=2.0) # 8.89s
        self.wait(2.93) # 11.82s
        self.play(FadeIn(t3, shift=UP * 0.2), run_time=2.2) # 14.02s
        self.wait(3.71) # 17.73s

        # 2. Credits and Closing Card (17.73s - 29.644s)
        self.play(FadeOut(card_sum), FadeOut(t1), FadeOut(t2), FadeOut(t3), run_time=1.2) # 18.93s

        credit_card = RoundedRectangle(
            corner_radius=0.2, width=10.5, height=4.2,
            fill_color=PANEL_BG, fill_opacity=0.95,
            stroke_color=ORANGE_ACCENT, stroke_width=2.0
        ).move_to([0, -0.3, 0])

        c_title = Text("GAUSSIAN ELIMINATION", font=FONT_MONO, font_size=24, color=ORANGE_ACCENT, weight=BOLD)
        c_sub = Text("UNDERSTANDING MATHEMATICS STEP BY STEP", font=FONT_SANS, font_size=14, color=WHITE_TEXT)
        c_divider = Line([-4.5, 0, 0], [4.5, 0, 0], stroke_width=1, stroke_color=PANEL_BORDER)

        c_details = VGroup(
            Text("Course: M3 Linear Algebra  •  College Internal Assessment", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("Technology: Python 3  •  Manim Community Edition  •  FFmpeg", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("Disclosure: AI Voice Narration & AI-Assisted Motion Graphics Production", font=FONT_MONO, font_size=11, color=GREY_DARK),
        ).arrange(DOWN, buff=0.15)

        c_title.move_to(credit_card.get_center() + UP * 1.3)
        c_sub.move_to(credit_card.get_center() + UP * 0.8)
        c_divider.move_to(credit_card.get_center() + UP * 0.4)
        c_details.move_to(credit_card.get_center() + DOWN * 0.6)

        c_group = VGroup(credit_card, c_title, c_sub, c_divider, c_details)
        self.play(FadeIn(c_group, scale=0.95), run_time=2.0) # 20.93s
        self.wait(6.0) # 26.93s
        self.play(FadeOut(c_group), FadeOut(hud), FadeOut(bg), run_time=2.5) # 29.43s
        self.wait(0.214) # 29.644s

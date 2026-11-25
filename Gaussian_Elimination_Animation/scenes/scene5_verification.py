"""
Scene 5: Verification and Interpretation (4:31.391 - 5:12.432, duration 41.041s)
Gaussian Elimination Animation
"""
from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_elements import *

class Scene5Verification(Scene):
    def construct(self):
        bg = BackgroundGrid()
        hud = TopHUD(scene_number=5, total_scenes=6, scene_title="VERIFICATION")
        self.add(bg, hud)

        card_verif = DashboardCard(width=11.2, height=5.4, title="SOLUTION VERIFICATION SUITE")
        card_verif.move_to([0, -0.4, 0])

        self.play(FadeIn(card_verif), run_time=1.2) # 1.2s
        self.wait(1.21) # 2.41s

        # Parameter pill
        param_pill = RoundedRectangle(
            corner_radius=0.1, width=7.0, height=0.6,
            fill_color="#181D26", fill_opacity=0.9,
            stroke_color=ORANGE_ACCENT, stroke_width=1.2
        ).move_to(card_verif.get_center() + UP * 1.7)
        param_text = Text("INPUT CANDIDATE:  x = 1,   y = 2,   z = 3", font=FONT_MONO, font_size=13, color=WHITE_TEXT)
        param_text.move_to(param_pill.get_center())

        self.play(FadeIn(param_pill), Write(param_text), run_time=2.0) # 4.41s
        self.wait(7.66) # 12.07s

        # 3 Test Lanes for the Equations
        # Equation 1 (12.07s - 18.10s)
        lane1_box = RoundedRectangle(corner_radius=0.1, width=9.6, height=0.75, fill_color="#12161E", fill_opacity=0.8, stroke_color=PANEL_BORDER, stroke_width=1).move_to(card_verif.get_center() + UP * 0.7)
        lane1_eq = Text("EQ 1:  (1) + (2) + (3)  =  6   ⇒   6 = 6", font=FONT_MONO, font_size=13, color=WHITE_TEXT).move_to(lane1_box.get_center() + LEFT * 1.5)
        lane1_tag = Text("✓ CORRECT", font=FONT_MONO, font_size=12, color=GREEN_SUCCESS, weight=BOLD).move_to(lane1_box.get_center() + RIGHT * 3.3)
        lane1 = VGroup(lane1_box, lane1_eq, lane1_tag)

        self.play(FadeIn(lane1_box), Write(lane1_eq), run_time=2.5) # 14.57s
        self.play(FadeIn(lane1_tag, scale=1.2), run_time=1.0) # 15.57s
        self.wait(2.53) # 18.10s

        # Equation 2 (18.10s - 24.14s)
        lane2_box = RoundedRectangle(corner_radius=0.1, width=9.6, height=0.75, fill_color="#12161E", fill_opacity=0.8, stroke_color=PANEL_BORDER, stroke_width=1).move_to(card_verif.get_center() + DOWN * 0.2)
        lane2_eq = Text("EQ 2:  2(1) - (2) + (3)  =  3   ⇒   3 = 3", font=FONT_MONO, font_size=13, color=WHITE_TEXT).move_to(lane2_box.get_center() + LEFT * 1.5)
        lane2_tag = Text("✓ CORRECT", font=FONT_MONO, font_size=12, color=GREEN_SUCCESS, weight=BOLD).move_to(lane2_box.get_center() + RIGHT * 3.3)
        lane2 = VGroup(lane2_box, lane2_eq, lane2_tag)

        self.play(FadeIn(lane2_box), Write(lane2_eq), run_time=2.5) # 20.60s
        self.play(FadeIn(lane2_tag, scale=1.2), run_time=1.0) # 21.60s
        self.wait(2.54) # 24.14s

        # Equation 3 (24.14s - 30.17s)
        lane3_box = RoundedRectangle(corner_radius=0.1, width=9.6, height=0.75, fill_color="#12161E", fill_opacity=0.8, stroke_color=PANEL_BORDER, stroke_width=1).move_to(card_verif.get_center() + DOWN * 1.1)
        lane3_eq = Text("EQ 3:  (1) + 2(2) - (3)  =  2   ⇒   2 = 2", font=FONT_MONO, font_size=13, color=WHITE_TEXT).move_to(lane3_box.get_center() + LEFT * 1.5)
        lane3_tag = Text("✓ CORRECT", font=FONT_MONO, font_size=12, color=GREEN_SUCCESS, weight=BOLD).move_to(lane3_box.get_center() + RIGHT * 3.3)
        lane3 = VGroup(lane3_box, lane3_eq, lane3_tag)

        self.play(FadeIn(lane3_box), Write(lane3_eq), run_time=2.5) # 26.64s
        self.play(FadeIn(lane3_tag, scale=1.2), run_time=1.0) # 27.64s
        self.wait(2.53) # 30.17s

        # Simultaneous Satisfaction & Geometric link (30.17s - 41.041s)
        bottom_badge = RoundedRectangle(
            corner_radius=0.1, width=9.6, height=0.7,
            fill_color=GREEN_BG, fill_opacity=0.9,
            stroke_color=GREEN_SUCCESS, stroke_width=1.5
        ).move_to(card_verif.get_center() + DOWN * 1.95)
        bottom_text = Text("ALL 3 CONSTRAINTS SATISFIED SIMULTANEOUSLY  //  POINT (1, 2, 3) CONFIRMED", font=FONT_MONO, font_size=11, color=GREEN_SUCCESS, weight=BOLD)
        bottom_text.move_to(bottom_badge.get_center())

        self.play(FadeIn(bottom_badge), Write(bottom_text), run_time=2.0) # 32.17s
        self.wait(8.871) # 41.041s

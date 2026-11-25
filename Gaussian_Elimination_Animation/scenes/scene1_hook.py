"""
Scene 1: The Hook (0:00 - 0:57)
Gaussian Elimination Animation
"""
from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_elements import *

class Scene1Hook(Scene):
    def construct(self):
        # 1. Background and HUD
        bg = BackgroundGrid()
        hud = TopHUD(scene_number=1, total_scenes=6, scene_title="THE HOOK")
        self.add(bg, hud)

        # 2. Opening Title Sequence (0:00 - 0:08)
        title_box = RoundedRectangle(
            corner_radius=0.2, width=10.0, height=2.8,
            fill_color=PANEL_BG, fill_opacity=0.95,
            stroke_color=ORANGE_ACCENT, stroke_width=2.0
        ).move_to([0, 0, 0])

        title_main = Text("GAUSSIAN ELIMINATION", font=FONT_MONO, font_size=32, color=ORANGE_ACCENT, weight=BOLD)
        title_sub = Text("A VISUAL JOURNEY THROUGH LINEAR ALGEBRA", font=FONT_SANS, font_size=16, color=WHITE_TEXT)
        title_tag = Text("SYS.INIT // LINEAR ALGEBRA CONSOLE // LEVEL: ZERO", font=FONT_MONO, font_size=11, color=GREY_TEXT)

        title_main.move_to(title_box.get_center() + UP * 0.45)
        title_sub.move_to(title_box.get_center() + DOWN * 0.15)
        title_tag.move_to(title_box.get_center() + DOWN * 0.75)

        title_group = VGroup(title_box, title_main, title_sub, title_tag)

        self.play(FadeIn(title_group, shift=UP * 0.3), run_time=2.5)
        self.wait(3.5) # until ~6.0s
        self.play(FadeOut(title_group, shift=DOWN * 0.3), run_time=1.5) # until 7.5s
        self.wait(1.0) # until 8.5s

        # 3. Everyday Situation (8.5s - 29.0s)
        # Left card: Store Problem
        card_store = DashboardCard(width=6.5, height=5.2, title="STORE PROBLEM // UNKNOWN PRICES")
        card_store.move_to([-3.4, -0.4, 0])

        item1_text = VGroup(
            Text("ITEM SET A", font=FONT_MONO, font_size=13, color=ORANGE_ACCENT),
            Text("1 Notebook + 1 Pen  =  ₹30", font=FONT_MONO, font_size=17, color=WHITE_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(card_store.get_center() + UP * 1.0 + LEFT * 0.2)

        item2_text = VGroup(
            Text("ITEM SET B", font=FONT_MONO, font_size=13, color=ORANGE_ACCENT),
            Text("2 Notebooks + 1 Pen  =  ₹50", font=FONT_MONO, font_size=17, color=WHITE_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(card_store.get_center() + DOWN * 0.2 + LEFT * 0.2)

        question_text = Text("Find exact price of each item?", font=FONT_SANS, font_size=15, color=ORANGE_GLOW)
        question_text.move_to(card_store.get_center() + DOWN * 1.5)

        # Right card: Mathematical Definitions (appears at 29s)
        card_math = DashboardCard(width=6.0, height=5.2, title="MATHEMATICAL FORMULATION")
        card_math.move_to([3.5, -0.4, 0])

        def_unknown = VGroup(
            Text("UNKNOWNS (VARIABLES):", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("x = Price of Notebook\ny = Price of Pen", font=FONT_MONO, font_size=15, color=WHITE_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(card_math.get_center() + UP * 1.2 + LEFT * 0.2)

        def_equations = VGroup(
            Text("EQUATIONS (RELATIONSHIPS):", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("x +  y = 30\n2x + y = 50", font=FONT_MONO, font_size=18, color=ORANGE_ACCENT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(card_math.get_center() + DOWN * 0.2 + LEFT * 0.2)

        # Play store card appearance (8.5s - 20.5s)
        self.play(FadeIn(card_store), run_time=1.5)
        self.play(Write(item1_text), run_time=2.5)
        self.wait(3.0) # ~15.5s
        self.play(Write(item2_text), run_time=2.5) # ~18.0s
        self.wait(3.0) # ~21.0s
        self.play(FadeIn(question_text, shift=UP * 0.2), run_time=1.5)
        self.wait(2.5) # ~25.0s

        # 4. Math definitions (29.0s - 39.0s)
        self.play(FadeIn(card_math), run_time=1.5) # ~26.5s
        self.wait(2.5) # 29.0s
        self.play(Write(def_unknown), run_time=3.0) # ~32.0s
        self.wait(1.0) # 33.0s
        self.play(Write(def_equations), run_time=3.5) # ~36.5s
        self.wait(2.5) # 39.0s

        # 5. Deduction & Solution (39.0s - 50.0s)
        # Adding 1 notebook increases price by 20 rupees
        diff_badge = RoundedRectangle(
            corner_radius=0.12, width=5.2, height=0.8,
            fill_color="#2A1B0E", fill_opacity=0.95,
            stroke_color=ORANGE_ACCENT, stroke_width=1.5
        ).move_to(card_math.get_center() + DOWN * 1.45)
        diff_text = Text("Difference: +1 Notebook  =  +₹20", font=FONT_MONO, font_size=13, color=WHITE_TEXT)
        diff_text.move_to(diff_badge.get_center())

        self.play(FadeIn(diff_badge), Write(diff_text), run_time=2.0) # 41.0s
        self.wait(3.0) # 44.0s

        # Final answer badge
        sol_badge = RoundedRectangle(
            corner_radius=0.12, width=5.2, height=0.8,
            fill_color=GREEN_BG, fill_opacity=0.95,
            stroke_color=GREEN_SUCCESS, stroke_width=1.8
        ).move_to(card_math.get_center() + DOWN * 1.45)
        sol_text = Text("Notebook = ₹20  |  Pen = ₹10  ✓", font=FONT_MONO, font_size=13, color=GREEN_SUCCESS, weight=BOLD)
        sol_text.move_to(sol_badge.get_center())

        self.play(Transform(diff_badge, sol_badge), Transform(diff_text, sol_text), run_time=1.5) # 45.5s
        self.wait(4.5) # 50.0s

        # 6. Conclusion of Scene 1 (50.0s - 57.0s)
        self.play(
            FadeOut(card_store), FadeOut(item1_text), FadeOut(item2_text), FadeOut(question_text),
            FadeOut(card_math), FadeOut(def_unknown), FadeOut(def_equations), FadeOut(diff_badge), FadeOut(diff_text),
            run_time=1.5
        ) # 51.5s

        closing_card = RoundedRectangle(
            corner_radius=0.18, width=9.0, height=2.2,
            fill_color=PANEL_BG, fill_opacity=0.95,
            stroke_color=ORANGE_ACCENT, stroke_width=2.0
        ).move_to([0, -0.3, 0])
        closing_title = Text("SYSTEMATIC ALGORITHM REQUIRED", font=FONT_MONO, font_size=20, color=ORANGE_ACCENT)
        closing_desc = Text("When multiple unknowns scale up, guessing fails.\nGaussian Elimination provides exact algebraic certainty.", font=FONT_SANS, font_size=15, color=WHITE_TEXT)
        closing_title.move_to(closing_card.get_center() + UP * 0.4)
        closing_desc.move_to(closing_card.get_center() + DOWN * 0.3)

        closing_group = VGroup(closing_card, closing_title, closing_desc)
        self.play(FadeIn(closing_group, shift=UP * 0.2), run_time=1.5) # 53.0s
        self.wait(4.0) # 57.0s

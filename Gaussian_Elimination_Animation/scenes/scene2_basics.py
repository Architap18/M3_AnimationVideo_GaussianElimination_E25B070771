"""
Scene 2: Understanding the Basics (0:57 - 2:05.615, duration 68.615s)
Gaussian Elimination Animation
"""
from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_elements import *

class Scene2Basics(Scene):
    def construct(self):
        bg = BackgroundGrid()
        hud = TopHUD(scene_number=2, total_scenes=6, scene_title="CORE CONCEPTS")
        self.add(bg, hud)

        # 1. 3 Unknowns & Linear Equations (0.0s - 18.62s)
        card_eq = DashboardCard(width=6.6, height=5.2, title="SYSTEM OF THREE LINEAR EQUATIONS")
        card_eq.move_to([-3.4, -0.4, 0])

        eq_text = VGroup(
            Text("a₁x + b₁y + c₁z = d₁", font=FONT_MONO, font_size=18, color=WHITE_TEXT),
            Text("a₂x + b₂y + c₂z = d₂", font=FONT_MONO, font_size=18, color=WHITE_TEXT),
            Text("a₃x + b₃y + c₃z = d₃", font=FONT_MONO, font_size=18, color=WHITE_TEXT),
        ).arrange(DOWN, buff=0.35).move_to(card_eq.get_center() + UP * 0.4)

        linear_def = VGroup(
            Text("LINEAR PROPERTY: Degree = 1", font=FONT_MONO, font_size=13, color=ORANGE_ACCENT),
            Text("No x², no √x, no xy products.", font=FONT_SANS, font_size=13, color=GREY_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(card_eq.get_center() + DOWN * 1.5)

        self.play(FadeIn(card_eq), Write(eq_text), run_time=3.5) # 3.5s
        self.wait(2.38) # 5.88s
        self.play(FadeIn(linear_def, shift=UP * 0.2), run_time=2.5) # 8.38s
        self.wait(3.38) # 11.76s

        # Breakdown: Variables vs Coefficients (11.76s - 18.62s)
        badge_vocab = RoundedRectangle(
            corner_radius=0.1, width=5.6, height=1.0,
            fill_color="#1E232E", fill_opacity=0.9,
            stroke_color=PANEL_BORDER, stroke_width=1.2
        ).move_to(card_eq.get_center() + DOWN * 0.5)

        vocab_text = VGroup(
            Text("Variables:    x,  y,  z   (Unknowns)", font=FONT_MONO, font_size=12, color=BLUE_CYAN),
            Text("Coefficients: a,  b,  c   (Scale factors)", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(badge_vocab.get_center())

        self.play(FadeIn(badge_vocab), Write(vocab_text), run_time=2.5) # 14.26s
        self.wait(4.36) # 18.62s

        # 2. Transition to Augmented Matrix (18.62s - 32.83s)
        card_mat = DashboardCard(width=6.0, height=5.2, title="THE AUGMENTED MATRIX [ A | b ]")
        card_mat.move_to([3.5, -0.4, 0])

        mat_sample = MatrixGrid(
            [["a₁", "b₁", "c₁", "d₁"],
             ["a₂", "b₂", "c₂", "d₂"],
             ["a₃", "b₃", "c₃", "d₃"]],
            pivots=[(0, 0)],
            font_size=16, h_buff=1.0, v_buff=0.75
        ).move_to(card_mat.get_center() + UP * 0.3)

        mat_labels = VGroup(
            Text("← Coefficients (A) →", font=FONT_MONO, font_size=11, color=ORANGE_ACCENT),
            Text("Constants (b)", font=FONT_MONO, font_size=11, color=BLUE_CYAN)
        )
        mat_labels[0].move_to(mat_sample.get_center() + DOWN * 1.3 + LEFT * 0.8)
        mat_labels[1].move_to(mat_sample.get_center() + DOWN * 1.3 + RIGHT * 1.4)

        self.play(FadeIn(card_mat), run_time=2.0) # 20.62s
        self.wait(2.41) # 23.03s
        self.play(Create(mat_sample), run_time=3.0) # 26.03s
        self.wait(1.41) # 27.44s
        self.play(FadeIn(mat_labels), run_time=2.0) # 29.44s
        self.wait(3.39) # 32.83s

        # 3. What is Gaussian Elimination & Pivot (32.83s - 49.01s)
        # Clear left card for Gaussian definition & Pivot
        self.play(
            FadeOut(eq_text), FadeOut(linear_def), FadeOut(badge_vocab), FadeOut(vocab_text),
            run_time=1.5
        ) # 34.33s

        card_eq.title_text.become(Text("WHAT IS GAUSSIAN ELIMINATION?", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT).move_to(card_eq.title_text.get_center()))

        def_gauss = VGroup(
            Text("SYSTEMATIC SIMPLIFICATION:", font=FONT_MONO, font_size=13, color=WHITE_TEXT),
            Text("Transform the matrix step-by-step\ninto Row Echelon Form (Triangular)\nuntil solving becomes effortless.", font=FONT_SANS, font_size=13, color=GREY_TEXT),
            Text("PIVOT ELEMENT:", font=FONT_MONO, font_size=13, color=ORANGE_ACCENT),
            Text("The leading non-zero coefficient in a row,\nused to eliminate entries below it.", font=FONT_SANS, font_size=13, color=WHITE_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(card_eq.get_center() + DOWN * 0.2)

        self.play(Write(def_gauss[0:2]), run_time=4.0) # 38.33s
        self.wait(4.30) # 42.63s
        self.play(Write(def_gauss[2:4]), run_time=3.5) # 46.13s
        self.wait(2.88) # 49.01s

        # 4. Three Elementary Row Operations (49.01s - 68.615s)
        self.play(
            FadeOut(card_mat), FadeOut(mat_sample), FadeOut(mat_labels),
            FadeOut(card_eq), FadeOut(def_gauss),
            run_time=1.5
        ) # 50.51s

        card_ops = DashboardCard(width=11.5, height=5.2, title="THE THREE ELEMENTARY ROW OPERATIONS")
        card_ops.move_to([0, -0.4, 0])

        op1 = VGroup(
            RoundedRectangle(corner_radius=0.1, width=10.2, height=0.9, fill_color="#181D26", fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=1),
            Text("1. ROW INTERCHANGE:     Ri  ↔  Rj", font=FONT_MONO, font_size=15, color=WHITE_TEXT),
            Text("Swap any two rows to position a convenient pivot.", font=FONT_SANS, font_size=12, color=GREY_TEXT)
        )
        op1[1].move_to(op1[0].get_center() + UP * 0.15 + LEFT * 1.5)
        op1[2].move_to(op1[0].get_center() + DOWN * 0.18 + LEFT * 0.8)
        op1.move_to(card_ops.get_center() + UP * 1.3)

        op2 = VGroup(
            RoundedRectangle(corner_radius=0.1, width=10.2, height=0.9, fill_color="#181D26", fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=1),
            Text("2. ROW SCALING:         Ri  →  k · Ri    (k ≠ 0)", font=FONT_MONO, font_size=15, color=WHITE_TEXT),
            Text("Multiply every entry in a row by a non-zero scalar.", font=FONT_SANS, font_size=12, color=GREY_TEXT)
        )
        op2[1].move_to(op2[0].get_center() + UP * 0.15 + LEFT * 1.2)
        op2[2].move_to(op2[0].get_center() + DOWN * 0.18 + LEFT * 0.8)
        op2.move_to(card_ops.get_center() + UP * 0.25)

        op3 = VGroup(
            RoundedRectangle(corner_radius=0.1, width=10.2, height=0.9, fill_color="#181D26", fill_opacity=0.9, stroke_color=PANEL_BORDER, stroke_width=1),
            Text("3. ROW COMBINATION:     Ri  →  Ri  +  k · Rj", font=FONT_MONO, font_size=15, color=ORANGE_ACCENT),
            Text("Add or subtract a multiple of one row from another to eliminate variables.", font=FONT_SANS, font_size=12, color=GREY_TEXT)
        )
        op3[1].move_to(op3[0].get_center() + UP * 0.15 + LEFT * 0.8)
        op3[2].move_to(op3[0].get_center() + DOWN * 0.18 + LEFT * 0.2)
        op3.move_to(card_ops.get_center() + DOWN * 0.8)

        golden_rule = Text("★ GOLDEN PRINCIPLE: Elementary row operations NEVER alter the solution set!", font=FONT_MONO, font_size=13, color=GREEN_SUCCESS)
        golden_rule.move_to(card_ops.get_center() + DOWN * 1.7)

        self.play(FadeIn(card_ops), run_time=1.0) # 51.51s
        self.wait(0.93) # 52.44s
        self.play(FadeIn(op1, shift=RIGHT * 0.2), run_time=1.5) # 53.94s
        self.wait(0.46) # 54.40s
        self.play(FadeIn(op2, shift=RIGHT * 0.2), run_time=2.0) # 56.40s
        self.wait(1.92) # 58.32s
        self.play(FadeIn(op3, shift=RIGHT * 0.2), run_time=2.5) # 60.82s
        self.wait(3.38) # 64.20s
        self.play(FadeIn(golden_rule), run_time=1.5) # 65.70s
        self.wait(2.915) # 68.615s

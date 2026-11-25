"""
Scene 4: Complete Worked Example (2:39.264 - 4:31.391, duration 112.127s)
Gaussian Elimination Animation
"""
from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_elements import *

class Scene4Solution(Scene):
    def construct(self):
        bg = BackgroundGrid()
        hud = TopHUD(scene_number=4, total_scenes=6, scene_title="WORKED SOLUTION")
        self.add(bg, hud)

        # Left Card: Live Matrix Stage
        card_matrix = DashboardCard(width=6.8, height=5.4, title="AUGMENTED MATRIX [ A | b ]")
        card_matrix.move_to([-3.4, -0.4, 0])

        # Right Card: Operation & Back-Substitution Telemetry
        card_telemetry = DashboardCard(width=5.8, height=5.4, title="CALCULATION TELEMETRY")
        card_telemetry.move_to([3.6, -0.4, 0])

        self.play(FadeIn(card_matrix), FadeIn(card_telemetry), run_time=1.5) # 1.5s

        # 1. System Display (1.5s - 17.25s)
        eq_initial = VGroup(
            Text("System to Solve:", font=FONT_MONO, font_size=13, color=ORANGE_ACCENT),
            Text("1)   x +  y +  z = 6", font=FONT_MONO, font_size=15, color=WHITE_TEXT),
            Text("2)  2x -  y +  z = 3", font=FONT_MONO, font_size=15, color=WHITE_TEXT),
            Text("3)   x + 2y -  z = 2", font=FONT_MONO, font_size=15, color=WHITE_TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(card_telemetry.get_center() + UP * 0.8)

        self.play(Write(eq_initial), run_time=3.5) # 5.0s
        self.wait(12.25) # 17.25s

        # 2. Step 1: Initial Augmented Matrix (17.25s - 22.83s)
        mat1 = MatrixGrid(
            [[1, 1, 1, 6],
             [2, -1, 1, 3],
             [1, 2, -1, 2]],
            pivots=[(0, 0)],
            font_size=17, h_buff=1.1, v_buff=0.8
        ).move_to(card_matrix.get_center() + DOWN * 0.2)

        step1_badge = OperationBadge("STEP 1: AUGMENTED MATRIX", font_size=12).move_to(card_telemetry.get_center() + DOWN * 1.5)

        self.play(Create(mat1), FadeIn(step1_badge), run_time=3.0) # 20.25s
        self.wait(2.58) # 22.83s

        # 3. Step 2: Clear Column 1 Below First Pivot (22.83s - 50.73s)
        # 22.83 - 29.93s: Highlight pivot
        pivot_note = Text("Pivot 1 = 1 (Row 1, Col 1)", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT).move_to(card_telemetry.get_center() + UP * 1.7)
        self.play(FadeIn(pivot_note), run_time=1.5) # 24.33s
        self.wait(5.60) # 29.93s

        # 29.93s - 43.63s: Row 2 -> Row 2 - 2*Row 1
        self.play(FadeOut(step1_badge), run_time=0.5) # 30.43s
        op_r2 = OperationBadge("R2 → R2 - 2·R1", font_size=14).move_to(card_telemetry.get_center() + UP * 0.7)
        calc_r2 = VGroup(
            Text("[ 2  -1   1 |  3]", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("- 2·[ 1   1   1 |  6]", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT),
            Line([-1.8, 0, 0], [1.8, 0, 0], stroke_width=1, stroke_color=GREY_DARK),
            Text("=   [ 0  -3  -1 | -9]", font=FONT_MONO, font_size=13, color=WHITE_TEXT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(card_telemetry.get_center() + DOWN * 0.3)

        self.play(FadeIn(op_r2), Write(calc_r2), run_time=3.0) # 33.43s
        self.wait(2.08) # 35.51s

        # Update matrix to intermediate with row 2 modified
        mat2_int = MatrixGrid(
            [[1, 1, 1, 6],
             [0, -3, -1, -9],
             [1, 2, -1, 2]],
            pivots=[(0, 0)],
            font_size=17, h_buff=1.1, v_buff=0.8
        ).move_to(card_matrix.get_center() + DOWN * 0.2)

        self.play(Transform(mat1, mat2_int), run_time=2.0) # 37.51s
        self.wait(6.12) # 43.63s

        # 43.63s - 50.73s: Row 3 -> Row 3 - Row 1
        self.play(FadeOut(op_r2), FadeOut(calc_r2), run_time=0.8) # 44.43s
        op_r3 = OperationBadge("R3 → R3 - R1", font_size=14).move_to(card_telemetry.get_center() + UP * 0.7)
        calc_r3 = VGroup(
            Text("[ 1   2  -1 |  2]", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("-   [ 1   1   1 |  6]", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT),
            Line([-1.8, 0, 0], [1.8, 0, 0], stroke_width=1, stroke_color=GREY_DARK),
            Text("=   [ 0   1  -2 | -4]", font=FONT_MONO, font_size=13, color=WHITE_TEXT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(card_telemetry.get_center() + DOWN * 0.3)

        self.play(FadeIn(op_r3), Write(calc_r3), run_time=2.0) # 46.43s

        mat2 = MatrixGrid(
            [[1, 1, 1, 6],
             [0, -3, -1, -9],
             [0, 1, -2, -4]],
            pivots=[(0, 0)],
            font_size=17, h_buff=1.1, v_buff=0.8
        ).move_to(card_matrix.get_center() + DOWN * 0.2)

        self.play(Transform(mat1, mat2), run_time=1.8) # 48.23s
        self.wait(2.50) # 50.73s

        # 4. Step 3: Swap R2 <-> R3 to make pivot 1 (50.73s - 64.43s)
        self.play(FadeOut(op_r3), FadeOut(calc_r3), run_time=0.8) # 51.53s
        op_swap = OperationBadge("STEP 3: R2 ↔ R3 (ROW SWAP)", font_size=13).move_to(card_telemetry.get_center() + UP * 0.7)
        swap_desc = Text("Swap Row 2 and Row 3 to obtain\na clean pivot = 1 and avoid fractions!", font=FONT_SANS, font_size=12, color=WHITE_TEXT).move_to(card_telemetry.get_center() + DOWN * 0.2)

        self.play(FadeIn(op_swap), Write(swap_desc), run_time=2.5) # 54.03s

        mat3 = MatrixGrid(
            [[1, 1, 1, 6],
             [0, 1, -2, -4],
             [0, -3, -1, -9]],
            pivots=[(0, 0), (1, 1)],
            font_size=17, h_buff=1.1, v_buff=0.8
        ).move_to(card_matrix.get_center() + DOWN * 0.2)

        self.play(Transform(mat1, mat3), run_time=2.5) # 56.53s
        self.wait(2.32) # 58.85s
        
        pivot2_note = Text("Second Pivot = 1 (Row 2, Col 2)", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT).move_to(card_telemetry.get_center() + DOWN * 1.5)
        self.play(FadeIn(pivot2_note), run_time=1.5) # 60.35s
        self.wait(4.08) # 64.43s

        # 5. Step 4: Eliminate -3 below pivot: R3 -> R3 + 3*R2 (64.43s - 73.06s)
        self.play(FadeOut(op_swap), FadeOut(swap_desc), FadeOut(pivot2_note), run_time=0.8) # 65.23s
        op_r3_elim = OperationBadge("R3 → R3 + 3·R2", font_size=14).move_to(card_telemetry.get_center() + UP * 0.7)
        calc_r3_elim = VGroup(
            Text("[ 0  -3  -1 |  -9]", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("+ 3·[ 0   1  -2 |  -4]", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT),
            Line([-1.8, 0, 0], [1.8, 0, 0], stroke_width=1, stroke_color=GREY_DARK),
            Text("=   [ 0   0  -7 | -21]", font=FONT_MONO, font_size=13, color=WHITE_TEXT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(card_telemetry.get_center() + DOWN * 0.3)

        self.play(FadeIn(op_r3_elim), Write(calc_r3_elim), run_time=2.5) # 67.73s

        mat4 = MatrixGrid(
            [[1, 1, 1, 6],
             [0, 1, -2, -4],
             [0, 0, -7, -21]],
            pivots=[(0, 0), (1, 1), (2, 2)],
            font_size=17, h_buff=1.1, v_buff=0.8
        ).move_to(card_matrix.get_center() + DOWN * 0.2)

        self.play(Transform(mat1, mat4), run_time=2.0) # 69.73s

        ref_badge = Text("★ ROW ECHELON FORM (REF) ACHIEVED! ★", font=FONT_MONO, font_size=11, color=GREEN_SUCCESS).move_to(card_matrix.get_center() + DOWN * 2.1)
        self.play(FadeIn(ref_badge), run_time=1.0) # 70.73s
        self.wait(2.33) # 73.06s

        # 6. Back-Substitution (73.06s - 99.44s)
        self.play(FadeOut(op_r3_elim), FadeOut(calc_r3_elim), FadeOut(pivot_note), FadeOut(eq_initial), run_time=1.0) # 74.06s

        # Step 5: Solve z from Row 3 (73.06s - 80.16s)
        back_title = Text("BACK-SUBSTITUTION (BOTTOM TO TOP)", font=FONT_MONO, font_size=12, color=ORANGE_ACCENT).move_to(card_telemetry.get_center() + UP * 1.8)
        bs_z = VGroup(
            Text("From Row 3: -7z = -21", font=FONT_MONO, font_size=13, color=WHITE_TEXT),
            Text("z = -21 / -7  ⇒  z = 3", font=FONT_MONO, font_size=14, color=ORANGE_ACCENT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(card_telemetry.get_center() + UP * 0.9)

        self.play(FadeIn(back_title), Write(bs_z), run_time=2.5) # 76.56s
        self.wait(3.60) # 80.16s

        # Step 6: Solve y from Row 2 (80.16s - 89.30s)
        bs_y = VGroup(
            Text("From Row 2: y - 2z = -4", font=FONT_MONO, font_size=13, color=WHITE_TEXT),
            Text("y - 2(3) = -4  ⇒  y - 6 = -4", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("y = -4 + 6    ⇒  y = 2", font=FONT_MONO, font_size=14, color=ORANGE_ACCENT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(card_telemetry.get_center() + DOWN * 0.1)

        self.play(Write(bs_y), run_time=3.5) # 83.66s
        self.wait(5.64) # 89.30s

        # Step 7: Solve x from Row 1 (89.30s - 99.44s)
        bs_x = VGroup(
            Text("From Row 1: x + y + z = 6", font=FONT_MONO, font_size=13, color=WHITE_TEXT),
            Text("x + (2) + (3) = 6  ⇒  x + 5 = 6", font=FONT_MONO, font_size=12, color=GREY_TEXT),
            Text("x = 6 - 5        ⇒  x = 1", font=FONT_MONO, font_size=14, color=ORANGE_ACCENT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(card_telemetry.get_center() + DOWN * 1.3)

        self.play(Write(bs_x), run_time=3.5) # 92.80s
        self.wait(6.64) # 99.44s

        # 7. Final Solution Badge (99.44s - 112.127s)
        self.play(
            FadeOut(card_matrix), FadeOut(mat1), FadeOut(ref_badge),
            FadeOut(card_telemetry), FadeOut(back_title), FadeOut(bs_z), FadeOut(bs_y), FadeOut(bs_x),
            run_time=1.5
        ) # 100.94s

        final_card = RoundedRectangle(
            corner_radius=0.22, width=8.5, height=3.6,
            fill_color=PANEL_BG, fill_opacity=0.96,
            stroke_color=ORANGE_ACCENT, stroke_width=2.5
        ).move_to([0, -0.3, 0])

        final_title = Text("SYSTEM SOLUTION CONFIRMED", font=FONT_MONO, font_size=18, color=ORANGE_ACCENT)
        final_vals = VGroup(
            Text("x = 1", font=FONT_MONO, font_size=24, color=WHITE_TEXT, weight=BOLD),
            Text("y = 2", font=FONT_MONO, font_size=24, color=WHITE_TEXT, weight=BOLD),
            Text("z = 3", font=FONT_MONO, font_size=24, color=WHITE_TEXT, weight=BOLD)
        ).arrange(RIGHT, buff=0.9)

        coord_badge = Text("Unique Intersection Vector:  X* = [ 1,  2,  3 ]ᵀ", font=FONT_MONO, font_size=14, color=GREEN_SUCCESS)

        final_title.move_to(final_card.get_center() + UP * 0.9)
        final_vals.move_to(final_card.get_center() + DOWN * 0.05)
        coord_badge.move_to(final_card.get_center() + DOWN * 1.0)

        final_group = VGroup(final_card, final_title, final_vals, coord_badge)
        self.play(FadeIn(final_group, scale=0.9), run_time=2.0) # 102.94s
        self.wait(9.187) # 112.127s

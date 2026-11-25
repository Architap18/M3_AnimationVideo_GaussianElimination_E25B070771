"""
Scene 3: Visual Intuition in 3D Space (2:05.615 - 2:39.264, duration 33.649s)
Gaussian Elimination Animation
"""
from manim import *
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ui_elements import *

class Scene3Geometry(ThreeDScene):
    def construct(self):
        # 1. 2D HUD fixed in frame
        hud = TopHUD(scene_number=3, total_scenes=6, scene_title="3D GEOMETRY")
        geo_info = DashboardCard(width=4.5, height=2.2, title="GEOMETRIC INTERPRETATION")
        geo_info.move_to([-4.8, -2.5, 0])
        
        info_lines = VGroup(
            Text("• 1 Equation = Flat 2D Plane", font=FONT_MONO, font_size=11, color=WHITE_TEXT),
            Text("• 2 Planes = Line Intersection", font=FONT_MONO, font_size=11, color=BLUE_CYAN),
            Text("• 3 Planes = Unique Point (1, 2, 3)", font=FONT_MONO, font_size=11, color=ORANGE_ACCENT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(geo_info.get_center() + DOWN * 0.2)

        self.add_fixed_in_frame_mobjects(hud, geo_info, info_lines)

        # 2. 3D Camera Setup
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES, distance=8)

        # 3. 3D Axes
        axes = ThreeDAxes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            z_range=[-1, 5, 1],
            x_length=5, y_length=5, z_length=5,
            axis_config={"color": GREY_DARK, "stroke_width": 2}
        )
        x_lab = axes.get_x_axis_label(Text("X", font=FONT_MONO, font_size=14, color=GREY_TEXT))
        y_lab = axes.get_y_axis_label(Text("Y", font=FONT_MONO, font_size=14, color=GREY_TEXT))
        z_lab = axes.get_z_axis_label(Text("Z", font=FONT_MONO, font_size=14, color=GREY_TEXT))
        axes_group = VGroup(axes, x_lab, y_lab, z_lab)

        self.play(Create(axes_group), run_time=2.5) # 2.5s
        self.wait(2.45) # 4.95s

        # 4. Plane 1 (Equation 1: x + y + z = 6) (4.95s - 11.38s)
        # Centered around (1, 2, 3)
        p1 = Polygon(
            axes.c2p(3, 3, 0),
            axes.c2p(3, 0, 3),
            axes.c2p(-1, 2, 5),
            axes.c2p(-1, 5, 2),
            fill_color="#2E4057", fill_opacity=0.45,
            stroke_color="#5D8AA8", stroke_width=1.5
        )
        p1_label = Text("Plane 1: x + y + z = 6", font=FONT_MONO, font_size=12, color=WHITE_TEXT)
        self.add_fixed_orientation_mobjects(p1_label)
        p1_label.move_to(axes.c2p(3.2, 3.2, 0.2))

        self.play(FadeIn(p1), FadeIn(p1_label), run_time=3.0) # 7.95s
        self.wait(3.43) # 11.38s

        # 5. Plane 2 (Equation 2: 2x - y + z = 3) (11.38s - 15.34s)
        p2 = Polygon(
            axes.c2p(2, 4, 3),
            axes.c2p(2, 1, 0),
            axes.c2p(0, 0, 3),
            axes.c2p(0, 3, 6),
            fill_color="#5B3A29", fill_opacity=0.45,
            stroke_color=ORANGE_ACCENT, stroke_width=1.5
        )
        # Intersection line between Plane 1 and Plane 2
        # Passes through (1, 2, 3)
        int_line = Line3D(
            start=axes.c2p(0.5, 2.5, 3.0),
            end=axes.c2p(1.5, 1.5, 3.0),
            color=BLUE_CYAN, thickness=0.03
        )

        self.play(FadeIn(p2), Create(int_line), run_time=2.5) # 13.88s
        self.wait(1.46) # 15.34s

        # 6. Plane 3 (Equation 3: x + 2y - z = 2) (15.34s - 22.27s)
        p3 = Polygon(
            axes.c2p(0, 2, 2),
            axes.c2p(3, 1, 3),
            axes.c2p(2, 3, 6),
            axes.c2p(-1, 4, 5),
            fill_color="#2C4C38", fill_opacity=0.45,
            stroke_color=GREEN_SUCCESS, stroke_width=1.5
        )
        self.play(FadeIn(p3), run_time=3.0) # 18.34s
        self.wait(3.93) # 22.27s

        # 7. Unique Intersection Point (1, 2, 3) (22.27s - 27.71s)
        sol_pt = Dot3D(point=axes.c2p(1, 2, 3), radius=0.12, color=ORANGE_ACCENT)
        sol_ring = Circle(radius=0.25, stroke_color=ORANGE_ACCENT, stroke_width=2.5)
        self.add_fixed_orientation_mobjects(sol_ring)
        sol_ring.move_to(axes.c2p(1, 2, 3))

        sol_coord_badge = RoundedRectangle(
            corner_radius=0.08, width=2.4, height=0.6,
            fill_color=PANEL_BG, fill_opacity=0.95,
            stroke_color=ORANGE_ACCENT, stroke_width=1.5
        )
        sol_coord_txt = Text("(1, 2, 3)", font=FONT_MONO, font_size=14, color=WHITE_TEXT, weight=BOLD)
        sol_coord_badge.move_to(axes.c2p(1.0, 2.0, 3.8))
        sol_coord_txt.move_to(sol_coord_badge.get_center())
        self.add_fixed_orientation_mobjects(sol_coord_badge, sol_coord_txt)

        self.play(FadeIn(sol_pt), Create(sol_ring), FadeIn(sol_coord_badge), Write(sol_coord_txt), run_time=2.5) # 24.77s
        self.wait(2.94) # 27.71s

        # 8. Camera rotation & Wrap-up (27.71s - 33.649s)
        self.move_camera(theta=-15 * DEGREES, phi=55 * DEGREES, run_time=4.0) # 31.71s
        self.wait(1.939) # 33.649s

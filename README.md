# GAUSSIAN ELIMINATION – FUTURISTIC MATHEMATICS ANIMATION

[![Linear Algebra M3](https://img.shields.io/badge/Course-M3%20Linear%20Algebra-orange.svg)](#)
[![Manim Community](https://img.shields.io/badge/Rendered%20with-Manim%20CE%20v0.19.1-blue.svg)](https://www.manim.community/)
[![Resolution](https://img.shields.io/badge/Resolution-1920%C3%971080%20(16%3A9)-green.svg)](#)
[![Duration](https://img.shields.io/badge/Duration-05%3A42%20(Under%207m)-brightgreen.svg)](#)
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow.svg)](#)

A complete, high-production 5-minute educational animated video explaining **Gaussian Elimination** from absolute zero for college **M3 Linear Algebra** internal assessment.

The video visualizes systems of linear equations, augmented matrices, elementary row operations, and 3D geometric intuition styled as a **premium futuristic AI intelligence dashboard**.

---

## 🌟 Visual Theme & Design Language

The visual design recreates the aesthetic of an advanced AI telemetry dashboard:
- **Background & Canvas:** Dark charcoal and near-black panels (`#0B0D11`, `#13161C`) overlaid with technical coordinate dots and corner crosshairs.
- **Card Panels:** Rounded dashboard cards (`#13161C`) featuring header divider bars, telemetry lights, and subtle glowing borders (`#252B36`).
- **Mathematical Color Coding:**
  - ⚪ **Crisp White (`#F4F6F8`):** Equations and primary mathematical symbols.
  - 🟠 **Futuristic Orange (`#FF7A00` / `#FF9E40`):** Pivot elements, active row operations, and critical step highlights.
  - 🔘 **Slate Grey (`#8C96A5`):** Intermediate steps, coordinate axes, and supporting annotations.
  - 🟢 **Emerald Green (`#00E676`):** Final verified solutions, constraint validation checks, and victory badges.
  - 🔵 **Cyan (`#00D2FF`):** Variable identification, 3D plane intersection lines, and active telemetry.
- **Typography:** Clean monospaced numerals (`Menlo` / `Courier`) for matrix column alignment and modern sans-serif (`Helvetica Neue`) for interface labels.

---

## 📐 Mathematical Rigor & Worked Example

The video solves the 3×3 system step by step without skipping any calculation:

$$\begin{aligned}
x + y + z &= 6 \\
2x - y + z &= 3 \\
x + 2y - z &= 2
\end{aligned}$$

### Derivation Steps:
1. **Construct the Augmented Matrix:**
   $$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & -1 & 1 & 3 \\ 1 & 2 & -1 & 2 \end{array}\right]$$
2. **First Pivot Elimination ($R_1, C_1 = 1$):**
   - $R_2 \leftarrow R_2 - 2R_1 \implies [0, -3, -1 \mid -9]$
   - $R_3 \leftarrow R_3 - R_1 \implies [0, 1, -2 \mid -4]$
3. **Row Swap for Numerical Simplicity:**
   - $R_2 \leftrightarrow R_3 \implies$ Row 2 becomes $[0, 1, -2 \mid -4]$ with a clean pivot $1$ (avoiding fractions).
4. **Second Pivot Elimination:**
   - $R_3 \leftarrow R_3 + 3R_2 \implies [0, 0, -7 \mid -21]$
   - **Row Echelon Form (REF) reached!**
5. **Back-Substitution (Bottom to Top):**
   - Row 3: $-7z = -21 \implies \mathbf{z = 3}$
   - Row 2: $y - 2(3) = -4 \implies y - 6 = -4 \implies \mathbf{y = 2}$
   - Row 1: $x + (2) + (3) = 6 \implies x + 5 = 6 \implies \mathbf{x = 1}$
6. **Solution Vector:**
   $$\mathbf{X^*} = [1, 2, 3]^T$$
7. **Complete 3-Equation Verification:**
   - Eq 1: $1 + 2 + 3 = 6 \implies 6 = 6$ ✓
   - Eq 2: $2(1) - 2 + 3 = 3 \implies 3 = 3$ ✓
   - Eq 3: $1 + 2(2) - 3 = 2 \implies 2 = 2$ ✓

---

## 🎬 Six-Scene Video Choreography

| Scene | Phase Title | Time Range | Duration | Pedagogical Focus |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **The Hook** | `00:00 - 00:57` | 57.0s | Starts from absolute zero: Notebook & pen store problem ($x+y=30, 2x+y=50$). Defines unknowns and equations. |
| **2** | **The Basics** | `00:57 - 02:05` | 68.6s | Introduces 3 unknowns, linear degree, coefficient extraction, augmented matrix $[A \mid b]$, pivots, and 3 row operations. |
| **3** | **Visual Intuition** | `02:05 - 02:39` | 33.6s | 3D space geometry: 3 intersecting planes meeting at a unique point $(1, 2, 3)$. Orbit camera visualization. |
| **4** | **Worked Solution** | `02:39 - 04:31` | 112.1s | Full step-by-step matrix reduction, row swaps, Row Echelon Form, and bottom-to-top back substitution. |
| **5** | **Verification** | `04:31 - 05:12` | 41.0s | 3-lane validation suite substituting $(1, 2, 3)$ into all 3 original equations. Reconnects algebra to 3D geometry. |
| **6** | **Summary & Credits**| `05:12 - 05:42` | 29.6s | 3 Key architectural takeaways, M3 Linear Algebra course details, and AI production disclosures. |

**Total Runtime:** Exactly `05:42.076` (342.08 seconds), synchronized to the millisecond with authentic female voiceover audio.

---

## 📂 Project Architecture

```
Gaussian_Elimination_Animation/
├── main.py                     # Master build and rendering pipeline
├── ui_elements.py              # Reusable futuristic UI toolkit (Cards, HUD, MatrixGrid)
├── generate_storyboard_pdf.py  # Storyboard PDF generator using ReportLab
├── scenes/
│   ├── scene1_hook.py          # Scene 1: Real-world store hook & definitions
│   ├── scene2_basics.py        # Scene 2: 3D equations, augmented matrix, pivots
│   ├── scene3_geometry.py      # Scene 3: 3D plane intersection visualization
│   ├── scene4_solution.py      # Scene 4: Complete worked example & back-substitution
│   ├── scene5_verification.py  # Scene 5: Three-equation verification suite
│   └── scene6_summary.py       # Scene 6: Architectural takeaways & credits
├── assets/
│   ├── backgrounds/            # Grid textures & assets
│   ├── fonts/                  # Monospace & sans typography
│   └── music/                  # Audio tracks & sound design
├── narration/
│   ├── narration_script.md     # Full synchronized narration script with timestamps
│   └── generated_audio/
│       ├── voiceover.m4a       # Master voiceover audio (05:42.08)
│       └── voiceover.mp3       # Compatible MP3 stream
├── subtitles/
│   └── subtitles.srt           # 60 timed subtitle entries matching video narration
├── storyboard.pdf              # Publication-ready multi-page storyboard document
├── references.md               # Complete academic textbook citations & software licenses
├── requirements.txt            # Python dependencies
└── final_video.mp4             # High-definition 1080p 30fps assembled MP4 video
```

---

## 🛠️ Installation & Setup (macOS)

### Prerequisites
- Python 3.10+
- FFmpeg (bundled or system installed)

### 1. Clone & Enter Directory
```bash
git clone <repository-url>
cd mathsvd/Gaussian_Elimination_Animation
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run & Render

### Render the Entire Video (Full Pipeline)
To automatically render all 6 scenes at **1920×1080 (30 FPS)**, concatenate them, multiplex the audio voiceover, and output `final_video.mp4`:
```bash
python3 main.py
```

### Render Individual Scenes
You can render any individual scene for rapid testing or evaluation:
```bash
# Render Scene 1 (The Hook)
manim -r 1920,1080 --fps 30 scenes/scene1_hook.py Scene1Hook

# Render Scene 2 (The Basics)
manim -r 1920,1080 --fps 30 scenes/scene2_basics.py Scene2Basics

# Render Scene 3 (3D Geometry)
manim -r 1920,1080 --fps 30 scenes/scene3_geometry.py Scene3Geometry

# Render Scene 4 (Worked Solution)
manim -r 1920,1080 --fps 30 scenes/scene4_solution.py Scene4Solution

# Render Scene 5 (Verification Suite)
manim -r 1920,1080 --fps 30 scenes/scene5_verification.py Scene5Verification

# Render Scene 6 (Summary & Credits)
manim -r 1920,1080 --fps 30 scenes/scene6_summary.py Scene6Summary
```

### Regenerate Storyboard PDF
```bash
python3 generate_storyboard_pdf.py
```

---

## 📋 Quality Control & Verification Checklist

- [x] **Correct Mathematics:** Step-by-step derivation verified independently ($x=1, y=2, z=3$).
- [x] **All 6 Scenes Rendered:** 100% successful rendering without dropped frames or errors.
- [x] **No Placeholder Narration:** Master human-like voiceover audio synchronized to the millisecond.
- [x] **Clean Visual Hierarchy:** No overlapping typography or matrix overcrowding.
- [x] **Video Specs:** Exactly 1920×1080, 16:9 widescreen, 30 FPS, H.264 / AAC.
- [x] **Duration Compliance:** 05:42.08 (strictly below the 7-minute ceiling).
- [x] **Subtitles:** Standard SRT file synchronized with all 60 narration entries.
- [x] **Academic Documentation:** References cited according to university standards.

---

## 📜 Academic Attribution & AI Disclosures

- **Academic Context:** Developed for college M3 Linear Algebra curriculum (Systems of Linear Equations, Matrix Theory, and Numerical Gaussian Elimination).
- **AI-Assisted Production:** Motion graphics choreography, timing alignment, and UI design were assisted by DeepMind AI agent tools.
- **Voice Narration:** Synthesized neural voiceover provided for educational accessibility.

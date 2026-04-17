#!/usr/bin/env python3
"""Random-dot snake animation SVG — no contribution data, pure random layout."""
import random, os

COLS     = 52
ROWS     = 7
CS       = 11    # cell size px
G        = 2     # gap px
S        = CS + G
PAD      = 8
SPEED    = 55    # ms per step
SL       = 5     # snake body length
FOOD_PCT = 0.42

W = PAD * 2 + COLS * S - G
H = PAD * 2 + ROWS * S - G

C_BG    = "#0d1117"
C_EMPTY = "#161b22"
C_FOOD  = "#26a641"
C_HEAD  = "#56d364"
C_BODY  = "#3fb950"

def ox(c): return PAD + c * S
def oy(r): return PAD + r * S

def boustrophedon():
    path = []
    for r in range(ROWS):
        cs = range(COLS) if r % 2 == 0 else range(COLS - 1, -1, -1)
        for c in cs:
            path.append((r, c))
    return path

def build_animate(i, N, is_food):
    eps = 1e-5
    t0 = round(i / N, 6)
    t1 = round(min((i + 1) / N, 1 - eps), 6)
    t2 = round(min((i + SL) / N, 1 - eps), 6)

    kts, vals = [], []

    base = C_FOOD if is_food else C_EMPTY

    if t0 > 0:
        kts += [0, t0];  vals += [base, C_HEAD]
    else:
        kts += [0];      vals += [C_HEAD]

    if t1 > t0:
        kts.append(t1);  vals.append(C_BODY)

    if t2 > t1:
        kts.append(t2);  vals.append(C_EMPTY)

    kts.append(1);       vals.append(C_EMPTY)

    return ";".join(str(k) for k in kts), ";".join(vals)

def gen_svg():
    path = boustrophedon()
    N    = len(path)
    dur  = round(N * SPEED / 1000, 3)

    food = {(r, c) for r, c in path if random.random() < FOOD_PCT}
    pos  = {rc: i for i, rc in enumerate(path)}

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<rect width="{W}" height="{H}" fill="{C_BG}" rx="6"/>',
    ]

    for r in range(ROWS):
        for c in range(COLS):
            x, y    = ox(c), oy(r)
            is_food = (r, c) in food
            i       = pos[(r, c)]
            base    = C_FOOD if is_food else C_EMPTY
            kt, vs  = build_animate(i, N, is_food)
            lines.append(
                f'<rect x="{x}" y="{y}" width="{CS}" height="{CS}" rx="2" fill="{base}">'
                f'<animate attributeName="fill" dur="{dur}s" repeatCount="indefinite" '
                f'calcMode="discrete" keyTimes="{kt}" values="{vs}"/>'
                f'</rect>'
            )

    lines.append('</svg>')
    return '\n'.join(lines)

if __name__ == "__main__":
    os.makedirs("dist", exist_ok=True)
    svg = gen_svg()
    for name in ["github-contribution-grid-snake-dark.svg",
                 "github-contribution-grid-snake.svg"]:
        with open(f"dist/{name}", "w", encoding="utf-8") as f:
            f.write(svg)
    print(f"Done — {W}x{H}px | {len(svg)//1024}KB")

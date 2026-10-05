"""Generar banner personal: python3 scripts/banner/personalize.py."""
from pathlib import Path
from html import escape
ROOT = Path(__file__).resolve().parents[2]
for theme, bg, fg in [("dark", "#0b1628", "#e2e8f0"), ("light", "#f1f5f9", "#0f172a")]:
    rows = ["$ whoami", "Benjamin Aguilar", "Full Stack · Odoo & FastAPI · Estudiante de Ing. Informática", "Python / FastAPI / React / AWS / OpenAI", "Cloud Computing · Inteligencia Artificial · Ciberseguridad", "$ focus: IA · Seguridad · DevOps · Cloud", "aguilarb.tech · @Benjyyy16"]
    texts = "".join(f'<text x="55" y="{80+i*48}" font-size="{38 if i == 1 else 20}" fill="{fg if i not in (0,5) else '#0891b2'}">{escape(row)}</text>' for i,row in enumerate(rows))
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="430" viewBox="0 0 1180 430" role="img"><title>Benjamin Aguilar — Python, Odoo y automatización</title><rect width="1180" height="430" rx="24" fill="{bg}"/><rect x="24" y="24" width="1132" height="382" rx="16" fill="none" stroke="#0891b2"/><g font-family="monospace">{texts}</g></svg>'
    (ROOT / "assets" / f"banner-{theme}.svg").write_text(svg, encoding="utf-8")

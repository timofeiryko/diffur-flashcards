# -*- coding: utf-8 -*-
"""
Builder script for Differential Equations Flashcards Single-Page App (diffur-flashcards/index.html)
"""

import os
import json
import re

import cards_part1
import cards_part2
import cards_part3
import cards_part4
import cards_part5
import cards_part6

def build():
    parts_modules = [
        cards_part1,
        cards_part2,
        cards_part3,
        cards_part4,
        cards_part5,
        cards_part6
    ]

    PARTS = []
    SECTIONS = []
    CARDS = []

    card_counter = 1

    for mod in parts_modules:
        PARTS.append(mod.PART_INFO)
        for sec in mod.SECTIONS:
            SECTIONS.append(sec)
        for card in mod.CARDS:
            card_entry = {
                "n": card_counter,
                "s": card["s"],
                "p": card["p"],
                "q": card["q"],
                "a": card["a"],
                "f": card.get("f", False)
            }
            CARDS.append(card_entry)
            card_counter += 1

    print(f"Total Parts: {len(PARTS)}")
    print(f"Total Sections: {len(SECTIONS)}")
    print(f"Total Cards: {len(CARDS)}")

    data_json = json.dumps({
        "PARTS": PARTS,
        "SECTIONS": SECTIONS,
        "CARDS": CARDS
    }, ensure_ascii=False, indent=2)

    # Read base KaTeX fonts, CSS, and JS from physchem-flashcards/index.html
    physchem_path = os.path.join("..", "physchem-flashcards", "index.html")
    with open(physchem_path, "r", encoding="utf-8") as f:
        physchem_html = f.read()

    # Extract KaTeX font style (Style 0)
    styles = re.findall(r'<style.*?>.*?</style>', physchem_html, re.S)
    katex_font_style = styles[0] # contains base64 KaTeX fonts and core CSS

    # Extract KaTeX script 0 (katex min js) and script 1 (auto-render)
    scripts = re.findall(r'<script.*?>.*?</script>', physchem_html, re.S)
    katex_core_js = scripts[0]
    katex_autorender_js = scripts[1]

    # Custom App CSS
    app_css = """
<style>
:root {
  --bg: #0b1329;
  --bg-subtle: #152243;
  --surface: #152243;
  --surface-hover: #1e2f5b;
  --surface-active: #283e77;
  --border: #283e77;
  --border-subtle: #192a54;
  --ink: #f8fafc;
  --ink-secondary: #94a3b8;
  --ink-muted: #64748b;
  --primary: #38bdf8;
  --primary-hover: #0ea5e9;
  --primary-glow: rgba(56, 189, 248, 0.18);
  --success: #34d399;
  --success-bg: rgba(52, 211, 153, 0.15);
  --warning: #fbbf24;
  --warning-bg: rgba(251, 191, 36, 0.15);
  --danger: #f87171;
  --danger-bg: rgba(248, 113, 113, 0.15);
  --accent: #818cf8;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  --radius-xl: 24px;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 14px rgba(0,0,0,0.35);
  --shadow-lg: 0 10px 30px rgba(0,0,0,0.45);
  --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

:root[data-theme="light"] {
  --bg: #f8fafc;
  --bg-subtle: #edf2f7;
  --surface: #ffffff;
  --surface-hover: #f1f5f9;
  --surface-active: #e2e8f0;
  --border: #cbd5e1;
  --border-subtle: #e2e8f0;
  --ink: #0f172a;
  --ink-secondary: #475569;
  --ink-muted: #94a3b8;
  --primary: #0284c7;
  --primary-hover: #0369a1;
  --primary-glow: rgba(2, 132, 199, 0.1);
  --success: #059669;
  --success-bg: rgba(5, 150, 105, 0.1);
  --warning: #d97706;
  --warning-bg: rgba(217, 119, 6, 0.1);
  --danger: #dc2626;
  --danger-bg: rgba(220, 38, 38, 0.1);
  --accent: #6366f1;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 14px rgba(0,0,0,0.08);
  --shadow-lg: 0 10px 30px rgba(0,0,0,0.12);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-sans);
  background-color: var(--bg);
  color: var(--ink);
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
  -webkit-font-smoothing: antialiased;
  padding-bottom: env(safe-area-inset-bottom);
}

header {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  padding: 14px 20px;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: var(--shadow-sm);
  backdrop-filter: blur(12px);
}

.header-inner {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.logo-group {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.logo-badge {
  background: linear-gradient(135deg, #0284c7, #6366f1);
  color: #fff;
  font-weight: 800;
  font-size: 0.85rem;
  padding: 5px 10px;
  border-radius: var(--radius-sm);
  letter-spacing: 0.5px;
  box-shadow: 0 2px 8px rgba(99, 102, 241, 0.4);
}

.logo-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--ink);
}

.logo-sub {
  font-size: 0.75rem;
  color: var(--ink-secondary);
  display: block;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-icon {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  color: var(--ink-secondary);
  width: 38px;
  height: 38px;
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
  font-size: 1.1rem;
}

.btn-icon:hover {
  background: var(--surface-hover);
  color: var(--ink);
  border-color: var(--primary);
}

main {
  flex: 1;
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
  padding: 20px 16px 40px;
  display: flex;
  flex-direction: column;
}

/* Home / Setup Screen */
#view-menu {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 12px;
}

.stat-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 14px;
  text-align: center;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.stat-val {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--primary);
  line-height: 1.1;
  margin-bottom: 4px;
}

.stat-card.known .stat-val { color: var(--success); }
.stat-card.doubt .stat-val { color: var(--warning); }
.stat-card.fail .stat-val { color: var(--danger); }

.stat-lbl {
  font-size: 0.75rem;
  color: var(--ink-secondary);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Filter presets bar */
.filter-presets {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  padding-bottom: 6px;
  scrollbar-width: thin;
}

.chip-btn {
  background: var(--surface);
  border: 1px solid var(--border);
  color: var(--ink-secondary);
  padding: 8px 14px;
  border-radius: 999px;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: var(--transition);
}

.chip-btn:hover {
  background: var(--surface-hover);
  color: var(--ink);
  border-color: var(--ink-muted);
}

.chip-btn.active {
  background: var(--primary-glow);
  color: var(--primary);
  border-color: var(--primary);
}

/* Search bar */
.search-wrapper {
  position: relative;
}

.search-input {
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: 12px 16px 12px 42px;
  font-size: 0.95rem;
  color: var(--ink);
  outline: none;
  transition: var(--transition);
}

.search-input:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px var(--primary-glow);
}

.search-icon {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--ink-muted);
  font-size: 1.1rem;
  pointer-events: none;
}

/* Tree view of Parts & Sections */
.deck-tree {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.part-block {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
  transition: var(--transition);
}

.part-header {
  padding: 16px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  cursor: pointer;
  user-select: none;
  border-left: 4px solid var(--part-color, var(--primary));
}

.part-title-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.part-title {
  font-size: 1rem;
  font-weight: 700;
  color: var(--ink);
}

.part-count {
  font-size: 0.8rem;
  color: var(--ink-secondary);
  background: var(--bg-subtle);
  padding: 2px 8px;
  border-radius: 999px;
  font-weight: 600;
}

.section-list {
  border-top: 1px solid var(--border-subtle);
  background: var(--bg);
  display: flex;
  flex-direction: column;
}

.section-item {
  padding: 12px 18px 12px 34px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-subtle);
  cursor: pointer;
  transition: var(--transition);
}

.section-item:last-child {
  border-bottom: none;
}

.section-item:hover {
  background: var(--surface-hover);
}

.section-item-left {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.custom-checkbox {
  width: 18px;
  height: 18px;
  border-radius: 4px;
  border: 2px solid var(--ink-muted);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
}

.custom-checkbox.checked {
  background: var(--primary);
  border-color: var(--primary);
  color: #fff;
}

.section-name {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--ink);
}

.section-badge {
  font-size: 0.75rem;
  color: var(--ink-secondary);
  background: var(--surface);
  padding: 2px 8px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
}

/* Start Practice Bar (Sticky Bottom) */
.start-bar {
  position: sticky;
  bottom: 16px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  box-shadow: var(--shadow-lg);
  margin-top: 20px;
  z-index: 90;
  backdrop-filter: blur(16px);
}

.start-info {
  display: flex;
  flex-direction: column;
}

.start-count {
  font-size: 1.1rem;
  font-weight: 800;
  color: var(--ink);
}

.start-sub {
  font-size: 0.8rem;
  color: var(--ink-secondary);
}

.btn-start {
  background: linear-gradient(135deg, #0284c7, #6366f1);
  color: #fff;
  border: none;
  padding: 12px 28px;
  border-radius: var(--radius-md);
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: var(--transition);
  box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
}

.btn-start:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
}

.btn-start:disabled {
  opacity: 0.5;
  transform: none;
  cursor: not-allowed;
}

/* Flashcard Active Mode */
#view-quiz {
  display: none;
  flex-direction: column;
  flex: 1;
  gap: 16px;
  max-width: 800px;
  margin: 0 auto;
  width: 100%;
}

.quiz-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.quiz-progress-wrap {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.progress-labels {
  display: flex;
  justify-content: space-between;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--ink-secondary);
}

.progress-bar-bg {
  height: 8px;
  background: var(--bg-subtle);
  border-radius: 999px;
  overflow: hidden;
  border: 1px solid var(--border-subtle);
}

.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #0284c7, #818cf8);
  width: 0%;
  border-radius: 999px;
  transition: width 0.3s ease;
}

.card-container {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: 28px 24px;
  box-shadow: var(--shadow-md);
  display: flex;
  flex-direction: column;
  gap: 20px;
  min-height: 380px;
  position: relative;
  transition: var(--transition);
}

.card-header-tag {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  border-bottom: 1px solid var(--border-subtle);
  padding-bottom: 12px;
}

.card-sec-badge {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--primary);
  background: var(--primary-glow);
  padding: 4px 10px;
  border-radius: var(--radius-sm);
  display: inline-block;
  max-width: 80%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-num-badge {
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--ink-muted);
  font-family: var(--font-mono);
}

.card-question {
  font-size: 1.22rem;
  font-weight: 600;
  line-height: 1.5;
  color: var(--ink);
  padding: 8px 0;
}

.btn-flip {
  background: var(--bg-subtle);
  border: 2px dashed var(--border);
  color: var(--primary);
  padding: 16px;
  border-radius: var(--radius-md);
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  transition: var(--transition);
  text-align: center;
  margin-top: auto;
}

.btn-flip:hover {
  background: var(--surface-hover);
  border-color: var(--primary);
}

.card-answer-wrap {
  display: none;
  flex-direction: column;
  gap: 16px;
  border-top: 1px solid var(--border-subtle);
  padding-top: 18px;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

.card-answer-body {
  font-size: 1.02rem;
  line-height: 1.65;
  color: var(--ink);
}

.card-answer-body p {
  margin-bottom: 12px;
}

.card-answer-body p:last-child {
  margin-bottom: 0;
}

.card-answer-body ol, .card-answer-body ul {
  padding-left: 22px;
  margin-bottom: 12px;
}

.card-answer-body li {
  margin-bottom: 6px;
}

.card-answer-body b {
  color: var(--primary);
}

/* Rating Controls */
.rate-group {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-top: 10px;
}

.btn-rate {
  border: none;
  padding: 14px 10px;
  border-radius: var(--radius-md);
  font-size: 0.95rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  transition: var(--transition);
}

.btn-rate span.shortcut {
  font-size: 0.75rem;
  font-weight: 500;
  opacity: 0.8;
  font-family: var(--font-mono);
}

.btn-rate.fail {
  background: var(--danger-bg);
  color: var(--danger);
  border: 1px solid rgba(248, 113, 113, 0.3);
}

.btn-rate.fail:hover {
  background: var(--danger);
  color: #fff;
  transform: translateY(-2px);
}

.btn-rate.doubt {
  background: var(--warning-bg);
  color: var(--warning);
  border: 1px solid rgba(251, 191, 36, 0.3);
}

.btn-rate.doubt:hover {
  background: var(--warning);
  color: #000;
  transform: translateY(-2px);
}

.btn-rate.known {
  background: var(--success-bg);
  color: var(--success);
  border: 1px solid rgba(52, 211, 153, 0.3);
}

.btn-rate.known:hover {
  background: var(--success);
  color: #fff;
  transform: translateY(-2px);
}

/* Finish Summary Screen */
#view-summary {
  display: none;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 24px;
  max-width: 600px;
  margin: 40px auto;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: 36px 24px;
  box-shadow: var(--shadow-lg);
}

.summary-trophy {
  font-size: 3.5rem;
  line-height: 1;
}

.summary-title {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--ink);
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  width: 100%;
}

.summary-card {
  padding: 16px 10px;
  border-radius: var(--radius-md);
  border: 1px solid var(--border);
  background: var(--bg);
}

.summary-val {
  font-size: 1.5rem;
  font-weight: 800;
}

.summary-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 100%;
}

.btn-full {
  width: 100%;
  padding: 14px;
  border-radius: var(--radius-md);
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: var(--transition);
}

.btn-primary {
  background: linear-gradient(135deg, #0284c7, #6366f1);
  color: #fff;
  box-shadow: 0 4px 14px rgba(99, 102, 241, 0.4);
}

.btn-secondary {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  color: var(--ink);
}

.btn-secondary:hover {
  background: var(--surface-hover);
}

/* Modal for Help / Settings */
.modal-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(4px);
  z-index: 1000;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  max-width: 550px;
  width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  box-shadow: var(--shadow-lg);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-title {
  font-size: 1.25rem;
  font-weight: 700;
}

.modal-body {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--ink-secondary);
}

.modal-body h4 {
  color: var(--ink);
  margin: 14px 0 6px;
}

.modal-body ul {
  padding-left: 20px;
  margin-bottom: 10px;
}

.modal-body kbd {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 2px 6px;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--ink);
}

/* Math styling */
.katex-display {
  margin: 0.8em 0 !important;
  overflow-x: auto;
  overflow-y: hidden;
  padding: 4px 0;
}

@media (max-width: 600px) {
  .header-inner { padding: 0 4px; }
  .card-container { padding: 20px 16px; min-height: 320px; }
  .card-question { font-size: 1.1rem; }
  .rate-group { grid-template-columns: 1fr; }
  .start-bar { border-radius: var(--radius-lg); padding: 12px 16px; }
  .stats-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>
"""

    html_template = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Флеш-карточки: Дифференциальные уравнения (Письмак МФТИ)</title>
  <meta name="description" content="Интерактивный тренажер и флеш-карточки по ДУ для подготовки к письменному экзамену МФТИ. Полный разбор методов, интегралов, фазовых портретов, параметров и блиц-задач.">
  <meta name="theme-color" content="#0b1329">
  __KATEX_FONTS__
  __APP_CSS__
</head>
<body>

<header>
  <div class="header-inner">
    <div class="logo-group" onclick="App.showMenu()">
      <div class="logo-badge">МФТИ · ДУ</div>
      <div>
        <div class="logo-title">Диффуры: Письмак</div>
        <span class="logo-sub">Интерактивный курс-тренажер</span>
      </div>
    </div>
    <div class="header-actions">
      <button class="btn-icon" id="btn-theme" title="Сменить тему" onclick="App.toggleTheme()">🌓</button>
      <button class="btn-icon" id="btn-help" title="Помощь и горячие клавиши" onclick="App.showHelp()">❓</button>
      <button class="btn-icon" id="btn-reset" title="Сбросить прогресс" onclick="App.resetProgress()">🔄</button>
    </div>
  </div>
</header>

<main>
  <!-- Screen 1: Deck / Menu -->
  <section id="view-menu">
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-val" id="stat-total">0</div>
        <div class="stat-lbl">Всего карточек</div>
      </div>
      <div class="stat-card known">
        <div class="stat-val" id="stat-known">0</div>
        <div class="stat-lbl">Выучено</div>
      </div>
      <div class="stat-card doubt">
        <div class="stat-val" id="stat-doubt">0</div>
        <div class="stat-lbl">Сомневался</div>
      </div>
      <div class="stat-card fail">
        <div class="stat-val" id="stat-fail">0</div>
        <div class="stat-lbl">В ошибках</div>
      </div>
    </div>

    <!-- Quick Presets -->
    <div class="filter-presets">
      <button class="chip-btn active" onclick="App.applyPreset('all', this)">🚀 Все карточки</button>
      <button class="chip-btn" onclick="App.applyPreset('trio', this)">⭐ Базовое Трио (Экзамен 18-24б)</button>
      <button class="chip-btn" onclick="App.applyPreset('integrals', this)">📐 Интегралы и замены</button>
      <button class="chip-btn" onclick="App.applyPreset('odes', this)">⚙️ ОДУ 1-2 порядков и Клеро</button>
      <button class="chip-btn" onclick="App.applyPreset('pdes', this)">🌊 УрЧП и первые интегралы</button>
      <button class="chip-btn" onclick="App.applyPreset('theor', this)">📚 Теорминимум и теоремы</button>
      <button class="chip-btn" onclick="App.applyPreset('blitz', this)">⚡ Блиц в уме (15 сек)</button>
      <button class="chip-btn" onclick="App.applyPreset('errors', this)">🚨 Копилка ошибок</button>
    </div>

    <!-- Search Bar -->
    <div class="search-wrapper">
      <span class="search-icon">🔍</span>
      <input type="text" class="search-input" id="search-input" placeholder="Поиск по темам, формулам или методам (напр. вронскиан, якоби, клеро, резонанс)..." oninput="App.onSearch(this.value)">
    </div>

    <!-- Options bar -->
    <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.85rem; color:var(--ink-secondary);">
      <div style="display:flex; gap:14px; align-items:center;">
        <label style="cursor:pointer; display:flex; align-items:center; gap:6px;">
          <input type="checkbox" id="opt-shuffle"> 🔀 Вразброс (Shuffle)
        </label>
      </div>
      <div style="display:flex; gap:10px;">
        <button class="chip-btn" style="padding:4px 10px; font-size:0.75rem;" onclick="App.selectAllSections(true)">Выбрать все</button>
        <button class="chip-btn" style="padding:4px 10px; font-size:0.75rem;" onclick="App.selectAllSections(false)">Снять все</button>
      </div>
    </div>

    <!-- Tree deck -->
    <div class="deck-tree" id="deck-tree"></div>

    <!-- Bottom Action Bar -->
    <div class="start-bar">
      <div class="start-info">
        <div class="start-count" id="selected-card-count">0 карточек</div>
        <div class="start-sub" id="selected-sec-count">0 разделов выбрано</div>
      </div>
      <button class="btn-start" id="btn-start" onclick="App.startSession()">
        <span>Начать тренировку</span> ➔
      </button>
    </div>
  </section>

  <!-- Screen 2: Active Quiz / Flashcard -->
  <section id="view-quiz">
    <div class="quiz-topbar">
      <button class="btn-icon" onclick="App.showMenu()" title="Вернуться к меню">✕</button>
      <div class="quiz-progress-wrap">
        <div class="progress-labels">
          <span id="quiz-part-name">Часть I</span>
          <span id="quiz-counter">1 / 100</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="quiz-progress-fill"></div>
        </div>
      </div>
    </div>

    <div class="card-container" id="current-card">
      <div class="card-header-tag">
        <span class="card-sec-badge" id="card-sec-title">Раздел 1</span>
        <span class="card-num-badge" id="card-index-badge">#1</span>
      </div>

      <div class="card-question" id="card-q">...</div>

      <button class="btn-flip" id="btn-flip" onclick="App.revealAnswer()">
        🔍 Показать ответ и объяснение <span style="opacity:0.7; font-size:0.85rem;">(Пробел)</span>
      </button>

      <div class="card-answer-wrap" id="card-answer-wrap">
        <div class="card-answer-body" id="card-a">...</div>
        
        <div class="rate-group">
          <button class="btn-rate fail" onclick="App.rateCard('f')">
            <span>❌ Не знал</span>
            <span class="shortcut">Клавиша 1</span>
          </button>
          <button class="btn-rate doubt" onclick="App.rateCard('d')">
            <span>🤔 Сомневался</span>
            <span class="shortcut">Клавиша 2</span>
          </button>
          <button class="btn-rate known" onclick="App.rateCard('k')">
            <span>✅ Знал отлично</span>
            <span class="shortcut">Клавиша 3</span>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Screen 3: Summary -->
  <section id="view-summary">
    <div class="summary-trophy">🏆</div>
    <div class="summary-title">Тренировка завершена!</div>
    <p style="color:var(--ink-secondary); font-size:0.95rem;">Отличный шаг к уверенным 18-24 первичным баллам на экзамене!</p>

    <div class="summary-grid">
      <div class="summary-card">
        <div class="summary-val" style="color:var(--success);" id="sum-known">0</div>
        <div class="stat-lbl">Знал</div>
      </div>
      <div class="summary-card">
        <div class="summary-val" style="color:var(--warning);" id="sum-doubt">0</div>
        <div class="stat-lbl">Сомневался</div>
      </div>
      <div class="summary-card">
        <div class="summary-val" style="color:var(--danger);" id="sum-fail">0</div>
        <div class="stat-lbl">Повторить</div>
      </div>
    </div>

    <div class="summary-actions">
      <button class="btn-full btn-primary" id="btn-repeat-errors" onclick="App.repeatErrors()">🔁 Прогнать ошибки этого захода</button>
      <button class="btn-full btn-secondary" onclick="App.showMenu()">📋 Вернуться в меню</button>
    </div>
  </section>
</main>

<!-- Modal: Help & Keyboard shortcuts -->
<div class="modal-overlay" id="modal-help" onclick="if(event.target===this) App.closeHelp()">
  <div class="modal-card">
    <div class="modal-header">
      <div class="modal-title">Горячие клавиши и подсказки</div>
      <button class="btn-icon" onclick="App.closeHelp()">✕</button>
    </div>
    <div class="modal-body">
      <h4>Управление с клавиатуры:</h4>
      <ul>
        <li><kbd>Пробел</kbd> или <kbd>Enter</kbd> — Перевернуть карточку / Показать решение.</li>
        <li><kbd>1</kbd> — Отметить «Не знал» (отправить в копилку ошибок).</li>
        <li><kbd>2</kbd> — Отметить «Сомневался».</li>
        <li><kbd>3</kbd> — Отметить «Знал отлично».</li>
        <li><kbd>←</kbd> / <kbd>→</kbd> — Переход между карточками.</li>
        <li><kbd>Esc</kbd> — Выйти в главное меню.</li>
      </ul>

      <h4>Методология подготовки:</h4>
      <p>Каждая карточка разбита на 4 структурных блока: <b>💡 Суть и откуда берётся</b>, <b>📐 Формула / Метод</b>, <b>⚠️ Ловушка на письмаке</b> и <b>🎯 Устный самоконтроль</b>. Это помогает сформировать прочные нейронные связи без зубрежки формул вслепую.</p>

      <h4>Прогресс и офлайн-режим:</h4>
      <p>Ваш прогресс автоматически сохраняется в браузере. Приложение полностью автономно и работает без подключения к интернету!</p>
    </div>
  </div>
</div>

__KATEX_CORE_JS__
__KATEX_AUTORENDER_JS__

<script>
const DATA = __DATA_JSON__;

const App = {
  selectedSections: new Set(),
  activeDeck: [],
  currentIndex: 0,
  currentCard: null,
  isAnswerRevealed: false,
  sessionStats: { k: 0, d: 0, f: 0, errorCards: [] },
  searchQuery: "",

  STORAGE_KEY: "du_flashcards_v1",

  init() {
    this.loadState();
    this.renderTree();
    this.updateStats();
    this.updateSelectionCounts();
    this.initKeyboard();

    // Theme initialization
    const savedTheme = localStorage.getItem("du_theme") || "dark";
    if (savedTheme === "light") {
      document.documentElement.setAttribute("data-theme", "light");
    }
  },

  getState() {
    try {
      return JSON.parse(localStorage.getItem(this.STORAGE_KEY)) || { ratings: {}, errorPool: [] };
    } catch(e) {
      return { ratings: {}, errorPool: [] };
    }
  },

  saveState(state) {
    try {
      localStorage.setItem(this.STORAGE_KEY, JSON.stringify(state));
    } catch(e) {}
  },

  loadState() {
    // Select all sections by default if first time
    if (this.selectedSections.size === 0) {
      DATA.SECTIONS.forEach(s => this.selectedSections.add(s.n));
    }
  },

  toggleTheme() {
    const isLight = document.documentElement.getAttribute("data-theme") === "light";
    if (isLight) {
      document.documentElement.removeAttribute("data-theme");
      localStorage.setItem("du_theme", "dark");
    } else {
      document.documentElement.setAttribute("data-theme", "light");
      localStorage.setItem("du_theme", "light");
    }
  },

  showHelp() {
    document.getElementById("modal-help").style.display = "flex";
  },

  closeHelp() {
    document.getElementById("modal-help").style.display = "none";
  },

  resetProgress() {
    if (confirm("Вы уверены, что хотите сбросить весь прогресс изучения и очистить копилку ошибок?")) {
      localStorage.removeItem(this.STORAGE_KEY);
      this.updateStats();
      this.renderTree();
      alert("Прогресс успешно сброшен!");
    }
  },

  renderTree() {
    const container = document.getElementById("deck-tree");
    container.innerHTML = "";
    const state = this.getState();

    DATA.PARTS.forEach(part => {
      const partSections = DATA.SECTIONS.filter(s => s.p === part.i);
      const partCards = DATA.CARDS.filter(c => c.p === part.i);

      const partBlock = document.createElement("div");
      partBlock.className = "part-block";
      partBlock.style.setProperty("--part-color", part.color);

      // Part header
      const header = document.createElement("div");
      header.className = "part-header";

      const titleWrap = document.createElement("div");
      titleWrap.className = "part-title-wrap";

      const title = document.createElement("div");
      title.className = "part-title";
      title.textContent = part.name;

      const count = document.createElement("span");
      count.className = "part-count";
      count.textContent = `${partCards.length} карт`;

      titleWrap.appendChild(title);
      titleWrap.appendChild(count);

      // Part select-all toggle button
      const togglePartBtn = document.createElement("button");
      togglePartBtn.className = "chip-btn";
      togglePartBtn.style.padding = "4px 10px";
      togglePartBtn.style.fontSize = "0.75rem";
      
      const allPartSecsSelected = partSections.every(s => this.selectedSections.has(s.n));
      togglePartBtn.textContent = allPartSecsSelected ? "Снять часть" : "Выбрать часть";
      togglePartBtn.onclick = (e) => {
        e.stopPropagation();
        if (allPartSecsSelected) {
          partSections.forEach(s => this.selectedSections.delete(s.n));
        } else {
          partSections.forEach(s => this.selectedSections.add(s.n));
        }
        this.renderTree();
        this.updateSelectionCounts();
      };

      header.appendChild(titleWrap);
      header.appendChild(togglePartBtn);

      // Section list
      const secList = document.createElement("div");
      secList.className = "section-list";

      partSections.forEach(sec => {
        const secCards = DATA.CARDS.filter(c => c.s === sec.n);
        const isSelected = this.selectedSections.has(sec.n);

        const secItem = document.createElement("div");
        secItem.className = "section-item";

        // Filter by search query if any
        if (this.searchQuery) {
          const match = sec.t.toLowerCase().includes(this.searchQuery) ||
                        secCards.some(c => c.q.toLowerCase().includes(this.searchQuery) || c.a.toLowerCase().includes(this.searchQuery));
          if (!match) {
            secItem.style.display = "none";
          }
        }

        const left = document.createElement("div");
        left.className = "section-item-left";

        const cb = document.createElement("div");
        cb.className = "custom-checkbox" + (isSelected ? " checked" : "");
        cb.innerHTML = isSelected ? "✓" : "";

        const name = document.createElement("div");
        name.className = "section-name";
        name.textContent = sec.t;

        left.appendChild(cb);
        left.appendChild(name);

        const badge = document.createElement("span");
        badge.className = "section-badge";
        badge.textContent = `${secCards.length} карт`;

        secItem.appendChild(left);
        secItem.appendChild(badge);

        secItem.onclick = () => {
          if (this.selectedSections.has(sec.n)) {
            this.selectedSections.delete(sec.n);
          } else {
            this.selectedSections.add(sec.n);
          }
          this.renderTree();
          this.updateSelectionCounts();
        };

        secList.appendChild(secItem);
      });

      partBlock.appendChild(header);
      partBlock.appendChild(secList);
      container.appendChild(partBlock);
    });
  },

  selectAllSections(selectAll) {
    if (selectAll) {
      DATA.SECTIONS.forEach(s => this.selectedSections.add(s.n));
    } else {
      this.selectedSections.clear();
    }
    this.renderTree();
    this.updateSelectionCounts();
  },

  applyPreset(preset, btn) {
    document.querySelectorAll(".filter-presets .chip-btn").forEach(b => b.classList.remove("active"));
    if (btn) btn.classList.add("active");

    this.selectedSections.clear();

    if (preset === "all") {
      DATA.SECTIONS.forEach(s => this.selectedSections.add(s.n));
    } else if (preset === "trio") {
      // Part 1: Sections 5, 6, 7, 8, 9, 10
      [5, 6, 7, 8, 9, 10].forEach(n => this.selectedSections.add(n));
    } else if (preset === "integrals") {
      // Part 0: Sections 1, 2, 3, 4
      [1, 2, 3, 4].forEach(n => this.selectedSections.add(n));
    } else if (preset === "odes") {
      // Part 2: Sections 11, 12, 13, 14, 15, 16, 17
      [11, 12, 13, 14, 15, 16, 17].forEach(n => this.selectedSections.add(n));
    } else if (preset === "pdes") {
      // Part 3: Sections 18, 19, 20
      [18, 19, 20].forEach(n => this.selectedSections.add(n));
    } else if (preset === "theor") {
      // Part 4: Sections 21, 22, 23, 24, 25, 26, 27
      [21, 22, 23, 24, 25, 26, 27].forEach(n => this.selectedSections.add(n));
    } else if (preset === "blitz") {
      // Part 5: Sections 28, 29, 30, 31
      [28, 29, 30, 31].forEach(n => this.selectedSections.add(n));
    } else if (preset === "errors") {
      const state = this.getState();
      const errSet = new Set(state.errorPool || []);
      const errSecs = new Set();
      DATA.CARDS.forEach(c => {
        if (errSet.has(c.n)) errSecs.add(c.s);
      });
      errSecs.forEach(n => this.selectedSections.add(n));
    }

    this.renderTree();
    this.updateSelectionCounts();
  },

  onSearch(val) {
    this.searchQuery = (val || "").trim().toLowerCase();
    this.renderTree();
  },

  updateSelectionCounts() {
    const selectedSecs = Array.from(this.selectedSections);
    const selectedCards = DATA.CARDS.filter(c => this.selectedSections.has(c.s));

    document.getElementById("selected-card-count").textContent = `${selectedCards.length} карт`;
    document.getElementById("selected-sec-count").textContent = `${selectedSecs.length} разделов выбрано`;
    document.getElementById("btn-start").disabled = (selectedCards.length === 0);
  },

  updateStats() {
    const state = this.getState();
    const ratings = state.ratings || {};
    const errorPool = state.errorPool || [];

    let known = 0, doubt = 0, fail = errorPool.length;

    Object.values(ratings).forEach(r => {
      if (r === "k") known++;
      else if (r === "d") doubt++;
    });

    document.getElementById("stat-total").textContent = DATA.CARDS.length;
    document.getElementById("stat-known").textContent = known;
    document.getElementById("stat-doubt").textContent = doubt;
    document.getElementById("stat-fail").textContent = fail;
  },

  startSession(customCards = null) {
    let cards = [];
    if (customCards) {
      cards = customCards;
    } else {
      cards = DATA.CARDS.filter(c => this.selectedSections.has(c.s));
    }

    if (cards.length === 0) {
      alert("Выберите хотя бы один раздел с карточками!");
      return;
    }

    if (document.getElementById("opt-shuffle").checked) {
      cards = [...cards].sort(() => Math.random() - 0.5);
    }

    this.activeDeck = cards;
    this.currentIndex = 0;
    this.sessionStats = { k: 0, d: 0, f: 0, errorCards: [] };

    document.getElementById("view-menu").style.display = "none";
    document.getElementById("view-summary").style.display = "none";
    document.getElementById("view-quiz").style.display = "flex";

    this.renderCurrentCard();
  },

  showMenu() {
    document.getElementById("view-quiz").style.display = "none";
    document.getElementById("view-summary").style.display = "none";
    document.getElementById("view-menu").style.display = "flex";
    this.updateStats();
    this.renderTree();
  },

  renderCurrentCard() {
    if (this.currentIndex >= this.activeDeck.length) {
      this.showSummary();
      return;
    }

    this.currentCard = this.activeDeck[this.currentIndex];
    this.isAnswerRevealed = false;

    // Part & Section metadata
    const part = DATA.PARTS.find(p => p.i === this.currentCard.p);
    const sec = DATA.SECTIONS.find(s => s.n === this.currentCard.s);

    document.getElementById("quiz-part-name").textContent = part ? part.name.split(".")[0] : "";
    document.getElementById("quiz-counter").textContent = `${this.currentIndex + 1} / ${this.activeDeck.length}`;
    
    const progressPct = ((this.currentIndex) / this.activeDeck.length) * 100;
    document.getElementById("quiz-progress-fill").style.width = `${progressPct}%`;

    document.getElementById("card-sec-title").textContent = sec ? sec.t : "";
    document.getElementById("card-index-badge").textContent = `#${this.currentCard.n}`;

    document.getElementById("card-q").innerHTML = this.currentCard.q;
    document.getElementById("card-a").innerHTML = this.currentCard.a;

    document.getElementById("btn-flip").style.display = "block";
    document.getElementById("card-answer-wrap").style.display = "none";

    // Re-render KaTeX math
    this.renderMath();
  },

  revealAnswer() {
    this.isAnswerRevealed = true;
    document.getElementById("btn-flip").style.display = "none";
    document.getElementById("card-answer-wrap").style.display = "flex";
    this.renderMath();
  },

  rateCard(rating) {
    const cardId = this.currentCard.n;
    const state = this.getState();
    if (!state.ratings) state.ratings = {};
    if (!state.errorPool) state.errorPool = [];

    state.ratings[cardId] = rating;

    if (rating === "f" || rating === "d") {
      if (!state.errorPool.includes(cardId)) {
        state.errorPool.push(cardId);
      }
      this.sessionStats.errorCards.push(this.currentCard);
    } else if (rating === "k") {
      state.errorPool = state.errorPool.filter(id => id !== cardId);
    }

    this.saveState(state);

    if (rating === "k") this.sessionStats.k++;
    else if (rating === "d") this.sessionStats.d++;
    else if (rating === "f") this.sessionStats.f++;

    this.currentIndex++;
    this.renderCurrentCard();
  },

  showSummary() {
    document.getElementById("view-quiz").style.display = "none";
    document.getElementById("view-summary").style.display = "flex";

    document.getElementById("sum-known").textContent = this.sessionStats.k;
    document.getElementById("sum-doubt").textContent = this.sessionStats.d;
    document.getElementById("sum-fail").textContent = this.sessionStats.f;

    const btnRepeat = document.getElementById("btn-repeat-errors");
    btnRepeat.style.display = (this.sessionStats.errorCards.length > 0) ? "block" : "none";
    
    this.updateStats();
  },

  repeatErrors() {
    if (this.sessionStats.errorCards.length > 0) {
      this.startSession(this.sessionStats.errorCards);
    }
  },

  renderMath() {
    if (typeof renderMathInElement === "function") {
      renderMathInElement(document.getElementById("current-card"), {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false },
          { left: "\\\\(", right: "\\\\)", display: false },
          { left: "\\\\[", right: "\\\\]", display: true }
        ],
        throwOnError: false
      });
    }
  },

  initKeyboard() {
    window.addEventListener("keydown", (e) => {
      // Don't trigger shortcuts if typing in search input
      if (document.activeElement && document.activeElement.tagName === "INPUT") {
        return;
      }

      const isQuizOpen = document.getElementById("view-quiz").style.display === "flex";

      if (e.key === "Escape") {
        this.closeHelp();
        if (isQuizOpen) this.showMenu();
      }

      if (!isQuizOpen) return;

      if (e.code === "Space" || e.key === "Enter") {
        e.preventDefault();
        if (!this.isAnswerRevealed) {
          this.revealAnswer();
        }
      } else if (this.isAnswerRevealed) {
        if (e.key === "1") {
          this.rateCard("f");
        } else if (e.key === "2") {
          this.rateCard("d");
        } else if (e.key === "3") {
          this.rateCard("k");
        }
      }
    });
  }
};

window.addEventListener("DOMContentLoaded", () => {
  App.init();
});
</script>

</body>
</html>
"""

    html_content = html_template \
        .replace("__KATEX_FONTS__", katex_font_style) \
        .replace("__APP_CSS__", app_css) \
        .replace("__KATEX_CORE_JS__", katex_core_js) \
        .replace("__KATEX_AUTORENDER_JS__", katex_autorender_js) \
        .replace("__DATA_JSON__", data_json)

    output_path = os.path.join("index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Successfully generated {output_path} ({len(html_content)} bytes)")

if __name__ == "__main__":
    build()

# -*- coding: utf-8 -*-
"""
Lineer Cebir Vize Hazırlık Platformu - Master HTML Derleyici
Akışkan SPA Sayfa Geçişleri, Sabit Sol Kenar Çubuğu (Fixed Sidebar),
Aydınlık Mod & Koyu Gri (Dark Gray) Teması, Zarif Spotlight Kartlar,
Sıfır Emoji (Tamamen Modern SVG İkonlar).
Üniversite Lisans Dersi Notları Birebir Müfredat
"""
import os, sys, json
from data_theory import THEORY_CHAPTERS
from data_problems import SOLVED_PROBLEMS, REAL_EXAM_QUESTIONS
from data_cheatsheet import CHEATSHEET_CARDS
from data_quiz import QUIZ_QUESTIONS
from data_calculators import CALCULATOR_HTML

VIEWS_METADATA = [
    {
        "id": "giris",
        "title": "Vize Stratejisi & Sıfırdan Zirveye Yol Haritası",
        "short_title": "Giriş & Strateji",
        "badge": "Rehber",
        "category": "Müfredat Konuları"
    },
    {
        "id": "bolum1",
        "title": "Bölüm 1: Determinantlar",
        "short_title": "1. Determinantlar",
        "badge": "Hafta 1 & 11",
        "category": "Müfredat Konuları"
    },
    {
        "id": "bolum2",
        "title": "Bölüm 2: Cramer Kuralı ile Çözüm",
        "short_title": "2. Cramer ile Çözüm",
        "badge": "Hafta 1 & 11",
        "category": "Müfredat Konuları"
    },
    {
        "id": "bolum3",
        "title": "Bölüm 3: Matris Cebiri",
        "short_title": "3. Matris Cebiri",
        "badge": "Hafta 3 & 12",
        "category": "Müfredat Konuları"
    },
    {
        "id": "bolum4",
        "title": "Bölüm 4: Denk Matrisler & Rank",
        "short_title": "4. Denk Matrisler & Rank",
        "badge": "Hafta 5 & 12",
        "category": "Müfredat Konuları"
    },
    {
        "id": "bolum5",
        "title": "Bölüm 5: Lineer Denklem Sistemleri & Gauss",
        "short_title": "5. Gauss ile Çözüm",
        "badge": "Hafta 4 & 12",
        "category": "Müfredat Konuları"
    },
    {
        "id": "bolum6",
        "title": "Bonus Bölüm: Lineer Bağımlılık",
        "short_title": "Bonus: Lineer Bağımlılık",
        "badge": "Hafta 6",
        "category": "Müfredat Konuları"
    },
    {
        "id": "sorular",
        "title": "Geçen Yılın Çıkmış Vize Soruları & Soru Bankası",
        "short_title": "Çıkmış Vize Soruları",
        "badge": "6 Çıkmış Soru",
        "category": "Uygulama & Sınav"
    },
    {
        "id": "laboratuvar",
        "title": "Canlı İnteraktif Matris Laboratuvarı",
        "short_title": "Matris Laboratuvarı",
        "badge": "Hesaplayıcılar",
        "category": "Uygulama & Sınav"
    },
    {
        "id": "deneme",
        "title": "Vize Deneme Sınavı (10 Soru)",
        "short_title": "Vize Deneme Sınavı",
        "badge": "Simülasyon",
        "category": "Uygulama & Sınav"
    },
    {
        "id": "hapbilgi",
        "title": "15 Dakika Vize Hapı (Son Tekrar)",
        "short_title": "15 Dk Vize Hapı",
        "badge": "Hızlı Özet",
        "category": "Uygulama & Sınav"
    }
]

def make_bottom_nav(current_idx, views):
    """Her sayfa görünümünün altına akışkan önceki / sonraki bölüm geçiş butonları üretir."""
    prev_btn = ""
    next_btn = ""

    if current_idx > 0:
        prev_view = views[current_idx - 1]
        prev_btn = f"""
        <button onclick="switchView('{prev_view['id']}')" class="px-5 py-3 rounded-2xl bg-[var(--bg-card)] border border-[var(--border-color)] hover:border-indigo-500/50 flex items-center gap-3 transition group active:scale-95 shadow-sm text-left">
            <svg class="w-5 h-5 text-indigo-400 group-hover:-translate-x-1 transition shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
            <div>
                <span class="text-[10px] text-[var(--text-muted)] uppercase tracking-wider block font-bold">Önceki Bölüm</span>
                <span class="text-xs sm:text-sm font-bold text-[var(--text-primary)] group-hover:text-indigo-400 transition">{prev_view['short_title']}</span>
            </div>
        </button>
        """
    else:
        prev_btn = "<div></div>"

    if current_idx < len(views) - 1:
        next_view = views[current_idx + 1]
        next_btn = f"""
        <button onclick="switchView('{next_view['id']}')" class="px-5 py-3 rounded-2xl bg-gradient-to-r from-indigo-600 to-indigo-500 hover:from-indigo-500 hover:to-indigo-400 text-white flex items-center gap-3 shadow-lg shadow-indigo-600/25 transition group active:scale-95 text-right">
            <div>
                <span class="text-[10px] text-indigo-200 uppercase tracking-wider block font-bold">Sonraki Bölüm</span>
                <span class="text-xs sm:text-sm font-bold text-white">{next_view['short_title']}</span>
            </div>
            <svg class="w-5 h-5 text-white group-hover:translate-x-1 transition shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        </button>
        """
    else:
        next_btn = f"""
        <button onclick="switchView('giris')" class="px-5 py-3 rounded-2xl bg-gradient-to-r from-emerald-600 to-teal-500 hover:from-emerald-500 hover:to-teal-400 text-white flex items-center gap-3 shadow-lg shadow-emerald-600/25 transition group active:scale-95 text-right">
            <div>
                <span class="text-[10px] text-emerald-100 uppercase tracking-wider block font-bold">Başa Dön</span>
                <span class="text-xs sm:text-sm font-bold text-white">Giriş & Strateji</span>
            </div>
            <svg class="w-5 h-5 text-white shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
        </button>
        """

    return f"""
    <div class="view-footer-nav flex items-center justify-between gap-4 mt-14 pt-8 border-t border-[var(--border-color)] flex-wrap">
        {prev_btn}
        {next_btn}
    </div>
    """

def generate_index_html():
    print("Derleme Başlatılıyor: Sabit Kenar Çubuğu, Aydınlık/Koyu Gri Mod & Akışkan SPA Görünümleri...")

    # 0. Real Exam Questions HTML Assembly (Geçen Yılın Çıkmış Soruları)
    real_exam_html = ""
    for q in REAL_EXAM_QUESTIONS:
        steps_rendered = "".join([f"<li class='p-3.5 rounded-xl bg-[var(--bg-box)] border border-[var(--border-color)] text-[var(--text-secondary)] leading-relaxed'>{s}</li>" for s in q['steps']])
        real_exam_html += f"""
        <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-amber-500/30 shadow-xl space-y-5 relative overflow-hidden">
            <div class="flex items-start justify-between gap-3 flex-wrap relative z-10">
                <div class="space-y-1">
                    <div class="flex items-center gap-2 flex-wrap">
                        <span class="px-3 py-1 rounded-full bg-amber-500/20 text-amber-400 border border-amber-500/40 text-xs font-black font-mono tracking-wider uppercase">Çıkmış Sınav Sorusu {q['q_num']}</span>
                        <span class="px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 text-[11px] font-semibold">{q['badge']}</span>
                        <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 text-[11px] font-mono font-bold">{q['score']}</span>
                    </div>
                    <h3 class="text-lg sm:text-xl font-black text-[var(--text-primary)] tracking-tight pt-1">{q['title']}</h3>
                </div>
                <button onclick="toggleProblemSolution('{q['id']}')" id="btn-prob-{q['id']}" class="px-4 py-2 rounded-xl bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-500 hover:to-amber-400 text-white text-xs font-bold shadow-lg shadow-amber-600/25 transition flex items-center gap-2 active:scale-95 cursor-pointer">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                    Çözümü İncele
                </button>
            </div>

            <div class="p-4 rounded-xl bg-[var(--bg-box)] border border-[var(--border-color)] text-sm sm:text-base text-[var(--text-primary)] leading-relaxed">
                <span class="text-[11px] font-bold text-amber-400 uppercase tracking-widest block mb-1.5 flex items-center gap-1.5">
                    <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    Orijinal Sınav Kağıdındaki Soru:
                </span>
                {q['question']}
            </div>

            <div id="sol-{q['id']}" class="hidden space-y-4 pt-2 border-t border-[var(--border-color)]">
                <div class="p-4 rounded-xl bg-indigo-950/20 border border-indigo-500/30 text-xs sm:text-sm text-indigo-200 leading-relaxed space-y-1">
                    <div class="flex items-center gap-1.5 text-indigo-400 font-bold text-xs uppercase tracking-wider mb-1">
                        <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        Çocuğa Anlatır Gibi (Sıfırdan Mantık)
                    </div>
                    {q['kid_logic']}
                </div>

                <div class="space-y-2">
                    <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block flex items-center gap-1.5">
                        <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                        Adım Adım Profesyonel Çözüm:
                    </span>
                    <ol class="space-y-2 text-xs sm:text-sm list-decimal list-inside">
                        {steps_rendered}
                    </ol>
                </div>

                <div class="p-4 rounded-xl bg-rose-950/20 border border-rose-500/30 text-xs sm:text-sm text-rose-200 leading-relaxed flex items-start gap-2.5">
                    <svg class="w-5 h-5 text-rose-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                    <div>{q['exam_trap']}</div>
                </div>

                <div class="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold text-center text-sm sm:text-base">
                    Sınav Kağıdına Yazılacak Net Sonuç: $${q['result']}$$
                </div>
            </div>
        </div>
        """

    # 1. Solved Problems HTML Assembly
    problems_html = ""
    for p in SOLVED_PROBLEMS:
        steps_rendered = "".join([f"<li class='p-3.5 rounded-xl bg-[var(--bg-box)] border border-[var(--border-color)] text-[var(--text-secondary)] leading-relaxed'>{s}</li>" for s in p['steps']])
        problems_html += f"""
        <div class="glass-3d-card p-6 rounded-2xl border border-[var(--border-color)] shadow-lg space-y-4">
            <div class="flex items-start justify-between gap-3 flex-wrap">
                <div>
                    <div class="flex items-center gap-2 mb-1.5">
                        <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 text-[10px] font-bold tracking-wide uppercase font-mono">{p['category']}</span>
                        <span class="text-xs text-[var(--text-muted)] font-mono flex items-center gap-1">
                            <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                            {p['source']}
                        </span>
                    </div>
                    <h4 class="text-base sm:text-lg font-bold text-[var(--text-primary)] tracking-tight">{p['title']}</h4>
                </div>
                <button onclick="toggleProblemSolution('{p['id']}')" id="btn-prob-{p['id']}" class="px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-md shadow-indigo-600/30 transition flex items-center gap-1.5 active:scale-95">
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/></svg>
                    Çözümü Göster
                </button>
            </div>

            <div class="p-4 rounded-xl bg-[var(--bg-box)] border border-[var(--border-color)] text-sm text-[var(--text-primary)]">
                <span class="text-[10px] font-bold text-amber-400 uppercase tracking-widest block mb-1">Soru Metni:</span>
                {p['question']}
            </div>

            <div id="sol-{p['id']}" class="hidden space-y-3 pt-3 border-t border-[var(--border-color)]">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                    Adım Adım Detaylı Çözüm (Neden-Sonuç İlişkisiyle):
                </span>
                <ol class="space-y-2 text-xs sm:text-sm list-decimal list-inside">
                    {steps_rendered}
                </ol>
                <div class="p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 font-bold text-center">
                    Sonuç: $${p['result']}$$
                </div>
            </div>
        </div>
        """

    # 2. Cheatsheet HTML Assembly
    cheatsheet_html = ""
    for c in CHEATSHEET_CARDS:
        cheatsheet_html += f"""
        <div class="glass-3d-card p-6 rounded-2xl border border-{c['color']}-500/30 space-y-3 shadow-lg">
            <div class="flex items-center justify-between gap-2">
                <div class="flex items-center gap-2.5">
                    <div class="w-8 h-8 rounded-lg bg-{c['color']}-500/10 border border-{c['color']}-500/30 flex items-center justify-center">
                        {c['icon']}
                    </div>
                    <h4 class="font-bold text-[var(--text-primary)] text-sm sm:text-base">{c['title']}</h4>
                </div>
                <span class="px-2.5 py-0.5 rounded-full bg-{c['color']}-500/10 text-{c['color']}-400 border border-{c['color']}-500/30 text-[10px] font-bold tracking-wider uppercase font-mono">{c['tag']}</span>
            </div>
            <div class="p-3.5 rounded-xl bg-[var(--bg-box)] border border-[var(--border-color)] text-[var(--text-primary)] text-xs sm:text-sm">
                {c['rule']}
            </div>
            <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs leading-relaxed flex items-start gap-2">
                <svg class="w-4 h-4 text-amber-400 shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <span><strong>Sınav İpucu:</strong> {c['tip']}</span>
            </div>
        </div>
        """

    # 3. Assemble All 11 Independent Views
    all_views_html = ""

    # Views 0 to 6: Theory Chapters
    for i, ch in enumerate(THEORY_CHAPTERS):
        is_active = "active" if i == 0 else ""
        bottom_nav = make_bottom_nav(i, VIEWS_METADATA)
        all_views_html += f"""
        <!-- VIEW: {ch['id']} -->
        <div id="view-{ch['id']}" class="app-view {is_active}">
            <div class="flex items-center justify-between border-b border-[var(--border-color)] pb-4 mb-8 flex-wrap gap-3">
                <div class="flex items-center gap-3.5">
                    <div class="w-10 h-10 rounded-2xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center">
                        {ch['icon']}
                    </div>
                    <div>
                        <div class="flex items-center gap-2 mb-0.5">
                            <span class="px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 text-[10px] font-bold tracking-wider uppercase font-mono">{ch['badge']}</span>
                        </div>
                        <h2 class="text-xl sm:text-2xl font-black text-[var(--text-primary)] tracking-tight">{ch['title']}</h2>
                    </div>
                </div>
                <button onclick="toggleSectionProgress('{ch['id']}')" id="btn-prog-{ch['id']}" class="px-3.5 py-1.5 rounded-xl bg-[var(--bg-box)] hover:bg-[var(--bg-box-alt)] text-[var(--text-muted)] border border-[var(--border-color)] text-xs font-semibold flex items-center gap-1.5 transition active:scale-95 shadow-sm">
                    <span id="icon-prog-{ch['id']}">
                        <svg class="w-4 h-4 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    </span>
                    <span id="text-prog-{ch['id']}">Tamamlandı Olarak İşaretle</span>
                </button>
            </div>

            {ch['content']}

            {bottom_nav}
        </div>
        """

    # View 7: Solved Exam Problems
    idx_sorular = 7
    bottom_nav_sorular = make_bottom_nav(idx_sorular, VIEWS_METADATA)
    all_views_html += f"""
    <!-- VIEW: sorular -->
    <div id="view-sorular" class="app-view">
        <div class="flex items-center justify-between border-b border-[var(--border-color)] pb-4 mb-8 flex-wrap gap-3">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                </div>
                <div>
                    <h2 class="text-2xl font-black text-[var(--text-primary)]">Geçen Yılın Çıkmış Vize Soruları & Soru Bankası</h2>
                    <p class="text-xs text-[var(--text-muted)]">Orijinal Sınav Kağıdındaki 6 Soru + Hafta 11 & 12 Uygulama Arşivi</p>
                </div>
            </div>
            <div class="flex items-center gap-2">
                <span class="px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-mono font-bold">6 Orijinal Çıkmış Soru</span>
                <span class="px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-mono font-bold">13 Alıştırma Sorusu</span>
            </div>
        </div>

        <!-- BÖLÜM 1: GEÇEN YILIN GERÇEK ÇIKMIŞ VİZE SINAVI (BİREBİR 6 SORU) -->
        <div class="space-y-6 mb-12">
            <div class="p-6 rounded-2xl bg-gradient-to-r from-amber-500/10 via-indigo-500/5 to-transparent border border-amber-500/30">
                <div class="flex items-center gap-2 text-amber-400 font-bold text-sm uppercase tracking-wider mb-2">
                    <svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/></svg>
                    BÖLÜM 1: GEÇEN YILIN BİREBİR ÇIKMIŞ VİZE SINAVI (100 TAM PUANLIK 6 SORU)
                </div>
                <p class="text-sm text-[var(--text-secondary)] leading-relaxed">
                    Aşağıdaki 6 soru, doğrudan vize sınav kağıdındaki orijinal sorulardır. Her soruda <strong>çocuğa anlatır gibi sıfırdan mantık</strong>, adım adım matematiksel işlemler ve <strong>hocanın puan kırdığı sınav tuzakları</strong> eksiksiz açıklanmıştır.
                </p>
            </div>

            <div id="real-exam-container" class="space-y-6">
                {real_exam_html}
            </div>
        </div>

        <!-- BÖLÜM 2: DERS NOTLARINDAKİ DİĞER ALIŞTIRMALAR -->
        <div class="space-y-6 pt-8 border-t border-[var(--border-color)]">
            <div class="flex items-center justify-between gap-3 flex-wrap">
                <div>
                    <h3 class="text-xl font-bold text-[var(--text-primary)]">Bölüm 2: Hafta 11 & 12 Uygulama Dersi Soru Arşivi</h3>
                    <p class="text-xs text-[var(--text-muted)]">PDF'lerdeki Diğer Tüm Çözümlü Alıştırmalar ve Konu Pekiştirme Soruları</p>
                </div>
            </div>
            <div id="problems-container" class="space-y-4">
                {problems_html}
            </div>
        </div>

        {bottom_nav_sorular}
    </div>
    """

    # View 8: Interactive Calculators Laboratory
    idx_lab = 8
    bottom_nav_lab = make_bottom_nav(idx_lab, VIEWS_METADATA)
    all_views_html += f"""
    <!-- VIEW: laboratuvar -->
    <div id="view-laboratuvar" class="app-view">
        <div class="flex items-center justify-between border-b border-[var(--border-color)] pb-4 mb-8">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                </div>
                <div>
                    <h2 class="text-2xl font-extrabold text-[var(--text-primary)]">Canlı İnteraktif Matris Laboratuvarı</h2>
                    <p class="text-xs text-[var(--text-muted)]">Gerçek Zamanlı Çözüm Motoru (Determinant, Cramer, Gauss & Rank)</p>
                </div>
            </div>
        </div>
        {CALCULATOR_HTML}
        {bottom_nav_lab}
    </div>
    """

    # View 9: Mock Exam
    idx_deneme = 9
    bottom_nav_deneme = make_bottom_nav(idx_deneme, VIEWS_METADATA)
    all_views_html += f"""
    <!-- VIEW: deneme -->
    <div id="view-deneme" class="app-view">
        <div class="flex items-center justify-between border-b border-[var(--border-color)] pb-4 mb-8">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                </div>
                <div>
                    <h2 class="text-2xl font-extrabold text-[var(--text-primary)]">Vize Deneme Sınavı (10 Soru)</h2>
                    <p class="text-xs text-[var(--text-muted)]">Vize Sınav Formatında Anında Puanlama</p>
                </div>
            </div>
        </div>
        <div class="glass-3d-card p-6 sm:p-8 rounded-3xl border border-[var(--border-color)] mb-6">
            <div class="flex items-center justify-between flex-wrap gap-4 mb-6 pb-6 border-b border-[var(--border-color)]">
                <div>
                    <h3 class="text-lg font-bold text-[var(--text-primary)]">Gerçek Vize Simülasyonu</h3>
                    <p class="text-[var(--text-muted)] text-xs">Soruları çözün, şıkkınızı işaretleyin. Yanlış ve doğru adımları anında açılır.</p>
                </div>
                <div id="quiz-score-badge" class="px-5 py-2.5 rounded-2xl bg-[var(--bg-box)] border border-amber-500/40 text-center shadow-lg">
                    <span class="text-[10px] text-[var(--text-muted)] uppercase tracking-widest block font-bold">Mevcut Skor</span>
                    <span id="quiz-score-text" class="text-xl font-black font-mono text-amber-400">0 / 10</span>
                </div>
            </div>
            <div id="quiz-container" class="space-y-6"></div>
        </div>
        {bottom_nav_deneme}
    </div>
    """

    # View 10: 15-Minute Cheatsheet
    idx_hap = 10
    bottom_nav_hap = make_bottom_nav(idx_hap, VIEWS_METADATA)
    all_views_html += f"""
    <!-- VIEW: hapbilgi -->
    <div id="view-hapbilgi" class="app-view">
        <div class="flex items-center justify-between border-b border-[var(--border-color)] pb-4 mb-8">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-rose-500/10 border border-rose-500/30 flex items-center justify-center text-rose-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                </div>
                <div>
                    <h2 class="text-2xl font-extrabold text-[var(--text-primary)]">15 Dakika Vize Hapı (Son Tekrar)</h2>
                    <p class="text-xs text-[var(--text-muted)]">Sınav Salonuna Girmeden Önce Okunacak Kritik Kurallar</p>
                </div>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
            {cheatsheet_html}
        </div>
        {bottom_nav_hap}
    </div>
    """

    # 4. Read template and substitute placeholders
    with open("template.html", "r", encoding="utf-8") as f:
        template = f.read()

    quiz_json = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)

    rendered = template.replace("<!-- ALL_VIEWS_CONTENT -->", all_views_html)
    rendered = rendered.replace("/* QUIZ_DATA_PLACEHOLDER */", quiz_json)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(rendered)

    size = os.path.getsize("index.html")
    print(f"BAŞARILI! Yeni index.html oluşturuldu. Dosya Boyutu: {size:,} bytes")

if __name__ == "__main__":
    generate_index_html()

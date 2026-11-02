# -*- coding: utf-8 -*-
"""
İnteraktif Matris & Lineer Cebir Laboratuvarı
Tamamen Glassmorphism & SVG İkonlar (Sıfır Emoji)
"""

CALCULATOR_HTML = r"""
<div class="space-y-8">
    <!-- 1. Determinant Calculator -->
    <div class="glass-3d-card p-6 sm:p-8 rounded-3xl border border-white/10 shadow-2xl relative overflow-hidden">
        <div class="flex items-center justify-between mb-4 flex-wrap gap-3">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                </div>
                <div>
                    <h4 class="text-xl font-bold text-white">1. Canlı Determinant & Sarrus Hesaplayıcı</h4>
                    <p class="text-slate-400 text-xs">Sayıları girin; hem Sarrus hem de 2x2/3x3 kuralları adım adım açılsın.</p>
                </div>
            </div>
            <div class="flex gap-1.5 p-1 rounded-xl bg-slate-950/60 border border-white/5">
                <button onclick="setDetSize(2)" id="det-btn-2" class="px-4 py-1.5 rounded-lg text-xs font-bold transition">2x2</button>
                <button onclick="setDetSize(3)" id="det-btn-3" class="px-4 py-1.5 rounded-lg text-xs font-bold transition">3x3</button>
            </div>
        </div>

        <div id="det-grid-container" class="flex justify-center my-6">
            <!-- Dynamic Grid -->
        </div>

        <div class="flex justify-center items-center gap-3 flex-wrap">
            <button onclick="calculateDeterminant()" class="px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs sm:text-sm shadow-lg shadow-emerald-900/40 transition flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/></svg>
                Determinantı Hesapla
            </button>
            <button onclick="fillExampleDet()" class="px-4 py-3 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 font-semibold text-xs sm:text-sm border border-white/5 transition flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                PDF'teki Örnek Değerleri Doldur
            </button>
        </div>

        <div id="det-result-box" class="mt-6 hidden p-6 rounded-2xl bg-slate-950/90 border border-emerald-500/30 text-sm space-y-3"></div>
    </div>

    <!-- 2. Cramer Solver -->
    <div class="glass-3d-card p-6 sm:p-8 rounded-3xl border border-white/10 shadow-2xl relative overflow-hidden">
        <div class="flex items-center gap-3 mb-2">
            <div class="w-10 h-10 rounded-xl bg-blue-500/10 border border-blue-500/30 flex items-center justify-center text-blue-400">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>
            </div>
            <div>
                <h4 class="text-xl font-bold text-white">2. Cramer Kuralı ile Lineer Sistem Çözücü ($3 \times 3$)</h4>
                <p class="text-slate-400 text-xs">Katsayıları ($A$) ve sonuç sütununu ($B$) girin; $\Delta$ ve $\Delta_j$ hesaplanarak durum tespiti yapılsın.</p>
            </div>
        </div>

        <div id="cramer-grid-container" class="flex justify-center my-6 overflow-x-auto p-2"></div>

        <div class="flex justify-center items-center gap-3 flex-wrap">
            <button onclick="calculateCramer()" class="px-6 py-3 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-bold text-xs sm:text-sm shadow-lg shadow-blue-900/40 transition flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                Cramer ile Çöz
            </button>
            <button onclick="fillExampleCramer()" class="px-4 py-3 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 font-semibold text-xs sm:text-sm border border-white/5 transition flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                Hafta 11 Örnek 2'yi Doldur
            </button>
        </div>

        <div id="cramer-result-box" class="mt-6 hidden p-6 rounded-2xl bg-slate-950/90 border border-blue-500/30 text-sm space-y-3"></div>
    </div>

    <!-- 3. Gauss & Rank Calculator -->
    <div class="glass-3d-card p-6 sm:p-8 rounded-3xl border border-white/10 shadow-2xl relative overflow-hidden">
        <div class="flex items-center gap-3 mb-2">
            <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
            </div>
            <div>
                <h4 class="text-xl font-bold text-white">3. Gauss Eleme & Matris Rankı Bulucu ($3 \times 4$)</h4>
                <p class="text-slate-400 text-xs">Elementer satır işlemlerini adım adım uygulayarak matrisi basamaklı (kanonik) hale getirir ve rankı hesaplar.</p>
            </div>
        </div>

        <div id="gauss-grid-container" class="flex justify-center my-6 overflow-x-auto p-2"></div>

        <div class="flex justify-center items-center gap-3 flex-wrap">
            <button onclick="calculateGauss()" class="px-6 py-3 rounded-xl bg-gradient-to-r from-amber-600 to-orange-600 hover:from-amber-500 hover:to-orange-500 text-white font-bold text-xs sm:text-sm shadow-lg shadow-amber-900/40 transition flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                Kanonik Hale Getir ve Rank Bul
            </button>
            <button onclick="fillExampleGauss()" class="px-4 py-3 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 font-semibold text-xs sm:text-sm border border-white/5 transition flex items-center gap-2">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                Hafta 12 Örnek 9'u Doldur
            </button>
        </div>

        <div id="gauss-result-box" class="mt-6 hidden p-6 rounded-2xl bg-slate-950/90 border border-amber-500/30 text-sm space-y-3"></div>
    </div>
</div>
"""

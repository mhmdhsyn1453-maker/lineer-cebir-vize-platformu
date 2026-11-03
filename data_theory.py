# -*- coding: utf-8 -*-
"""
Bölüm Teori ve Konu Anlatımları - Her Alt Başlıkta Eksiksiz Sayısal Örnekler
Lisans Dersi Notları Birebir Müfredat
Modern SVG İkonlar, Sıfır Emoji, Kristal Netliğinde Sıfırdan Zirveye Anlatım
"""

THEORY_CHAPTERS = [
    {
        "id": "giris",
        "title": "Vize Stratejisi & Sıfırdan Zirveye Yol Haritası",
        "badge": "Rehber",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>""",
        "content": r"""
<div class="space-y-6">
    <div class="glass-hero p-8 rounded-3xl relative overflow-hidden border border-white/10 shadow-2xl">
        <div class="absolute -right-10 -bottom-10 w-64 h-64 bg-indigo-600/20 rounded-full blur-3xl pointer-events-none"></div>
        <div class="relative z-10">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-semibold mb-4">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                Sıfır Temelle Başlayanlar İçin Özel Hazırlandı
            </div>
            <h3 class="text-2xl sm:text-3xl font-black text-white tracking-tight mb-3">
                Bu Dersten Zerre Anlamıyorum Diyorsan: Korkma, Doğru Yerdesin!
            </h3>
            <p class="text-slate-300 text-sm sm:text-base leading-relaxed max-w-3xl">
                Lineer Cebir soyut kurallardan ibaret değildir. Bu platformda <strong>her alt başlıkta en az bir tam çözümlü sayısal örnek</strong> göreceksin. 
                Sınav doğrudan bu ders notlarındaki ve PDF'lerdeki soruların mantığından gelecektir. 
                Her konuyu, mantığını ve sınav tuzaklarını adım adım incele.
            </p>
        </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
        <div class="glass-panel p-6 rounded-2xl border border-white/5 relative group hover:border-indigo-500/30 transition-all duration-300">
            <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                </div>
                <h4 class="text-lg font-bold text-white">Sorumlu Olduğumuz 5 Konu (JPEG Notu)</h4>
            </div>
            <ul class="space-y-2.5 text-xs sm:text-sm text-slate-300">
                <li class="flex items-center gap-2.5 p-2 rounded-lg bg-slate-900/40 border border-white/5">
                    <span class="w-6 h-6 rounded-md bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 font-bold flex items-center justify-center text-xs">1</span>
                    <span><strong>DETERMİNANTLAR</strong> (Hafta 1 & Hafta 11 Soru Çözümleri)</span>
                </li>
                <li class="flex items-center gap-2.5 p-2 rounded-lg bg-slate-900/40 border border-white/5">
                    <span class="w-6 h-6 rounded-md bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 font-bold flex items-center justify-center text-xs">2</span>
                    <span><strong>DETERMİNANT İLE ÇÖZÜLEN SİSTEMLER</strong> (Cramer - Hafta 1 & 11)</span>
                </li>
                <li class="flex items-center gap-2.5 p-2 rounded-lg bg-slate-900/40 border border-white/5">
                    <span class="w-6 h-6 rounded-md bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 font-bold flex items-center justify-center text-xs">3</span>
                    <span><strong>MATRİS CEBİRİ</strong> (Hafta 3 & Hafta 12 Soru Çözümleri)</span>
                </li>
                <li class="flex items-center gap-2.5 p-2 rounded-lg bg-slate-900/40 border border-white/5">
                    <span class="w-6 h-6 rounded-md bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 font-bold flex items-center justify-center text-xs">4</span>
                    <span><strong>DENK MATRİSLER & RANK</strong> (Hafta 5 & Hafta 12 Soru Çözümleri)</span>
                </li>
                <li class="flex items-center gap-2.5 p-2 rounded-lg bg-slate-900/40 border border-white/5">
                    <span class="w-6 h-6 rounded-md bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 font-bold flex items-center justify-center text-xs">5</span>
                    <span><strong>LİNEER DENKLEM SİSTEMLERİNİN ÇÖZÜMÜ</strong> (Gauss - Hafta 4 & 12)</span>
                </li>
            </ul>
        </div>

        <div class="glass-panel p-6 rounded-2xl border border-white/5 relative group hover:border-emerald-500/30 transition-all duration-300">
            <div class="flex items-center gap-3 mb-4">
                <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                </div>
                <h4 class="text-lg font-bold text-white">Her Başlıkta Örnekli Öğrenme Yöntemi</h4>
            </div>
            <div class="space-y-3 text-xs sm:text-sm text-slate-300">
                <p>
                    Aşağıdaki her alt başlıkta (örneğin <strong>1.1, 1.2, 3.1, 4.2</strong> vb.) o kuralın tam olarak ne anlama geldiğini gösteren 
                    <strong>ayrıntılı çözülmüş sayısal bir örnek</strong> yer almaktadır.
                </p>
                <p>
                    Soyut tanımları okuduktan sonra altındaki örneği kağıda yazarak uygula. 
                    Böylece hiçbir kural havada kalmayacak, hepsi zihninde somut bir matematiksel işleme dönüşecektir.
                </p>
            </div>
        </div>
    </div>
</div>
"""
    },
    {
        "id": "bolum1",
        "title": "Bölüm 1: Determinantlar",
        "badge": "Hafta 1 & 11",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"/></svg>""",
        "content": r"""
<div class="space-y-6">
    <!-- Sıfırdan Başlayana Mantık -->
    <div class="glass-panel p-6 rounded-2xl border-l-4 border-l-indigo-500 bg-indigo-950/20">
        <div class="flex items-center gap-2.5 text-indigo-300 font-bold text-base mb-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            Sıfırdan Başlayana: Determinant Gerçekte Nedir ve Neden Hesaplanır?
        </div>
        <p class="text-slate-300 text-sm leading-relaxed mb-3">
            Matris dediğimiz şey sayılardan oluşan bir tablodur (örneğin $3 \times 3$ boyutunda 9 adet sayı). 
            <strong>Determinant</strong> ise bu tabloyu tek bir reel sayıya indirgeme yöntemidir. 
            Bu çıkan sayı bize matrisin tersinin olup olmadığını ($|A| \neq 0$ ise tersi vardır) ve denklem sisteminin tek çözümü olup olmadığını söyler.
        </p>
        <div class="text-xs text-amber-300 font-medium">
            <span class="badge badge-accent">ALTIN KURAL</span> Determinant SADECE kare matrislerde ($2\times 2, 3\times 3, n\times n$) hesaplanabilir. Dikdörtgen matrislerin determinantı OLMAZ!
        </div>
    </div>

    <!-- 1.1 2x2 Determinant -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">1.1</span>
            <h4 class="text-lg font-bold text-white">$2 \times 2$ Determinant Hesabı</h4>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">
            İki satır ve iki sütundan oluşan matrisin determinantında ana köşegen (sol üstten sağ alta) çarpımından, ters köşegen (sağ üstten sol alta) çarpımı çıkarılır:
        </p>
        <div class="p-4 rounded-xl bg-slate-950/80 border border-white/5 text-center">
            $$\det(A) = |A| = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = (a \cdot d) - (b \cdot c)$$
        </div>

        <!-- 1.1 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                1.1 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 5 & -3 \\ 2 & 4 \end{bmatrix}$ matrisinin determinantını hesaplayınız.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-1.5 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p>• Sol üstten sağ alta çarpım: $a \cdot d = 5 \cdot 4 = 20$</p>
                <p>• Sağ üstten sol alta çarpım: $b \cdot c = (-3) \cdot 2 = -6$</p>
                <p>• Formülü uygula: $\det(A) = 20 - (-6) = 20 + 6 = \mathbf{26}$</p>
                <p class="text-emerald-400 pt-1">Sonuç: $|A| = 26 \neq 0$ olduğundan matris regülerdir ve tersi alınabilir.</p>
            </div>
        </div>
    </div>

    <!-- 1.2 3x3 Sarrus Kuralı -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">1.2</span>
            <h4 class="text-lg font-bold text-white">$3 \times 3$ Determinant ve SARRUS Kuralı</h4>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">
            $3 \times 3$ determinantlarda ilk iki satır matrisin altına aynen yazılır. Sağa inen 3 çapraz $(+)$ toplanır, sola inen 3 çapraz $(-)$ çıkarılır.
        </p>

        <!-- 1.2 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                1.2 İçin Tam Çözümlü Sayısal Örnek (Sarrus):
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\Delta = \begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{vmatrix}$ determinantını Sarrus kuralı ile hesaplayınız.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>Adım 1:</strong> İlk 2 satırı alta ekle:</p>
                <p class="text-center text-slate-400">
                    $$\begin{matrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \\ \hline 1 & 2 & 3 \\ 0 & 1 & 4 \end{matrix}$$
                </p>
                <p><strong>Adım 2 (Sağa inen (+) çarpımlar):</strong><br>
                • $1 \cdot 1 \cdot 0 = 0$<br>
                • $0 \cdot 6 \cdot 3 = 0$<br>
                • $5 \cdot 2 \cdot 4 = 40$<br>
                Toplam (+) = $0 + 0 + 40 = \mathbf{40}$</p>
                <p><strong>Adım 3 (Sola inen (-) çarpımlar):</strong><br>
                • $3 \cdot 1 \cdot 5 = 15$<br>
                • $4 \cdot 6 \cdot 1 = 24$<br>
                • $0 \cdot 2 \cdot 0 = 0$<br>
                Toplam (-) = $15 + 24 + 0 = \mathbf{39}$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: $\Delta = (+) - (-) = 40 - 39 = \mathbf{1}$.</p>
            </div>
        </div>
        <div class="p-3.5 rounded-xl bg-rose-950/30 border border-rose-500/40 text-rose-300 text-xs">
            <span class="badge badge-accent">HOCA TUZAĞI</span> Sarrus kuralı <strong>SADECE $3 \times 3$</strong> matrislerde geçerlidir! $4 \times 4$'te uygularsan sıfır alırsın!
        </div>
    </div>

    <!-- 1.3 Minör ve Kofaktör -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">1.3</span>
            <h4 class="text-lg font-bold text-white">Altdeterminant (Minör) ve Eşçarpan (Kofaktör)</h4>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">
            • <strong>Minör ($M_{ij}$):</strong> $i$. satır ve $j$. sütun kapatıldığında kalan determinant.<br>
            • <strong>Kofaktör ($A_{ij}$):</strong> $A_{ij} = (-1)^{i+j} M_{ij}$. Dama tahtası işaret kuralıdır.
        </p>

        <!-- 1.3 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                1.3 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 2 & -1 & 3 \\ 0 & 4 & 5 \\ 1 & 2 & -2 \end{bmatrix}$ matrisinde $a_{12} = -1$ elemanının minörünü ($M_{12}$) ve kofaktörünü ($A_{12}$) bulunuz.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>Minör ($M_{12}$):</strong> 1. satırı ve 2. sütunu elinle kapat. Kalanlar:<br>
                $$M_{12} = \begin{vmatrix} 0 & 5 \\ 1 & -2 \end{vmatrix} = (0 \cdot -2) - (5 \cdot 1) = 0 - 5 = \mathbf{-5}$$</p>
                <p><strong>Kofaktör ($A_{12}$):</strong> Formül $A_{12} = (-1)^{1+2} M_{12} = (-1)^3 \cdot (-5) = (-1) \cdot (-5) = \mathbf{+5}$.</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: Minör $M_{12} = -5$, Kofaktör $A_{12} = 5$'tir.</p>
            </div>
        </div>
    </div>

    <!-- 1.4 Laplace Açılımı Masterclass -->
    <div class="glass-3d-card p-6 sm:p-8 rounded-2xl border border-white/5 space-y-6">
        <!-- Başlık ve Rozetler -->
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-white/5 pb-4">
            <div class="flex items-center gap-3">
                <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">1.4</span>
                <h4 class="text-lg sm:text-xl font-bold text-white tracking-tight">Laplace Açılımı (Kofaktör ile Determinant Hesabı)</h4>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[11px] font-mono">Her Boyutta Geçerli ($n \times n$)</span>
                <span class="px-2.5 py-0.5 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-400 text-[11px] font-mono">Sıfır Avcısı Stratejisi</span>
            </div>
        </div>

        <!-- 1. Temel Sezgi ve Mantık (Sıfırdan Başlayanlar İçin) -->
        <div class="space-y-3">
            <h5 class="text-sm font-bold text-indigo-400 flex items-center gap-2 uppercase tracking-wider">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                1. Temel Mantık: Laplace Açılımı Nedir ve Neden Zorunludur?
            </h5>
            <p class="text-slate-300 text-sm leading-relaxed">
                $2 \times 2$ determinant hesabı çok basittir: sağ çapraz eksi sol çapraz ($ad - bc$). $3 \times 3$ matrisler için de pratik bir Sarrus kuralı vardır. <strong>Fakat Sarrus kuralı $4 \times 4$ ve daha büyük matrislerde KESİNLİKLE GEÇERSİZDİR!</strong>
            </p>
            <p class="text-slate-300 text-sm leading-relaxed">
                İşte <strong>Laplace Açılımı</strong>, boyutu ne olursa olsun ($3\times 3, 4\times 4, 5\times 5 \dots$) devasa matrisleri minik ve sevimli $2\times 2$ determinantlara parçalayarak çözmemizi sağlayan evrensel anahtardır.
            </p>
            <div class="p-4 rounded-xl bg-indigo-950/20 border border-indigo-500/20 text-xs sm:text-sm text-indigo-200">
                <strong>Laplace'ın En Büyük Özgürlüğü:</strong> Matrisin <u>istediğiniz herhangi bir satırını</u> veya <u>istediğiniz herhangi bir sütununu</u> seçebilirsiniz! Hangi satırı veya sütunu seçerseniz seçin çıkan <strong>sonuç daima aynıdır</strong>.
            </div>
        </div>

        <!-- 2. Dama Tahtası İşaret Kuralı -->
        <div class="space-y-3">
            <h5 class="text-sm font-bold text-indigo-400 flex items-center gap-2 uppercase tracking-wider">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
                2. Dama Tahtası İşaret Kuralı (Formülsüz Kolay Yol)
            </h5>
            <p class="text-slate-300 text-sm leading-relaxed">
                Kitaplardaki $(-1)^{i+j}$ formülü öğrencilerin en çok kafasını karıştıran ve işlem hatası yaptıkları yerdir. Bunun yerine satranç/dama tahtası kuralını aklınızda tutun:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-2 text-center">
                    <span class="text-xs font-mono font-bold text-slate-400 block">$3 \times 3$ İçin İşaret Şablonu</span>
                    <div class="text-base sm:text-lg font-mono tracking-widest text-indigo-300 font-bold py-2 bg-slate-950/50 rounded-lg border border-white/5">
                        $$\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}$$
                    </div>
                    <p class="text-[11px] text-slate-400">Sol üst köşe ($a_{11}$) daima <strong>$+$</strong> ile başlar, komşuları sürekli zıt işarete döner.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-2 text-center">
                    <span class="text-xs font-mono font-bold text-slate-400 block">$4 \times 4$ İçin İşaret Şablonu</span>
                    <div class="text-base sm:text-lg font-mono tracking-widest text-teal-300 font-bold py-2 bg-slate-950/50 rounded-lg border border-white/5">
                        $$\begin{bmatrix} + & - & + & - \\ - & + & - & + \\ + & - & + & - \\ - & + & - & + \end{bmatrix}$$
                    </div>
                    <p class="text-[11px] text-slate-400">Örneğin 2. satırı seçerseniz işaret sırası: <strong>$-, +, -, +$</strong> olur!</p>
                </div>
            </div>
            <div class="p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/20 text-xs text-amber-200">
                <strong>Hayati İpucu:</strong> Sınav kağıdında açılım yapacağınız satır veya sütunun hemen üstüne kurşun kalemle bu işaretleri ($+$ veya $-$) küçükçe not edin. Böylece asla işaret hatası yapmazsınız!
            </div>
        </div>

        <!-- 3. Satır-Sütun Karalama Yöntemi ve Formül -->
        <div class="space-y-3">
            <h5 class="text-sm font-bold text-indigo-400 flex items-center gap-2 uppercase tracking-wider">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/></svg>
                3. "Satır-Sütun Karalama" (Cross-Out) Tekniği
            </h5>
            <p class="text-slate-300 text-sm leading-relaxed">
                Açılım yapacağınız satır veya sütunun her bir elemanı için:
            </p>
            <ol class="list-decimal list-inside space-y-1.5 text-xs sm:text-sm text-slate-300 pl-2">
                <li>O elemanın bulunduğu <strong>satırı</strong> ve <strong>sütunu</strong> parmağınızla kapatın (karalayın).</li>
                <li>Dışarıda açıkta kalan sayıları alarak bir $2\times 2$ determinant (minör) oluşturun.</li>
                <li>Bu minörü, elemanın kendi değeri ve dama tahtasındaki işaretiyle çarpın:
                    $$\text{Terim} = (\pm \text{İşaret}) \cdot (\text{Eleman}) \cdot (\text{Kalan Minör})$$
                </li>
                <li>Seçtiğiniz sıradaki tüm elemanlar için bunu yapıp sonuçları toplayın!</li>
            </ol>
        </div>

        <!-- 4. Hocaların Söylemediği Altın Taktik: Sıfır Avcısı -->
        <div class="p-5 rounded-2xl bg-gradient-to-br from-indigo-950/40 via-purple-950/20 to-slate-900 border border-indigo-500/30 space-y-3">
            <div class="flex items-center gap-2 text-indigo-400 font-bold text-sm uppercase tracking-wider">
                <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                Hocaların Tahtada Hızlıca Geçtiği Altın Taktik: "Sıfır Avcısı"
            </div>
            <p class="text-slate-200 text-sm leading-relaxed">
                Hangi satırı veya sütunu seçeceğiniz size bağlıysa, neden 1. satırı seçip 3 tane ayrı ayrı minör hesaplayarak zaman kaybedesiniz?
            </p>
            <div class="p-3.5 rounded-xl bg-indigo-900/30 border border-indigo-500/20 text-xs sm:text-sm text-slate-200">
                <strong>Strateji:</strong> Matrisin içine bakın ve <strong>en çok $0$ (sıfır) barındıran</strong> satırı veya sütunu seçin!
                Çünkü $0 \cdot (\text{Minör}) = 0$'dır; o elemanın minörünü hesaplamanıza <u>hiç gerek kalmaz</u>, doğrudan sıfır yazıp geçersiniz. Bir satırda iki tane sıfır varsa, 1 dakikalık soru 10 saniyede biter!
            </div>
        </div>

        <!-- ÖRNEK 1 -->
        <div class="p-5 rounded-2xl bg-slate-900/80 border border-indigo-500/30 space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/5 pb-2">
                <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    Örnek 1: Klasik $3 \times 3$ Açılımı (1. Satıra Göre Adım Adım)
                </span>
                <span class="text-[11px] font-mono text-slate-400">Temel Seviye</span>
            </div>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\Delta = \begin{vmatrix} 3 & 2 & -1 \\ 1 & 4 & 0 \\ 2 & 5 & 2 \end{vmatrix}$ determinantını 1. satıra göre Laplace açılımı ile hesaplayınız.
            </p>
            <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-indigo-300 font-bold">Adım 1: 1. Satır elemanları ve Dama Tahtası işaretleri:</p>
                <p>• $a_{11} = 3 \rightarrow \text{İşaret: } \mathbf{+}$</p>
                <p>• $a_{12} = 2 \rightarrow \text{İşaret: } \mathbf{-}$</p>
                <p>• $a_{13} = -1 \rightarrow \text{İşaret: } \mathbf{+}$</p>
                
                <p class="text-indigo-300 font-bold pt-2">Adım 2: Terimleri tek tek hesaplayalım:</p>
                <p>1. Terim: $(+1) \cdot 3 \cdot \begin{vmatrix} 4 & 0 \\ 5 & 2 \end{vmatrix} = 3 \cdot (4 \cdot 2 - 0 \cdot 5) = 3 \cdot (8 - 0) = \mathbf{24}$</p>
                <p>2. Terim: $(-1) \cdot 2 \cdot \begin{vmatrix} 1 & 0 \\ 2 & 2 \end{vmatrix} = -2 \cdot (1 \cdot 2 - 0 \cdot 2) = -2 \cdot (2 - 0) = \mathbf{-4}$</p>
                <p>3. Terim: $(+1) \cdot (-1) \cdot \begin{vmatrix} 1 & 4 \\ 2 & 5 \end{vmatrix} = -1 \cdot (1 \cdot 5 - 4 \cdot 2) = -1 \cdot (5 - 8) = -1 \cdot (-3) = \mathbf{+3}$</p>

                <p class="text-indigo-300 font-bold pt-2">Adım 3: Terimleri toplayalım:</p>
                <p class="text-emerald-400 font-bold text-sm">$$\Delta = 24 + (-4) + 3 = \mathbf{23}$$</p>
            </div>
        </div>

        <!-- ÖRNEK 2 -->
        <div class="p-5 rounded-2xl bg-slate-900/80 border border-teal-500/30 space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/5 pb-2">
                <span class="text-xs font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    Örnek 2: "Sıfır Avcısı" Taktik Açılımı (10 Saniyede Çözüm)
                </span>
                <span class="text-[11px] font-mono text-amber-400">Sınav Taktikli Soru</span>
            </div>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\Delta = \begin{vmatrix} 4 & 7 & 2 \\ 0 & 5 & 0 \\ 3 & -1 & 6 \end{vmatrix}$ determinantını en pratik yöntemle hesaplayınız.
            </p>
            <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-teal-300 font-bold">Strateji: 2. Satıra bakın: İki adet $0$ var! Bu satıra göre açacağız.</p>
                <p>2. Satırın Dama Tahtası işaret sırası: $\mathbf{-}, \mathbf{+}, \mathbf{-}$</p>
                
                <p class="text-teal-300 font-bold pt-2">Açılım:</p>
                <p>$$\Delta = - (0 \cdot M_{21}) + 5 \cdot M_{22} - (0 \cdot M_{23})$$</p>
                <p>Sıfırlar otomatik gittiği için sadece ortadaki $M_{22}$ minörünü (2. satır ve 2. sütunu kapatarak) hesaplarız:</p>
                <p>$$M_{22} = \begin{vmatrix} 4 & 2 \\ 3 & 6 \end{vmatrix} = (4 \cdot 6) - (2 \cdot 3) = 24 - 6 = 18$$</p>
                <p>Kofaktörle çarpım: $\Delta = (+1) \cdot 5 \cdot 18 = \mathbf{90}$.</p>
                <p class="text-emerald-400 font-bold text-sm pt-1">Sonuç: $\Delta = \mathbf{90}$. (Normalde 3 işlem yapacakken tek işlemle bitti!)</p>
            </div>
        </div>

        <!-- ÖRNEK 3 -->
        <div class="p-5 rounded-2xl bg-slate-900/80 border border-purple-500/30 space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/5 pb-2">
                <span class="text-xs font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                    Örnek 3: $4 \times 4$ Determinant (Sarrus'un İflas Ettiği Yer!)
                </span>
                <span class="text-[11px] font-mono text-purple-300">Vizede Çıkabilecek Ağır Soru</span>
            </div>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\Delta = \begin{vmatrix} 2 & 0 & 0 & 0 \\ 5 & 3 & 1 & -2 \\ 1 & 0 & 4 & 2 \\ 3 & 2 & 1 & 1 \end{vmatrix}$ determinantını hesaplayınız.
            </p>
            <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-amber-400 font-bold">Önemli Uyarı: $4\times 4$'te Sarrus uygulanmaz! Mutlaka Laplace açılımı yapılmalıdır.</p>
                <p class="text-purple-300 font-bold pt-1">Adım 1: 1. Satırda tam 3 tane sıfır var! ($2, 0, 0, 0$)</p>
                <p>1. Satıra göre açarsak diğer üç terim sıfırla çarpılıp uçar:</p>
                <p>$$\Delta = (+1) \cdot 2 \cdot \begin{vmatrix} 3 & 1 & -2 \\ 0 & 4 & 2 \\ 2 & 1 & 1 \end{vmatrix} - 0 + 0 - 0$$</p>
                
                <p class="text-purple-300 font-bold pt-2">Adım 2: Kalan $3 \times 3$ determinantı ($D_3$) hesaplayalım:</p>
                <p>Bu matrisin 1. sütununda da bir tane sıfır var ($a_{21}=0$). 1. sütuna göre açalım:</p>
                <p>• 1. Terim: $(+1) \cdot 3 \cdot \begin{vmatrix} 4 & 2 \\ 1 & 1 \end{vmatrix} = 3 \cdot (4 - 2) = 3 \cdot 2 = 6$</p>
                <p>• 2. Terim: $(-1) \cdot 0 \cdot \text{Minör} = 0$</p>
                <p>• 3. Terim: $(+1) \cdot 2 \cdot \begin{vmatrix} 1 & -2 \\ 4 & 2 \end{vmatrix} = 2 \cdot (1 \cdot 2 - (-2) \cdot 4) = 2 \cdot (2 + 8) = 2 \cdot 10 = 20$</p>
                <p>$$D_3 = 6 - 0 + 20 = 26$$</p>

                <p class="text-purple-300 font-bold pt-2">Adım 3: Ana determinanta dönelim:</p>
                <p class="text-emerald-400 font-bold text-sm">$$\Delta = 2 \cdot D_3 = 2 \cdot 26 = \mathbf{52}$$</p>
            </div>
        </div>

        <!-- 5. Sınavda Hayat Kurtaran 4 Kritik Hoca Tuzağı -->
        <div class="p-5 rounded-2xl bg-rose-950/20 border border-rose-500/30 space-y-3">
            <div class="flex items-center gap-2 text-rose-400 font-bold text-sm uppercase tracking-wider">
                <svg class="w-5 h-5 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                Vize Sınavında En Çok Puan Kırdıran 4 Klasik Hata
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">1. 2. Satırın İlk İşaretini Unutmak:</strong>
                    Öğrenci 2. satıra göre açarken ilk elemanın önüne artı koyar. Oysa 2. satır dama tahtasında <strong>EKSİ ($-$)</strong> ile başlar!
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">2. Çift Eksi Tuzağı:</strong>
                    Elemanın kendi değeri $-3$ ise ve dama tahtasından da $-$ geliyorsa, çarpım $(-1) \cdot (-3) = \mathbf{+3}$ olur. İşaretleri iç içe çarpmayı unutmayın.
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">3. $4 \times 4$'te Sarrus Yapmak:</strong>
                    Hoca $4 \times 4$ sorarsa kesinlikle ilk iki satırı alta yazıp çapraz çarpmaya kalkmayın; sıfır puan alırsınız. $4\times 4$'te tek çare Laplace'tır!
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">4. Orantılı Satırları Görememek:</strong>
                    Laplace yapmaya başlamadan önce ilk 3 saniye bakın: Bir satır diğerinin katıysa (örneğin $S_2 = 2 S_1$) işlem yapmadan direkt $\det = 0$ yazın!
                </div>
            </div>
        </div>
    </div>

    <!-- 1.5 Determinantın 8 Altın Kuralı -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">1.5</span>
            <h4 class="text-lg font-bold text-white">Determinantın 8 Altın Kuralı ve Sayısal Örnekleri</h4>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">1. Transpoze Kuralı:</strong>
                $\det(A) = \det(A^T)$.
                <span class="text-slate-400 block font-mono">Örn: $\begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} = -2$, transpozu $\begin{vmatrix} 1 & 3 \\ 2 & 4 \end{vmatrix} = -2$.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">2. Satır Değişimi:</strong>
                İki satır yer değiştirirse işaret eksi olur.
                <span class="text-slate-400 block font-mono">Örn: $\begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} = -2 \implies \begin{vmatrix} 3 & 4 \\ 1 & 2 \end{vmatrix} = +2$.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">3. Eşit/Orantılı Satırlar:</strong>
                İki satır aynı veya katı ise determinant sıfırdır.
                <span class="text-slate-400 block font-mono">Örn: $\begin{vmatrix} 1 & 3 \\ 2 & 6 \end{vmatrix} = (6 - 6) = \mathbf{0}$.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">4. Komple Sıfır Satır:</strong>
                Tüm elemanları 0 olan satır varsa determinant doğrudan 0'dır.
                <span class="text-slate-400 block font-mono">Örn: $\begin{vmatrix} 0 & 0 \\ 4 & 5 \end{vmatrix} = \mathbf{0}$.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">5. Skaler Çarpım:</strong>
                $\det(k A) = k^n \det(A)$.
                <span class="text-slate-400 block font-mono">Örn: $2\times 2$ matriste $\det(A)=3$ ise $\det(2A) = 2^2 \cdot 3 = \mathbf{12}$.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">6. Satır Ekleme (Değişmezlik):</strong>
                Bir satırın katını diğerine eklemek determinantı değiştirmez.
                <span class="text-slate-400 block font-mono">Örn: $\begin{vmatrix} 1 & 2 \\ 3 & 4 \end{vmatrix} \xrightarrow{S_2 - 3S_1} \begin{vmatrix} 1 & 2 \\ 0 & -2 \end{vmatrix} = -2$.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">7. Çarpım Kuralı:</strong>
                $\det(A \cdot B) = \det(A) \cdot \det(B)$.
                <span class="text-slate-400 block font-mono">Örn: $\det(A)=2, \det(B)=5 \implies \det(AB) = \mathbf{10}$.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-indigo-400 block font-bold">8. Üçgen Matris Determinantı:</strong>
                Köşegen altı veya üstü sıfırsa determinant köşegen çarpımıdır.
                <span class="text-slate-400 block font-mono">Örn: $\begin{vmatrix} 3 & 5 \\ 0 & 4 \end{vmatrix} = 3 \cdot 4 = \mathbf{12}$.</span>
            </div>
        </div>

        <!-- 1.5 Sınav Taktikli Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3 mt-4">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                1.5 İçin Tam Çözümlü Sayısal Sınav Örneği (Hızlı Determinant Tespiti):
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 1 & 4 & -2 \\ 2 & 8 & -4 \\ 5 & 7 & 9 \end{bmatrix}$ matrisinin determinantı nedir?
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>İnceleme & Kural Tespiti:</strong><br>
                2. satıra dikkat edelim: $(2, 8, -4) = 2 \cdot (1, 4, -2)$. Yani $S_2 = 2 \cdot S_1$ (orantılı satırlar!).</p>
                <p><strong>Çözüm:</strong><br>
                Determinantın 3. Altın Kuralı gereğince: Bir matrisin herhangi iki satırı birbiriyle aynı veya orantılıysa, Sarrus veya Laplace ile zaman kaybetmeden doğrudan:</p>
                $$\det(A) = 0$$
                <p class="text-emerald-400 font-bold pt-1">Sınav İpucu: Hoca vizede büyük sayılar içeren $3 \times 3$ veya $4 \times 4$ determinant sorarsa, mutlaka satırların katı olup olmadığını (veya tamamen 0 olup olmadığını) ilk 5 saniyede kontrol edin!</p>
            </div>
        </div>
    </div>
</div>
"""
    },
    {
        "id": "bolum2",
        "title": "Bölüm 2: Determinant ile Denklem Çözümü (Cramer)",
        "badge": "Hafta 1 & 11",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>""",
        "content": r"""
<div class="space-y-6">
    <div class="glass-panel p-6 rounded-2xl border-l-4 border-l-blue-500 bg-blue-950/20">
        <div class="flex items-center gap-2.5 text-blue-300 font-bold text-base mb-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            Sıfırdan Başlayana: Cramer Kuralı Neyi Çözer?
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">
            Cramer Kuralı, bilinmeyenleri ($x_1, x_2, \dots$) yok etme metoduyla uğraşmadan, doğrudan determinant oranlarıyla bulur:
            $x_j = \frac{\Delta_j}{\Delta}$.
        </p>
    </div>

    <!-- 2.1 Cramer Formülü ve Örnek -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-blue-500/20 text-blue-400 font-mono text-xs font-bold">2.1</span>
            <h4 class="text-lg font-bold text-white">Cramer Kuralı Formülü ve Çözüm Adımları</h4>
        </div>

        <!-- 2.1 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-blue-950/30 border border-blue-500/30 space-y-3">
            <span class="text-xs font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                2.1 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} 2x + 3y = 8 \\ 3x - y = 1 \end{cases}$ sistemini Cramer kuralı ile çözünüz.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>1. Ana Katsayılar Determinantı ($\Delta$):</strong><br>
                $$\Delta = \begin{vmatrix} 2 & 3 \\ 3 & -1 \end{vmatrix} = [2 \cdot (-1)] - (3 \cdot 3) = -2 - 9 = \mathbf{-11} \neq 0$$
                $\Delta \neq 0$ olduğu için tek bir çözüm vardır!</p>
                <p><strong>2. $x$ için Determinant ($\Delta_x$ - 1. sütun yerine sağdaki 8 ve 1'i koy):</strong><br>
                $$\Delta_x = \begin{vmatrix} 8 & 3 \\ 1 & -1 \end{vmatrix} = [8 \cdot (-1)] - (3 \cdot 1) = -8 - 3 = \mathbf{-11}$$</p>
                <p><strong>3. $y$ için Determinant ($\Delta_y$ - 2. sütun yerine sağdaki 8 ve 1'i koy):</strong><br>
                $$\Delta_y = \begin{vmatrix} 2 & 8 \\ 3 & 1 \end{vmatrix} = (2 \cdot 1) - (8 \cdot 3) = 2 - 24 = \mathbf{-22}$$</p>
                <p><strong>4. Bilinmeyenleri Bul:</strong><br>
                • $x = \frac{\Delta_x}{\Delta} = \frac{-11}{-11} = \mathbf{1}$<br>
                • $y = \frac{\Delta_y}{\Delta} = \frac{-22}{-11} = \mathbf{2}$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: Çözüm kümesi $(x = 1, y = 2)$'dir.</p>
            </div>
        </div>
    </div>

    <!-- 2.2 3 Kritik Durum ve Sayısal Örnekler -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-blue-500/20 text-blue-400 font-mono text-xs font-bold">2.2</span>
            <h4 class="text-lg font-bold text-white">3 Kritik Çözüm Durumu (Tek Çözüm, Çözümsüzlük, Sonsuz Çözüm)</h4>
        </div>
        <!-- 2.2 Sayısal Örnek Başlığı -->
        <div class="px-2 pt-2">
            <span class="text-xs font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5 mb-2">
                <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                2.2 İçin Tam Çözümlü Sayısal Örnek (3 Durumun Sayısal İspatı):
            </span>
        </div>
        <div class="space-y-4 text-xs sm:text-sm">
            <div class="p-4 rounded-xl bg-emerald-950/30 border border-emerald-500/30 space-y-1">
                <span class="font-bold text-emerald-400 text-sm block">Durum 1: $\Delta \neq 0$ $\implies$ TEK ÇÖZÜM</span>
                <p class="text-slate-300">Örnek: Yukarıdaki 2.1 örneğinde $\Delta = -11 \neq 0$ çıktığı için tek bir kesin çözüm $(1, 2)$ elde edilmiştir.</p>
            </div>
            <div class="p-4 rounded-xl bg-rose-950/30 border border-rose-500/30 space-y-2">
                <span class="font-bold text-rose-400 text-sm block">Durum 2: $\Delta = 0$ ve En Az Biri $\Delta_j \neq 0$ $\implies$ ÇÖZÜM YOKTUR ($\emptyset$)</span>
                <div class="p-3 rounded-lg bg-slate-950/70 border border-white/5 font-mono text-slate-300">
                    Sayısal Örnek: $\begin{cases} x + y = 3 \\ 2x + 2y = 8 \end{cases}$<br>
                    $\Delta = \begin{vmatrix} 1 & 1 \\ 2 & 2 \end{vmatrix} = 2 - 2 = 0$.<br>
                    $\Delta_x = \begin{vmatrix} 3 & 1 \\ 8 & 2 \end{vmatrix} = 6 - 8 = -2 \neq 0$.<br>
                    $x = \frac{\Delta_x}{\Delta} = \frac{-2}{0}$ (Tanımsız! Çözüm YOKTUR!).
                </div>
            </div>
            <div class="p-4 rounded-xl bg-amber-950/30 border border-amber-500/30 space-y-2">
                <span class="font-bold text-amber-400 text-sm block">Durum 3: $\Delta = 0$ ve Tüm $\Delta_j = 0$ $\implies$ SONSUZ ÇÖZÜM</span>
                <div class="p-3 rounded-lg bg-slate-950/70 border border-white/5 font-mono text-slate-300">
                    Sayısal Örnek: $\begin{cases} x + y = 3 \\ 2x + 2y = 6 \end{cases}$<br>
                    $\Delta = 0$, $\Delta_x = \begin{vmatrix} 3 & 1 \\ 6 & 2 \end{vmatrix} = 6 - 6 = 0$. $\frac{0}{0}$ belirsizliği!<br>
                    2. denklem 1.nin kopyasıdır. $y = t$ serbest değişken atanır: $x = 3 - t, y = t$ (Sonsuz Çözüm!).
                </div>
            </div>
        </div>
    </div>

    <!-- 2.3 Homojen Sistemler ve Örnek -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-purple-500/20 text-purple-400 font-mono text-xs font-bold">2.3</span>
            <h4 class="text-lg font-bold text-white">Homojen Sistemler ($AX = 0$) ve $k$ Parametresi</h4>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">
            Homojen sistemde eşitliğin sağı $0$'dır. Sıfırdan farklı çözüm olması için <strong>$\det(A) = 0$</strong> olmalıdır.
        </p>

        <!-- 2.3 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-purple-950/30 border border-purple-500/30 space-y-3">
            <span class="text-xs font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                2.3 İçin Tam Çözümlü Sayısal Örnek (Hocanın En Sevdiği Soru):
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} x + 2y = 0 \\ 3x + ky = 0 \end{cases}$ homojen sisteminin aşikar olandan ($0,0$) farklı çözümünün olması için $k$ kaç olmalıdır?
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p>Kural: Katsayılar determinantı sıfır olmalıdır ($\det(A) = 0$).</p>
                <p>$$\det(A) = \begin{vmatrix} 1 & 2 \\ 3 & k \end{vmatrix} = 0 \implies (1 \cdot k) - (2 \cdot 3) = 0 \implies k - 6 = 0 \implies \mathbf{k = 6}$$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: $k=6$ olmalıdır. $k=6$ yazıldığında $x = -2t, y = t$ sonsuz çözümü elde edilir.</p>
            </div>
        </div>
    </div>
</div>
"""
    },
    {
        "id": "bolum3",
        "title": "Bölüm 3: Matris Cebiri",
        "badge": "Hafta 3 & 12",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>""",
        "content": r"""
<div class="space-y-6">
    <!-- 3.1 Özel Matrisler ve Sayısal Örnekler -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">3.1</span>
            <h4 class="text-lg font-bold text-white">Özel Matris Tipleri ve Sayısal Gösterimleri</h4>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs text-slate-300 font-mono">
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5">
                <strong class="text-indigo-400 block font-bold mb-1">Köşegen Matris:</strong>
                $\begin{bmatrix} 4 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 7 \end{bmatrix}$
                <span class="text-slate-400 text-[11px] block mt-1">Köşegen dışı tamamen 0.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5">
                <strong class="text-indigo-400 block font-bold mb-1">Skaler Matris:</strong>
                $\begin{bmatrix} 5 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 5 \end{bmatrix}$
                <span class="text-slate-400 text-[11px] block mt-1">Köşegendeki tüm sayılar eşit.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5">
                <strong class="text-indigo-400 block font-bold mb-1">Birim Matris ($I$):</strong>
                $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$
                <span class="text-slate-400 text-[11px] block mt-1">Köşegeni 1, diğerleri 0.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5">
                <strong class="text-indigo-400 block font-bold mb-1">Üst Üçgen Matris:</strong>
                $\begin{bmatrix} 2 & 3 & 4 \\ 0 & 5 & 1 \\ 0 & 0 & 6 \end{bmatrix}$
                <span class="text-slate-400 text-[11px] block mt-1">Köşegen altı tamamen 0.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5">
                <strong class="text-indigo-400 block font-bold mb-1">Alt Üçgen Matris:</strong>
                $\begin{bmatrix} 1 & 0 & 0 \\ 4 & 2 & 0 \\ 3 & 5 & 8 \end{bmatrix}$
                <span class="text-slate-400 text-[11px] block mt-1">Köşegen üstü tamamen 0.</span>
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5">
                <strong class="text-indigo-400 block font-bold mb-1">Sıfır Matrisi ($O$):</strong>
                $\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$
                <span class="text-slate-400 text-[11px] block mt-1">Tüm elemanları 0.</span>
            </div>
        </div>

        <!-- 3.1 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3 mt-4">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                3.1 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 7 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 7 \end{bmatrix}$ ve $B = \begin{bmatrix} 2 & 0 & 0 \\ 4 & 5 & 0 \\ 1 & -3 & 6 \end{bmatrix}$ matrislerinin tiplerini belirleyiniz.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>$A$ Matrisi İncelemesi:</strong><br>
                Köşegen dışındaki tüm elemanlar 0 olduğu için bir <strong>köşegen matristir</strong>. Köşegendeki tüm sayılar birbirine eşit ($7$) olduğu için aynı zamanda bir <strong>skaler matristir</strong> ($A = 7 \cdot I_3$).</p>
                <p><strong>$B$ Matrisi İncelemesi:</strong><br>
                Köşegenin üzerindeki tüm elemanlar 0'dır ($a_{12}=0, a_{13}=0, a_{23}=0$). Dolayısıyla bu bir <strong>alt üçgen matristir</strong> (Lower triangular).</p>
            </div>
        </div>
    </div>

    <!-- 3.2 Matris Eşitliği, Toplama, Skaler Çarpım -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">3.2</span>
            <h4 class="text-lg font-bold text-white">Matris Eşitliği ve Toplama/Çıkarma İşlemleri</h4>
        </div>

        <!-- 3.2 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                3.2 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 1 & 3 \\ 2 & 0 \end{bmatrix}$ ve $B = \begin{bmatrix} 4 & -1 \\ 0 & 2 \end{bmatrix}$ ise $2A - B$ matrisini bulunuz.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p>• $2A$ skaler çarpımı (her elemanı 2 ile çarp):<br>
                $$2A = 2 \cdot \begin{bmatrix} 1 & 3 \\ 2 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 6 \\ 4 & 0 \end{bmatrix}$$</p>
                <p>• $2A - B$ çıkarma işlemi (karşılıklı elemanları çıkar):<br>
                $$2A - B = \begin{bmatrix} 2 - 4 & 6 - (-1) \\ 4 - 0 & 0 - 2 \end{bmatrix} = \begin{bmatrix} -2 & 7 \\ 4 & -2 \end{bmatrix}$$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: $2A - B = \begin{bmatrix} -2 & 7 \\ 4 & -2 \end{bmatrix}$'dir.</p>
            </div>
        </div>
    </div>

    <!-- 3.3 Matris Çarpımı -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">3.3</span>
            <h4 class="text-lg font-bold text-white">Matris Çarpımı ($A \cdot B$) - Satır $\times$ Sütun</h4>
        </div>

        <!-- 3.3 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                3.3 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ ve $B = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}$ ise $A \cdot B$ matrisini hesaplayınız.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p>• 1. Satır $\times$ 1. Sütun: $(1 \cdot 2) + (2 \cdot 1) = 2 + 2 = \mathbf{4}$</p>
                <p>• 1. Satır $\times$ 2. Sütun: $(1 \cdot 0) + (2 \cdot 3) = 0 + 6 = \mathbf{6}$</p>
                <p>• 2. Satır $\times$ 1. Sütun: $(3 \cdot 2) + (4 \cdot 1) = 6 + 4 = \mathbf{10}$</p>
                <p>• 2. Satır $\times$ 2. Sütun: $(3 \cdot 0) + (4 \cdot 3) = 0 + 12 = \mathbf{12}$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: $$A \cdot B = \begin{bmatrix} 4 & 6 \\ 10 & 12 \end{bmatrix}$$</p>
            </div>
        </div>
        <div class="p-3.5 rounded-xl bg-rose-950/30 border border-rose-500/40 text-rose-300 text-xs">
            <span class="badge badge-accent">ÖNEMLİ DİKKAT</span> $B \cdot A$ çarpımını yapsaydık sonuç $\begin{bmatrix} 2 & 4 \\ 10 & 14 \end{bmatrix}$ çıkacaktı. $AB \neq BA$!
        </div>
    </div>

    <!-- 3.4 Transpoz, Simetrik, Antisimetrik -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">3.4</span>
            <h4 class="text-lg font-bold text-white">Transpoz, Simetrik ve Antisimetrik Matrisler</h4>
        </div>

        <!-- 3.4 Sayısal Örnekler -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs font-mono">
            <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-1.5">
                <span class="text-emerald-400 font-bold block">Simetrik Matris Örneği ($A^T = A$):</span>
                $$S = \begin{bmatrix} 1 & \mathbf{3} & \mathbf{4} \\ \mathbf{3} & 2 & \mathbf{5} \\ \mathbf{4} & \mathbf{5} & 6 \end{bmatrix} \implies S^T = S$$
                <span class="text-slate-400">Köşegene göre katlandığında sayılar birebir çakışır.</span>
            </div>
            <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-1.5">
                <span class="text-rose-400 font-bold block">Antisimetrik Matris Örneği ($A^T = -A$):</span>
                $$K = \begin{bmatrix} \mathbf{0} & 2 & -3 \\ -2 & \mathbf{0} & 4 \\ 3 & -4 & \mathbf{0} \end{bmatrix} \implies K^T = -K$$
                <span class="text-amber-300 font-bold">Kural: Köşegen elemanları MUTLAKA SIFIR (0) olmalıdır!</span>
            </div>
        </div>

        <!-- 3.4 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3 mt-4">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                3.4 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 2 & 5 & 1 \\ 4 & -3 & 7 \end{bmatrix}$ matrisinin transpozunu ($A^T$) bulunuz ve $(A^T)^T$ ifadesinin neye eşit olduğunu gösteriniz.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>Adım 1: Satırları Sütun Yap ($A^T$):</strong><br>
                $A$, $2 \times 3$ boyutundadır. Transpozu $3 \times 2$ olacaktır:<br>
                1. satır $[2, 5, 1]$ sütun olur: $\begin{bmatrix} 2 \\ 5 \\ 1 \end{bmatrix}$<br>
                2. satır $[4, -3, 7]$ sütun olur: $\begin{bmatrix} 4 \\ -3 \\ 7 \end{bmatrix}$<br>
                $$A^T = \begin{bmatrix} 2 & 4 \\ 5 & -3 \\ 1 & 7 \end{bmatrix}$$</p>
                <p><strong>Adım 2: Tekrar Transpoz Al:</strong><br>
                $$(A^T)^T = \begin{bmatrix} 2 & 5 & 1 \\ 4 & -3 & 7 \end{bmatrix} = A$$</p>
                <p class="text-indigo-400 font-bold pt-1">Kural: Bir matrisin iki kere transpozu alınırsa kendisi elde edilir: $(A^T)^T = A$.</p>
            </div>
        </div>
    </div>

    <!-- 3.5 Ters Matris ve Singülerlik -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">3.5</span>
            <h4 class="text-lg font-bold text-white">Kare Matrisin Tersi ($A^{-1}$) ve Singülerlik</h4>
        </div>

        <!-- 3.5 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                3.5 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 2 & 1 \\ 5 & 3 \end{bmatrix}$ matrisinin tersini ($A^{-1}$) bulunuz.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>Adım 1: Determinantı Hesapla:</strong><br>
                $$|A| = (2 \cdot 3) - (1 \cdot 5) = 6 - 5 = \mathbf{1} \neq 0$$
                $|A| \neq 0$ olduğu için tersi vardır!</p>
                <p><strong>Adım 2: $2\times 2$ Ters Formülünü Uygula:</strong><br>
                Köşegendeki 2 ve 3 yer değiştirir, 1 ve 5 eksi alır:<br>
                $$A^{-1} = \frac{1}{|A|} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix} = \frac{1}{1} \begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix} = \mathbf{\begin{bmatrix} 3 & -1 \\ -5 & 2 \end{bmatrix}}$$</p>
                <p class="text-emerald-400 font-bold pt-1">Doğrulama: $A \cdot A^{-1} = \begin{bmatrix} 2&1\\5&3 \end{bmatrix} \begin{bmatrix} 3&-1\\-5&2 \end{bmatrix} = \begin{bmatrix} 1&0\\0&1 \end{bmatrix} = I$.</p>
            </div>
        </div>
    </div>

    <!-- 3.6 Karakteristik Matris ve Özdeğerler -->
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">3.6</span>
            <h4 class="text-lg font-bold text-white">Karakteristik Denklem ve Özdeğerler ($\lambda$)</h4>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">
            Karakteristik matris $A - \lambda I$ matrisidir. Determinantı sıfıra eşitlenerek ($|A - \lambda I| = 0$) özdeğerler bulunur.
        </p>

        <!-- 3.6 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                3.6 İçin Tam Çözümlü Sayısal Örnek (Hafta 3 / 12 Konusu):
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 2 & 2 \\ 1 & 3 \end{bmatrix}$ matrisinin özdeğerlerini ($\lambda_1, \lambda_2$) bulunuz.
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p><strong>Adım 1: Karakteristik Matrisi Yaz ($A - \lambda I$):</strong><br>
                $$A - \lambda I = \begin{bmatrix} 2 - \lambda & 2 \\ 1 & 3 - \lambda \end{bmatrix}$$</p>
                <p><strong>Adım 2: Determinantı Sıfıra Eşitle:</strong><br>
                $$|A - \lambda I| = (2 - \lambda)(3 - \lambda) - (2 \cdot 1) = 0$$<br>
                $$6 - 5\lambda + \lambda^2 - 2 = 0 \implies \lambda^2 - 5\lambda + 4 = 0$$</p>
                <p><strong>Adım 3: Çarpanlara Ayır:</strong><br>
                $$(\lambda - 1)(\lambda - 4) = 0 \implies \mathbf{\lambda_1 = 1, \quad \lambda_2 = 4}$$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: Matrisin özdeğerleri $\lambda_1 = 1$ ve $\lambda_2 = 4$'tür.</p>
            </div>
        </div>
    </div>
</div>
"""
    },
    {
        "id": "bolum4",
        "title": "Bölüm 4: Denk Matrisler & Rank",
        "badge": "Hafta 5 & 12",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>""",
        "content": r"""
<div class="space-y-6">
    <!-- 4.0 Bölüm Başlığı & Masterclass Rozetleri -->
    <div class="glass-3d-card p-6 sm:p-8 rounded-2xl border border-white/5 space-y-6">
        <div class="flex flex-wrap items-center justify-between gap-3 border-b border-white/5 pb-4">
            <div class="flex items-center gap-3">
                <span class="px-2.5 py-1 rounded-md bg-emerald-500/20 text-emerald-400 font-mono text-xs font-bold">4.0</span>
                <h4 class="text-lg sm:text-xl font-bold text-white tracking-tight">Denk Matrisler, Eşelon Form & Rank Masterclass</h4>
            </div>
            <div class="flex flex-wrap items-center gap-2">
                <span class="px-2.5 py-0.5 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-[11px] font-mono">Çocuğa Anlatır Gibi Sıfırdan Mantık</span>
                <span class="px-2.5 py-0.5 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-400 text-[11px] font-mono">Dedektif Analojisi</span>
            </div>
        </div>

        <!-- 4.1: Rank Nedir? (Çocuğa Anlatır Gibi Dedektif Analojisi) -->
        <div class="space-y-3">
            <h5 class="text-sm font-bold text-emerald-400 flex items-center gap-2 uppercase tracking-wider">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                4.1 Rank Nedir? (Çocuğa Anlatır Gibi Dedektif Analojisi)
            </h5>
            <p class="text-slate-300 text-sm leading-relaxed">
                Kitaplar rankı <em>"alt determinantların en büyük mertebesi"</em> veya <em>"boyut"</em> gibi karışık tanımlarla anlatır. Gelin bunu <strong>ilkokul seviyesinde bir benzetmeyle</strong> kafamıza kazıyalım:
            </p>
            
            <!-- Analoji Kutusu -->
            <div class="p-5 rounded-2xl bg-indigo-950/30 border border-indigo-500/30 space-y-3">
                <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
                    Dedektif Masası Analojisi:
                </span>
                <p class="text-slate-200 text-xs sm:text-sm leading-relaxed">
                    Bir masada 3 adet bilgi notu olduğunu düşünün:<br>
                    • <strong>1. Not:</strong> <em>"Ahmet 1 ekmek aldı = 10 TL"</em><br>
                    • <strong>2. Not:</strong> <em>"Ahmet 1 süt aldı = 20 TL"</em><br>
                    • <strong>3. Not:</strong> <em>"Ahmet 2 ekmek ve 2 süt aldı = 60 TL"</em><br>
                    3. nota dikkatle bakın: 1. ve 2. notu 2 ile çarpıp toplarsanız zaten 3. not çıkar! Yani 3. not masaya <strong>HİÇBİR YENİ BİLGİ KATMAZ</strong>, gereksiz bir kopyadır (çöptür)!
                </p>
                <div class="p-3 rounded-xl bg-slate-950/60 border border-white/5 text-xs text-indigo-200 font-mono">
                    İşte matrislerde her bir satır bir ifadedir. Birbirinin kopyası olan satırları elediğimizde masada geriye kalan <strong>GERÇEK, YENİ VE SIFIRLANMAYAN SATIR SAYISINA "RANK" DENİR!</strong>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2 text-xs text-slate-300">
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 text-center space-y-1">
                    <span class="text-emerald-400 font-bold block">Rank = 3</span>
                    <p class="text-[11px] text-slate-400">3 satır da birbirinden bağımsızdır. Hiçbir satır sıfırlanamaz (Tam Rank).</p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 text-center space-y-1">
                    <span class="text-amber-400 font-bold block">Rank = 2</span>
                    <p class="text-[11px] text-slate-400">1 satır diğerlerinin kopyasıdır ve işlem yapılınca tamamen $[0, 0, 0]$ olup elenir.</p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 text-center space-y-1">
                    <span class="text-rose-400 font-bold block">Rank = 1</span>
                    <p class="text-[11px] text-slate-400">2 satır birden gereksiz kopyadır ve elenir. Geriye sadece tek bir satır kalır.</p>
                </div>
            </div>
        </div>

        <!-- 4.2: Denk Matrisler ve 3 Elementer Satır İşlemi -->
        <div class="space-y-3 pt-4 border-t border-white/5">
            <h5 class="text-sm font-bold text-emerald-400 flex items-center gap-2 uppercase tracking-wider">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg>
                4.2 Denk Matrisler ($A \sim B$) ve 3 Yasal Matematik Hamlesi
            </h5>
            <p class="text-slate-300 text-sm leading-relaxed">
                Neden iki matris arasına eşittir ($=$) değil de denktir ($\sim$) işareti koyarız? Çünkü satır işlemleri yaparken sayılar değişir ama matrisin özü, çözümü ve <strong>RANKI ASLA DEĞİŞMEZ!</strong>
            </p>
            <p class="text-slate-300 text-sm leading-relaxed">
                Bir matrise uygulayabileceğiniz <strong>sadece 3 yasal işlem</strong> vardır:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs text-slate-300">
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1.5">
                    <strong class="text-indigo-400 block font-mono">1. Satır Takası ($S_i \leftrightarrow S_j$)</strong>
                    <p class="text-[11px] text-slate-400">İki satırın yerini değiştirebilirsiniz. Örneğin üst satırda $1$ elde etmek için 1. satırla 3. satırı takas edebilirsiniz.</p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1.5">
                    <strong class="text-teal-400 block font-mono">2. Sabitle Çarpma ($c \cdot S_i \to S_i$)</strong>
                    <p class="text-[11px] text-slate-400">Bir satırdaki tüm sayıları sıfırdan farklı bir sayıyla ($c \neq 0$) çarpabilir veya bölebilirsiniz (örneğin 2'ye bölmek).</p>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1.5">
                    <strong class="text-emerald-400 block font-mono">3. Katını Ekleme/Çıkarma ($S_i + c S_j$)</strong>
                    <p class="text-[11px] text-slate-400">En güçlü silahımız! Bir satırın $c$ katını alıp diğer satıra ekleyerek altındaki sayıları sıfırlarız.</p>
                </div>
            </div>
        </div>

        <!-- 4.3: Eşelon (Basamak) Form ve Pivot Nedir? -->
        <div class="space-y-3 pt-4 border-t border-white/5">
            <h5 class="text-sm font-bold text-emerald-400 flex items-center gap-2 uppercase tracking-wider">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
                4.3 Eşelon (Basamak) Form ve Pivot Nedir?
            </h5>
            <p class="text-slate-300 text-sm leading-relaxed">
                Rank bulabilmek için matrisi <strong>merdiven basamağı</strong> haline getirmemiz gerekir. Buna <strong>Eşelon Form</strong> denir.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-2">
                    <span class="text-xs font-mono font-bold text-indigo-400 block">1. Pivot (Baş Eleman) Nedir?</span>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Bir satırda soldan sağa bakarken karşılaştığınız <strong>İLK SIFIR OLMAYAN SAYI</strong> o satırın pivotudur.<br>
                        Örnek: $[0, 0, \mathbf{4}, -1, 3]$ satırının pivotu $\mathbf{4}$'tür.
                    </p>
                </div>
                <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-2">
                    <span class="text-xs font-mono font-bold text-teal-400 block">2. Eşelon Formun 3 Kuralı</span>
                    <ul class="text-xs text-slate-300 space-y-1 list-disc list-inside">
                        <li>Her satırın pivotu, üsttekinin <strong>sağında</strong> olmalıdır (merdiven iner gibi).</li>
                        <li>Her pivotun <strong>altındaki tüm sayılar $0$</strong> olmalıdır.</li>
                        <li>Tamamen sıfır $[0, 0, \dots, 0]$ olan satırlar <strong>en altta</strong> toplanmalıdır.</li>
                    </ul>
                </div>
            </div>

            <!-- Görsel Şablon -->
            <div class="p-4 rounded-xl bg-slate-950/70 border border-white/5 text-center space-y-2">
                <span class="text-xs font-mono text-slate-400">Kusursuz Bir Eşelon Form Görseli:</span>
                <div class="text-sm sm:text-base font-mono text-emerald-300 font-bold py-2">
                    $$\begin{bmatrix}
                    \mathbf{1} & 3 & -1 & 5 \\
                    0 & \mathbf{2} & 4 & 1 \\
                    0 & 0 & \mathbf{5} & -2 \\
                    0 & 0 & 0 & 0
                    \end{bmatrix} \implies \text{Pivotlar: } 1, 2, 5 \implies \mathbf{\text{Rank} = 3}$$
                </div>
                <p class="text-[11px] text-slate-400">4. satır tamamen sıfırlandı; sıfır olmayan 3 satır kaldı. O halde rank = 3'tür!</p>
            </div>
        </div>

        <!-- 4.4: 5 Adımda Rank Bulma Algoritması -->
        <div class="space-y-3 pt-4 border-t border-white/5">
            <h5 class="text-sm font-bold text-emerald-400 flex items-center gap-2 uppercase tracking-wider">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/></svg>
                4.4 Yemek Tarifi Gibi: 5 Adımda Rank Bulma Rehberi
            </h5>
            <ol class="space-y-2 text-xs sm:text-sm text-slate-300 list-decimal list-inside pl-2 font-mono">
                <li><strong>Sol Üst Köşeyi Kontrol Et ($a_{11}$):</strong> Sayı $0$ ise, alt satırlardan sıfır olmayan (mümkünse başında $1$ olan) bir satırla yer değiştir ($S_1 \leftrightarrow S_i$).</li>
                <li><strong>1. Sütunu Temizle:</strong> $a_{11}$'in altındaki tüm sayıları $S_k \leftarrow S_k - c \cdot S_1$ formülüyle sıfırla!</li>
                <li><strong>2. Satıra Geç:</strong> 2. satırın pivotunu ($a_{22}$) belirle ve onun da altındaki tüm sayıları sıfırla.</li>
                <li><strong>Sıfır Satırlarını En Dibe Gönder:</strong> İşlemler sırasında tamamen sıfıra $[0, 0, \dots, 0]$ dönüşen satırlar olursa en alta taşı.</li>
                <li><strong>Hayatta Kalan Satırları Say:</strong> Tamamen sıfır olmayan satırların toplam adedi senin <strong>RANK</strong>'ındır!</li>
            </ol>
        </div>
    </div>

    <!-- ÖRNEK 1 -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-white/5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/5 pb-2">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                Örnek 1: $3 \times 3$ Matriste Bir Satırın Sıfırlanması & Rank Hesabı
            </span>
            <span class="text-[11px] font-mono text-slate-400">Temel Seviye</span>
        </div>
        <p class="text-slate-200 text-sm font-semibold">
            Soru: $A = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 4 & -2 \\ 3 & 1 & 4 \end{bmatrix}$ matrisinin rankını bulunuz.
        </p>
        <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
            <p class="text-emerald-300 font-bold">Adım 1: 1. Satır pivotumuz $a_{11} = 1$. Altındaki $2$ ve $3$ sayılarını sıfırlayalım:</p>
            <p>• $S_2 \leftarrow S_2 - 2S_1 = [2, 4, -2] - 2 \cdot [1, 2, -1] = [2-2, 4-4, -2 - (-2)] = [\mathbf{0, 0, 0}]$<br>
            <span class="text-amber-400 font-sans">Aman Allahım! 2. satır tamamen sıfırlandı! Çünkü 2. satır, 1. satırın tam 2 katıydı (bağımlıydı)!</span></p>
            <p>• $S_3 \leftarrow S_3 - 3S_1 = [3, 1, 4] - 3 \cdot [1, 2, -1] = [3-3, 1-6, 4 - (-3)] = [\mathbf{0, -5, 7}]$</p>

            <p class="text-emerald-300 font-bold pt-2">Adım 2: Sıfırlanan satırı en alta kaydıralım ($S_2 \leftrightarrow S_3$):</p>
            <p>$$A \sim \begin{bmatrix} 1 & 2 & -1 \\ 0 & -5 & 7 \\ 0 & 0 & 0 \end{bmatrix}$$</p>

            <p class="text-emerald-300 font-bold pt-2">Adım 3: Eşelon Formu Değerlendirelim:</p>
            <p>• 1. Satır: $[1, 2, -1]$ (Sıfırdan farklı)</p>
            <p>• 2. Satır: $[0, -5, 7]$ (Sıfırdan farklı)</p>
            <p>• 3. Satır: $[0, 0, 0]$ (Tamamen sıfır, ranka dahil edilmez!)</p>
            <p class="text-emerald-400 font-bold text-sm pt-1">Sonuç: Sıfır olmayan 2 satır kaldığı için $\mathbf{\text{rank}(A) = 2}$'dir!</p>
        </div>
    </div>

    <!-- ÖRNEK 2 -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-white/5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/5 pb-2">
            <span class="text-xs font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                Örnek 2: $3 \times 4$ Dikdörtgen Matriste Eşelon Form ve Rank
            </span>
            <span class="text-[11px] font-mono text-teal-300">Orta Seviye</span>
        </div>
        <p class="text-slate-200 text-sm font-semibold">
            Soru: $B = \begin{bmatrix} 1 & -2 & 0 & 3 \\ 2 & -4 & 1 & 5 \\ 3 & -6 & 2 & 7 \end{bmatrix}$ matrisinin rankını bulunuz.
        </p>
        <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
            <p class="text-teal-300 font-bold">Adım 1: 1. Sütunu Sıfırlayalım:</p>
            <p>• $S_2 \leftarrow S_2 - 2S_1 = [2, -4, 1, 5] - [2, -4, 0, 6] = [\mathbf{0, 0, 1, -1}]$</p>
            <p>• $S_3 \leftarrow S_3 - 3S_1 = [3, -6, 2, 7] - [3, -6, 0, 9] = [\mathbf{0, 0, 2, -2}]$</p>
            <p>Matris:<br>
            $$\begin{bmatrix} 1 & -2 & 0 & 3 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 2 & -2 \end{bmatrix}$$</p>

            <p class="text-teal-300 font-bold pt-2">Adım 2: 3. Sütun Pivotuyla 3. Satırı Sıfırlayalım:</p>
            <p>2. satır $[0, 0, 1, -1]$ ve 3. satır $[0, 0, 2, -2]$ dikkat ederseniz birbirinin tam 2 katıdır!<br>
            $S_3 \leftarrow S_3 - 2S_2 = [0, 0, 2, -2] - 2 \cdot [0, 0, 1, -1] = [\mathbf{0, 0, 0, 0}]$ (3. satır tamamen sıfırlandı!)</p>

            <p class="text-teal-300 font-bold pt-2">Adım 3: Eşelon Form:</p>
            <p>$$\begin{bmatrix} 1 & -2 & 0 & 3 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$</p>
            <p class="text-emerald-400 font-bold text-sm pt-1">Sonuç: Sıfır olmayan satır sayısı 2'dir $\implies \mathbf{\text{rank}(B) = 2}$!</p>
        </div>
    </div>

    <!-- ÖRNEK 3 -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-white/5 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/5 pb-2">
            <span class="text-xs font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                Örnek 3: $4 \times 4$ Matriste Pivot Takası ve Vize Seviyesi Rank Hesabı
            </span>
            <span class="text-[11px] font-mono text-purple-300">Vize Seviyesi Ağır Soru</span>
        </div>
        <p class="text-slate-200 text-sm font-semibold">
            Soru: $C = \begin{bmatrix} 2 & 4 & 2 & 6 \\ 1 & 2 & 2 & 5 \\ 3 & 6 & 5 & 14 \\ 1 & 2 & 0 & 1 \end{bmatrix}$ matrisinin rankını bulunuz.
        </p>
        <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
            <p class="text-amber-400 font-sans font-bold">Taktik: 1. satırı 2'ye bölüp kesirlerle uğraşmak yerine 2. satırdaki hazır $1$'i yukarı taşıyalım ($S_1 \leftrightarrow S_2$):</p>
            <p>$$C \sim \begin{bmatrix} 1 & 2 & 2 & 5 \\ 2 & 4 & 2 & 6 \\ 3 & 6 & 5 & 14 \\ 1 & 2 & 0 & 1 \end{bmatrix}$$</p>

            <p class="text-purple-300 font-bold pt-2">Adım 1: 1. Sütunu Sıfırlayalım:</p>
            <p>• $S_2 \leftarrow S_2 - 2S_1 = [0, 0, -2, -4]$ ($-2$'ye bölersek: $[0, 0, 1, 2]$)</p>
            <p>• $S_3 \leftarrow S_3 - 3S_1 = [0, 0, -1, -1]$</p>
            <p>• $S_4 \leftarrow S_4 - S_1 = [0, 0, -2, -4]$ (Dikkat! 2. satır ile 4. satır tıpatıp aynı oldu!)</p>

            <p class="text-purple-300 font-bold pt-2">Adım 2: 4. Satırı Sıfırlayalım ($S_4 \leftarrow S_4 - S_2$):</p>
            <p>$$[0, 0, -2, -4] - [0, 0, -2, -4] = [\mathbf{0, 0, 0, 0}]$$</p>

            <p class="text-purple-300 font-bold pt-2">Adım 3: 3. Satırdaki Pivotu Bulalım ($S_3 + S_2'$):</p>
            <p>$S_2$ satırını $[-2, -4]$ halinden $[1, 2]$ yaptık. $S_3$ satırı $[-1, -1]$ idi. İkisini toplarsak:<br>
            $[0, 0, -1, -1] + [0, 0, 1, 2] = [\mathbf{0, 0, 0, 1}]$</p>

            <p class="text-purple-300 font-bold pt-2">Adım 4: Son Eşelon Form:</p>
            <p>$$\begin{bmatrix} 1 & 2 & 2 & 5 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$</p>
            <p class="text-emerald-400 font-bold text-sm pt-1">Sonuç: 3 adet sıfırdan farklı basamak satırı kaldı $\implies \mathbf{\text{rank}(C) = 3}$!</p>
        </div>
    </div>

    <!-- 4.6: Ek Matris (Adjoint - adj(A)) ve Ters Matris İlişkisi (Detaylı Anlatım) -->
    <div class="glass-3d-card p-6 sm:p-8 rounded-2xl border border-white/5 space-y-6">
        <!-- Başlık -->
        <div class="flex items-center gap-3 border-b border-white/5 pb-4">
            <span class="px-3 py-1 rounded-lg bg-emerald-500/20 text-emerald-400 font-mono text-xs font-bold">4.6</span>
            <div>
                <h4 class="text-lg sm:text-xl font-bold text-white">Ek Matris (Adjoint - $\text{adj}(A)$) ve Ters Matris ($A^{-1}$) Rehberi</h4>
                <p class="text-xs text-slate-400">Sıfırdan zirveye: Mantık, 4 adımlı algoritma, $2\times 2$ hilesi, adım adım $3\times 3$ çözümü ve sınav tuzakları</p>
            </div>
        </div>

        <!-- 4.6.1: Çocuğa Anlatır Gibi: Matrislerde Bölme Neden Yok ve Adjoint Nereden Çıktı? -->
        <div class="p-5 rounded-2xl bg-indigo-950/25 border border-indigo-500/30 space-y-3">
            <div class="flex items-center gap-2 text-indigo-400 font-bold text-sm">
                <svg class="w-5 h-5 text-indigo-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <span>Temel Mantık: Matrislerde Neden Bölme Yok ve Ters Matris ($A^{-1}$) Nedir?</span>
            </div>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                İlkokul matematiğinde bir sayıyı etkisiz eleman olan $1$'e götürmek için böleriz: $5 \div 5 = 1$ ya da çarpımsal tersini kullanırız: $5 \cdot \frac{1}{5} = 5 \cdot 5^{-1} = 1$.
            </p>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                Fakat matrisler dünyasında <strong class="text-rose-400 underline">BÖLME İŞLEMİ DİYE BİR ŞEY YOKTUR!</strong> Yani bir matrisi başka bir matrise bölemezsiniz: $\frac{B}{A}$ yazımı matematiksel olarak kesinlikle <u>tanımsız ve yasaktır</u>.
            </p>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                Bölme yapamadığımız için matematikçiler bir çözüm buldu: "Madem bölemiyoruz, o zaman bir $A$ matrisini öyle bir matrisle çarpalım ki sonuç etkisiz matris olan <strong>Birim Matris ($I$)</strong> çıksın!" dediler:
                $$A \cdot A^{-1} = A^{-1} \cdot A = I$$
                İşte bu $A^{-1}$ matrisini inşa eden en güçlü sihirli köprü <strong>Ek Matris (Adjoint Matris, $\text{adj}(A)$)</strong>'tir!
            </p>
            <div class="p-3.5 rounded-xl bg-slate-900/80 border border-indigo-500/30 text-center">
                <span class="text-xs text-indigo-300 font-mono block mb-1">ALTIN FORMÜL (TÜM VİZENİN EN KRİTİK FORMÜLÜ)</span>
                <p class="text-base sm:text-lg font-bold text-white">$$A^{-1} = \frac{1}{|A|} \text{adj}(A)$$</p>
                <p class="text-xs text-slate-400 mt-1">Burada $|A|$ sıradan bir <strong>sayıdır (skaler)</strong>, $\text{adj}(A)$ ise bir <strong>matristir</strong>. Bir matrisin tüm elemanlarını tek bir sayıya bölmek çok kolaydır!</p>
            </div>
        </div>

        <!-- 4.6.2: Adjoint ve Tersini Bulmanın 4 Adımlı Kusursuz Algoritması -->
        <div class="space-y-3">
            <h5 class="text-sm font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                Adjoint ve Ters Matris Bulmanın 4 Aşamalı Yol Haritası
            </h5>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                <!-- Adım 1 -->
                <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-2">
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-400">1. AŞAMA</span>
                        <strong class="text-white text-xs sm:text-sm">Güvenlik Kapısı: $|A| \neq 0$ mı?</strong>
                    </div>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Hemen kofaktör hesaplamaya başlama! Önce matrisin determinantını ($|A|$) bul. Eğer <strong>$|A| = 0$</strong> çıkarsa formüldeki payda sıfır olacağından <strong>TERSİ YOKTUR</strong> (Tekil / Singüler Matris)! "Tersi yoktur" yaz ve işlemi hemen bitir.
                    </p>
                </div>
                <!-- Adım 2 -->
                <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 space-y-2">
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-blue-500/20 text-blue-400">2. AŞAMA</span>
                        <strong class="text-white text-xs sm:text-sm">Kofaktörler Matrisi ($C$) Hesabı</strong>
                    </div>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Her elemanın satırını ve sütununu elinle kapat. Kalan küçük determinantı (Minör $M_{ij}$) hesapla. Ardından dama tahtası işaretiyle ($(-1)^{i+j}$) çarpıp kofaktör $A_{ij}$'yi bul ve matris formatında diz.
                    </p>
                </div>
                <!-- Adım 3 -->
                <div class="p-4 rounded-xl bg-rose-950/20 border border-rose-500/30 space-y-2">
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-400">3. AŞAMA</span>
                        <strong class="text-rose-300 text-xs sm:text-sm">EN BÜYÜK TUZAK: TRANSPOZE AL!</strong>
                    </div>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Hocaların öğrencileri elediği yer: Bulduğun Kofaktör Matrisi henüz Adjoint değildir! <strong>$\text{adj}(A) = C^T$</strong>'dir. Yani Kofaktör matrisinin <strong>satırlarını sütun yapacaksın</strong>! Bu adımı atlarsan soru gider.
                    </p>
                </div>
                <!-- Adım 4 -->
                <div class="p-4 rounded-xl bg-emerald-950/20 border border-emerald-500/30 space-y-2">
                    <div class="flex items-center gap-2">
                        <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-400">4. AŞAMA</span>
                        <strong class="text-emerald-300 text-xs sm:text-sm">Determinanta Böl ($A^{-1}$)</strong>
                    </div>
                    <p class="text-xs text-slate-300 leading-relaxed">
                        Bulduğun $\text{adj}(A)$ matrisinin her bir elemanını ilk adımda hesapladığın $|A|$ sayısına böl: $A^{-1} = \frac{1}{|A|} \text{adj}(A)$. Ters matrisin artık hazır!
                    </p>
                </div>
            </div>
        </div>

        <!-- 4.6.3: 5 Saniyelik Yıldırım Hilesi (2x2 Matrisler İçin) -->
        <div class="p-5 rounded-2xl bg-amber-950/20 border border-amber-500/30 space-y-3">
            <div class="flex items-center gap-2 text-amber-400 font-bold text-sm">
                <svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                <span>5 Saniyelik Pratik Hile: $2 \times 2$ Matrislerin Adjoint'i ve Tersi</span>
            </div>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                $2 \times 2$ bir matris verildiğinde kofaktörlerle uğraşarak vakit kaybetmeyin! Tek kural vardır:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs font-mono">
                <div class="p-3 bg-slate-900/80 rounded-xl border border-white/5 space-y-1">
                    <span class="text-amber-400 font-bold block">1. KURAL: Esas Köşegen</span>
                    $a$ ile $d$'yi <strong>YER DEĞİŞTİR</strong>!
                </div>
                <div class="p-3 bg-slate-900/80 rounded-xl border border-white/5 space-y-1">
                    <span class="text-amber-400 font-bold block">2. KURAL: Yan Köşegen</span>
                    $b$ ile $c$'nin <strong>İŞARETİNİ DEĞİŞTİR</strong> ($-1$ ile çarp)!
                </div>
            </div>
            <div class="p-4 bg-slate-950/80 rounded-xl border border-amber-500/20 text-center font-mono text-xs sm:text-sm text-slate-200">
                $$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \implies \mathbf{\text{adj}(A) = \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}} \implies \mathbf{A^{-1} = \frac{1}{ad - bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}}$$
            </div>
            <div class="text-xs text-slate-300 space-y-1 bg-slate-900/50 p-3 rounded-lg border border-white/5">
                <p><strong>Örnek:</strong> $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ olsun.</p>
                <p>• $|A| = (1 \cdot 4) - (2 \cdot 3) = 4 - 6 = -2$</p>
                <p>• 1 ve 4 yer değiştirir, 2 ve 3 eksi olur $\implies \text{adj}(A) = \begin{bmatrix} 4 & -2 \\ -3 & 1 \end{bmatrix}$</p>
                <p>• $A^{-1} = -\frac{1}{2} \begin{bmatrix} 4 & -2 \\ -3 & 1 \end{bmatrix} = \begin{bmatrix} -2 & 1 \\ \frac{3}{2} & -\frac{1}{2} \end{bmatrix}$ (Tam 5 saniye!).</p>
            </div>
        </div>

        <!-- 4.6.4: 3x3 Matris İçin Adım Adım Başyapıt Örnek (Hiçbir Adım Atlanmadan) -->
        <div class="p-5 sm:p-6 rounded-2xl bg-cyan-950/20 border border-cyan-500/30 space-y-4">
            <div class="flex items-center justify-between flex-wrap gap-2 border-b border-cyan-500/20 pb-3">
                <span class="text-xs sm:text-sm font-bold text-cyan-400 uppercase tracking-wider flex items-center gap-1.5">
                    <svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    $3 \times 3$ Boyutunda Kusursuz Sayısal Başyapıt Örnek
                </span>
                <span class="text-[11px] font-mono px-2.5 py-0.5 rounded-full bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">Tüm 9 Kofaktör Açıkça Hesaplanmıştır</span>
            </div>

            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A = \begin{bmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{bmatrix}$ matrisinin Adjoint matrisini ($\text{adj}(A)$) ve ters matrisini ($A^{-1}$) adım adım bulunuz.
            </p>

            <!-- 1. Adım: Determinant -->
            <div class="p-4 rounded-xl bg-slate-900/80 border border-white/5 space-y-2 text-xs sm:text-sm text-slate-300">
                <p class="font-bold text-amber-400 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                    1. ADIM: Determinant Güvenlik Kontrolü ($|A| \neq 0$ mı?)
                </p>
                <p>1. satıra göre Laplace açılımı yapalım (çünkü içinde kolaylık sağlayan $0$ var):</p>
                <p>$$|A| = 1 \cdot \begin{vmatrix} -1 & 3 \\ 1 & 8 \end{vmatrix} - 0 \cdot \begin{vmatrix} 2 & 3 \\ 4 & 8 \end{vmatrix} + 2 \cdot \begin{vmatrix} 2 & -1 \\ 4 & 1 \end{vmatrix}$$</p>
                <p>$$|A| = 1 \cdot [(-1)(8) - (3)(1)] - 0 + 2 \cdot [(2)(1) - (-1)(4)]$$</p>
                <p>$$|A| = 1 \cdot (-8 - 3) + 2 \cdot (2 + 4) = -11 + 12 = \mathbf{1}$$</p>
                <p class="text-emerald-400 font-semibold font-mono">Sonuç: $|A| = 1 \neq 0 \implies$ Determinant sıfır olmadığı için matrisin tersi KESİNLİKLE VARDIR!</p>
            </div>

            <!-- 2. Adım: 9 Kofaktörün Hesabı -->
            <div class="p-4 rounded-xl bg-slate-900/80 border border-white/5 space-y-3 text-xs text-slate-300">
                <p class="font-bold text-blue-400 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-blue-400"></span>
                    2. ADIM: 9 Adet Kofaktörün Dama Tahtası İşaretleriyle Hesaplanması
                </p>
                <p class="text-slate-400">
                    Formülümüz: $A_{ij} = (-1)^{i+j} M_{ij}$. Dama tahtası işaret şablonu: $\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}$
                </p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 font-mono">
                    <!-- 1. Satır Kofaktörleri -->
                    <div class="p-3 rounded-lg bg-slate-950/70 border border-white/5 space-y-1.5">
                        <span class="text-cyan-300 font-bold block">1. Satır Kofaktörleri:</span>
                        <p>• $A_{11} = + \begin{vmatrix} -1 & 3 \\ 1 & 8 \end{vmatrix} = -8 - 3 = \mathbf{-11}$</p>
                        <p>• $A_{12} = - \begin{vmatrix} 2 & 3 \\ 4 & 8 \end{vmatrix} = -(16 - 12) = \mathbf{-4}$</p>
                        <p>• $A_{13} = + \begin{vmatrix} 2 & -1 \\ 4 & 1 \end{vmatrix} = +(2 - (-4)) = \mathbf{6}$</p>
                    </div>

                    <!-- 2. Satır Kofaktörleri -->
                    <div class="p-3 rounded-lg bg-slate-950/70 border border-white/5 space-y-1.5">
                        <span class="text-cyan-300 font-bold block">2. Satır Kofaktörleri:</span>
                        <p>• $A_{21} = - \begin{vmatrix} 0 & 2 \\ 1 & 8 \end{vmatrix} = -(0 - 2) = \mathbf{2}$</p>
                        <p>• $A_{22} = + \begin{vmatrix} 1 & 2 \\ 4 & 8 \end{vmatrix} = +(8 - 8) = \mathbf{0}$</p>
                        <p>• $A_{23} = - \begin{vmatrix} 1 & 0 \\ 4 & 1 \end{vmatrix} = -(1 - 0) = \mathbf{-1}$</p>
                    </div>

                    <!-- 3. Satır Kofaktörleri -->
                    <div class="p-3 rounded-lg bg-slate-950/70 border border-white/5 space-y-1.5">
                        <span class="text-cyan-300 font-bold block">3. Satır Kofaktörleri:</span>
                        <p>• $A_{31} = + \begin{vmatrix} 0 & 2 \\ -1 & 3 \end{vmatrix} = +(0 - (-2)) = \mathbf{2}$</p>
                        <p>• $A_{32} = - \begin{vmatrix} 1 & 2 \\ 2 & 3 \end{vmatrix} = -(3 - 4) = -(-1) = \mathbf{1}$</p>
                        <p>• $A_{33} = + \begin{vmatrix} 1 & 0 \\ 2 & -1 \end{vmatrix} = +(-1 - 0) = \mathbf{-1}$</p>
                    </div>
                </div>

                <div class="pt-2">
                    <p class="font-bold text-slate-200">Kofaktörler Matrisi ($C$):</p>
                    <p>$$C = \begin{bmatrix} A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \\ A_{31} & A_{32} & A_{33} \end{bmatrix} = \begin{bmatrix} -11 & -4 & 6 \\ 2 & 0 & -1 \\ 2 & 1 & -1 \end{bmatrix}$$</p>
                </div>
            </div>

            <!-- 3. Adım: Transpoze ve Adjoint -->
            <div class="p-4 rounded-xl bg-rose-950/20 border border-rose-500/30 space-y-2 text-xs sm:text-sm text-slate-300">
                <p class="font-bold text-rose-400 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-rose-400"></span>
                    3. ADIM: Sınavın En Kritik Hamlesi — Transpoze Al ve $\text{adj}(A)$'yı Yaz!
                </p>
                <p class="text-slate-300">
                    Kofaktör matrisinin <strong>satırlarını sütun</strong> yapıyoruz:
                </p>
                <div class="bg-slate-950/80 p-3 rounded-lg border border-white/5 font-mono text-xs space-y-1">
                    <p>• $C$'nin 1. satırı: $[-11, -4, 6] \implies \text{adj}(A)$'nın <strong>1. sütunu</strong> oldu!</p>
                    <p>• $C$'nin 2. satırı: $[2, 0, -1] \implies \text{adj}(A)$'nın <strong>2. sütunu</strong> oldu!</p>
                    <p>• $C$'nin 3. satırı: $[2, 1, -1] \implies \text{adj}(A)$'nın <strong>3. sütunu</strong> oldu!</p>
                </div>
                <p class="text-center py-1">
                    $$\mathbf{\text{adj}(A) = C^T = \begin{bmatrix} -11 & 2 & 2 \\ -4 & 0 & 1 \\ 6 & -1 & -1 \end{bmatrix}}$$
                </p>
            </div>

            <!-- 4. Adım: Ters Matris -->
            <div class="p-4 rounded-xl bg-emerald-950/25 border border-emerald-500/30 space-y-2 text-xs sm:text-sm text-slate-300">
                <p class="font-bold text-emerald-400 flex items-center gap-2">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                    4. ADIM: Formülü Uygulayarak Ters Matrisi ($A^{-1}$) Elde Etme
                </p>
                <p>$$A^{-1} = \frac{1}{|A|} \text{adj}(A) = \frac{1}{1} \begin{bmatrix} -11 & 2 & 2 \\ -4 & 0 & 1 \\ 6 & -1 & -1 \end{bmatrix} = \mathbf{\begin{bmatrix} -11 & 2 & 2 \\ -4 & 0 & 1 \\ 6 & -1 & -1 \end{bmatrix}}$$</p>
            </div>

            <!-- Sağlama Testi: A * adj(A) = |A| * I -->
            <div class="p-4 rounded-xl bg-purple-950/25 border border-purple-500/30 space-y-2 text-xs text-slate-300">
                <p class="font-bold text-purple-300 flex items-center gap-2">
                    <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    Sınavda Doğruluğu %100 Kanıtlama: Sağlama / Kontrol Testi
                </p>
                <p>
                    Vizede cevabınızın doğru olup olmadığını anlamak için matris ile Adjoint'ini çarpın: Kural gereği sonuç <strong>$|A| \cdot I$</strong> çıkmalıdır:
                </p>
                <p class="font-mono text-center">
                    $$A \cdot \text{adj}(A) = \begin{bmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{bmatrix} \begin{bmatrix} -11 & 2 & 2 \\ -4 & 0 & 1 \\ 6 & -1 & -1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = 1 \cdot I_3$$
                </p>
                <p class="text-purple-300 font-semibold">Gördüğünüz gibi Birim Matris çıktı! Demek ki bulduğumuz Adjoint ve Ters Matris %100 HATASIZ ve EKSİKSİZDİR.</p>
            </div>
        </div>

        <!-- 4.6.5: Vizede En Çok Can Yakan 4 Adjoint / Ters Matris Tuzağı -->
        <div class="space-y-3">
            <h5 class="text-sm font-bold text-rose-400 uppercase tracking-wider flex items-center gap-2">
                <svg class="w-4 h-4 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
                Vize Sınavında En Çok Puan Kırdıran 4 Adjoint Tuzağı
            </h5>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">1. Transpozeyi Unutup Kofaktör Matrisini Adjoint Sanmak:</strong>
                    Öğrencilerin %70'i $C$ matrisini bulur ve heyecanla doğrudan cevap kutusuna yazar. Hoca transpoze alınmadığını gördüğü an tüm adımı çizer! Unutma: $\text{adj}(A) = C^T$'dir.
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">2. Dama Tahtasındaki Eksi ile Determinantın Kendi Eksisi:</strong>
                    Örneğin $A_{32}$ elemanında formülden gelen bir eksi vardır: $-(-1)^{3+2} = -1$. İçerideki determinant da $-1$ çıkarsa: $-(-1) = \mathbf{+1}$ olur! İki eksi yan yana gelince artı yapmayı unutmayın.
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">3. $2 \times 2$ Kestirmesini $3 \times 3$'e Uygulamaya Çalışmak:</strong>
                    Köşegenleri yer değiştirip diğerlerini eksi yapma kuralı <u>SADECE ve SADECE $2 \times 2$</u> matrisler içindir! Asla $3 \times 3$ matrislere uygulanamaz. $3 \times 3$ için 9 kofaktörü tek tek hesaplamak zorundasınız.
                </div>
                <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                    <strong class="text-rose-400 block font-bold">4. Vizenin Yıldız Formülü: $|\text{adj}(A)| = |A|^{n-1}$</strong>
                    Hoca vizede der ki: "$3 \times 3$ tipindeki $A$ matrisinin determinantı $|A| = 4$ ise, $\text{adj}(A)$ matrisinin determinantı kaçtır?". Matrisin elemanlarını bilmeden çözülebilir mi? EVET! Kural: $|\text{adj}(A)| = |A|^{n-1} = 4^{3-1} = 4^2 = \mathbf{16}$. Bu formülü bilen saniyeler içinde tam puanı alır!
                </div>
            </div>
        </div>
    </div>

    <!-- 4.7: Vizede En Çok Puan Kırdıran 4 Klasik Rank Tuzağı -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-rose-500/30 bg-rose-950/10 space-y-4">
        <div class="flex items-center gap-2 text-rose-400 font-bold text-sm uppercase tracking-wider">
            <svg class="w-5 h-5 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
            Vize Sınavında En Çok Puan Kırdıran 4 Klasik Rank Tuzağı
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">1. Determinant Sıfır Değilse Rank Doğrudan $n$'dir!</strong>
                $3 \times 3$ kare matriste $|A| \neq 0$ ise hiç satır işlemi yapmana gerek yoktur; kural gereği doğrudan $\text{rank}(A) = 3$'tür! Satır işlemiyle zaman kaybetme.
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">2. Boyut Sınırını Asla Aşamazsınız:</strong>
                $m \times n$ bir matrisin rankı asla satır veya sütun sayısından büyük olamaz: $\text{rank}(A) \le \min(m, n)$. Örneğin $3 \times 5$'lik bir matrisin rankı en fazla 3 olabilir, asla 4 veya 5 çıkamaz!
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">3. Sıfır Satırını Ranka Sayma Hatası:</strong>
                En altta oluşan $[0, 0, \dots, 0]$ satırları ranka dahil edilmez. Rank yalnızca sıfırdan farklı (en az bir sayısı sıfır olmayan) diri satırların sayısıdır.
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">4. Kesirlerle Kendini Yakma:</strong>
                1. satırın ilk sayısı $3$ ise hemen satırı 3'e bölüp kesirli sayılarla boğuşma! Alt satırlarda başında $1$ olan bir satır varsa hemen yer değiştir ($S_1 \leftrightarrow S_i$). İşlemlerin 10 kat hızlanır.
            </div>
        </div>
    </div>
</div>
"""
    },
    {
        "id": "bolum5",
        "title": "Bölüm 5: Lineer Denklem Sistemlerinin Çözümü",
        "badge": "Hafta 4 & 12 (Gauss, İnvers, Cramer)",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>""",
        "content": r"""<div class="space-y-6">
    <!-- Giriş ve Kahraman Kartı -->
    <div class="glass-3d-card p-6 sm:p-8 rounded-2xl border border-white/5 space-y-5">
        <div class="flex items-center gap-3 border-b border-white/5 pb-4">
            <span class="px-3 py-1 rounded-lg bg-indigo-500/20 text-indigo-400 font-mono text-xs font-bold">5.0</span>
            <div>
                <h4 class="text-lg sm:text-xl font-bold text-white">Lineer Denklem Sistemlerinin Çözüm Rehberi</h4>
                <p class="text-xs text-slate-400">Gauss Eliminasyonu, Rouché-Capelli Rank Teoremi, Sonsuz Çözüm & Parametre Atama, Homojen Sistemler, İnvers Matris ve Cramer Kuralı</p>
            </div>
        </div>

        <!-- Çocuğa Anlatır Gibi: Lineer Denklem Sistemi Nedir ve Neden Matrise Çevrilir? -->
        <div class="p-5 rounded-2xl bg-indigo-950/25 border border-indigo-500/30 space-y-3">
            <div class="flex items-center gap-2 text-indigo-400 font-bold text-sm">
                <svg class="w-5 h-5 text-indigo-400 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <span>Temel Mantık: Lineer Denklem Sistemi Nedir ve Neden Matrise Çeviririz?</span>
            </div>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                İlkokul ve lisede iki bilinmeyenli basit denklemleri taraf tarafa toplayarak çözerdik:
                $$\begin{cases} 2x + y = 10 \\ x + 3y = 15 \end{cases}$$
                Burada $x$ ve $y$ olmak üzere sadece iki bilinmeyen vardı. Fakat mühendislikte, yapay zekada veya elektrik devrelerinde <strong>10 bilinmeyenli 10 denklem</strong> ya da 1000 bilinmeyenli devasa sistemler karşımıza çıkar. İnsan beyni bu denklemleri alt alta yazıp yok etmeye çalışırsa kaybolur!
            </p>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
                İşte bu yüzden matematikçiler sistemi tek bir matris denklemine dönüştürür:
                $$\mathbf{A \cdot X = B}$$
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs font-mono pt-1">
                <div class="p-3 bg-slate-900/80 rounded-xl border border-white/5 space-y-1">
                    <span class="text-cyan-400 font-bold block">1. Katsayılar Matrisi ($A$)</span>
                    Bilinmeyenlerin önündeki sayıların oluşturduğu $m \times n$ boyutlu matris.
                </div>
                <div class="p-3 bg-slate-900/80 rounded-xl border border-white/5 space-y-1">
                    <span class="text-purple-400 font-bold block">2. Bilinmeyenler Sütunu ($X$)</span>
                    Aradığımız $[x_1, x_2, \dots, x_n]^T$ bilinmeyenlerinin oluşturduğu sütun vektörü.
                </div>
                <div class="p-3 bg-slate-900/80 rounded-xl border border-white/5 space-y-1">
                    <span class="text-emerald-400 font-bold block">3. Sonuçlar Sütunu ($B$)</span>
                    Eşitliğin sağ tarafındaki sabit sayıların oluşturduğu $[b_1, b_2, \dots, b_m]^T$ vektörü.
                </div>
            </div>
        </div>
    </div>

    <!-- 5.1: Artırılmış (Genişletilmiş) Matris [A | B] -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3 border-b border-white/5 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-amber-500/20 text-amber-400 font-mono text-xs font-bold">5.1</span>
            <h4 class="text-lg font-bold text-white">Artırılmış (Genişletilmiş) Matris $[A \mid B]$ Nedir?</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Bir denklemin sol tarafına ne yaparsanız (örneğin 2 ile çarpmak veya başka denklemle toplamak), eşitliğin bozulmaması için sağ tarafına da aynısını yapmak zorundasınız.
            İşte bu sebeple katsayılar matrisi $A$'nın yanına sonuç sütunu $B$'yi dikey bir çizgiyle ekleriz. Ortaya çıkan bu yeni matrise <strong>Artırılmış (Genişletilmiş) Matris</strong> denir:
        </p>
        <div class="p-4 bg-slate-950/80 rounded-xl border border-amber-500/20 text-center font-mono text-xs sm:text-sm text-slate-200">
            $$[A \mid B] = \left[\begin{array}{cccc|c} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{array}\right]$$
        </div>
        <div class="p-4 rounded-xl bg-slate-900/60 border border-white/5 text-xs text-slate-300 space-y-1">
            <strong class="text-amber-400 block font-semibold">Örnek Gösterim:</strong>
            $$\begin{cases} 2x_1 - x_2 + 3x_3 = 5 \\ x_1 + 4x_2 - 2x_3 = 0 \\ 3x_1 + 0x_2 + x_3 = 7 \end{cases} \implies [A \mid B] = \left[\begin{array}{ccc|c} 2 & -1 & 3 & 5 \\ 1 & 4 & -2 & 0 \\ 3 & 0 & 1 & 7 \end{array}\right]$$
            <p class="text-slate-400 pt-1">Çizginin solu katsayılar matrisi $A$, sağı ise sonuçlar vektörü $B$'dir. Artık bilinmeyen harflerle ($x_1, x_2, x_3$) uğraşmadan yalnızca bu sayılar üzerinde satır işlemleri yapacağız!</p>
        </div>
    </div>

    <!-- 5.2: Hayati Teorem: Rouché-Capelli Teoremi (Rank Kriteri) -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-cyan-500/30 bg-cyan-950/10 space-y-4">
        <div class="flex items-center gap-3 border-b border-cyan-500/20 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-cyan-500/20 text-cyan-400 font-mono text-xs font-bold">5.2</span>
            <h4 class="text-lg font-bold text-white">Hayati Sınav Teoremi: Rouché-Capelli (Rank ile Çözüm Varlık & Teklik Analizi)</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Sınavda bir sistemi çözmeye başlamadan önce veya parametreli sorularda hocaların sorduğu en kritik kural şudur: 
            <strong>"Bu sistemin çözümü var mıdır, varsa kaç tanedir?"</strong>
            Bunu anlamak için katsayılar matrisi $A$'nın rankı ($\text{rank}(A)$) ile genişletilmiş matris $[A \mid B]$'nin rankı ($\text{rank}([A \mid B])$) kıyaslanır:
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3.5">
            <!-- Durum 1: Çözüm Yok -->
            <div class="p-4 rounded-xl bg-rose-950/30 border border-rose-500/30 space-y-2">
                <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-rose-500/20 text-rose-400 font-mono block w-fit">1. DURUM: ÇÖZÜM YOK</span>
                <strong class="text-white text-xs sm:text-sm block">$\text{rank}(A) < \text{rank}([A \mid B])$</strong>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Sistem <strong>tutarsızdır (çelişkilidir)</strong>. Eşelon formun en altında $[0, 0, \dots, 0 \mid k]$ ($k \neq 0$) şeklinde bir satır oluşur! Bu durum $0 = k$ gibi imkansız bir çelişki demektir. Çözüm kümesi boştur ($\emptyset$).
                </p>
            </div>

            <!-- Durum 2: Tek Çözüm -->
            <div class="p-4 rounded-xl bg-emerald-950/30 border border-emerald-500/30 space-y-2">
                <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-emerald-500/20 text-emerald-400 font-mono block w-fit">2. DURUM: TEK ÇÖZÜM</span>
                <strong class="text-white text-xs sm:text-sm block">$\text{rank}(A) = \text{rank}([A \mid B]) = n$</strong>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Sistem <strong>tutarlıdır ve tek bir çözümü</strong> vardır ($n = \text{bilinmeyen sayısı}$). Her bilinmeyenin bir pivotu vardır. Geriye doğru yerine koyma ile tek bir $(x_1, x_2, \dots, x_n)$ çözümü elde edilir.
                </p>
            </div>

            <!-- Durum 3: Sonsuz Çözüm -->
            <div class="p-4 rounded-xl bg-purple-950/30 border border-purple-500/30 space-y-2">
                <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-purple-500/20 text-purple-400 font-mono block w-fit">3. DURUM: SONSUZ ÇÖZÜM</span>
                <strong class="text-white text-xs sm:text-sm block">$\text{rank}(A) = \text{rank}([A \mid B]) = r < n$</strong>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Sistem tutarlıdır fakat <strong>sonsuz sayıda çözümü</strong> vardır. Bilinmeyen sayısı ranktan fazladır! Tam <strong>$n - r$</strong> adet bilinmeyene <u>serbest parametre</u> ($t, k \in \mathbb{R}$) atanır.
                </p>
            </div>
        </div>
    </div>

    <!-- 5.3: Gauss Eliminasyon Yöntemi ve Tek Çözümlü Sayısal Örnek -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-white/5 space-y-5">
        <div class="flex items-center gap-3 border-b border-white/5 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-emerald-500/20 text-emerald-400 font-mono text-xs font-bold">5.3</span>
            <h4 class="text-lg font-bold text-white">Gauss Eliminasyon (Yok Etme) Yöntemi ve Tek Çözüm</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Gauss Eliminasyon yönteminin mantığı 3 adımdan ibarettir:
            <strong>1.</strong> $[A \mid B]$ artırılmış matrisini kur. 
            <strong>2.</strong> Satır işlemleriyle basamaklı (üst üçgensel / eşelon) hale getir. 
            <strong>3.</strong> En alt satırdan başlayarak geriye doğru yerine koyma (Back Substitution) ile tüm bilinmeyenleri bul!
        </p>

        <!-- Sayısal Örnek: Tek Çözüm -->
        <div class="p-5 rounded-2xl bg-emerald-950/25 border border-emerald-500/30 space-y-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                5.3 İçin Adım Adım Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{cases}$ sistemini Gauss eleme yöntemi ile adım adım çözünüz.
            </p>
            
            <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-amber-400 font-sans font-bold">Adım 1: Artırılmış Matrisi $[A \mid B]$ kuralım:</p>
                <p>$$[A \mid B] = \left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 2 & -1 & 1 & 3 \\ 1 & 2 & -1 & 2 \end{array}\right]$$</p>

                <p class="text-cyan-400 font-sans font-bold pt-2">Adım 2: 1. Sütunu Pivot $1$'in Altından Sıfırlayalım:</p>
                <p>• $S_2 \leftarrow S_2 - 2S_1 = [2, -1, 1 \mid 3] - [2, 2, 2 \mid 12] = [\mathbf{0, -3, -1 \mid -9}]$</p>
                <p>• $S_3 \leftarrow S_3 - S_1 = [1, 2, -1 \mid 2] - [1, 1, 1 \mid 6] = [\mathbf{0, 1, -2 \mid -4}]$</p>
                <p>Matrisimiz şu hale gelir:</p>
                <p>$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & -3 & -1 & -9 \\ 0 & 1 & -2 & -4 \end{array}\right]$$</p>

                <p class="text-cyan-400 font-sans font-bold pt-2">Adım 3: Kolaylık İçin $S_2 \leftrightarrow S_3$ Yer Değiştirelim ve 2. Sütunu Sıfırlayalım:</p>
                <p>2. satır ile 3. satırı yer değiştirirsek pivotumuz $+1$ olur (kesirlerle uğraşmayız!):</p>
                <p>$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & -2 & -4 \\ 0 & -3 & -1 & -9 \end{array}\right]$$</p>
                <p>Şimdi 3. satırdaki $-3$'ü yok etmek için: $S_3 \leftarrow S_3 + 3S_2$:</p>
                <p>$$[0, -3, -1 \mid -9] + [0, 3, -6 \mid -12] = [\mathbf{0, 0, -7 \mid -21}]$$</p>

                <p class="text-emerald-400 font-sans font-bold pt-2">Adım 4: Eşelon Formu İnceleyelim ve Geriye Doğru Yerine Koyalım:</p>
                <p>$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & -2 & -4 \\ 0 & 0 & -7 & -21 \end{array}\right]$$</p>
                <p>Rank Kontrolü: $\text{rank}(A) = 3$, $\text{rank}([A \mid B]) = 3$, Bilinmeyen sayısı $n = 3$. Teorem gereği <strong>TEK ÇÖZÜM</strong> vardır!</p>
                <div class="bg-slate-900/90 p-3 rounded-lg border border-white/5 space-y-1 text-slate-200">
                    <p>• <strong>3. Satırdan:</strong> $-7z = -21 \implies \mathbf{z = 3}$</p>
                    <p>• <strong>2. Satırdan:</strong> $y - 2z = -4 \implies y - 2(3) = -4 \implies y - 6 = -4 \implies \mathbf{y = 2}$</p>
                    <p>• <strong>1. Satırdan:</strong> $x + y + z = 6 \implies x + 2 + 3 = 6 \implies x + 5 = 6 \implies \mathbf{x = 1}$</p>
                </div>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: Çözüm Kümesi tek bir noktadır: $(x, y, z) = (\mathbf{1, 2, 3})$.</p>
            </div>
        </div>
    </div>

    <!-- 5.4: Sonsuz Çözüm Durumu ve Serbest Parametre (t) Atama Sanatı -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-purple-500/30 bg-purple-950/10 space-y-4">
        <div class="flex items-center gap-3 border-b border-purple-500/20 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-purple-500/20 text-purple-400 font-mono text-xs font-bold">5.4</span>
            <h4 class="text-lg font-bold text-white">Sonsuz Çözüm Durumu ve Serbest Parametre ($t$) Atama Sanatı</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Öğrencilerin vizede en çok zorlandığı ama mantığı kavranınca en kolay puan toplanan yer burasıdır!
            Basamaklı matriste en altta $[0, 0, \dots, 0 \mid 0]$ gibi tamamen sıfır bir satır oluşursa rank bilinmeyen sayısından küçük kalır: $\text{rank}(A) = r < n$.
            Bu durumda <strong>$n - r$ adet bilinmeyene serbest parametre ($t, k \in \mathbb{R}$)</strong> atanır. Çünkü bu bilinmeyenlerin alacağı değeri kısıtlayan bir denklem kalmamıştır!
        </p>

        <!-- Sayısal Örnek: Sonsuz Çözüm -->
        <div class="p-5 rounded-2xl bg-purple-950/25 border border-purple-500/30 space-y-3">
            <span class="text-xs font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                5.4 İçin Adım Adım Sonsuz Çözüm Örneği:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} x + y + z = 4 \\ 2x + y + 3z = 7 \\ 3x + 2y + 4z = 11 \end{cases}$ sistemini çözünüz.
            </p>
            <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-amber-400 font-sans font-bold">Adım 1: Genişletilmiş Matris $[A \mid B]$ ve Satır İşlemleri:</p>
                <p>$$[A \mid B] = \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 2 & 1 & 3 & 7 \\ 3 & 2 & 4 & 11 \end{array}\right]$$</p>
                <p>• $S_2 \leftarrow S_2 - 2S_1 = [0, -1, 1 \mid -1]$</p>
                <p>• $S_3 \leftarrow S_3 - 3S_1 = [0, -1, 1 \mid -1]$ (Dikkat! 2. satır ile 3. satır tıpatıp aynı oldu!)</p>
                <p>• $S_3 \leftarrow S_3 - S_2 = [\mathbf{0, 0, 0 \mid 0}]$ (3. satır tamamen sıfırlandı!)</p>
                <p>Son basamaklı formumuz:</p>
                <p>$$\left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 0 & -1 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{array}\right] \sim \left[\begin{array}{ccc|c} 1 & 1 & 1 & 4 \\ 0 & 1 & -1 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right]$$</p>

                <p class="text-purple-400 font-sans font-bold pt-2">Adım 2: Rank Analizi ve Parametre Sayısı:</p>
                <p>$\text{rank}(A) = 2$, $\text{rank}([A \mid B]) = 2$, Bilinmeyen sayısı $n = 3$.</p>
                <p>$\text{rank}(A) = \text{rank}([A \mid B]) = 2 < 3 \implies \mathbf{SONSUZ\ ÇÖZÜM\ VARDIR!}$</p>
                <p>Serbest Parametre Sayısı: $n - r = 3 - 2 = \mathbf{1\ adet\ parametre}$.</p>

                <p class="text-purple-400 font-sans font-bold pt-2">Adım 3: Serbest Parametre Atama ve Geriye Doğru Çözüm:</p>
                <p>Pivotu olmayan $z$ bilinmeyenine serbest parametre diyelim: $\mathbf{z = t \quad (t \in \mathbb{R})}$.</p>
                <div class="bg-slate-900/90 p-3 rounded-lg border border-white/5 space-y-1 text-slate-200">
                    <p>• <strong>2. Satırdan:</strong> $y - z = 1 \implies y - t = 1 \implies \mathbf{y = 1 + t}$</p>
                    <p>• <strong>1. Satırdan:</strong> $x + y + z = 4 \implies x + (1 + t) + t = 4 \implies x + 1 + 2t = 4 \implies \mathbf{x = 3 - 2t}$</p>
                </div>

                <p class="text-emerald-400 font-sans font-bold pt-2">Adım 4: Genel Çözüm Vektörü Biçiminde Yazılış:</p>
                <p>$$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 3 - 2t \\ 1 + t \\ t \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \\ 0 \end{bmatrix} + t \begin{bmatrix} -2 \\ 1 \\ 1 \end{bmatrix}, \quad t \in \mathbb{R}$$</p>
                <p class="text-purple-300">Bu ifade geometrik olarak 3 boyutlu uzayda sonsuz noktadan oluşan bir <strong>DOĞRU</strong> belirtir!</p>
            </div>
        </div>
    </div>

    <!-- 5.5: Çözümsüzlük (Tutarsızlık) ve 0 = k Çelişkisi -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-rose-500/30 bg-rose-950/10 space-y-4">
        <div class="flex items-center gap-3 border-b border-rose-500/20 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-rose-500/20 text-rose-400 font-mono text-xs font-bold">5.5</span>
            <h4 class="text-lg font-bold text-white">Çözümsüzlük (Tutarsızlık) Durumu ve $0 = k$ Çelişkisi</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Ders notlarında hocanın özellikle sorduğu klasik tuzak soru tipidir.
            Satır işlemleri yaparken sol taraftaki tüm katsayılar sıfırlanıp sağ tarafta sıfırdan farklı bir sayı kalırsa sistem patlar:
        </p>

        <!-- Sayısal Örnek: Çözümsüzlük -->
        <div class="p-5 rounded-2xl bg-rose-950/25 border border-rose-500/30 space-y-3">
            <span class="text-xs font-bold text-rose-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                5.5 İçin Ders Notu Orijinal Çözümsüzlük Örneği:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} x_1 + x_3 = 1 \\ 2x_1 - x_2 + 2x_3 = 0 \\ 2x_1 + 2x_2 + 2x_3 = 1 \end{cases}$ sistemini çözünüz.
            </p>
            <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-amber-400 font-sans font-bold">Adım 1: $[A \mid B]$ Matrisi:</p>
                <p>$$[A \mid B] = \left[\begin{array}{ccc|c} 1 & 0 & 1 & 1 \\ 2 & -1 & 2 & 0 \\ 2 & 2 & 2 & 1 \end{array}\right]$$</p>
                <p>• $S_2 \leftarrow S_2 - 2S_1 = [0, -1, 0 \mid -2]$</p>
                <p>• $S_3 \leftarrow S_3 - 2S_1 = [0, 2, 0 \mid -1]$</p>
                <p>Şimdi 3. satırdaki $+2$'yi yok etmek için $S_3 \leftarrow S_3 + 2S_2$ uygulayalım:</p>
                <p>$$[0, 2, 0 \mid -1] + [0, -2, 0 \mid -4] = [\mathbf{0, 0, 0 \mid -5}]$$</p>
                <p>Matrisin son hali:</p>
                <p>$$\left[\begin{array}{ccc|c} 1 & 0 & 1 & 1 \\ 0 & -1 & 0 & -2 \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \mathbf{-5} \end{array}\right]$$</p>

                <p class="text-rose-400 font-sans font-bold pt-2">Adım 2: Çelişkiyi Teşhis Edelim:</p>
                <p>3. satırın matematiksel anlamı şudur:</p>
                <p class="text-center text-rose-300 font-bold text-base py-1">$$0 \cdot x_1 + 0 \cdot x_2 + 0 \cdot x_3 = -5 \implies \mathbf{0 = -5 \quad (İMKANSIZ!)}$$</p>
                <p>Rank Analizi: $\text{rank}(A) = 2$ iken genişletilmiş matrisin rankı $\text{rank}([A \mid B]) = 3$'tür.</p>
                <p class="text-rose-400 font-bold">$$\text{rank}(A) < \text{rank}([A \mid B]) \implies 2 < 3$$</p>
                <p class="text-slate-200">Rouché-Capelli teoremi gereği sistem <strong>TUTARSIZDIR</strong>. Çözüm kümesi <strong>BOŞ KÜMEDİR</strong> ($Ç.K. = \emptyset$). İşlemi burada noktalayınız.</p>
            </div>
        </div>
    </div>

    <!-- 5.6: Lineer Homojen Denklem Sistemleri (AX = 0) -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-blue-500/30 bg-blue-950/10 space-y-4">
        <div class="flex items-center gap-3 border-b border-blue-500/20 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-blue-500/20 text-blue-400 font-mono text-xs font-bold">5.6</span>
            <h4 class="text-lg font-bold text-white">Lineer Homojen Denklem Sistemleri ($A \cdot X = 0$)</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Eşitliğin sağ tarafındaki tüm sabit sayılar sıfır ise ($B = [0, 0, \dots, 0]^T$) bu sisteme <strong>Homojen Sistem</strong> denir.
        </p>
        <div class="p-4 rounded-xl bg-blue-950/30 border border-blue-500/20 text-xs text-blue-200 space-y-2">
            <strong class="text-blue-300 text-sm block">VİZE İÇİN ALTIN KURAL:</strong>
            <p>Homojen sistemler <strong>ASLA ÇÖZÜMSÜZ OLAMAZ!</strong> Çünkü tüm bilinmeyenlere sıfır verirseniz ($x_1 = 0, x_2 = 0, \dots, x_n = 0$), denklem her zaman $0 = 0$ olarak sağlanır. Buna <strong>AŞİKAR ÇÖZÜM (Trivial Solution)</strong> denir.</p>
            <p>Soru şudur: <em>"Aşikar çözümden başka, sıfırdan farklı çözümler de var mıdır?"</em></p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-1">
            <div class="p-4 rounded-xl bg-slate-900/80 border border-white/5 space-y-2">
                <span class="text-cyan-400 font-mono text-xs font-bold block">DURUM 1: $|A| \neq 0$ veya $\text{rank}(A) = n$</span>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Sistemin <strong>YALNIZCA AŞİKAR ÇÖZÜMÜ</strong> vardır:
                    $$x_1 = 0, \quad x_2 = 0, \quad \dots, \quad x_n = 0$$
                    Sıfırdan farklı hiçbir çözüm bulunamaz!
                </p>
            </div>
            <div class="p-4 rounded-xl bg-slate-900/80 border border-white/5 space-y-2">
                <span class="text-purple-400 font-mono text-xs font-bold block">DURUM 2: $|A| = 0$ veya $\text{rank}(A) < n$</span>
                <p class="text-xs text-slate-300 leading-relaxed">
                    Sistemin aşikar olanın dışında <strong>SIFIRDAN FARKLI SONSUZ ÇÖZÜMÜ</strong> de vardır! Tam $n - r$ adet serbest parametre seçilerek sonsuz çözüm uzayı ifade edilir.
                </p>
            </div>
        </div>

        <!-- Homojen Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-blue-950/25 border border-blue-500/30 space-y-3">
            <span class="text-xs font-bold text-blue-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                Ders Notu Orijinal Homojen Sistem Örneği:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} x_1 + 2x_2 - 3x_3 = 0 \\ 3x_1 + x_2 - 2x_3 = 0 \\ 2x_1 - x_2 + x_3 = 0 \end{cases}$ sisteminin çözümlerini bulunuz.
            </p>
            <div class="space-y-2 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-amber-400 font-sans font-bold">1. Adım: Katsayılar Matrisinin Determinantını İnceleyelim:</p>
                <p>$$|A| = \begin{vmatrix} 1 & 2 & -3 \\ 3 & 1 & -2 \\ 2 & -1 & 1 \end{vmatrix}$$</p>
                <p>1. satıra göre açarsak:<br>
                $|A| = 1(1 - 2) - 2(3 - (-4)) - 3(-3 - 2) = 1(-1) - 2(7) - 3(-5) = -1 - 14 + 15 = \mathbf{0}$!</p>
                <p class="text-purple-300 font-bold">Determinant $|A| = 0$ çıktı $\implies$ Demek ki bu sistemin SIFIRDAN FARKLI SONSUZ ÇÖZÜMÜ vardır!</p>

                <p class="text-cyan-400 font-sans font-bold pt-2">2. Adım: Satır İşlemleriyle Eşelon Form:</p>
                <p>$$\begin{bmatrix} 1 & 2 & -3 \\ 3 & 1 & -2 \\ 2 & -1 & 1 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & -3 \\ 0 & -5 & 7 \\ 0 & 0 & 0 \end{bmatrix}$$</p>
                <p>$\text{rank}(A) = 2 < 3 \implies 3 - 2 = 1$ serbest parametre ($x_3 = t$).</p>
                <p>• $-5x_2 + 7t = 0 \implies \mathbf{x_2 = \frac{7}{5}t}$</p>
                <p>• $x_1 + 2(\frac{7}{5}t) - 3t = 0 \implies x_1 + \frac{14}{5}t - \frac{15}{5}t = 0 \implies \mathbf{x_1 = \frac{1}{5}t}$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: $X = t \begin{bmatrix} 1/5 \\ 7/5 \\ 1 \end{bmatrix}$ veya kesirlerden kurtulmak için ($t = 5k$ seçerek): $\mathbf{X = k \begin{bmatrix} 1 \\ 7 \\ 5 \end{bmatrix}, \quad k \in \mathbb{R}}$.</p>
            </div>
        </div>
    </div>

    <!-- 5.7: Cramer Sistemi ve İnvers Matris ile Çözüm (X = A^-1 * B) -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-emerald-500/30 bg-emerald-950/10 space-y-4">
        <div class="flex items-center gap-3 border-b border-emerald-500/20 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-emerald-500/20 text-emerald-400 font-mono text-xs font-bold">5.7</span>
            <h4 class="text-lg font-bold text-white">Cramer Sistemi ve İnvers Matris Yardımıyla Çözüm ($X = A^{-1} B$)</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Eğer bir denklem sisteminde denklem sayısı bilinmeyen sayısına eşitse ($m = n$) ve katsayılar matrisinin determinantı sıfırdan farklıysa ($|A| \neq 0$), bu sisteme <strong>CRAMER SİSTEMİ</strong> denir.
            Böyle sistemlerin katsayılar matrisinin tersi ($A^{-1}$) mevcuttur ve denklem matrisel olarak tek hamlede çözülür:
            $$A \cdot X = B \implies A^{-1} \cdot A \cdot X = A^{-1} \cdot B \implies \mathbf{X = A^{-1} B}$$
        </p>

        <!-- Sınav Taktik Kutusu: Kesir Tuzağından Kaçış -->
        <div class="p-4 rounded-xl bg-amber-950/30 border border-amber-500/30 text-xs sm:text-sm text-amber-200 space-y-2">
            <strong class="text-amber-300 flex items-center gap-1.5 font-bold">
                <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                VİZENİN HAYAT KURTARAN TAKTİK SIRRI (KESİR TUZAĞI):
            </strong>
            <p>Ders notlarında hocanın özellikle vurguladığı profesyonel tüyo: $A^{-1}$ matrisini $\frac{1}{|A|} \text{adj}(A)$ olarak baştan kesirli sayılarla hesaplayıp $B$ ile çarpmaya kalkarsanız payda eşitlemekten sınav süreniz biter ve işlem hatası yaparsınız!</p>
            <p class="font-bold text-white font-mono bg-slate-900/80 p-2.5 rounded-lg text-center">
                $$\mathbf{X = \frac{1}{|A|} \Big( \text{adj}(A) \cdot B \Big)}$$
            </p>
            <p><strong>Doğru Yol:</strong> Önce tam sayılardan oluşan $\text{adj}(A)$ ile $B$ sütununu çarpın! Çıkan tamsayı sonuç sütununu <u>en son tek bir adımda</u> $|A|$'ya bölün. Bu taktik sizi %100 hızlandırır ve sıfır hata yaptırır.</p>
        </div>

        <!-- Ders Notu 3x3 Orijinal İnvers Çözüm Örneği -->
        <div class="p-5 rounded-2xl bg-emerald-950/25 border border-emerald-500/30 space-y-3">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                5.7 İçin Ders Notu Orijinal $3 \times 3$ Sayısal Örneği:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} 3x_1 + 2x_2 - x_3 = 5 \\ x_1 + x_2 - 3x_3 = 1 \\ 2x_1 - x_2 + x_3 = 2 \end{cases}$ sistemini invers matris ($X = A^{-1} B$) yardımıyla çözünüz.
            </p>
            <div class="space-y-3 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p class="text-amber-400 font-sans font-bold">1. Adım: Katsayılar Matrisi $A$ ve Sonuç Vektörü $B$:</p>
                <p>$$A = \begin{bmatrix} 3 & 2 & -1 \\ 1 & 1 & -3 \\ 2 & -1 & 1 \end{bmatrix}, \quad B = \begin{bmatrix} 5 \\ 1 \\ 2 \end{bmatrix}$$</p>

                <p class="text-cyan-400 font-sans font-bold pt-2">2. Adım: Determinant $|A|$ Hesabı:</p>
                <p>$$|A| = 3(1 - 3) - 2(1 - (-6)) - 1(-1 - 2) = 3(-2) - 2(7) - 1(-3) = -6 - 14 + 3 = \mathbf{-17} \neq 0$$</p>
                <p>Determinant sıfır olmadığı için sistem bir Cramer sistemidir ve tersi vardır.</p>

                <p class="text-cyan-400 font-sans font-bold pt-2">3. Adım: Adjoint Matrisi $\text{adj}(A)$ Hesabı (Transpoze Kuralı ile):</p>
                <p>9 kofaktör hesaplanıp transpozesi alındığında Adjoint matrisimiz:</p>
                <p>$$\text{adj}(A) = \begin{bmatrix} -2 & -1 & -5 \\ -7 & 5 & 8 \\ -3 & 7 & 1 \end{bmatrix}$$</p>

                <p class="text-cyan-400 font-sans font-bold pt-2">4. Adım: Taktiksel Çarpım $\text{adj}(A) \cdot B$:</p>
                <p>$$\text{adj}(A) \cdot B = \begin{bmatrix} -2 & -1 & -5 \\ -7 & 5 & 8 \\ -3 & 7 & 1 \end{bmatrix} \begin{bmatrix} 5 \\ 1 \\ 2 \end{bmatrix} = \begin{bmatrix} (-2)(5) + (-1)(1) + (-5)(2) \\ (-7)(5) + (5)(1) + (8)(2) \\ (-3)(5) + (7)(1) + (1)(2) \end{bmatrix} = \mathbf{\begin{bmatrix} -21 \\ -14 \\ -6 \end{bmatrix}}$$</p>

                <p class="text-emerald-400 font-sans font-bold pt-2">5. Adım: Determinanta Bölerek Çözüm $X$'i Bulalım:</p>
                <p>$$X = \frac{1}{|A|} (\text{adj}(A) \cdot B) = \frac{1}{-17} \begin{bmatrix} -21 \\ -14 \\ -6 \end{bmatrix} = \mathbf{\begin{bmatrix} 21/17 \\ 14/17 \\ 6/17 \end{bmatrix}}$$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: $\mathbf{x_1 = \frac{21}{17}, \quad x_2 = \frac{14}{17}, \quad x_3 = \frac{6}{17}}$ olarak tek hamlede bulunur.</p>
            </div>
        </div>
    </div>

    <!-- 5.8: Cramer Kuralı (Determinant Yöntemi) -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3 border-b border-white/5 pb-3">
            <span class="px-2.5 py-1 rounded-md bg-amber-500/20 text-amber-400 font-mono text-xs font-bold">5.8</span>
            <h4 class="text-lg font-bold text-white">Cramer Kuralı (Determinant ile Doğrudan Çözüm)</h4>
        </div>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
            Matris tersi almadan, sadece determinant hesaplayarak her bir bilinmeyeni doğrudan çekip bulma yöntemidir:
            $$\mathbf{x_1 = \frac{|A_1|}{|A|}, \quad x_2 = \frac{|A_2|}{|A|}, \quad x_3 = \frac{|A_3|}{|A|}, \quad \dots}$$
            Burada <strong>$A_i$</strong> matrisi, orijinal katsayılar matrisi $A$'nın <u>$i$. sütununun sökülüp yerine sonuç sütunu $B$'nin takılmasıyla</u> elde edilen matristir!
        </p>

        <!-- Sayısal Örnek: Cramer Kuralı -->
        <div class="p-5 rounded-2xl bg-amber-950/20 border border-amber-500/30 space-y-3">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                5.8 İçin Tam Çözümlü Cramer Kuralı Örneği:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{cases}$ sistemini Cramer kuralı ile çözünüz.
            </p>
            <div class="space-y-2 text-xs sm:text-sm text-slate-300 font-mono bg-slate-950/70 p-4 rounded-xl border border-white/5">
                <p>• <strong>Ana Determinant:</strong> $|A| = \begin{vmatrix} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 1 & 2 & -1 \end{vmatrix} = \mathbf{7} \neq 0$</p>
                <p>• <strong>1. Sütuna $B=[6,3,2]^T$ takılırsa:</strong> $|A_1| = \begin{vmatrix} \mathbf{6} & 1 & 1 \\ \mathbf{3} & -1 & 1 \\ \mathbf{2} & 2 & -1 \end{vmatrix} = \mathbf{7} \implies \mathbf{x = \frac{7}{7} = 1}$</p>
                <p>• <strong>2. Sütuna $B=[6,3,2]^T$ takılırsa:</strong> $|A_2| = \begin{vmatrix} 1 & \mathbf{6} & 1 \\ 2 & \mathbf{3} & 1 \\ 1 & \mathbf{2} & -1 \end{vmatrix} = \mathbf{14} \implies \mathbf{y = \frac{14}{7} = 2}$</p>
                <p>• <strong>3. Sütuna $B=[6,3,2]^T$ takılırsa:</strong> $|A_3| = \begin{vmatrix} 1 & 1 & \mathbf{6} \\ 2 & -1 & \mathbf{3} \\ 1 & 2 & \mathbf{2} \end{vmatrix} = \mathbf{21} \implies \mathbf{z = \frac{21}{7} = 3}$</p>
                <p class="text-emerald-400 font-bold pt-1">Sonuç: $(x, y, z) = (\mathbf{1, 2, 3})$. Gauss eliminasyonu ile bulduğumuz sonucun aynısı!</p>
            </div>
        </div>
    </div>

    <!-- 5.9: Vizede En Çok Puan Kırdıran 5 Klasik Denklem Tuzağı -->
    <div class="glass-3d-card p-6 sm:p-7 rounded-2xl border border-rose-500/30 bg-rose-950/10 space-y-4">
        <div class="flex items-center gap-2 text-rose-400 font-bold text-sm uppercase tracking-wider">
            <svg class="w-5 h-5 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
            Vize Sınavında En Çok Puan Kırdıran 5 Klasik Denklem Sistemi Tuzağı
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-300">
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">1. Genişletilmiş Matriste Asla Sütun İşlemi Yapmayın:</strong>
                $[A \mid B]$ üzerinde yalnızca <u>satır işlemleri</u> serbesttir. Sütunların yerini değiştirirseniz bilinmeyenlerin ($x_1, x_2$) yerlerini birbirine katarsınız ve soru tamamen çöpe gider!
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">2. Matris Çarpım Sırasını Ters Yazma Hatası ($B \cdot A^{-1}$ YASAKTIR):</strong>
                Formül $X = A^{-1} B$'dir. Matris çarpımı değişmeli değildir! Soldan $A^{-1}$ ile çarpmanız şarttır. $B \cdot A^{-1}$ yazarsanız boyut uyumsuzluğundan çarpılamaz bile!
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">3. Homojen Sisteme "Çözümü Yoktur" Demek:</strong>
                Homojen sistemlerin ($AX = 0$) sağ tarafı sıfır olduğu için daima en azından $x_1=0, \dots, x_n=0$ aşikar çözümü vardır. Homojen sisteme asla "çözümsüzdür" yazmayın!
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1">
                <strong class="text-rose-400 block font-bold">4. Çelişki Satırını Görüp Çözüm Aramaya Devam Etmek:</strong>
                $[0, 0, 0 \mid 5]$ satırını gördüğünüz an durun! Bazı öğrenciler panikle $z=5$ sanıp yerine koymaya çalışır. $0 = 5$ bir çelişkidir, anında "Çözüm Yoktur ($Ç.K. = \emptyset$)" yazın.
            </div>
            <div class="p-3.5 rounded-xl bg-slate-900/60 border border-white/5 space-y-1 md:col-span-2">
                <strong class="text-rose-400 block font-bold">5. Serbest Parametre Sayısını Formülsüz Tahmin Etme Hatası:</strong>
                Sonsuz çözümlü sorularda parametre sayısı rastgele değil, kesin matematiksel kurala bağlıdır: $\mathbf{k = n - r}$ (Bilinmeyen Sayısı - Rank). Örneğin 4 bilinmeyenli ve rankı 2 olan bir sistemde tam $4 - 2 = 2$ adet bağımsız parametre ($t_1, t_2 \in \mathbb{R}$) seçilmek zorundadır.
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "id": "bolum6",
        "title": "Bonus Bölüm: Matrislerde Lineer Bağımlılık",
        "badge": "Hafta 6",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"/></svg>""",
        "content": r"""
<div class="space-y-6">
    <div class="glass-3d-card p-6 rounded-2xl border border-white/5 space-y-4">
        <div class="flex items-center gap-3">
            <span class="px-2.5 py-1 rounded-md bg-purple-500/20 text-purple-400 font-mono text-xs font-bold">6.1</span>
            <h4 class="text-lg font-bold text-white">Lineer Bağımlılık ve Bağımsızlık Sayısal Örnekleri</h4>
        </div>
        <p class="text-slate-300 text-sm leading-relaxed">
            $\lambda_1 A_1 + \lambda_2 A_2 = 0$ denklemini test ederiz. Yalnızca $\lambda_1 = \lambda_2 = 0$ iken sağlanıyorsa bağımsızdır; sıfırdan farklı sayılarla da sağlanıyorsa bağımlıdır.
        </p>

        <!-- 6.1 Sayısal Örnek -->
        <div class="p-5 rounded-2xl bg-purple-950/30 border border-purple-500/30 space-y-3">
            <span class="text-xs font-bold text-purple-400 uppercase tracking-wider flex items-center gap-1.5">
                <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                6.1 İçin Tam Çözümlü Sayısal Örnek:
            </span>
            <p class="text-slate-200 text-sm font-semibold">
                Soru: $A_1 = [1, 2]$ ve $A_2 = [2, 4]$ vektörleri lineer bağımlı mıdır, bağımsız mıdır?
            </p>
            <div class="text-xs sm:text-sm text-slate-300 space-y-2 font-mono bg-slate-950/60 p-4 rounded-xl border border-white/5">
                <p>Denklem: $\lambda_1 [1, 2] + \lambda_2 [2, 4] = [0, 0]$</p>
                <p>$$\begin{cases} \lambda_1 + 2\lambda_2 = 0 \\ 2\lambda_1 + 4\lambda_2 = 0 \end{cases}$$</p>
                <p>Eğer $\lambda_2 = 1$ seçersek $\lambda_1 = -2$ olur. Sıfırdan farklı sayılarla sağlandığı için:<br>
                $$-2 \cdot A_1 + 1 \cdot A_2 = 0 \implies A_2 = 2 A_1$$</p>
                <p class="text-rose-400 font-bold pt-1">Sonuç: $A_2$, $A_1$'in tam 2 katıdır. Dolayısıyla bu iki vektör <strong>LİNEER BAĞIMLIDIR</strong>.</p>
            </div>
        </div>
    </div>
</div>
"""
    }
]

# -*- coding: utf-8 -*-
"""
15 Dakika Vize Hapı & Formül Kartları
Dr. Yusuf Karadede Lisans Notları Birebir Özet
(Modern SVG İkonlar, Sıfır Emoji)
"""

CHEATSHEET_CARDS = [
    {
        "title": "1. Homojen Sistemde Aşikar Olmayan Çözüm Şartı",
        "tag": "Vizede Kesin Çıkar",
        "color": "rose",
        "icon": """<svg class="w-5 h-5 text-rose-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>""",
        "rule": r"Homojen sistemde ($AX=0$) sıfırdan farklı ($x,y,z \neq 0$) çözüm olması için TEK ŞART: $$\det(A) = 0$$",
        "tip": "Katsayılar matrisinin determinantını 0'a eşitle, sorudaki parametreyi ($k$) bul, sonra yerine koyup serbest değişken ($z=\mu$) ile genel çözümü yaz!"
    },
    {
        "title": "2. Sarrus Kuralı Nerede Uygulanır, Nerede Uygulanamaz?",
        "tag": "En Yaygın Hata",
        "color": "amber",
        "icon": """<svg class="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>""",
        "rule": r"Sarrus Kuralı SADECE VE SADECE $3 \times 3$ matrislerde geçerlidir! $$4 \times 4 \text{ ve üstünde KESİNLİKLE UYGULANAMAZ!}$$",
        "tip": "4x4 veya daha büyük matris gelirse MUTLAKA en çok sıfırı olan satır veya sütuna göre Laplace açılımı yap!"
    },
    {
        "title": "3. Rank ve Çözüm Durumları (Rouché-Capelli Altın Tablosu)",
        "tag": "Sistem Çözümleri",
        "color": "blue",
        "icon": """<svg class="w-5 h-5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>""",
        "rule": r"• $\text{rank}(A) < \text{rank}([A|B]) \implies$ ÇÖZÜM YOKTUR ($\emptyset$)<br>• $\text{rank}(A) = \text{rank}([A|B]) = n \implies$ TEK ÇÖZÜM<br>• $\text{rank}(A) = \text{rank}([A|B]) = r < n \implies$ SONSUZ ÇÖZÜM ($n-r$ serbest değişken)",
        "tip": "Artırılmış matriste en alt satır $[0\ 0\ 0 \mid c]$ ($c \neq 0$) çıkarsa hiç vakit kaybetme: 'Sistem uyumsuzdur, çözüm yoktur' de!"
    },
    {
        "title": "4. Adjoint (Ek Matris) ve Ters Matris İlişkisi",
        "tag": "Ters Matris",
        "color": "emerald",
        "icon": """<svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg>""",
        "rule": r"$$A^{-1} = \frac{1}{|A|} \text{adj}(A) \quad (|A| \neq 0)$$ $$\text{adj}(A) = [A_{ij}]^T \quad (\text{Kofaktörler Matrisinin Transpozesi!})$$",
        "tip": "Kofaktörleri bulduktan sonra TRANSPOZESİNİ ALMAYI UNUTMA! $|A|=0$ ise ters matris YOKTUR (singüler matris)."
    },
    {
        "title": "5. Matris Çarpımının 2 Hayati Kuralı",
        "tag": "İşlemler",
        "color": "purple",
        "icon": """<svg class="w-5 h-5 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>""",
        "rule": r"1) Çarpılabilirlik: $A_{m \times k} \cdot B_{k \times n} = C_{m \times n}$ (İç boyutlar eşit olmalı!)<br>2) $A \cdot B \neq B \cdot A$ (Değişme özelliği YOKTUR!)",
        "tip": "Soru sana $A \cdot B = B \cdot A$ diyorsa bu çok özel bir durumdur, genel olarak eşit kabul etme!"
    },
    {
        "title": "6. Cramer Kuralında Sonsuz Çözüm Durumu",
        "tag": "Cramer",
        "color": "indigo",
        "icon": """<svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>""",
        "rule": r"$\Delta = 0$ ve $\Delta_1 = \Delta_2 = \Delta_3 = 0$ ise sistemin SONSUZ ÇÖZÜMÜ vardır.",
        "tip": "Hemen bir denklemi at, $x_3 = \mu$ veya $t$ de. Diğerlerini $\mu$'ye bağla. Hoca özel çözüm isterse $\mu=0$ ve $\mu=3$ verip noktaları yaz!"
    },
    {
        "title": "7. Antisimetrik Matrisin Gizli Kuralı",
        "tag": "Tanımlar",
        "color": "cyan",
        "icon": """<svg class="w-5 h-5 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>""",
        "rule": r"Antisimetrik matriste $A^T = -A$'dır. Bu tanım gereği: $$\text{Ana köşegen elemanlarının TAMAMI SIFIRDIR } (a_{ii} = 0)!$$",
        "tip": "Eğer sınavda köşegeninde sıfırdan farklı sayı olan bir matrise antisimetrik dersen hoca anında çizer!"
    }
]

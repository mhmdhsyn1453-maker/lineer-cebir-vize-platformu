# -*- coding: utf-8 -*-
"""
Hocanın PDF'lerindeki Tüm Çözümlü Sorular (Vize Arşivi)
Hafta 11 & Hafta 12 + Hafta 1, 3, 4, 5 Problemleri
Adım Adım, Eksiksiz, Sıfırdan Mantıklı Çözümler
(Tamamen SVG İkonlar, Sıfır Emoji)
"""

SOLVED_PROBLEMS = [
    {
        "id": "h11_o1",
        "category": "Determinantlar",
        "title": "Hafta 11 - Örnek 1: $2 \\times 2$ Temel Determinant Hesabı",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 2)",
        "question": r"Aşağıdaki $2 \times 2$ determinantın değerini hesaplayınız: $$\Delta = \begin{vmatrix} 4 & 2 \\ 6 & 0 \end{vmatrix}$$",
        "steps": [
            r"<strong>Kural Hatırlatması:</strong> $2 \times 2$ determinantta sol üstten sağ alta çarpımdan, sağ üstten sol alta çarpım çıkarılır: $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = a \cdot d - b \cdot c$.",
            r"<strong>1. Çarpım (Ana Köşegen):</strong> $4 \cdot 0 = 0$",
            r"<strong>2. Çarpım (Ters Köşegen):</strong> $2 \cdot 6 = 12$",
            r"<strong>Sonuç:</strong> $\Delta = 0 - 12 = -12$. (Determinant sıfırdan farklı olduğu için bu matrisin tersi vardır!)."
        ],
        "result": r"\Delta = -12"
    },
    {
        "id": "h11_o2",
        "category": "Determinantlar",
        "title": "Hafta 11 - Örnek 2: Negatif Elemanlı $2 \\times 2$ Determinant",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 2)",
        "question": r"Aşağıdaki determinantın değerini hesaplayınız: $$\Delta = \begin{vmatrix} -3 & 2 \\ 9 & 4 \end{vmatrix}$$",
        "steps": [
            r"<strong>Kural:</strong> $(a \cdot d) - (b \cdot c)$",
            r"<strong>1. Çarpım:</strong> $(-3) \cdot 4 = -12$",
            r"<strong>2. Çarpım:</strong> $2 \cdot 9 = 18$",
            r"<strong>Farkı Al:</strong> $\Delta = -12 - 18 = -30$."
        ],
        "result": r"\Delta = -30"
    },
    {
        "id": "h11_o3",
        "category": "Determinantlar",
        "title": "Hafta 11 - Örnek 3: Çift Eksi İşaretli $2 \\times 2$ Determinant",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 3)",
        "question": r"Aşağıdaki determinantın değerini hesaplayınız: $$\Delta = \begin{vmatrix} 2 & -4 \\ 3 & 10 \end{vmatrix}$$",
        "steps": [
            r"<strong>1. Çarpım:</strong> $2 \cdot 10 = 20$",
            r"<strong>2. Çarpım:</strong> $(-4) \cdot 3 = -12$",
            r"<strong>Kritik İşaret Adımı:</strong> Çıkarma işlemindeki eksi ile $-12$'nin eksisi yan yana gelince artıya döner: $\Delta = 20 - (-12) = 20 + 12 = 32$."
        ],
        "result": r"\Delta = 32"
    },
    {
        "id": "h11_o4",
        "category": "Determinantlar",
        "title": "Hafta 11 - Örnek 4: Sarrus Kuralı ile $3 \\times 3$ Determinant",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 3-4)",
        "question": r"Aşağıdaki determinantı <strong>Sarrus Kuralı</strong> ile hesaplayınız: $$\Delta = \begin{vmatrix} 3 & 2 & -2 \\ -1 & 0 & 1 \\ 2 & 1 & 2 \end{vmatrix}$$",
        "steps": [
            r"<strong>Adım 1 (İlk 2 satırı alta kopyala):</strong><br>$$\begin{matrix} 3 & 2 & -2 \\ -1 & 0 & 1 \\ 2 & 1 & 2 \\ \hline 3 & 2 & -2 \\ -1 & 0 & 1 \end{matrix}$$",
            r"<strong>Adım 2 (Sol üstten sağ alta inen 3 çaprazı çarp ve topla):</strong><br>• $3 \cdot 0 \cdot 2 = 0$<br>• $(-1) \cdot 1 \cdot (-2) = 2$<br>• $2 \cdot 2 \cdot 1 = 4$<br>Toplam $(+) = 0 + 2 + 4 = \mathbf{6}$",
            r"<strong>Adım 3 (Sağ üstten sol alta inen 3 çaprazı çarp ve topla):</strong><br>• $(-2) \cdot 0 \cdot 2 = 0$<br>• $1 \cdot 1 \cdot 3 = 3$<br>• $2 \cdot 2 \cdot (-1) = -4$<br>Toplam $(-)$ = $0 + 3 + (-4) = \mathbf{-1}$",
            r"<strong>Adım 4 (Farkı al):</strong><br>$$\Delta = (+) - (-) = 6 - (-1) = 6 + 1 = \mathbf{7}$$"
        ],
        "result": r"\Delta = 7"
    },
    {
        "id": "h11_o5",
        "category": "Determinantlar",
        "title": "Hafta 11 - Örnek 5: Laplace Açılımı ile $3 \\times 3$ Determinant",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 4-5)",
        "question": r"Aşağıdaki determinantı 1. satıra göre <strong>Laplace Açılımı</strong> yardımıyla hesaplayınız: $$\Delta = \begin{vmatrix} 1 & -1 & 2 \\ 0 & 3 & 2 \\ 1 & 3 & -2 \end{vmatrix}$$",
        "steps": [
            r"<strong>Laplace 1. Satır Formülü:</strong> $\Delta = a_{11}A_{11} + a_{12}A_{12} + a_{13}A_{13}$",
            r"<strong>Dama Tahtası İşaretleri:</strong> $a_{11}$ için $(+)$, $a_{12}$ için $(-)$, $a_{13}$ için $(+)$",
            r"<strong>1. Terim ($a_{11}=1$):</strong> 1. satır ve 1. sütunu kapat:<br>$1 \cdot (+1) \cdot \begin{vmatrix} 3 & 2 \\ 3 & -2 \end{vmatrix} = 1 \cdot [(-6) - (6)] = -12$",
            r"<strong>2. Terim ($a_{12}=-1$):</strong> 1. satır ve 2. sütunu kapat:<br>$(-1) \cdot (-1) \cdot \begin{vmatrix} 0 & 2 \\ 1 & -2 \end{vmatrix} = +1 \cdot [0 - 2] = -2$",
            r"<strong>3. Terim ($a_{13}=2$):</strong> 1. satır ve 3. sütunu kapat:<br>$2 \cdot (+1) \cdot \begin{vmatrix} 0 & 3 \\ 1 & 3 \end{vmatrix} = 2 \cdot [0 - 3] = -6$",
            r"<strong>Toplam:</strong> $\Delta = -12 + (-2) + (-6) = \mathbf{-20}$."
        ],
        "result": r"\Delta = -20"
    },
    {
        "id": "h11_o6",
        "category": "Determinantlar",
        "title": "Hafta 11 - Örnek 6: En Çok Sıfır Olan Satıra Göre Laplace Açılımı",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 5)",
        "question": r"Aşağıdaki determinantı en uygun satıra göre Laplace açılımı ile hesaplayınız: $$\Delta = \begin{vmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 0 & 0 & 5 \end{vmatrix}$$",
        "steps": [
            r"<strong>Stratejik Tercih:</strong> 3. satırda iki adet $0$ vardır ($a_{31}=0, a_{32}=0, a_{33}=5$). Sıfırların kofaktörünü hesaplamaya gerek yoktur, çünkü sıfırla çarpılınca yok olurlar!",
            r"<strong>Formül:</strong> $\Delta = 0 \cdot A_{31} + 0 \cdot A_{32} + 5 \cdot A_{33} = 5 \cdot A_{33}$",
            r"<strong>$A_{33}$ Kofaktörü (3. satır ve 3. sütunu kapat, işaret $(-1)^{3+3}=+1$):</strong><br>$$A_{33} = (+1) \cdot \begin{vmatrix} 1 & 2 \\ 4 & 5 \end{vmatrix} = (1 \cdot 5) - (2 \cdot 4) = 5 - 8 = -3$$",
            r"<strong>Sonuç:</strong> $\Delta = 5 \cdot (-3) = \mathbf{-15}$."
        ],
        "result": r"\Delta = -15"
    },
    {
        "id": "h11_sist_o1",
        "category": "Lineer Sistemler",
        "title": "Hafta 11 - Sistem Örnek 1: Determinant ile Sonsuz Çözümlü Sistem Analizi",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 8-11)",
        "question": r"Aşağıdaki sistemi determinantlar yardımıyla inceleyip çözünüz: $$\begin{cases} 2x_1 + x_2 - 3x_3 = 5 \\ 4x_1 + 2x_2 - 6x_3 = 10 \\ x_1 - x_2 + 2x_3 = 1 \end{cases}$$",
        "steps": [
            r"<strong>Adım 1: Katsayılar Determinantı ($\Delta$):</strong><br>$$\Delta = \begin{vmatrix} 2 & 1 & -3 \\ 4 & 2 & -6 \\ 1 & -1 & 2 \end{vmatrix}$$<br>Dikkat edilirse 2. denklem, 1. denklemin tam 2 katıdır ($4x_1+2x_2-6x_3 = 2 \cdot (2x_1+x_2-3x_3)$). Determinant kuralı gereği iki satır orantılıysa <strong>$\Delta = 0$</strong>'dır!",
            r"<strong>Adım 2: $\Delta_1, \Delta_2, \Delta_3$ Analizi:</strong> Eşitliğin sağındaki sonuçlar da aynı orana sahiptir ($10 = 2 \cdot 5$). Dolayısıyla tüm $\Delta_j = 0$ çıkar.",
            r"<strong>Adım 3: Teorem Sonucu:</strong> $\Delta = 0$ ve tüm $\Delta_j = 0$ olduğundan bu sistemin <strong>SONSUZ SAYIDA ÇÖZÜMÜ VARDIR</strong>.",
            r"<strong>Adım 4: Genel Çözümün Bulunması:</strong><br>2. denklem 1. denklemin kopyası olduğu için elenir. Geriye 2 adet bağımsız denklem kalır:<br>1) $2x_1 + x_2 - 3x_3 = 5$<br>2) $x_1 - x_2 + 2x_3 = 1$",
            r"Bilinmeyen sayısı 3, bağımsız denklem sayısı 2 olduğundan $3 - 2 = 1$ serbest parametre seçilir. <strong>$x_3 = \mu$</strong> diyelim:<br>$$\begin{cases} 2x_1 + x_2 = 5 + 3\mu \\ x_1 - x_2 = 1 - 2\mu \end{cases}$$",
            r"İki denklemi taraf tarafa topla: $3x_1 = 6 + \mu \implies x_1 = \frac{\mu + 6}{3}$<br>Denklemde yerine koy: $x_2 = x_1 - (1 - 2\mu) = \frac{7\mu + 3}{3}$",
            r"<strong>Adım 5: Özel Çözümler:</strong> $\mu$'ye istediğimiz sayıyı verebiliriz:<br>• $\mu = 0$ için $\implies (x_1=2, x_2=1, x_3=0)$<br>• $\mu = 3$ için $\implies (x_1=3, x_2=8, x_3=3)$"
        ],
        "result": r"x_1 = \frac{\mu+6}{3}, \quad x_2 = \frac{7\mu+3}{3}, \quad x_3 = \mu \quad (\mu \in \mathbb{R})"
    },
    {
        "id": "h11_sist_o2",
        "category": "Lineer Sistemler",
        "title": "Hafta 11 - Sistem Örnek 2: Cramer Kuralı ile Tek Çözümlü Sistem",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 11-12)",
        "question": r"Cramer Kuralı yardımıyla aşağıdaki denklem sistemini çözünüz: $$\begin{cases} x_1 + 2x_2 - x_3 = -7 \\ 2x_1 - x_2 + 3x_3 = 11 \\ 3x_1 + x_2 + x_3 = 2 \end{cases}$$",
        "steps": [
            r"<strong>Adım 1: Katsayılar Determinantı ($\Delta$):</strong><br>$$\Delta = \begin{vmatrix} 1 & 2 & -1 \\ 2 & -1 & 3 \\ 3 & 1 & 1 \end{vmatrix} = -5 \neq 0$$<br>$\Delta \neq 0$ olduğu için sistem <strong>CRAMER SİSTEMİDİR ve TEK BİR ÇÖZÜMÜ VARDIR</strong>.",
            r"<strong>Adım 2: $\Delta_1$ Hesabı (1. sütun yerine sonuçları $[-7, 11, 2]^T$ yaz):</strong><br>$$\Delta_1 = \begin{vmatrix} -7 & 2 & -1 \\ 11 & -1 & 3 \\ 2 & 1 & 1 \end{vmatrix} = 5$$",
            r"<strong>Adım 3: $\Delta_2$ Hesabı (2. sütun yerine sonuçları yaz):</strong><br>$$\Delta_2 = \begin{vmatrix} 1 & -7 & -1 \\ 2 & 11 & 3 \\ 3 & 2 & 1 \end{vmatrix} = -10$$",
            r"<strong>Adım 4: $\Delta_3$ Hesabı (3. sütun yerine sonuçları yaz):</strong><br>$$\Delta_3 = \begin{vmatrix} 1 & 2 & -7 \\ 2 & -1 & 11 \\ 3 & 1 & 2 \end{vmatrix} = 15$$",
            r"<strong>Adım 5: Değerleri Bölerek Bul:</strong><br>• $x_1 = \frac{\Delta_1}{\Delta} = \frac{5}{-5} = \mathbf{-1}$<br>• $x_2 = \frac{\Delta_2}{\Delta} = \frac{-10}{-5} = \mathbf{2}$<br>• $x_3 = \frac{\Delta_3}{\Delta} = \frac{15}{-5} = \mathbf{-3}$"
        ],
        "result": r"x_1 = -1, \quad x_2 = 2, \quad x_3 = -3"
    },
    {
        "id": "h11_sist_o3",
        "category": "Lineer Sistemler",
        "title": "Hafta 11 - Sistem Örnek 3: Homojen Sistemde Aşikar Olmayan Çözüm Parametresi ($k$)",
        "source": "lineer-cebir-11_-hafta.pdf (Sayfa 13-14)",
        "question": r"Aşağıdaki homojen sistemin aşikar olandan ($0,0,0$) farklı çözümlerinin olması için $k$ ne olmalıdır? Bu $k$ değerine göre genel çözümü bulunuz: $$\begin{cases} 3x + ky - z = 0 \\ 2x - 2y + 3z = 0 \\ x + 5y + 2z = 0 \end{cases}$$",
        "steps": [
            r"<strong>Teori:</strong> Homojen sistemde sıfırdan farklı çözüm olması için katsayılar matrisinin determinantı <strong>SIFIR OLMALIDIR ($\Delta = 0$)</strong>!",
            r"<strong>Adım 1: Determinantı 0'a Eşitle:</strong><br>$$\Delta = \begin{vmatrix} 3 & k & -1 \\ 2 & -2 & 3 \\ 1 & 5 & 2 \end{vmatrix} = 0$$",
            r"1. Satıra göre Laplace açılımı yapalım:<br>$3 \cdot (-4 - 15) - k \cdot (4 - 3) - 1 \cdot (10 - (-2)) = 0$<br>$3(-19) - k(1) - 12 = 0 \implies -57 - k - 12 = 0 \implies \mathbf{k = -69}$!",
            r"<strong>Adım 2: Genel Çözümün Bulunması:</strong><br>$k = -69$ için sistem bağımlıdır. 2. ve 3. denklemleri alalım:<br>1) $2x - 2y + 3z = 0$<br>2) $x + 5y + 2z = 0$",
            r"$z = \mu$ yardımcı serbest bilinmeyen seçelim:<br>$$\begin{cases} 2x - 2y = -3\mu \\ x + 5y = -2\mu \end{cases}$$",
            r"Denklem sistemi çözüldüğünde: $x = -\frac{19}{12}\mu, \quad y = -\frac{1}{12}\mu, \quad z = \mu$ elde edilir."
        ],
        "result": r"k = -69, \quad x = -\frac{19}{12}\mu, \quad y = -\frac{1}{12}\mu, \quad z = \mu"
    },
    {
        "id": "h12_o5",
        "category": "Matris Cebiri",
        "title": "Hafta 12 - Örnek 5: Singüler Matris ve Tersi Olmama Durumu",
        "source": "lineer-cebir-12_-hafta.pdf (Sayfa 7)",
        "question": r"Aşağıdaki $A$ matrisinin tersini bulunuz: $$A = \begin{bmatrix} 3 & 6 \\ 2 & 4 \end{bmatrix}$$",
        "steps": [
            r"<strong>Adım 1 (İlk Refleks):</strong> Bir matrisin tersini aramadan önce İLK OLARAK determinantını hesaplamalısın!",
            r"<strong>Adım 2 (Determinant Hesabı):</strong><br>$$|A| = \begin{vmatrix} 3 & 6 \\ 2 & 4 \end{vmatrix} = (3 \cdot 4) - (6 \cdot 2) = 12 - 12 = 0$$",
            r"<strong>Adım 3 (Hüküm):</strong> $|A| = 0$ olduğu için bu matris <strong>SİNGÜLERDİR (TEKİLDİR)</strong> ve <strong>TERSİ YOKTUR!</strong> (Ters formülündeki paydada 0 olamayacağı için ters matris tanımsızdır)."
        ],
        "result": r"|A| = 0 \implies \text{A matrisinin tersi YOKTUR (Singüler Matris)}."
    },
    {
        "id": "h12_o9",
        "category": "Denk Matrisler & Rank",
        "title": "Hafta 12 - Örnek 9: Elementer Satır İşlemleri ile Kanonik Form ve Rank",
        "source": "lineer-cebir-12_-hafta.pdf (Sayfa 10-12)",
        "question": r"Aşağıdaki matrisi elementer satır işlemleriyle kanonik (eşelon) hale getirip rankını bulunuz: $$A = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & -1 & 5 \\ 3 & 6 & -2 & 8 \end{bmatrix}$$",
        "steps": [
            r"<strong>Hedefimiz:</strong> 1. sütunun altındaki sayıları ($2$ ve $3$) sıfırlamak!",
            r"<strong>1. Hamle ($S_2 - 2S_1 \to S_2$):</strong> 2. satırdan 1. satırın 2 katını çıkar:<br>$[2, 4, -1, 5] - [2, 4, -2, 6] = [0, 0, 1, -1]$",
            r"<strong>2. Hamle ($S_3 - 3S_1 \to S_3$):</strong> 3. satırdan 1. satırın 3 katını çıkar:<br>$[3, 6, -2, 8] - [3, 6, -3, 9] = [0, 0, 1, -1]$",
            r"Matris:<br>$$\begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 1 & -1 \end{bmatrix}$$",
            r"<strong>3. Hamle ($S_3 - S_2 \to S_3$):</strong> 3. satırdan 2. satırı çıkar:<br>$[0, 0, 1, -1] - [0, 0, 1, -1] = [0, 0, 0, 0]$ (3. satır komple sıfırlandı!)",
            r"Kanonik Matris:<br>$$\begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 1 & -1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$",
            r"<strong>Rank Kuralı:</strong> Sıfırdan farklı satır sayısı = 2'dir.<br>Dolayısıyla matrisin <strong>RANKI = 2</strong>'dir!"
        ],
        "result": r"\text{rank}(A) = 2"
    },
    {
        "id": "h12_o11",
        "category": "Lineer Sistemler",
        "title": "Hafta 12 - Örnek 11: Artırılmış Matris ile Sonsuz Çözümlü Sistem (Gauss)",
        "source": "lineer-cebir-12_-hafta.pdf (Sayfa 13-14)",
        "question": r"Gauss eliminasyon yöntemiyle aşağıdaki sistemi çözünüz: $$\begin{cases} x_1 - x_2 + 2x_3 = 1 \\ 3x_1 + 2x_2 - x_3 = 5 \\ 2x_1 + 3x_2 - 3x_3 = 4 \end{cases}$$",
        "steps": [
            r"<strong>Adım 1: Artırılmış Matrisi $[A \mid B]$ Yaz:</strong><br>$$\left[\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 3 & 2 & -1 & 5 \\ 2 & 3 & -3 & 4 \end{array}\right]$$",
            r"<strong>Adım 2: 1. Sütunu Sıfırla:</strong><br>• $S_2 - 3S_1 \to S_2$: $[0, 5, -7 \mid 2]$<br>• $S_3 - 2S_1 \to S_3$: $[0, 5, -7 \mid 2]$",
            r"<strong>Adım 3: 3. Satırı Sıfırla ($S_3 - S_2 \to S_3$):</strong><br>$$\left[\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 0 & 5 & -7 & 2 \\ 0 & 0 & 0 & 0 \end{array}\right]$$",
            r"<strong>Adım 4: Rank Analizi:</strong> $\text{rank}(A) = \text{rank}([A \mid B]) = 2 < 3$ (bilinmeyen sayısı). <strong>SONSUZ ÇÖZÜM VARDIR!</strong>",
            r"<strong>Adım 5: Genel Çözüm ($x_3 = t$):</strong><br>• 2. satırdan: $5x_2 - 7t = 2 \implies x_2 = \frac{2}{5} + \frac{7}{5}t$<br>• 1. satırdan yerine koyarak: $x_1 = \frac{7}{5} - \frac{3}{5}t$"
        ],
        "result": r"x_1 = \frac{7}{5} - \frac{3}{5}t, \quad x_2 = \frac{2}{5} + \frac{7}{5}t, \quad x_3 = t \quad (t \in \mathbb{R})"
    },
    {
        "id": "h12_o12",
        "category": "Lineer Sistemler",
        "title": "Hafta 12 - Örnek 12: Uyumsuz (Çözümsüz) Sistem Analizi (Gauss)",
        "source": "lineer-cebir-12_-hafta.pdf (Sayfa 14-15)",
        "question": r"Aşağıdaki sistemi Gauss yöntemiyle inceleyip çözünüz: $$\begin{cases} x_1 + x_3 = 1 \\ 2x_1 - x_2 + 2x_3 = 0 \\ 2x_1 + 2x_2 + 2x_3 = 1 \end{cases}$$",
        "steps": [
            r"<strong>Adım 1: Artırılmış Matrisi Yaz:</strong><br>$$\left[\begin{array}{ccc|c} 1 & 0 & 1 & 1 \\ 2 & -1 & 2 & 0 \\ 2 & 2 & 2 & 1 \end{array}\right]$$",
            r"<strong>Adım 2: 1. Sütunu Sıfırla:</strong><br>• $S_2 - 2S_1 \to S_2$: $[0, -1, 0 \mid -2]$<br>• $S_3 - 2S_1 \to S_3$: $[0, 2, 0 \mid -1]$",
            r"<strong>Adım 3: $S_3 + 2S_2 \to S_3$:</strong><br>Satır 3: $[0, 2 + 2(-1), 0 \mid -1 + 2(-2)] = [0, 0, 0 \mid -5]$",
            r"Eşelon Matris:<br>$$\left[\begin{array}{ccc|c} 1 & 0 & 1 & 1 \\ 0 & -1 & 0 & -2 \\ 0 & 0 & 0 & -5 \end{array}\right]$$",
            r"<strong>Adım 4: Çelişkiyi Gör:</strong><br>Son satır şunu söyler: $0 \cdot x_1 + 0 \cdot x_2 + 0 \cdot x_3 = -5 \implies \mathbf{0 = -5}$!<br>Sıfır eksi beşe eşit olamaz!",
            r"<strong>Sonuç:</strong> $\text{rank}(A) = 2 \neq \text{rank}([A \mid B]) = 3$ olduğundan sistem <strong>UYUMSUZDUR (TUTARSIZDIR)</strong>. Çözüm kümesi boştur: $\mathcal{C} = \emptyset$."
        ],
        "result": r"\text{rank}(A) \neq \text{rank}([A \mid B]) \implies \text{ÇÖZÜM YOKTUR } (\mathcal{C} = \emptyset)"
    }
]

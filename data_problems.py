# -*- coding: utf-8 -*-
"""
Lineer Cebir Vize Problemleri & Geçen Yılın Orijinal Çıkmış Vize Sınavı
Sıfırdan Zirveye, Çocuğa Anlatır Gibi Kristal Netliğinde Çözümler
(Tamamen SVG İkonlar, Sıfır Emoji)
"""

REAL_EXAM_QUESTIONS = [
    {
        "id": "cikmis_1",
        "q_num": 1,
        "title": "Soru 1: Matris Eşitliğinden 4 Bilinmeyenli Denklem Çözümü",
        "score": "15 Puan",
        "badge": "Matris Eşitliği",
        "question": r"""Aşağıda verilen matris eşitliklerinden elde edilen denklem sistemlerini çözünüz:
$$\begin{bmatrix}
2 & x-2 & -1 \\
3 & y+1 & 0
\end{bmatrix}_{2 \times 3}
=
\begin{bmatrix}
2x-y & 2 & z-t \\
z+t & 7 & 0
\end{bmatrix}_{2 \times 3}$$""",
        "kid_logic": r"""<strong>Çocuğa Anlatır Gibi Temel Mantık:</strong><br>
İki matris birbirine eşit ($\mathbf{A = B}$) diyorsa, bu tıpkı iki ikiz kutu gibidir! Sol kutunun 1. kat 2. odasındaki sayı neyse, sağ kutunun da 1. kat 2. odasındaki sayı <strong>tıpatıp aynı</strong> olmak zorundadır. Tek yapmamız gereken kutuları karşılıklı eşleştirip ilkokul denklem çözümü gibi bilinmeyenleri bulmak!""",
        "steps": [
            r"<strong>1. Eşleşme ($x$'i Bulma):</strong> 1. satır, 2. sütundaki elemanları birbirine eşitleyelim:<br>$$x - 2 = 2 \implies x = 2 + 2 \implies \mathbf{x = 4}$$",
            r"<strong>2. Eşleşme ($y$'yi Bulma):</strong> 2. satır, 2. sütundaki elemanları eşitleyelim:<br>$$y + 1 = 7 \implies y = 7 - 1 \implies \mathbf{y = 6}$$",
            r"<strong>1. Satır 1. Sütun Kontrolü:</strong> $2 = 2x - y$ denkleminde bulduğumuz $x=4$ ve $y=6$'yı yerine koyalım:<br>$$2(4) - 6 = 8 - 6 = 2 \quad (\text{Harika! Eşitlik doğrulandı!})$$",
            r"<strong>3. Eşleşme ($z$ ve $t$ için İki Basit Denklem):</strong><br>• 1. satır 3. sütun: $z - t = -1$<br>• 2. satır 1. sütun: $z + t = 3$",
            r"<strong>4. İki Denklemi Alt Alta Toplama (Eski Yöntem):</strong><br>$$\begin{array}{r@{\ }l} z - t &= -1 \\ +\quad z + t &= 3 \\ \hline 2z &= 2 \implies \mathbf{z = 1} \end{array}$$",
            r"<strong>5. $t$'yi Bulma:</strong> $z=1$ değerini $z + t = 3$ denkleminde yerine koyalım:<br>$$1 + t = 3 \implies \mathbf{t = 2}$$",
            r"<strong>6. 2. Satır 3. Sütun Kontrolü:</strong> $0 = 0$ (Zaten eşit, soru eksiksiz sağlandı)."
        ],
        "exam_trap": r"<strong>Hoca Nereden Puan Kırar?</strong> Öğrenciler genelde $x=4$ ve $y=6$'yı kolayca bulur ama $z-t=-1$ ile $z+t=3$ sistemini çözerken eksi işaretini karıştırıp $t$'yi yanlış bulur. Sınav kağıdında bulduğunuz tüm değerleri ($x, y, z, t$) matrise geri koyup eşitliğin sağlandığını 1 satırla hocaya gösterirseniz tam puan alırsınız!",
        "result": r"x = 4, \quad y = 6, \quad z = 1, \quad t = 2"
    },
    {
        "id": "cikmis_2",
        "q_num": 2,
        "title": "Soru 2: $5 \times 6$ Matrisini Kanonik (Eşelon) Hale Getirerek Rankını Bulma",
        "score": "20 Puan",
        "badge": "Kanonik Form & Rank",
        "question": r"""Aşağıda verilen $A$ matrisini kanonik (satır eşelon) hale getirerek rankını bulunuz:
$$A = \begin{bmatrix}
2 & 2 & 1 & 0 & 1 & 0 \\
3 & 4 & 0 & 0 & 0 & 0 \\
6 & 6 & 6 & 1 & 0 & 5 \\
2 & 3 & 1 & 0 & 1 & 0 \\
1 & 1 & 1 & 0 & 1 & 0
\end{bmatrix}_{5 \times 6}$$""",
        "kid_logic": r"""<strong>Çocuğa Anlatır Gibi Temel Mantık:</strong><br>
<strong>Rank nedir?</strong> Bir matriste satırları birbiriyle toplayıp çıkararak merdiven basamağı (eşelon form) yaptığımızda <strong>yok olmayan (tamamen sıfıra dönüşmeyen) satır sayısıdır</strong>!<br>
Eğer bir satır diğerlerinin gizli bir kopyasıysa sıfırlanıp uçar. Kalan diri satırlar matrisin gücünü (rankını) gösterir.""",
        "steps": [
            r"<strong>1. Hamle (En Akıllıca Başlangıç - Pivotu 1 Yapma):</strong><br>5. satıra dikkatle bakın: $[1, 1, 1, 0, 1, 0]$! Zaten $1$ ile başlıyor. Kesirlerle uğraşmamak için hemen 1. satır ile 5. satırın yerini değiştirelim ($S_1 \leftrightarrow S_5$):<br>$$A \sim \begin{bmatrix} 1 & 1 & 1 & 0 & 1 & 0 \\ 3 & 4 & 0 & 0 & 0 & 0 \\ 6 & 6 & 6 & 1 & 0 & 5 \\ 2 & 3 & 1 & 0 & 1 & 0 \\ 2 & 2 & 1 & 0 & 1 & 0 \end{bmatrix}$$",
            r"<strong>2. Hamle (1. Sütundaki Tüm Alt Elemanları Sıfırlama):</strong><br>1. satırdaki $1$'i pivot alıp altındakileri yok edelim:<br>• $S_2 \leftarrow S_2 - 3S_1 = [0, 1, -3, 0, -3, 0]$<br>• $S_3 \leftarrow S_3 - 6S_1 = [0, 0, 0, 1, -6, 5]$<br>• $S_4 \leftarrow S_4 - 2S_1 = [0, 1, -1, 0, -1, 0]$<br>• $S_5 \leftarrow S_5 - 2S_1 = [0, 0, -1, 0, -1, 0]$<br>Matris:<br>$$\begin{bmatrix} 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & -3 & 0 & -3 & 0 \\ 0 & 0 & 0 & 1 & -6 & 5 \\ 0 & 1 & -1 & 0 & -1 & 0 \\ 0 & 0 & -1 & 0 & -1 & 0 \end{bmatrix}$$",
            r"<strong>3. Hamle (2. Sütunu Sıfırlama):</strong><br>2. satır pivotu $1$'dir. 4. satırdaki $1$'i sıfırlamak için $S_4 \leftarrow S_4 - S_2$ yapalım:<br>$$[0, 1, -1, 0, -1, 0] - [0, 1, -3, 0, -3, 0] = [0, 0, 2, 0, 2, 0]$$",
            r"<strong>4. Hamle (Hayati Adım - Satırın Sıfırlanması!):</strong><br>Yeni 4. satır $[0, 0, 2, 0, 2, 0]$ (2'ye bölersek $[0, 0, 1, 0, 1, 0]$).<br>5. satır ise $[0, 0, -1, 0, -1, 0]$!<br>İkisini toplarsak ($S_5 \leftarrow S_5 + \frac{1}{2}S_4$):<br>$$[0, 0, -1, 0, -1, 0] + [0, 0, 1, 0, 1, 0] = [\mathbf{0, 0, 0, 0, 0, 0}]$$<br><strong>5. satır tamamen sıfırlandı!</strong>",
            r"<strong>5. Hamle (Basamakları Düzenleme):</strong><br>Pivot sütunlarına göre satırları sıraladığımızda:<br>$$\begin{bmatrix} 1 & 1 & 1 & 0 & 1 & 0 \\ 0 & 1 & -3 & 0 & -3 & 0 \\ 0 & 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & -6 & 5 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$",
            r"<strong>Rank Hesabı:</strong> Sıfırdan farklı satır sayısı tam <strong>4</strong> adettir. En alt satır tamamen sıfırlanmıştır."
        ],
        "exam_trap": r"<strong>Hoca Nereden Puan Kırar?</strong> 1. satırı doğrudan 2'ye bölüp rasyonel sayılarla ($\frac{1}{2}$) işlem yapmaya kalkan öğrenci 5 dakika içinde işlem hatası yapıp tıkanır. Sırrımız: 5. satırdaki hazır $1$'i yukarı taşımaktır! Ayrıca 5. satırın tamamen $[0, 0, 0, 0, 0, 0]$ olduğunu kağıtta göstermeden direkt rank = 4 yazarsanız işlem puanı kırılır.",
        "result": r"\text{rank}(A) = 4 \quad (\text{5 satırdan 4'ü bağımsızdır})"
    },
    {
        "id": "cikmis_3",
        "q_num": 3,
        "title": "Soru 3: $5 \times 5$ Büyük Matrisin Determinantını Satır İşlemi & Laplace ile Bulma",
        "score": "15 Puan",
        "badge": "5x5 Determinant & Laplace",
        "question": r"""Aşağıda verilen $B$ matrisinin determinantını hesaplayınız:
$$B = \begin{bmatrix}
1 & 1 & 3 & 0 & 2 \\
3 & 1 & 0 & 1 & 2 \\
0 & 1 & 3 & 0 & 2 \\
4 & -2 & 3 & 1 & 0 \\
5 & 1 & 0 & 0 & 6
\end{bmatrix}_{5 \times 5}$$""",
        "kid_logic": r"""<strong>Çocuğa Anlatır Gibi Temel Mantık:</strong><br>
Sakın panik yapma! Sarrus kuralı $5 \times 5$'te <strong>kesinlikle çalışmaz</strong>. Hoca bu soruyu sana 2 saat uğraş diye değil, <strong>akıllı bir dedektif gibi bakıp gizli benzerliği yakalaman için</strong> sordu!<br>
1. satır ile 3. satıra bir baksana: İkisinin de kuyruğu $[1, 3, 0, 2]$ ile bitiyor! Birbirinden çıkarırsan bir anda 4 tane sıfır doğar ve soru çocuk oyuncağına döner!""",
        "steps": [
            r"<strong>1. Adım (Sihirli Satır Hamlesi $S_1 - S_3$):</strong><br>Determinant kuralı: Bir satırdan diğerini çıkarırsan determinant DEĞİŞMEZ!<br>$$S_1 \leftarrow S_1 - S_3 = [1, 1, 3, 0, 2] - [0, 1, 3, 0, 2] = [\mathbf{1, 0, 0, 0, 0}]$$<br>Gördün mü? 1. satırda tam 4 tane sıfır oluştu!",
            r"<strong>2. Adım (1. Satıra Göre Laplace Açılımı):</strong><br>1. satırdaki sıfırlar yok olacağı için geriye sadece en baştaki $1$ kalır:<br>$$\det(B) = (+1) \cdot 1 \cdot \begin{vmatrix} 1 & 0 & 1 & 2 \\ 1 & 3 & 0 & 2 \\ -2 & 3 & 1 & 0 \\ 1 & 0 & 0 & 6 \end{vmatrix}_{4 \times 4}$$<br>Kocaman $5 \times 5$ matris tek hamlede $4 \times 4$'e indi!",
            r"<strong>3. Adım ($4 \times 4$ Matriste 2. Sütundaki 3'leri Yok Etme):</strong><br>2. satırda $3$, 3. satırda da $3$ var. $S_3 \leftarrow S_3 - S_2$ yapalım:<br>$$[-2, 3, 1, 0] - [1, 3, 0, 2] = [-3, 0, 1, -2]$$<br>Kalan $4 \times 4$ matris:<br>$$\begin{vmatrix} 1 & 0 & 1 & 2 \\ 1 & 3 & 0 & 2 \\ -3 & 0 & 1 & -2 \\ 1 & 0 & 0 & 6 \end{vmatrix}$$",
            r"<strong>4. Adım (2. Sütuna Göre Laplace Açılımı):</strong><br>2. sütunda sadece 2. satırdaki $3$ sayısı sıfırdan farklıdır! 2. satır 2. sütunun dama tahtası işareti $(+)$'dır:<br>$$\det(M_4) = (+1) \cdot 3 \cdot \begin{vmatrix} 1 & 1 & 2 \\ -3 & 1 & -2 \\ 1 & 0 & 6 \end{vmatrix}_{3 \times 3}$$",
            r"<strong>5. Adım ($3 \times 3$ Determinantı 3. Satıra Göre Açma):</strong><br>3. satırda bir tane $0$ var ($[1, 0, 6]$):<br>• $a_{31} = 1 \implies (+1) \cdot 1 \cdot \begin{vmatrix} 1 & 2 \\ 1 & -2 \end{vmatrix} = 1 \cdot (-2 - 2) = -4$<br>• $a_{32} = 0 \implies 0$<br>• $a_{33} = 6 \implies (+1) \cdot 6 \cdot \begin{vmatrix} 1 & 1 \\ -3 & 1 \end{vmatrix} = 6 \cdot (1 - (-3)) = 6 \cdot 4 = 24$<br>$$\det(M_3) = -4 + 24 = \mathbf{20}$$",
            r"<strong>6. Adım (Tüm Çarpanları Birleştirme):</strong><br>$$\det(M_4) = 3 \cdot 20 = 60$$<br>$$\det(B) = 1 \cdot \det(M_4) = 1 \cdot 60 = \mathbf{60}$$"
        ],
        "exam_trap": r"<strong>Hoca Nereden Puan Kırar?</strong> En büyük hata: $5 \times 5$'lik matrisi doğrudan açmaya çalışmak veya Sarrus uygulamaktır. Sarrus sadece ve sadece $3 \times 3$ içindir! Bu soruda hoca öğrencinin $S_1 - S_3$ hamlesini görüp görmediğini test eder. O adımı yazan öğrenciye hoca tam puanı basar.",
        "result": r"\det(B) = 60"
    },
    {
        "id": "cikmis_4",
        "q_num": 4,
        "title": "Soru 4: Homojen Sistemde Aşikar Olmayan Çözüm Şartı ve Genel Çözüm",
        "score": "20 Puan",
        "badge": "Homojen Sistem & Parametre",
        "question": r"""Aşağıda verilen denklem sisteminin aşikar olandan farklı çözümü olması için $k$ ne olmalıdır? Bulacağınız $k$ değerine göre sistemi çözünüz:
$$\begin{cases}
3x + ky - z = 0 \\
2x - 2y + 3z = 0 \\
x + 5y + 2z = 0
\end{cases}$$""",
        "kid_logic": r"""<strong>Çocuğa Anlatır Gibi Temel Mantık:</strong><br>
Denklemlerin sağ tarafı hep sıfır ($=0$). Bu tarz sistemlere 'homojen sistem' denir.<br>
Eğer $x=0, y=0, z=0$ verirsen denklem zaten sağlanır; buna 'aşikar (bedava) çözüm' denir.<br>
Peki <strong>'aşikar olandan farklı çözüm'</strong> ne demek? Sıfırdan başka, sonsuz tane çözüm olsun demek! Bunun tek bir kuralı vardır: <strong>Katsayılar matrisinin determinantı SIFIR olmalıdır ($\Delta = 0$)!</strong>""",
        "steps": [
            r"<strong>1. Adım (Determinantı Sıfıra Eşitle):</strong><br>Katsayılar matrisini yazalım:<br>$$\Delta = \begin{vmatrix} 3 & k & -1 \\ 2 & -2 & 3 \\ 1 & 5 & 2 \end{vmatrix} = 0$$",
            r"<strong>2. Adım (Sarrus ile Determinantı Açma):</strong><br>• Pozitif Çaprazlar: $3(-2)(2) + 2(5)(-1) + 1(k)(3) = -12 - 10 + 3k = 3k - 22$<br>• Negatif Çaprazlar: $1(-2)(-1) + 3(5)(3) + 2(k)(2) = 2 + 45 + 4k = 4k + 47$<br>$$\Delta = (3k - 22) - (4k + 47) = 3k - 22 - 4k - 47 = -k - 69$$",
            r"<strong>3. Adım ($k$ Değerini Bulma):</strong><br>$$-k - 69 = 0 \implies \mathbf{k = -69}$$",
            r"<strong>4. Adım ($k = -69$ Değerini Yerine Koyup Sistemi Çözme):</strong><br>Denklemler:<br>(1) $3x - 69y - z = 0$<br>(2) $2x - 2y + 3z = 0$<br>(3) $x + 5y + 2z = 0 \implies x = -5y - 2z$",
            r"<strong>5. Adım ($x$'i 2. Denklemde Yerine Koyma):</strong><br>$$2(-5y - 2z) - 2y + 3z = 0 \implies -10y - 4z - 2y + 3z = 0 \implies -12y - z = 0 \implies \mathbf{z = -12y}$$",
            r"<strong>6. Adım ($x$'i $y$ Cinsinden Bulma):</strong><br>$$x = -5y - 2(-12y) = -5y + 24y \implies \mathbf{x = 19y}$$<br>(1. denklemi kontrol edelim: $3(19y) - 69y - (-12y) = 57y - 69y + 12y = 0$, tam doğrulandı!)",
            r"<strong>7. Adım (Serbest Değişken Atama ve Genel Çözüm):</strong><br>$y = t$ ($t \in \mathbb{R}$) serbest parametre dersek:<br>$$x = 19t, \quad y = t, \quad z = -12t$$"
        ],
        "exam_trap": r"<strong>Hoca Nereden Puan Kırar?</strong> Öğrencilerin yarısı $k=-69$'u bulduktan sonra sınavı bitti zanneder ve sistemi çözmeyi unutarak 10 puan kaybeder! Soruda 'Bulacağınız k değerine göre sistemi çözünüz' dendiği için genel çözümü parametreye ($t$) bağlı olarak $(19t, t, -12t)$ şeklinde yazmak şarttır.",
        "result": r"k = -69, \quad (x, y, z) = (19t, t, -12t) = t \cdot (19, 1, -12), \quad t \in \mathbb{R}"
    },
    {
        "id": "cikmis_5",
        "q_num": 5,
        "title": "Soru 5: 4 Bilinmeyenli Lineer Denklem Sistemini Gauss Yok Etme ile Çözme",
        "score": "15 Puan",
        "badge": "Gauss Eliminasyon",
        "question": r"""Aşağıda verilen 4 bilinmeyenli denklem sistemini çözünüz:
$$\begin{cases}
2x_2 - x_3 + 2x_4 = 12 \\
x_1 + 4x_2 + 2x_3 + 5x_4 = -2 \\
2x_1 + x_2 + 6x_3 + x_4 = -19 \\
x_1 - x_2 + x_3 - x_4 = -3
\end{cases}$$""",
        "kid_logic": r"""<strong>Çocuğa Anlatır Gibi Temel Mantık:</strong><br>
4 bilinmeyenli denklem sistemi kocaman bir bulmaca gibidir. Gauss yöntemiyle adım adım en baştaki bilinmeyeni ($x_1$) yok ederek aşağı doğru bir merdiven kurarız.<br>
En alt basamağa ulaştığımızda tek bir bilinmeyen kalır ($x_4$). Onu bulunca domino taşları gibi geriye doğru yerine koyarak sırasıyla $x_3, x_2, x_1$ değerlerini buluruz.""",
        "steps": [
            r"<strong>1. Adım (Artırılmış Matrisi Düzenli Yazma):</strong><br>Pivotu kolaylaştırmak için $x_1 - x_2 + x_3 - x_4 = -3$ denklemini 1. satıra alalım:<br>$$\left[\begin{array}{cccc|c} 1 & -1 & 1 & -1 & -3 \\ 1 & 4 & 2 & 5 & -2 \\ 2 & 1 & 6 & 1 & -19 \\ 0 & 2 & -1 & 2 & 12 \end{array}\right]$$",
            r"<strong>2. Adım (1. Sütunu Sıfırlama):</strong><br>• $S_2 \leftarrow S_2 - S_1 = [0, 5, 1, 6 \mid 1]$<br>• $S_3 \leftarrow S_3 - 2S_1 = [0, 3, 4, 3 \mid -13]$<br>• $S_4$: zaten $0$ ile başlıyor: $[0, 2, -1, 2 \mid 12]$",
            r"<strong>3. Adım (2. Sütunda Pivotu 1 Yapma):</strong><br>$S_2 \leftarrow S_2 - 2S_4$:<br>$$[0, 5, 1, 6 \mid 1] - 2[0, 2, -1, 2 \mid 12] = [0, 1, 3, 2 \mid -23]$$<br>Harika! $x_2$'nin katsayısı $1$ oldu.",
            r"<strong>4. Adım (2. Sütunun Altını Sıfırlama):</strong><br>• $S_3 \leftarrow S_3 - 3S_2' = [0, 0, -5, -3 \mid 56]$<br>• $S_4 \leftarrow S_4 - 2S_2' = [0, 0, -7, -2 \mid 58]$",
            r"<strong>5. Adım (3. Sütunu Sıfırlayıp $x_4$'ü Çekme):</strong><br>$5S_4 - 7S_3$ işlemini yapalım:<br>$$[0, 0, 0, 5(-2) - 7(-3) \mid 5(58) - 7(56)] = [0, 0, 0, 11 \mid -102]$$<br>$$11 x_4 = -102 \implies \mathbf{x_4 = -\frac{102}{11}}$$",
            r"<strong>6. Adım (Geriye Yerine Koyma - Back Substitution):</strong><br>• $-5x_3 - 3\left(-\frac{102}{11}\right) = 56 \implies \mathbf{x_3 = -\frac{62}{11}}$<br>• $x_2 + 3x_3 + 2x_4 = -23 \implies \mathbf{x_2 = \frac{137}{11}}$<br>• $x_1 - x_2 + x_3 - x_4 = -3 \implies \mathbf{x_1 = \frac{64}{11}}$"
        ],
        "exam_trap": r"<strong>Hoca Nereden Puan Kırar?</strong> Sonuçlar paydası 11 olan rasyonel kesirler çıkınca öğrenciler 'Ben kesin işlem hatası yaptım' korkusuna kapılır ve kağıdı karalar. Hiç korkmayın! Bu soru özellikle kesirli çıkması için tasarlanmış gerçek bir sınav sorusudur. Çözüm %100 doğrudur.",
        "result": r"x_1 = \frac{64}{11}, \quad x_2 = \frac{137}{11}, \quad x_3 = -\frac{62}{11}, \quad x_4 = -\frac{102}{11}"
    },
    {
        "id": "cikmis_6",
        "q_num": 6,
        "title": "Soru 6: Ek Matris (Adjoint) Yöntemi ile $3 \\times 3$ Matrisin Tersini (Invers) Bulma",
        "score": "15 Puan",
        "badge": "Ek Matris ile Ters (Invers)",
        "question": r"""Aşağıda verilen $A$ matrisinin varsa tersini (inversini) $A^{-1} = \frac{1}{|A|} \text{Adj}(A)$ formülünü kullanarak bulunuz:
$$A = \begin{bmatrix}
-1 & 3 & 0 \\
2 & -4 & 2 \\
4 & 5 & 7
\end{bmatrix}_{3 \times 3}$$""",
        "kid_logic": r"""<strong>Çocuğa Anlatır Gibi Temel Mantık:</strong><br>
Bir matrisin tersini bulmak demek, sayılarda $5$'in tersini $\frac{1}{5}$ bulmak gibidir.<br>
3 basit aşamada biter:<br>
1) <strong>Determinantı Bul ($|A|$):</strong> Sıfır çıkarsa 'Tersi yoktur' deyip soruyu bitirirsin! Sıfırdan farklı çıkarsa devam edersin.<br>
2) <strong>9 Tane Kofaktör Hesapla ($A_{ij}$):</strong> Satır ve sütunları kapatıp küçük $2\times 2$ determinantları bul.<br>
3) <strong>EN BÜYÜK SIR:</strong> Kofaktörleri yazdıktan sonra <strong>TRANSPOZESİNİ AL (satırları sütun yap)</strong>! İşte buna 'Ek Matris (Adj A)' denir. Sonra her sayıyı $|A|$'ya böl!""",
        "steps": [
            r"<strong>1. Adım (Sarrus ile Determinant Hesabı):</strong><br>İlk iki satırı alta yazalım:<br>• Pozitif Çaprazlar: $(-1)(-4)(7) + 2(5)(0) + 4(3)(2) = 28 + 0 + 24 = 52$<br>• Negatif Çaprazlar: $0(-4)(4) + 2(5)(-1) + 7(3)(2) = 0 - 10 + 42 = 32$<br>$$|A| = 52 - 32 = \mathbf{20} \neq 0 \implies \text{Determinant 0 olmadığı için matrisin tersi VARDIR!}$$",
            r"<strong>2. Adım (9 Elemanın Kofaktörlerini Dama Tahtası İşaretleriyle Bulma):</strong><br>• $A_{11} = + \begin{vmatrix} -4 & 2 \\ 5 & 7 \end{vmatrix} = -28 - 10 = \mathbf{-38}$<br>• $A_{12} = - \begin{vmatrix} 2 & 2 \\ 4 & 7 \end{vmatrix} = -(14 - 8) = \mathbf{-6}$<br>• $A_{13} = + \begin{vmatrix} 2 & -4 \\ 4 & 5 \end{vmatrix} = 10 - (-16) = \mathbf{26}$<br>• $A_{21} = - \begin{vmatrix} 3 & 0 \\ 5 & 7 \end{vmatrix} = -(21 - 0) = \mathbf{-21}$<br>• $A_{22} = + \begin{vmatrix} -1 & 0 \\ 4 & 7 \end{vmatrix} = -7 - 0 = \mathbf{-7}$<br>• $A_{23} = - \begin{vmatrix} -1 & 3 \\ 4 & 5 \end{vmatrix} = -(-5 - 12) = \mathbf{17}$<br>• $A_{31} = + \begin{vmatrix} 3 & 0 \\ -4 & 2 \end{vmatrix} = 6 - 0 = \mathbf{6}$<br>• $A_{32} = - \begin{vmatrix} -1 & 0 \\ 2 & 2 \end{vmatrix} = -(-2 - 0) = \mathbf{2}$<br>• $A_{33} = + \begin{vmatrix} -1 & 3 \\ 2 & -4 \end{vmatrix} = 4 - 6 = \mathbf{-2}$",
            r"<strong>3. Adım (Ek Matrisi - $\text{Adj}(A)$ - Yazma):</strong><br><strong>DİKKAT:</strong> Kofaktörler matrisinin TRANSPOZESİ alınır! (1. satır kofaktörleri 1. sütun olur):<br>$$\text{Adj}(A) = \begin{bmatrix} A_{11} & A_{21} & A_{31} \\ A_{12} & A_{22} & A_{32} \\ A_{13} & A_{23} & A_{33} \end{bmatrix} = \begin{bmatrix} -38 & -21 & 6 \\ -6 & -7 & 2 \\ 26 & 17 & -2 \end{bmatrix}$$",
            r"<strong>4. Adım ($A^{-1}$ Formülünü Uygulama):</strong><br>$$A^{-1} = \frac{1}{|A|} \text{Adj}(A) = \frac{1}{20} \begin{bmatrix} -38 & -21 & 6 \\ -6 & -7 & 2 \\ 26 & 17 & -2 \end{bmatrix}$$"
        ],
        "exam_trap": r"<strong>Hoca Nereden Puan Kırar?</strong> Öğrencilerin %70'i kofaktörleri doğru bulur ama $\text{Adj}(A)$ matrisini yazarken TRANSPOZESİNİ ALMAYI UNUTUR! Kofaktörleri bulduğun gibi düz yazarsan soru tamamen gider. Formüldeki 'Adj' kofaktörler matrisinin transpozesidir!",
        "result": r"|A| = 20, \quad A^{-1} = \frac{1}{20} \begin{bmatrix} -38 & -21 & 6 \\ -6 & -7 & 2 \\ 26 & 17 & -2 \end{bmatrix}"
    }
]

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

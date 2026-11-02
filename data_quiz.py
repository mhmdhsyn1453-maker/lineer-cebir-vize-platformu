# -*- coding: utf-8 -*-
"""
Lineer Cebir Vize Deneme Sınavı Soruları
Dr. Yusuf Karadede Sınav Formatında, Çözümlü ve Puanlamalı
(Sıfır Emoji, Tamamen SVG & Matematiksel İfadeler)
"""

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": r"$\begin{vmatrix} 4 & 2 \\ 6 & 0 \end{vmatrix}$ determinantının değeri kaçtır?",
        "options": ["12", "-12", "0", "-8"],
        "correct": 1,
        "explanation": r"$$\Delta = (4 \cdot 0) - (2 \cdot 6) = 0 - 12 = -12$$ Sol üstten sağ alta çarpımdan, sağ üstten sol alta çarpım çıkarılır."
    },
    {
        "id": 2,
        "question": r"Sarrus Kuralı hakkında aşağıda verilen ifadelerden hangisi KESİNLİKLE DOĞRUDUR?",
        "options": [
            "Her boyuttaki ($2x2, 3x3, 4x4$) kare matrislerde uygulanabilir.",
            "Yalnızca ve yalnızca 3x3 kare matrislerin determinantında uygulanabilir.",
            "Yalnızca 2x2 matrislerde uygulanabilir.",
            "Lineer denklem sistemlerinin rankını bulmak için kullanılan bir satır işlemidir."
        ],
        "correct": 1,
        "explanation": "Sarrus Kuralı sadece 3x3 boyutundaki determinantlar için geçerlidir. 4x4 veya daha büyük matrislerde kesinlikle uygulanamaz; 4x4 matrislerde Laplace açılımı yapılmalıdır."
    },
    {
        "id": 3,
        "question": r"$\begin{cases} 3x + ky - z = 0 \\ 2x - 2y + 3z = 0 \\ x + 5y + 2z = 0 \end{cases}$ homojen denklem sisteminin aşikar olandan ($0,0,0$) farklı çözümlerinin olması için $k$ parametresi ne olmalıdır?",
        "options": ["-69", "69", "0", "-57"],
        "correct": 0,
        "explanation": r"Homojen bir sistemin ($AX=0$) aşikar (sıfır) çözümünden farklı çözümlerinin olması için katsayılar matrisinin determinantı sıfır olmalıdır: $$\det(A) = 0 \implies \begin{vmatrix} 3 & k & -1 \\ 2 & -2 & 3 \\ 1 & 5 & 2 \end{vmatrix} = 0 \implies -57 - k - 12 = 0 \implies k = -69$$"
    },
    {
        "id": 4,
        "question": r"Bir $A$ kare matrisinin determinantı $|A| = 0$ bulunmuştur. Bu matris hakkında aşağıdakilerden hangisi söylenebilir?",
        "options": [
            "A matrisi regülerdir ve tersi vardır.",
            "A matrisi singülerdir (tekildir) ve tersi (inversi) YOKTUR.",
            "A matrisinin rankı kesinlikle sıfırdır.",
            "A matrisi kesinlikle birim matristir."
        ],
        "correct": 1,
        "explanation": r"$|A| = 0$ olan matrislere 'singüler' (tekil) matris denir. Ters matris formülünde $A^{-1} = \frac{1}{|A|}\text{adj}(A)$ paydada sıfır olamayacağından bu matrisin tersi mevcut değildir."
    },
    {
        "id": 5,
        "question": r"Bir matrise uygulanan 3 temel elementer satır işlemi ($S_i \leftrightarrow S_j, kS_i, kS_i+S_j$) matrisin hangi özelliğini ASLA DEĞİŞTİRMEZ?",
        "options": [
            "Determinantının sayısal değerini",
            "Matrisin Rankını",
            "Matrisin tüm elemanlarının cebirsel toplamını",
            "Matrisin köşegen elemanlarını"
        ],
        "correct": 1,
        "explanation": "Elementer satır ve sütun işlemleri birbirine denk matrisler ($A \sim B$) üretir. Denk matrislerin en önemli özelliği RANKLARININ BİRBİRİNE EŞİT OLMASIDIR; elementer işlemler rankı asla değiştirmez."
    },
    {
        "id": 6,
        "question": r"Gauss eliminasyonunda artırılmış matris $[A \mid B]$ basamaklı hale getirildiğinde en alt satır $\left[\begin{array}{ccc|c} 0 & 0 & 0 & 4 \end{array}\right]$ olarak çıkmıştır. Bu sistem hakkında ne söylenir?",
        "options": [
            "Sistemin tek bir çözümü vardır ve $x_3 = 4$'tür.",
            "Sistemin sonsuz sayıda çözümü vardır.",
            "Sistem uyumsuzdur (tutarsızdır) ve ÇÖZÜM YOKTUR ($\emptyset$).",
            "Sistem bir Cramer sistemidir."
        ],
        "correct": 2,
        "explanation": r"Bu satır $0 \cdot x_1 + 0 \cdot x_2 + 0 \cdot x_3 = 4 \implies 0 = 4$ matematiksel çelişkisini ifade eder. $\text{rank}(A) = 2$ iken $\text{rank}([A \mid B]) = 3$ olur; ranklar eşit olmadığı için sistem uyumsuzdur, çözüm kümesi boştur ($\emptyset$)."
    },
    {
        "id": 7,
        "question": r"3 bilinmeyenli bir lineer sistemde $\text{rank}(A) = \text{rank}([A \mid B]) = 2$ bulunmuştur. Çözüm kümesi hakkında ne söylenir?",
        "options": [
            "Sistemin tek bir benzersiz çözümü vardır.",
            "Sistemin çözümü yoktur.",
            "Sistemin sonsuz çözümü vardır ve $3 - 2 = 1$ adet serbest yardımcı bilinmeyen ($t$) atanır.",
            "Sistemin sonsuz çözümü vardır ve 2 adet serbest bilinmeyen atanır."
        ],
        "correct": 2,
        "explanation": r"$\text{rank}(A) = \text{rank}([A \mid B]) = r < n$ ($2 < 3$) olduğundan sistem uyumludur ve sonsuz sayıda çözümü vardır. Serbest bilinmeyen sayısı $n - r = 3 - 2 = 1$ tanedir ($x_3 = t$ gibi)."
    },
    {
        "id": 8,
        "question": r"$A = \begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$ matrisinin ters matrisi ($A^{-1}$) aşağıdakilerden hangisidir?",
        "options": [
            r"$\frac{1}{2}\begin{bmatrix} 3 & -1 \\ -4 & 2 \end{bmatrix}$",
            r"$\begin{bmatrix} 3 & -1 \\ -4 & 2 \end{bmatrix}$",
            r"$\frac{1}{2}\begin{bmatrix} 2 & -1 \\ -4 & 3 \end{bmatrix}$",
            r"Tersi yoktur çünkü determinantı sıfırdır."
        ],
        "correct": 0,
        "explanation": r"Determinant: $|A| = (2 \cdot 3) - (1 \cdot 4) = 6 - 4 = 2$. $2 \times 2$ pratik ters kuralından ana köşegen yer değiştirir ($2 \leftrightarrow 3$), ters köşegen eksi alır: $A^{-1} = \frac{1}{2}\begin{bmatrix} 3 & -1 \\ -4 & 2 \end{bmatrix}$."
    },
    {
        "id": 9,
        "question": r"Antisimetrik bir kare matris ($A^T = -A$) için ana köşegen elemanları ($a_{11}, a_{22}, \dots$) hakkında ne söylenebilir?",
        "options": [
            "Tamamı 1 olmak zorundadır.",
            "Tamamı sıfır (0) olmak zorundadır.",
            "Pozitif sayılar olmalıdır.",
            "İstediği reel değeri alabilir."
        ],
        "correct": 1,
        "explanation": r"Antisimetrik matris tanımı gereği $a_{ij} = -a_{ji}$'dir. Ana köşegen için satır ve sütun no aynıdır ($i = j$), dolayısıyla $a_{ii} = -a_{ii} \implies 2a_{ii} = 0 \implies a_{ii} = 0$ olmak ZORUNDADIR."
    },
    {
        "id": 10,
        "question": r"$A$ ve $B$ kare matrisleri için aşağıdakilerden hangisi DAİMA DOĞRUDUR?",
        "options": [
            r"$A \cdot B = B \cdot A$",
            r"$\det(A + B) = \det(A) + \det(B)$",
            r"$\det(A \cdot B) = \det(A) \cdot \det(B)$",
            r"$(A \cdot B)^T = A^T \cdot B^T$"
        ],
        "correct": 2,
        "explanation": r"Determinantın çarpım özelliği gereği $\det(A \cdot B) = \det(A) \cdot \det(B)$ daima geçerlidir. Matris çarpımında değişme özelliği yoktur ($AB \neq BA$), transpozda sıra ters döner ($(AB)^T = B^T A^T$), determinant toplamı da dağılmaz."
    }
]

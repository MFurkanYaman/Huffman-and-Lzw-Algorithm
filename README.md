# LZW and Huffman Compression Algorithms

This README explains the implementation and execution of LZW and Huffman compression algorithms in Python. The description is provided in both English and Turkish.

## EN:

### Project Overview

This project implements two common data compression algorithms: **LZW (Lempel-Ziv-Welch)** and **Huffman Encoding**. The goal is to compress the given text data, compare the initial and compressed file sizes, and measure the time taken for compression.

### LZW Compression

The LZW (Lempel-Ziv-Welch) algorithm is a lossless data compression method that builds a dictionary of previously seen sequences of characters. This Python implementation reads an input file, compresses the text using LZW, and writes the results to a file.

**Steps:**

1. **Read Input:** The text from `lzw_baslangic.txt` is read.
2. **Initialize Dictionary:** Each unique character from the input is added to the dictionary.
3. **Compression:** The input text is processed character by character to build sequences. If a sequence exists in the dictionary, it is extended; otherwise, it is added to the dictionary.
4. **Output:** The initial and compressed sizes are calculated, and the compression time is recorded.
5. **Write Output:** The results are written to `lzw.txt`.

### Huffman Compression

Huffman Encoding is another lossless data compression algorithm that uses variable-length codes to represent characters. The most frequent characters are assigned shorter codes, while less frequent ones are given longer codes.

**Steps:**

1. **Read Input:** The text from `huffman_baslangic.txt` is read.
2. **Divide into 8-bit Segments:** The text is divided into 8-bit segments.
3. **Frequency Calculation:** The frequency of each segment is calculated and stored in a dictionary.
4. **Compression:** Huffman encoding is applied based on the frequency of segments.
5. **Output:** The initial and compressed sizes are calculated, and the compression time is recorded.
6. **Write Output:** The results are written to `huffman.txt`.

---

## TR:

### Proje Özeti

Bu proje, yaygın olarak kullanılan iki veri sıkıştırma algoritmasını uygular: **LZW (Lempel-Ziv-Welch)** ve **Huffman Kodu**. Amaç, verilen metin verilerini sıkıştırmak, başlangıç ve sıkıştırılmış dosya boyutlarını karşılaştırmak ve sıkıştırma işlemi için geçen süreyi ölçmektir.

### LZW Sıkıştırma

LZW (Lempel-Ziv-Welch) algoritması, kayıpsız bir veri sıkıştırma yöntemidir. Daha önce görülen karakter dizilerinin bir sözlüğünü oluşturarak çalışır. Bu Python uygulaması, bir giriş dosyasını okur, metni LZW kullanarak sıkıştırır ve sonuçları bir dosyaya yazar.

**Adımlar:**

1. **Giriş Okuma:** `lzw_baslangic.txt` dosyasından metin okunur.
2. **Sözlük Başlatma:** Girişteki her bir benzersiz karakter sözlüğe eklenir.
3. **Sıkıştırma:** Giriş metni, diziler oluşturmak için karakter karakter işlenir. Eğer bir dizi sözlükte varsa genişletilir; aksi takdirde sözlüğe eklenir.
4. **Çıktı:** Başlangıç ve sıkıştırılmış boyutlar hesaplanır ve sıkıştırma süresi kaydedilir.
5. **Çıktı Yazma:** Sonuçlar `lzw.txt` dosyasına yazılır.

### Huffman Sıkıştırma

Huffman Kodu, karakterleri temsil etmek için değişken uzunlukta kodlar kullanan kayıpsız bir veri sıkıştırma algoritmasıdır. En sık kullanılan karakterlere daha kısa kodlar, daha az kullanılanlara ise daha uzun kodlar atanır.

**Adımlar:**

1. **Giriş Okuma:** `huffman_baslangic.txt` dosyasından metin okunur.
2. **8-bit Segmentlere Bölme:** Metin 8-bit segmentlere bölünür.
3. **Frekans Hesaplama:** Her segmentin frekansı hesaplanır ve bir sözlükte saklanır.
4. **Sıkıştırma:** Segmentlerin frekanslarına dayalı olarak Huffman kodlaması uygulanır.
5. **Çıktı:** Başlangıç ve sıkıştırılmış boyutlar hesaplanır ve sıkıştırma süresi kaydedilir.
6. **Çıktı Yazma:** Sonuçlar `huffman.txt` dosyasına yazılır.

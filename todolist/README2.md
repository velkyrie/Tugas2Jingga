# Tugas 5 PBP
## Vladi Jingga Mentari - 2106635631

http://tugas2jingga.herokuapp.com

## Inline, Internal, dan External CSS?
Perbedaan terletak pada peletakan CSS. Inline CSS ditulis langsung pada elemen HTML dalam satu line di dalam atribut `style=''`.
Internal CSS ditulis dalam tag `<style>` di dalam file HTML. Sementara itu, External CSS ditulis 
di dalam file `.css` yang biasa didefinisikan di bagian <head> file `html`.

## HTML5 Tag
Beberapa tag HTML adalah sebagai berikut,

| Group Tag | Tag | Fungsi | 
| ------------- | ------------- | ------------- |
| Tag Dasar | `<! DOCTYPE html>` | Deklarasi untuk mendefinisikan dokumen menjadi HTML |
| | `<html>` | Tag pembuka untuk membuat dokumen HTML |
| | `<head>` | Tag untuk mendifinisikan informasi meta, import css, import font, dan lain-lain. |
| | `<title>` | Tag untuk menampilkan judul di tab browser |
| | `<body>` | Tag untuk meletakkan semua konten website |
| Tag Teks | `<h1> - <h6>` | Membuat heading pada suatu halaman |
|  | `<p>` | Membuat paragraf atau teks ukuran default pada suatu halaman |
|  | `<br>` | Line break |
|  | `<hr>` | Memisahkan antar konten dan elemen |
| Tag Formatting | `<b>` | Membuat teks bold |
|  | `<p>` | Membuat paragraf atau teks ukuran default pada suatu halaman |
|  | `<i>` | Membuat teks miring |
|  | `<u>` | Membuat teks underline |

## CSS Selector
Secara garis besar, suatu elemen HTML bisa diakses dengan tiga tipe CSS Selector, yakni element selector, class selector, dan id selector.
| Tipe Selector | Penjelasan | Contoh | 
| ------------- | ------------- | ------------- |
| Element Selector | Ditulis tanpa menggunakan leading baik `#` atau `.` selector ini disesuaikan dengan tag-tag pada file HTML yang ingin diberikan style | `p { ... }` selector ini akan memilih semua elemen dengan tag `<p>` |
| Class Selector | Ditulis dengan menggunakan leading `.` developer harus mendefinisikan atribut `class=""` kemudian nama dari class yang telah dibuat dapat digunakan pada penulisan CSS | Contohnya developer mendefinisikan atribut class sebagai `class="hero"`. Maka pada file css, developer dapat memanggil `.hero{ ... }` selector ini akan memilih semua elemen dengan class hero |
| ID Selector | Ditulis dengan menggunakan leading `#` developer harus mendefinisikan atribut `id=""` kemudian nama dari id yang telah dibuat dapat digunakan pada penulisan CSS | Contohnya developer mendefinisikan atribut id sebagai `id="maincontent"`. Maka pada file css, developer dapat memanggil `#maincontent{ ... }` selector ini akan memilih semua elemen dengan id maincontent |

## Implementasi Checklist
1. Saya melakukan kustomisasi dengan Bootstrap dengan meng-import Bootstrap ke `/templates/base.html`
2. Menambahkan CSS dengan internal CSS pada `base.html`
3. Mengimplementasikan desain dengan syntax-syntax Bootstrap yang class-based untuk layout serta cards, dan melakukan eksplorasi di Google. Untuk CSS, dibantu oleh generator-generator seperti Mesh Gradient Generator, Glassmorphism Generator, dan lain sebagainya.

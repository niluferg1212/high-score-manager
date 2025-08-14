# 🏆 High Score Manager
Bu proje, kullanıcıların oyun skorlarını kaydetmelerine, güncellemelerine, aramalarına ve listelemelerine imkân sağlayan bir **yüksek skor yönetim sistemi**dir.

## ⚙️ Kurulum Bilgileri
1. Bilgisayarında **Python 3** kurulu olmalıdır.

2. Projeyi indir:

>`git clone https://github.com/kullanici_adi/High-Score-Manager.git`

>`cd High-Score-Manager`

## 🚀 Nasıl Başlatılır

1. Terminali aç.

2. Dosyanın olduğu klasöre git:
>`cd High-Score-Manager``

3. Programı çalıştır:
>`python high_score_manager.py`

## 📂 Proje Yapısı

```
High-Score-Manager/
│
├── high_score_manager.py   # Ana Python dosyası
├── README.md               # Proje açıklaması
```

## 🛠 Kullanılan Araçlar

* **Python 3**

* **csv** kütüphanesi (dosya okuma/yazma için)

* **Temel input/output işlemleri**

* **Bubble Sort algoritması**

## 🔎 Algoritmanın Mantığı
1. Kullanıcıdan isim ve skor alınır.

2. Eğer aynı isim zaten varsa:

    * Yeni skor daha yüksekse güncellenir.

    * Daha düşükse değişiklik yapılmaz.

3. Skorlar **bubble sort** algoritması ile büyükten küçüğe sıralanır.

4. Kullanıcı şu işlemleri yapabilir:

    * Yeni skor ekleme / güncelleme

    * İsim ile skor arama

    * Skor tablosunu görüntüleme

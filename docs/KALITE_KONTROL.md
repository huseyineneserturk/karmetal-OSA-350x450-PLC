# İlk dört hafta - kalite kontrol kaydı

Kontrol tarihi: **25.10.2026**. Bu kayıt belgelerin kalitesine ilişkindir; makinede emniyet veya siber güvenlik testi yapıldığı anlamına gelmez.

## Gereksinim eşlemesi

| Föydeki görev | Teslimdeki karşılığı | Sonuç |
|---|---|---|
| Lab 1 / 8 soru | PDF 1'de sekiz ayrı yanıt; normal ve koruma yolları | Tamam |
| Lab 1 / Safety Function Map | Giriş-mantık-son eleman işlevsel haritası; bilinmeyen donanım açık | Tamam / EP 03 |
| Lab 2 / Görev A | Bölge grupları, Safety PLC varsa konumu, C1-C5 ve kontroller | Tamam |
| Lab 2 / Görev B | Altı satır erişim kararı | Tamam / EP 05 |
| Lab 3 / 3 senaryo | Aktör, kapı, eylem, zincir, fiziksel sonuç ve gerekli koşul | Tamam |
| Lab 3 / puanlama | 2x3x3=18; 2x3x2=12; 1x3x1=3 | Hesaplar doğrulandı |
| Lab 3 / S=3 kuralı | R3 sayısal olarak düşük, zorunlu emniyet incelemesi ayrıca işaretli | Tamam / EP 04 |
| Lab 4 / mevcut-hedef | Bilinmeyen mevcut durum ile beş hedef gereksinim ayrı | Tamam |
| Lab 4 / bağımsızlık | İhlal halinde etki koşulları ve G6 bağımsızlık gereksinimi | Tamam / EP 02 + EP 06 |

Lab 1-4 görevleri, kullanıcının verdiği genel föyün PDF sayfa 2-5 içeriğiyle karşılaştırıldı. Örnek tek sayfa PDF yalnız yerleşim referansı olarak kullanıldı.

## Dosya ve görsel kontroller

- Dört çıktı PDF, Poppler ile 1500 piksel uzun kenarlı PNG'ye dönüştürüldü ve dört sayfanın tamamı gözle incelendi. Son sürümde taşma, üst üste metin veya bozuk Türkçe karakter görülmedi.
- `pypdf` ile her çıktı için 1 sayfa, doğru başlık/model, iki boş interaktif kimlik alanı ve alanların görünüm akışları doğrulandı.
- PDF kaynak bağlantıları: sırasıyla 2, 3, 3 ve 3 adet. K1/K3/K4/K5 bağlantıları tıklanabilir.
- Yeni föylerde örnekteki öğrencinin adı ve başka makineye ait metin bulunmadığı kontrol edildi.
- Lab 1'de 8 yanıt; Lab 2'de 3 yanıt ve 6 karar; Lab 3'te 3 doğru çarpım; Lab 4'te 5 hedef ilke kontrol edildi.
- README ve dokümanlardaki yerel Markdown bağlantılarının dosyalara çözüldüğü doğrulandı.
- Özgün iki PDF ve geçici render dosyaları `.gitignore` ile Git dışında bırakıldı; yerel kaynaklar korundu.

## Son PDF sürümlerinin SHA-256 değerleri

| Hafta | SHA-256 |
|---|---|
| 1 | `c1b49e1c6ce8bbd416b68c3eef7c2afe8ab58321be9b933220630df9aa907647` |
| 2 | `55eb7097a6de9ee72944b2701dc9bf573c67709a79c256d3201c79b936ca87df` |
| 3 | `6fdb059fa080da80694e10041fc3473f2c060bbf119cae5168b3a6e01c860e53` |
| 4 | `c1b4ead47f4a53c8e86ff78d14f132955fa89ed453f5e2031663155d13f880bf` |

## Açık kalanlar

25.10.2026 tesliminde Ad Soyad ve Grup alanları, kör test oturumu, canlı Trello panosu ve Lab 5-7 açıktı. 01.11.2026'da Lab 5 eklendi; Lab 6-7 ve diğer işler açık kalıyor. Sınıf çakışmama durumu öğrencinin teyidine dayanıyor; liste kontrolü yapılmadı. Bilinmeyen teknik özellikler kanıt bulunana kadar bilinmiyor kalacak.

## 5. hafta ek kontrolü - 01.11.2026

| Gereksinim | Karşılığı / sonuç |
|---|---|
| F1 PDF sayfa 6, örnek kayıt | Component X 2.4, CVE-XXXX-XXXX, Critical / CVSS 9.8, yama mevcut; tümü eğitim varsayımı olarak korundu. Gerçek CVE kimliği gibi sunulmadı. |
| Soru 1 | Bileşen, sürüm ve ulaşılabilirlik için üç ayrı bilinmiyor sonucu ve kanıt ihtiyacı. |
| Soru 2 | CVSS tek başına duruş gerekçesi değil; emniyet belirtisinde koşullu güvenli duruş ve kanıt koruma. Üretime devam onayı verilmedi. |
| Soru 3 | Üretimden ayrılmış temsilî test, paket bütünlüğü, uyumluluk, yedek/geri dönüş ve regresyon ölçütleri. |
| Soru 4 | Kapak/şerit duruşu, tepki süresi, reset ve yük tutma üzerinde değişiklik etkisi; yetkili validasyon ihtiyacı. |
| Soru 5 | Yama ertelenirse erişim sınırlama, servis cihazı denetimi, izleme, süreli risk kararı ve emniyet koşulu. |
| Çıktı ve EP | VD-05 / AÇIK - etkilenme belirsiz; EP 09 + EP 10 + EP 11. Tam SBOM veya uygulanmış yama değildir. |

Son PDF Poppler ile 1600 piksel uzun kenarlı PNG'ye çevrilip sayfanın tamamı gözle incelendi; taşma, çakışma veya bozuk Türkçe karakter görülmedi. `pypdf` kontrolünde bir sayfa, doğru model/tarih, dört kaynak bağlantısı ve iki boş interaktif kimlik alanı doğrulandı; alan değerleri ile widget görünüm akışları kontrol edildi. Görev 1'in üç tablo satırı ve görev 2-5'in dört ayrı yanıtı mevcut. İlk dört PDF'nin dosya baytları önceki Git commit'i ile karşılaştırıldı ve aynı bulundu. Yerel Markdown bağlantıları ve `git diff --check` kontrolü geçti.

Lab 5 SHA-256: `f7471be57342cc823b02133fcce4ca097648b45b902d7b12774187b32048306c`.

Bu kontroller belge kalitesi içindir. Gerçek makine testi, yama kurulumu ve kör test oturumu yapılmadı.

# Laboratuvarlar - kalite kontrol kaydı

**Güncel sürüm:** En sondaki “Sadeleştirilmiş yedi föy” bölümü geçerlidir. Önceki kayıtlar önceki PDF sürümlerine aittir; eski boş kimlik alanları ve dosya özetleri güncel dosyaları tanımlamaz.

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

## 5-6-7. hafta teslim kontrolü - 06.11.2026

5. haftanın beş görevi ve tek sayfalık PDF'si yeniden incelendi; önceki onaylı dosya korundu. 6 ve 7. haftalar ayrı dosyalar olarak üretildi. Üçü de `output/pdf/` altında ayrı PDF'dir.

| Gereksinim | Sonuç |
|---|---|
| Lab 6 / F1 PDF sayfa 7 | Beş zaman adımı ayrı yanıtlandı: ilk 15 dakika, ilk 2 saat, 24 saat, 72 saat, 14. gün. |
| Lab 6 / kanıt ve emniyet | Önce insan emniyeti; log/ayar/hash/teslim zinciri ve eksik kayıt bilgisi; yetkili rol ve yeniden başlatma koşulları mevcut. |
| Lab 6 / CRA | Kapsam ve eşik koşullu. Üretici farkındalığı ile 10:15 alarmı ayrıldı. 14 gün / bir ay nihai rapor ayrımı, ENISA ve Komisyon açıklamalarıyla kontrol edildi. |
| Lab 6 / çıktı | Incident Workflow / EP 13. Gerçek olay veya gönderilmiş bildirim iddiası yok. |
| Lab 7 / F1 PDF sayfa 8 | Yanlış OK, manipüle girdi ve düşük güven için üç ayrı yanıt ve üç satırlı karar tablosu mevcut. |
| Lab 7 / bağımsızlık | YZ dışı emniyet yolu ve yerel teyit; insan müdahalesi emniyet kilidini aşmaz. |
| Lab 7 / kanıt sınırı | Kamera/YZ varsayımsal. Güven eşiği, performans ve tepki süreleri uydurulmadı; doğrulama ihtiyacı açık. |
| Lab 7 / çıktı | AI Fail-Safe Decision / EP 03 + EP 15. Gerçek model veya saha testi sonucu iddiası yok. |

Son 6-7. hafta PDF'leri Poppler ile 1600 piksel uzun kenarlı PNG'ye dönüştürüldü ve iki sayfanın tamamı gözle incelendi. Başlıklar, şema, tablolar, kaynaklar ve dipnotlarda taşma/çakışma görülmedi. 5. hafta da görsel olarak yeniden incelendi. Yedi PDF'nin tamamında `pypdf` ile bir sayfa, doğru başlık/tarih/EP, iki boş interaktif kimlik alanı, widget görünüm akışları ve beklenen bağlantı sayıları doğrulandı. İlk beş PDF önceki Git commit'iyle bayt düzeyinde aynı bulundu. Yerel Markdown bağlantıları ile `git diff --check` kontrolü geçti.

| Hafta | SHA-256 |
|---|---|
| 5 (korundu) | `f7471be57342cc823b02133fcce4ca097648b45b902d7b12774187b32048306c` |
| 6 | `5903e31af025a0ab8b5e11a834219e828dc1e53287f4ac89a2f28ba65e5924ae` |
| 7 | `5f7355a4c5b865a31f78fb98ca3d8611d5a63f4d501d396bff068e347aa5f148` |

### Yedi haftalık tutarlılık denetimi

Lab 1'in emniyet fonksiyonları ve bilgi eksikleri, Lab 2/4'ün koşullu erişim mimarisi, Lab 3'ün senaryoları, Lab 5'in belirsiz etkilenme kararı, Lab 6'nın koşullu olay akışı ve Lab 7'nin varsayımsal YZ yolu karşılaştırıldı. Makine için yeni PLC/firmware, gerçek CVE, uzaktan erişim, Safety PLC/STO veya YZ varlığı iddia edilmedi. EP eşleşmeleri F1 ile uyumlu. Kaynak kaydı ve README yedi ayrı çıktıyı içeriyor; SWOT/SMART ve Trello görev taslağı güncellendi.

Belge seti hazırdır. Öğrenci kimlik alanları, öğrenci incelemesi ve kör test oturumu açık kalır; canlı Trello panosu veya gerçek sistem testi yapılmış sayılmaz.

## Sadeleştirilmiş yedi föy - 06.11.2026

Öğrencinin isteğiyle yedi teslim PDF'si aynı makine için yeniden yazıldı. Ana başlıklar, soru sırası ve istenen çıktılar korundu. Fazladan kabul ölçütü, kanıt paketi, takip/sorumlu ve benzeri analiz bölümleri çıkarıldı. Kaynak ve bilgi durumu kodları PDF'lerden kaldırıldı; kaynak listesi depoda tutuldu. Bilinmeyenler ve varsayımlar normal cümlelerle belirtildi. Föyde geçen teknik terimler gerektiğinde Türkçe açıklandı.

| Hafta | Föyde istenen kapsam | Kontrol |
|---|---|---|
| 1 | 8 yanıt, normal kontrol ve emniyet yolu haritası | Tamam |
| 2 | 3 yanıt, bölge/bağlantı şeması, 6 satır erişim kararı | Tamam |
| 3 | 3 senaryo, L x S x E hesabı, öncelik, 2 yanıt ve S=3 kuralı | Tamam |
| 4 | Mevcut/hedef için 5 ilke ve bağımsızlıkla ilgili 2 yanıt | Tamam |
| 5 | Verilen örnek zafiyet kaydı ve 5 yanıt | Tamam |
| 6 | Olay senaryosu ve 5 zaman adımı; süre düzeltmesi ilgili yanıt içinde | Tamam |
| 7 | Varsayımsal akış, 3 yanıt ve 3 satır karar tablosu | Tamam |

Yedi PDF de tek sayfa olarak üretildi ve son sürümlerinin tüm sayfaları Poppler görüntüleri üzerinden incelendi. Ad Soyad **Hüseyin Enes Ertürk**, Grup **Yazılım Gece B** olarak dolu. Kimlik alanları interaktif tutuldu. `pypdf` ile hem kanonik alan değerleri hem widget görünüm akışlarından çıkarılan metin kontrol edildi; iki gösterimde de Türkçe bilgiler birebir eşleşti. Sayfa başlığı, tarih, EP eşleşmesi, soru sayısı, tablo satırları ve risk çarpımları doğrulandı. PDF metinlerinde ek kaynak/bilgi kodları bulunmadığı ve yerel Markdown bağlantılarının geçerli olduğu kontrol edildi. `git diff --check` geçti.

| Hafta | Güncel SHA-256 |
|---|---|
| 1 | `06a6e1edc56befa62e5c68068f0f83264693f7002bbb7b9174bd0bf013ee26eb` |
| 2 | `b6ae108b40e29f490c6a6cc474f09cf78909a652b4931f49420b7fb406a65c2a` |
| 3 | `3d78d4aaffd7c8a9c7c7e8a8e43399c4d39740eecf6cd05c0e778c0489113e4f` |
| 4 | `4a74747bd093261b89f6dc3e5e782c3b1c586a7ea6eb4056f4044e725200bf80` |
| 5 | `9e0bfb7dcf608e976750ba48c0e1db4b4a68f91380be4373b7491f2332ed4b6c` |
| 6 | `69caad88266e51e8d57d5e385d765e354cc527d560111ef3f319caf3304496ff` |
| 7 | `b9ba560ec87f959e415d1c0ec9b4d2947374d79e3d1d4a9333ae95af06afc3e0` |

Özgün kaynak PDF'leri değiştirilmedi. Bu kayıt belge kontrolüdür; kör test veya gerçek makine deneyi yapılmış sayılmaz. Sıradaki adım öğrencinin sadeleştirilmiş föyleri okumasıdır.

# SWOT, SMART ve iş takibi

25.10.2026 - İlk dört hafta teslimi. Analiz öğrenci seviyesinde tutulur; yazılım geliştirme veya saha testi proje amacı değildir.

## SWOT

| Boyut | Değerlendirme | Dayanak / sınır |
|---|---|---|
| Güçlü yön | Üreticinin açıkladığı duruş tetikleri, emniyet fonksiyonlarını incelemek için somut başlangıç sağlar. | K1; bu beyan emniyet validasyonu değildir. |
| Güçlü yön | Ürün ve SAMİB kaydı kamuya açıktır. | K1/K2; pasif araştırmaya uygundur. |
| Zayıf yön | PLC/firmware, devre ve ağ bilgisi bulunamadı; değerlendirme ayrıntısı sınırlı. | B01-B05; bilgi eksikliği, makinenin zayıflığı diye sunulmaz. |
| Fırsat | Varsayımsal bölgeleme ve bakım gereksinimleriyle kanıt toplanacak alanlar düzenlenebilir. | Öğrenci önerisi; uygulanmış kontrol değildir. |
| Fırsat | SBOM ve konfigürasyon kayıtlarının kamuya açık bulunması sonraki haftaları güçlendirebilir. | Henüz bulunmadı. |
| Tehdit | Varsayım: servis yazma erişimi ve yetersiz bağımsızlık birlikte varsa parametre müdahalesi fiziksel zarara gidebilir. | Lab 3 R1-R3; doğrulanmış zafiyet değildir. |
| Tehdit | Proje açısından kanıtsız CVE veya mevzuat kapsamı iddiası akademik savunulabilirliği zedeler. | Kaynak/varsayım ayrımıyla yönetilir. |

## SMART hedefleri

Takvim, geç verilmiş teslim tarihleri uydurulmadan aşama sonuna bağlanır. T0: bu teslimin öğrenci tarafından kabulü.

| Hedef | Ölçüt / zaman | Durum |
|---|---|---|
| İlk dört föy | Bu teslim sonunda dört ayrı tek sayfa PDF; tüm Lab 1-4 görevleri ve EP eşleşmeleri var. | Hazır; görsel ve içerik kontrol kaydı ayrıca tutulur. |
| Kanıt disiplini | Bu teslim sonunda tüm makineye özgü iddiaların kaynak veya B/V/Ö/Ç etiketi bulunsun; doğrulanmamış model/sürüm/CVE sayısı sıfır olsun. | Kaynak ve bilinmeyenler kaydı oluşturuldu. |
| Kör masa başı oturumu | T0+7 gün içinde 4 senaryo; cevap anahtarı yanıt öncesi gösterilmeyecek; karar, gerekçe ve kanıt ihtiyacı kaydedilecek. | Planlandı; uygulanmadı. |
| Kalan üç laboratuvar | T0+21 gün içinde Lab 5-7'nin her biri ayrı çıktı; bilinmeyen bileşenlerde CVE eşlemesi yerine karar akışı. | Gelecek iş; bu teslimde üretilmedi. |
| Son denetim | Nihai teslimden en az 2 gün önce yedi laboratuvar için görev/kaynak/tutarlılık listesinde açık teslim hatası sıfır. | Gelecek iş; bilgi eksikleri ayrıca kalabilir. |

## Trello'ya aktarılabilir görevler

Canlı Trello panosu oluşturulmadı. Aşağıdaki dört liste basit iş akışıdır; kartlar elle aktarılabilir. Her kartta sorumlu öğrenci, kaynak bağlantısı ve bitiş ölçütü bulunmalı.

| Liste | Kart | Bitiş ölçütü |
|---|---|---|
| Araştırılacak | Model/varyant kılavuzu ve bileşen listesi | Kaynak kaydı veya “bulunamadı” sonucu |
| Araştırılacak | Lab 5 SBOM/CVE/Patch | Varlık-sürüm-erişilebilirlik ayrımı ve karar akışı |
| Araştırılacak | Lab 6 CRA Incident Simulation | Olay türüne göre doğru zaman çizgisi |
| Araştırılacak | Lab 7 AI Safety Challenge | Üç hata durumunda güvenli davranış; YZ varlığı varsayım olarak işaretli |
| Devam eden | Kimlik ve ders grubu alanlarını tamamla | Dört PDF'nin Ad Soyad/Grup alanları dolu |
| Kontrol edilecek | İlk dört föyü öğrenci olarak gözden geçir | Soru/yanıt, kaynak ve EP eşleşmeleri incelendi |
| Kontrol edilecek | Kör senaryo oturumu | Dört yanıt, gizli anahtarla değerlendirme ve sonuç kaydı |
| Tamamlanan | Makine seçimi ve çakışmama teyidi | Öğrencinin 25.10.2026 teyidi kayıtlı; bağımsız liste kontrolü değil |
| Tamamlanan | Kaynak/bilgi açığı ve ilk dört föy | Dosyalar depoda; kalan haftalar hazır gibi gösterilmez |
| Kontrol edilecek | GitHub yayımlama | Commit uzak depoda ve yerel/uzak commit eşit |

## Teslim kontrol listesi

- [x] Lab 1: 8 yanıt ve emniyet fonksiyon haritası.
- [x] Lab 2: bölge/bağlantı şeması, 3 yanıt, 6 erişim kararı.
- [x] Lab 3: 3 senaryo, L/S/E, skor, bant, S=3 istisnası ve takip.
- [x] Lab 4: mevcut/hedef, 5 ilke ve bağımsızlık gereksinimi.
- [x] Kaynak, varsayım, öneri ve bilgi eksikleri ayrıldı.
- [x] SWOT/SMART, mevzuat boşluğu ve Trello iş akışı hazırlandı.
- [ ] Kimlik alanları öğrenci tarafından tamamlandı.
- [ ] Kör test oturumu uygulandı.
- [ ] Lab 5-7 üretildi ve nihai yedi haftalık denetim yapıldı.

İlk dört hafta tamamlandıktan sonraki tek çalışma adımı: kimlikleri doldurup kör masa başı oturumunu başlatmak. Sonraki haftaya ait analizler ayrı bir aşamada ele alınır.

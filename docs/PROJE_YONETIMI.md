# SWOT, SMART ve iş takibi

25.10.2026 - İlk dört hafta teslimi. Analiz öğrenci seviyesinde tutulur; yazılım geliştirme veya saha testi proje amacı değildir.

**01.11.2026 güncellemesi:** Lab 5 ayrı föy olarak eklendi. İlk beş hafta hazır; son iki laboratuvar ve kör test oturumu henüz tamamlanmadı.

**06.11.2026 güncellemesi:** Lab 5 kontrol edildi; Lab 6 ve Lab 7 ayrı tek sayfa föyler olarak tamamlandı. Yedi laboratuvarın belge kapsamı hazır. Kimlik alanları, öğrenci incelemesi ve uygulanacak kör test oturumu ayrıca açık kalıyor.

**06.11.2026 sadeleştirme sürümü:** Öğrencinin isteğiyle yedi föy yeniden yazıldı; yalnız föydeki görevler, istenen şemalar ve tablolar bırakıldı. Kimlik alanları Hüseyin Enes Ertürk / Yazılım Gece B olarak dolduruldu. Yukarıdaki kayıtlar önceki sürümlerin durumudur.

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
| Kanıt disiplini | Makineye özgü iddialar kaynakla desteklensin; bilinmeyen ve varsayımlar açık cümlelerle belirtılsin; doğrulanmamış model/sürüm/CVE iddiası sıfır olsun. | Kaynak ve bilinmeyenler kaydı oluşturuldu; PDF'lerde gereksiz kodlar kaldırıldı. |
| Kör masa başı oturumu | T0+7 gün içinde 4 senaryo; cevap anahtarı yanıt öncesi gösterilmeyecek; karar, gerekçe ve kanıt ihtiyacı kaydedilecek. | Planlandı; uygulanmadı. |
| Kalan laboratuvarlar | T0+21 gün içinde Lab 5-7'nin her biri ayrı çıktı; bilinmeyen bileşenlerde CVE eşlemesi yerine karar akışı. | Lab 5, 01.11.2026; Lab 6-7, 06.11.2026'da hazırlandı. T0 kabul tarihi verilmediği için takvim başarısı iddia edilmedi. |
| Son denetim | Nihai teslimden en az 2 gün önce yedi laboratuvar için görev/kaynak/tutarlılık listesinde açık teslim hatası sıfır. | 06.11.2026'da belge kontrolü yapıldı. Nihai teslim tarihi bilinmiyor; süre hedefi ve öğrenci onayı ayrıca izlenir. |

## Trello'ya aktarılabilir görevler

Canlı Trello panosu oluşturulmadı. Aşağıdaki dört liste basit iş akışıdır; kartlar elle aktarılabilir. Her kartta sorumlu öğrenci, kaynak bağlantısı ve bitiş ölçütü bulunmalı.

| Liste | Kart | Bitiş ölçütü |
|---|---|---|
| Araştırılacak | Model/varyant kılavuzu ve bileşen listesi | Kaynak kaydı veya “bulunamadı” sonucu |
| Tamamlanan | Lab 5 SBOM/CVE/Patch | Üç koşul, beş yanıt ve koşullu karar; tam SBOM/gerçek CVE iddiası yok |
| Tamamlanan | Lab 6 CRA Incident Simulation | Beş zaman adımı, bildirim türü/süresi ayrımı ve EP 13 |
| Tamamlanan | Lab 7 AI Safety Challenge | Üç hata durumunda güvenli davranış, üç satırlı karar tablosu ve EP 03/15 |
| Tamamlanan | Kimlik ve ders grubu alanlarını tamamla | Yedi PDF'de Hüseyin Enes Ertürk / Yazılım Gece B dolu |
| Kontrol edilecek | İlk dört föyü öğrenci olarak gözden geçir | Soru/yanıt, kaynak ve EP eşleşmeleri incelendi |
| Kontrol edilecek | Lab 5'i öğrenci olarak gözden geçir | Örnek kayıt ile gerçek makine bilgisinin ayrımı incelendi |
| Kontrol edilecek | Lab 6-7'yi öğrenci olarak gözden geçir | Bildirim eşiği/süreleri ve YZ varsayımları incelendi |
| Kontrol edilecek | Kör senaryo oturumu | Dört yanıt, gizli anahtarla değerlendirme ve sonuç kaydı |
| Tamamlanan | Makine seçimi ve çakışmama teyidi | Öğrencinin 25.10.2026 teyidi kayıtlı; bağımsız liste kontrolü değil |
| Tamamlanan | Kaynak/bilgi açığı ve ilk dört föy | Dosyalar depoda; kalan haftalar hazır gibi gösterilmez |
| Kontrol edilecek | GitHub yayımlama | Commit uzak depoda ve yerel/uzak commit eşit |

## Teslim kontrol listesi

- [x] Lab 1: 8 yanıt ve emniyet fonksiyon haritası.
- [x] Lab 2: bölge/bağlantı şeması, 3 yanıt, 6 erişim kararı.
- [x] Lab 3: 3 senaryo, L/S/E, skor, bant, S=3 istisnası ve takip.
- [x] Lab 4: mevcut/hedef, 5 ilke ve bağımsızlık gereksinimi.
- [x] Lab 5: üç koşul, beş yanıt, telafi edici önlem ve EP 09/10/11 kararı.
- [x] Lab 6: beş zaman adımı, kanıt koruma, yetkili roller, koşullu CRA bildirim süreleri.
- [x] Lab 7: üç hata durumu, karar tablosu, bağımsız emniyet ve eşik için kanıt ihtiyacı.
- [x] Kaynak, varsayım, öneri ve bilgi eksikleri ayrıldı.
- [x] SWOT/SMART, mevzuat boşluğu ve Trello iş akışı hazırlandı.
- [x] Kimlik alanları öğrencinin verdiği ad ve grupla tamamlandı.
- [ ] Kör test oturumu uygulandı.
- [x] Yedi laboratuvarın belge kapsamı, kaynak/varsayım ayrımı ve tutarlılığı kontrol edildi.

Yedi haftalık belge setinden sonraki tek çalışma adımı: sadeleştirilmiş föylerin öğrenci incelemesini yapmak. Kör test oturumu planı hazır; sonuç anahtarı gösterilmeden ayrı oturumda uygulanacak.

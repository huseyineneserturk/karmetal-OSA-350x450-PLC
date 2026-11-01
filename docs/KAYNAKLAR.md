# Kaynaklar ve bilgi eksikleri

Araştırma/kayıt tarihi: **25.10.2026**. Araştırma pasiftir. Kaynak bağlantıları, erişim tarihi ve kaynağın hangi iddiayı desteklediği kaydedilmiştir. Tam web sayfaları depoda yeniden yayımlanmamıştır; içerik gelecekte değişebilir.

**5. hafta güncellemesi: 01.11.2026.** K1 ve K5 yeniden incelendi; K8/K9 aşağıdaki kayda eklendi. K1 ürün sayfası PLC/firmware sürümü veya modele özgü SBOM vermiyor. Bu, böyle bir belgenin hiçbir yerde bulunmadığı iddiası değildir.

| Kod | Birincil kaynak | Desteklediği bilgi / sınır |
|---|---|---|
| K1 | [Karmetal OSA 350x450 PLC](https://www.karmetal.com.tr/urun/30/osa-350x450-plc.html) | Model, kontrol paneli, hareket/algılama ve üreticinin bildirdiği duruş işlevleri. Devre veya siber güvenlik kanıtı değil. |
| K2 | [SAMİB Karmetal üye kaydı](https://samib.org.tr/uye/karmetal-san-tic-ltd-sti/) | Firmanın birlik üye kaydı. Doğrudan erişim ilk denemede zaman aşımına uğradı; arama dizinindeki sayfa içeriği üzerinden teyit edildi. Güncel sertifika kanıtı olarak kullanılmadı. |
| K3 | [ISA/IEC 62443-3-2:2020 resmî önizleme](https://www.isa.org/getmedia/661c718f-8e64-446d-acf9-2c6286db1b33/isa-62443-3-2-preview.pdf) | Sistem sınırı, zone/conduit, risk ve hedef güvenlik seviyesi için çerçeve. Tam standarda göre madde madde uygunluk iddiası yok. |
| K4 | [ISO 13849-1:2023](https://www.iso.org/standard/73481.html) | Emniyetle ilgili kumanda parçalarının tasarım/metodoloji kapsamı. Yalnız kamuya açık özet incelendi; makinenin PLr değerini vermez. |
| K5 | [NIST SP 800-82 Rev.3, final](https://csrc.nist.gov/pubs/sp/800/82/r3/final) ve [rapor](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r3.pdf) | OT bağlamı, bölgeleme ve bakım erişimi için rehber. Rev.4 taslak bilgisi var; bu projede final Rev.3 esas alınır. |
| K6 | [Avrupa Komisyonu - CRA](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act) ve [resmî açıklama](https://digital-strategy.ec.europa.eu/en/policies/cra-summary) | CRA takvimi ve kapsam koşulları. |
| K7 | [EUR-Lex - Makine Tüzüğü özeti](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=LEGISSUM:4682019) ve [Komisyon makine sayfası](https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en) | Düzeltilmiş uygulama tarihi ve makine emniyeti bağlamı. |
| K8 | [2026 Minimum Elements for a Software Bill of Materials - ASD/CISA ve ortakları](https://www.cyber.gov.au/publication/2026-minimum-elements-for-a-software-bill-of-materials-sbom) | 01.11.2026 erişimi. Bileşen/sürüm/bağımlılık bilgisi ve bilinmeyenin açık kaydı; Lab 5 kanıt ihtiyacı. Proje tablosu tam veya rehbere uygun SBOM sayılmaz. |
| K9 | [FIRST CVSS User Guide](https://www.first.org/cvss/user-guide.html) | 01.11.2026 erişimi. CVSS temel puanı ciddiyeti ölçer; tek başına ortama özgü risk kararı vermez. Föydeki 9.8 için sürüm/vektör verilmedi; puan yeniden hesaplanmadı. |
| F1 | Kullanıcının verdiği Lab Föyleri.pdf, 8 sayfa | Lab 1-5: PDF sayfa 2-6. Lab 5'in 5 sorusu ve EP 09/10/11 eşleşmesi sayfa 6'dan alındı. |
| F2 | Kullanıcının verdiği Lab1_Safety_Architecture.pdf, 1 sayfa | Yalnız görsel düzen referansı. PaketPro/KANTEC/robot bilgileri seçilen makineye aktarılmadı. |

## K1'de doğrulanan teknik bilgiler

| Özellik | Üretici sayfasındaki bilgi |
|---|---|
| Makine | Otomatik, sabit açılı şerit testere |
| Kontrol | PLC paneli; boy/adet girişi ve encoder ile boy ayarı |
| Ana motor / kesme hızı | 4 kW / 25-90 m/dakika |
| Şerit / mengene | 4.300 x 34 x 1,1 mm / hidrolik |
| Koruma/duruş bildirimi | Kapak açılması, şerit kopması ve şerit basıncı azalmasında otomatik duruş |

Bunlar ürün ailesine ait kamuya açık beyanlardır. Belirli seri numaralı bir kurulumda aynı donanımın bulunduğu doğrulanmadı. Mekanik tehlike yorumları birer analiz çıkarımıdır.

## Kanıt ve varsayım kaydı

| Kimlik | Bilinmeyen / varsayım | Neyi etkiler? | Gereken kanıt |
|---|---|---|---|
| B01 | PLC/panel marka-model, firmware bilinmiyor | Bileşen envanteri, sonraki CVE eşlemesi | Kamuya açık modelle eşleşen kılavuz/bileşen listesi |
| B02 | Safety PLC/röle, STO, devre ve reset bilinmiyor | Lab 1 bağımsızlık ve güvenli durum | Devre şeması, validasyon raporu, duruş ölçümü |
| B03 | Ağ ve bakım portları bilinmiyor | Lab 2-4 erişilebilirlik | Kurulumla eşleşen ağ/arayüz dokümanı |
| B04 | Uzaktan erişim ve internet bağlantısı bilinmiyor | R1 koşulu ve Lab 4 mevcut durum | Kamuya açık servis mimarisi; bulunmazsa bilinmiyor kalacak |
| B05 | Duruş süresi, PLr/SIL, saha maruziyeti bilinmiyor | Fonksiyon hedefi ve risk güveni | Risk değerlendirmesi, bileşen verileri ve validasyon |
| V01 | Servis cihazı/erişimi varsa parametre değiştirilebilir olabilir | R1-R3 | Tamamen varsayımsal; erişim ve yetki doğrulanmadan bulgu sayılmaz |
| V02 | Z0-Z5 ve C1-C5 hedef ağı | Lab 2-4 | Öneri; uygulanmış mimari değil |
| V03 | E, tehlikeye maruziyet olarak yorumlandı | Lab 3 | Föy değişkeni açıklamıyor; öğretim elemanı farklı tanım verirse yeniden puanla |
| B06 | AB pazarına arz tarihi, varyantı ve teknik dosya yok | Mevzuat kapsamı | Belgeler bulunmadan kapsam/uygunluk kararı yok |
| V04 | Component X 2.4, CVE-XXXX-XXXX, CVSS 9.8 ve yama mevcut ifadesi yalnız föyün örneği | Lab 5 karar alıştırması | Gerçek CVE kimliği, üretici duyurusu ve makine envanteriyle eşleştirilmedi |

## Lab 5 karar ve kanıt sınırı

VD-05: **Açık / etkilenme belirsiz.** Bileşen varlığı, etkilenen sürüm ve erişim/tetiklenme koşulu doğrulanmadı. Bu sonuç “etkilenmiyor” veya “üretime devam güvenli” anlamına gelmez. Tam SBOM, yama paketi veya gerçek test sonucu üretilmedi. NIST SP 800-82 Rev.3 bölüm 6.2.11 yama yönetimi rehberiyle tutarlı olarak önerilen test/geri dönüş süreci yazıldı; gerçek kurulum yapılmadı. Emniyet üzerindeki etki Lab 1/4'teki kapak/şerit duruşu, reset ve yük tutma gereksinimleriyle ilişkilendirildi.

Firma ile görüşmek bu çalışmanın kapsamı dışında kalır. Kamuya açık kanıt bulunamayan alanlar, gerçekmiş gibi tamamlanmaz. Sınıf seçimi için yalnız öğrencinin çakışmama teyidi kayıt altındadır.

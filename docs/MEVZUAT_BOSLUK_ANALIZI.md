# 2027 mevzuatı ve gereksinim boşlukları

Kontrol tarihi: **25.10.2026**. Öğretim elemanının tam ifadesi verilmediği için “2027 düzenlemesi kesin şudur” denemez. İki düzenlemenin de 2027 uygulama tarihi vardır. Makine emniyeti ve siber müdahalenin fiziksel etkisi bağlamı, Makine Tüzüğü ile de ilişkilidir; CRA ayrıca değerlendirilir.

| Kavram | Takvim / anlam | Projedeki ayrım |
|---|---|---|
| AB Makine Tüzüğü (EU) 2023/1230 | Yürürlük: 19.07.2023; genel uygulama: 20.01.2027. Bazı maddeler daha erken uygulanır. | Emniyet ve ilgili kumanda/yazılım bütünlüğü; CRA ile aynı düzenleme değil. |
| CRA (EU) 2024/2847 | Yürürlük: 10.12.2024; genel uygulama: 11.12.2027. Madde 14 bildirim: 11.09.2026; uygunluk değerlendirme kuruluşlarına ilişkin hükümler: 11.06.2026. | Dijital unsurlu ürünlerin siber güvenliği ve zafiyet yönetimi. “2027'de yürürlüğe giriyor” ifadesi teknik olarak genel uygulamayı anlatır. |
| CE işareti | İlgili ürün mevzuatına uygunluğun işaretidir; tek başına ayrı bir 2027 kanunu değildir. | Üyelik sayfasındaki genel CE ifadesi bu model/varyant için güncel uygunluk beyanını veya CRA uygunluğunu kanıtlamaz. |
| CVE | Bilinen siber güvenlik açığına verilen kayıt kimliği. | Mevzuat veya sertifika değildir. Bileşen/sürüm doğrulanmadığı için makineye CVE atanmadı. |

Kaynaklar: [Komisyon CRA takvimi](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act), [CRA resmî açıklaması](https://digital-strategy.ec.europa.eu/en/policies/cra-summary), [EUR-Lex Makine Tüzüğü özeti](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=LEGISSUM:4682019), [Komisyon makine sayfası](https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en). Makine Tüzüğü'nün ilk yayımlanan metnindeki 14 Ocak tarihi düzeltilmiştir; bu çalışmada resmî güncel açıklamalardaki **20 Ocak 2027** esas alınır. Orijinal EUR-Lex tam metin erişimi bot kontrolüne takıldığından erişilebilen resmî özet ve Komisyon açıklamaları kullanıldı.

## Koşullu uygulanabilirlik

CRA için ürünün AB pazarında sunulması, amaçlanan veya makul öngörülebilir kullanımında başka cihaz/ağla doğrudan ya da dolaylı veri bağlantısı bulunması ve istisnalar değerlendirilmelidir. İnternet bağlantısı tek başına şart değildir. PLC bulunması tek başına bu modelin CRA kapsamında olduğunun kanıtı değildir. 11.12.2027 öncesi piyasaya arz, esaslı değişiklik ve bildirim hükümlerinin geçiş kuralları ayrıca incelenir. [Resmî CRA açıklaması](https://digital-strategy.ec.europa.eu/en/policies/cra-summary).

Makine Tüzüğü için AB pazarına arz/hizmete sunma, tarih, ürün sınıfı ve ilgili geçiş koşulları incelenmelidir. Türkiye'deki ders için seçilmiş olması tek başına AB mevzuatının belirli makineye uygulanmasını kanıtlamaz. Bu çalışma ne kapsam ne uygunluk kararı verir. [Komisyon makine sayfası](https://single-market-economy.ec.europa.eu/sectors/mechanical-engineering/machinery_en).

## Gereksinim boşluğu analizi

“Kanıt yok” ifadesi uyumsuzluk tespiti anlamına gelmez.

| Konu | Gerekli inceleme | Elde olan / boşluk | Proje eylemi |
|---|---|---|---|
| Kapsam ve tarih | AB pazarına arz, varyant, bağlantı, değişiklik geçmişi | Model sayfası var; ilgili kayıtlar yok | Kapsamı koşullu bırak |
| Makine emniyeti | Risk analizi, kumanda güvenilirliği, yazılım/veri bütünlüğü | Duruş beyanı var; devre ve validasyon yok | Lab 1 ve 4'te gereksinim tanımla |
| Siber risk yönetimi | Erişim, yetki, kayıt, güncelleme/konfigürasyon güvenliği | Kontroller doğrulanmadı | Lab 2-4'te hedef gereksinim yaz |
| CRA zafiyet yönetimi | Bileşen envanteri, destek, bildirim ve düzeltme süreci | SBOM/firmware yok | Lab 5-6'da koşullu süreç hazırla |
| CE/teknik dosya | İlgili mevzuata göre uygunluk değerlendirmesi ve beyan | Modele/varyanta özgü dosya yok | Belgelendirilmiş uygunluk iddia etme |

## Lab 6 için bildirim takvimi kontrolü - 06.11.2026

| Süre | Başlangıç / koşul |
|---|---|
| Erken uyarı: gecikmeden, en geç 24 saat | Kapsam ve bildirim eşiği sağlandığında üreticinin ilgili aktif istismar/ciddi olaydan haberdar oluşu |
| Bildirim: gecikmeden, en geç 72 saat | Aynı farkındalık anı; erken uyarıdan sonra ilave 72 saat değil |
| Aktif istismar edilen zafiyet nihai raporu: en geç 14 gün | Düzeltici veya azaltıcı önlem kullanılabilir olduktan sonra |
| Ciddi olay nihai raporu: bir ay içinde | 72 saatlik olay bildiriminin sunulmasından sonra; tespitten 14 gün değil |

Kaynaklar: [ENISA SRP SSS](https://www.enisa.europa.eu/topics/product-security/vulnerability-services/eu-incident-response-and-cyber-crisis-management/single-reporting-platform-srp/frequently-asked-questions), [Komisyon bildirim açıklaması](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting). Kapsam/bildirim eşiği kararı üreticinin yetkili ekibine aittir; öğrenci çalışması bu kararı vermez. Bu nedenle Lab 6'daki 10:15 alarmı ile üreticinin farkındalık anı aynı sayılmadı. Bildirim sorumluluğu, öğrenciye veya yalnız vardiya sorumlusuna yüklenmedi. SRP'de seçilecek koordinatör CSIRT, ilgili yerleşiklik/temsil koşullarına göre belirlenir; üreticinin Türkiye'de olması nedeniyle rastgele bir AB ülkesine atama yapılmadı. Gerçek olay/bildirim yoktur.

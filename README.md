# Karmetal OSA 350x450 PLC - Endüstriyel Siber Güvenlik Projesi

Kamuya açık kaynaklarla yapılan öğrenci çalışması. Firma ile iletişim kurulmaz; gerçek makineye bağlanılmaz ve izinsiz test yapılmaz. Belgeler, gerçek bir açık keşfi veya uygunluk belgesi değildir.

**Güncel teslim:** İlk beş hafta için ayrı, tek sayfalık doldurulmuş laboratuvar föyleri. Örnekteki başlık, kimlik alanları, şema ve soru-cevap düzeni makineye uyarlanmıştır. Ad Soyad ve Grup alanları, bilgi verilmediği için PDF içinde doldurulabilir bırakılmıştır. Tarih belgenin hazırlanma tarihidir, ders tarihi varsayılmamıştır. İlk dört föy 25.10.2026, 5. hafta 01.11.2026 tarihlidir.

| Hafta | Föy | Çıktı / Evidence Pack |
|---|---|---|
| 1 | [Safety Architecture](output/pdf/Lab1_Safety_Architecture.pdf) | Safety Function Map / EP 03 |
| 2 | [IEC 62443 Mini Workshop](output/pdf/Lab2_IEC62443_Zone_Conduit.pdf) | Zone / Conduit Diagram / EP 05 |
| 3 | [Threat & Risk + Risk Matrix](output/pdf/Lab3_Threat_Risk_Matrix.pdf) | Risk Register / EP 04 |
| 4 | [Secure Remote Access](output/pdf/Lab4_Secure_Remote_Access.pdf) | Secure Architecture / EP 02 + EP 06 |
| 5 | [SBOM / CVE / Patch](output/pdf/Lab5_SBOM_CVE_Patch.pdf) | Vulnerability Decision / EP 09 + EP 10 + EP 11 |

Makine seçiminin sınıfta çakışmadığı öğrenci tarafından 25.10.2026'da teyit edildi. Sınıf listesi bağımsız olarak incelenmedi. Firma [SAMİB üye kaydında](https://samib.org.tr/uye/karmetal-san-tic-ltd-sti/) yer alıyor.

## Belgeleri okuma

- **[D] Doğrulanan:** Kamuya açık kaynakta belirtilmiş özellik; saha doğrulaması anlamına gelmez.
- **[B] Bilinmiyor:** Kaynaklarda doğrulanamayan bilgi. Bulunamaması, özelliğin olmadığı anlamına gelmez.
- **[V] Varsayım:** Eğitim amaçlı koşullu senaryo.
- **[Ö] Öneri:** Hedef gereksinim veya kontrol; mevcut makinede var olduğu iddia edilmez.
- **[Ç] Çıkarım:** Doğrulanmış hareket/işlevden çıkarılan analitik tehlike yorumu.

PLC modeli, firmware, Safety PLC, STO, ağ protokolü, internet bağlantısı, uzaktan erişim ve PL/SIL seviyesi bilinmiyor. Hiçbir CVE bu makineye atanmamıştır. Föydeki jenerik robot, SCADA ve IPC varlıkları kanıtsız şekilde makineye eklenmemiştir.

## Depo düzeni

- `output/pdf/`: Teslime hazır beş ayrı PDF.
- `data/labs.json`: Föylerin düzenlenebilir metni, tabloları ve kaynak kodları.
- `docs/KAYNAKLAR.md`: Kaynak listesi, teknik kanıtlar ve bilgi eksikleri.
- `docs/MEVZUAT_BOSLUK_ANALIZI.md`: CRA, Makine Tüzüğü, CE ve CVE ayrımı.
- `docs/PROJE_YONETIMI.md`: SWOT, SMART, Trello görevleri ve teslim listesi.
- `docs/KOR_TEST_PLANI.md`: Sonucu önceden görülmeyen masa başı testleri için protokol.
- `docs/KALITE_KONTROL.md`: İçerik ve PDF kontrol kaydı.
- `tools/build_labs.py`: Föyleri tekrar üretmek için küçük yardımcı araç; tek hafta seçilebilir.

Yerelde verilen özgün iki PDF korunur ve Git'e eklenmez. Örnek dosya başka bir öğrenciye ait kişisel bilgiler içerir; yeni belgelerde bu bilgiler kullanılmamıştır.

## Yeniden üretme

Python 3, `reportlab` ve Windows Arial yazı tipleri gerekir. Depo kökünden:

```powershell
python tools/build_labs.py
# Yalnız 5. haftayı üret:
python tools/build_labs.py --lab 5
```

Araç tek sayfa sınırını aşan içeriği hata sayar. Üretim sonrası görsel kontrol yine yapılmalıdır. PDF oluşturmak için kullanılan kod, makineyle haberleşmez.

## Tamamlanan ve kalan kapsam

İlk beş föy, kaynak/bilgi açığı kaydı ve proje yönetimi taslağı hazırdır. Lab 5'te föyün Component X 2.4 / CVSS 9.8 verisi yalnız eğitim varsayımıdır; gerçek CVE eşlemesi veya tam SBOM değildir. Sonuç, kanıt eksikliği nedeniyle etkilenmenin belirsiz olduğudur. Yama kurulumu ve gerçek makine testi yapılmadı. 6. CRA Incident Simulation ve 7. AI Safety Challenge sonraki teslimlerdir; tamamlanmış sayılmaz. Trello görevleri dosya olarak hazırlanmıştır, canlı Trello panosu oluşturulmamıştır. Kör testler planlandı; henüz uygulanmadı.

**Sıradaki tek adım:** Kimlik alanlarını tamamlayıp ilk kör masa başı oturumunu yürütmek.

# Kör masa başı test planı

**Durum: planlandı, uygulanmadı.** “Kör” burada katılımcının değerlendirme anahtarını yanıt vermeden görmemesi anlamındadır. Saldırı, port taraması veya makineye müdahale değildir. Bu protokol belge üzerinden verilen kararları ölçer; gerçek emniyet performansını doğrulamaz.

## Oturum akışı

1. Uygulayıcı, dört kurgusal vaka ve değerlendirme anahtarını oturum başında ayrı hazırlar. Anahtar öğrenci yanıtı kilitlenene kadar gösterilmez ve açık depoya önceden konmaz.
2. Vakalarda makineye ait olduğu doğrulanmayan özellikler açıkça “senaryo varsayımı” olarak verilir. Sıra karıştırılır. Gerçek sistem/kişisel veri veya gerçek hedef adresi kullanılmaz.
3. Öğrenci her vaka için ilk kararını, gerekçesini, güvenli durum ihtiyacını ve eksik kanıtı yazar. Yanıt zamanı kaydedilir; yanıt sonradan değiştirilmez.
4. Yanıtlar tamamlandıktan sonra anahtar açılır. Sonuçlar öğrenciye gösterilir; düzeltmeler ilk yanıtın yanında tutulur.
5. Anahtar yanıt öncesi görülürse o vaka kör sayılmaz. Yeni vaka hazırlanır. Yapay zekâ yanıtı da ilk öğrenci yanıtının yerine geçirilmez.

## Dört test kategorisi

| ID | Hafta / konu | Ölçülecek karar |
|---|---|---|
| KT1 | Lab 1 / emniyet fonksiyonu | Doğrulanmış özellik ile öneriyi ayırma; güvenli durum ve kanıt ihtiyacı |
| KT2 | Lab 2 / bölge sınırı | Gereksiz bölge geçişini fark etme; gerekli en az erişimi tanımlama |
| KT3 | Lab 3 / öncelik | L x S x E hesabı ve S=3 istisnasını doğru uygulama |
| KT4 | Lab 4 / servis erişimi | Erişim güvenliği ile emniyet bağımsızlığını birlikte değerlendirme |

Özel vaka metinleri ve yanıt anahtarı bu plana eklenmedi; sonraki oturumda üretilecek. Bu, katılımcının anahtarı önceden görmesini önler.

## Değerlendirme ve sonuç kaydı

Her vaka dört ölçütte 0/1 puan: (a) doğru ilk karar, (b) fiziksel sonuç/güvenli davranış, (c) kanıt-varsayım ayrımı, (d) gerekçe ve gerekli takip. Toplam 16 puan. Eğitim hedefi en az 12/16; S=3 senaryosunun inceleme dışında bırakılması ve kanıtsız “emniyet etkilenmez” kararı ayrıca kritik öğrenme hatası olarak işaretlenir. Bu eşik ders notu veya resmî emniyet kabul kriteri değildir.

Kayıt şablonu: `KT ID | Vaka sürümü | İlk yanıt zamanı | İlk karar | Gerekçe | Eksik kanıt | Puan | Anahtarın açılma zamanı | Düzeltme`. Sonuç satırları oturum yapılmadan doldurulmaz.

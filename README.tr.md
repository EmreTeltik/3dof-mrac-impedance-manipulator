# Değişken Yükler Altında MRAC ve Empedans Kontrollü 3-DOF Robot Kol

[English](README.md) · [Mevcut durum](STATUS.md) · [Yol haritası](ROADMAP.md)

Ege Üniversitesi Elektrik-Elektronik Mühendisliği bitirme projesi kapsamında, uç yükü değiştiğinde hareketini uyarlayabilen üç dönel eklemli bir robot kol geliştirilmesi ve fiziksel deneylerle değerlendirilmesi amaçlanmaktadır.

**Durum:** Bitirme tezi önerisi hazırlanmıştır; proje başlangıç aşamasındadır. TÜBİTAK **2209-A başvurusu planlanmaktadır/hazırlanmaktadır**. Destek alınmış olduğu iddia edilmemektedir. Depoda ön tasarım özeti, kontrol mimarisi, gereksinimler, doğrulama planı ve ideal kinematik hesaplama aracı bulunur.

## Teknik amaç

Model Referans Uyarlamalı Kontrol (MRAC) ile yük değişiminin neden olduğu dinamik belirsizlikler altında robotun referans modele yakın yörünge takibine dönmesi incelenecektir. Empedans kontrolüyle düşük hızlı etkileşimlerde sanal kütle, sönüm ve rijitlik davranışının şekillendirilmesi planlanmaktadır.

## Ön tasarım hedefleri

Bu sayılar ölçülmüş başarım değil, öneri belgesindeki hedeflerdir.

| Başlık | Hedef |
| --- | --- |
| Eklem yapısı | J1 yaw, J2 ve J3 pitch; toplam 3 DOF |
| Erişim | 270 mm nominal geometri |
| Bağ uzunlukları | 150 mm + 120 mm |
| Uç yükü | 100 g |
| Kontrol çevrimi | En az 500 Hz; hedef 1 kHz |
| Eklem açısı sayısal çözünürlüğü | ≤0,1°; fiziksel doğruluk ayrıca doğrulanacak |
| Kartezyen yörünge takibi | RMSE ≤5 mm |
| Yük değişimi sonrası toparlanma | Önceden tanımlı hata bandına göre ≤0,5 s |
| Yapı | PLA+ baskı ve standart mekanik parçalar |
| Kontrolcü | STM32H7 sınıfı aday |
| Modelleme | MATLAB/Simulink |

## Planlanan deneyler

Sabit yükte nominal yörünge takibi, ani ve kademeli yük değişimi, temel kontrolcü ile MRAC karşılaştırması, adaptif parametre sınırları, akım tepkisi ve gerçek zamanlı çevrim süresi değerlendirilecektir. Empedans katmanı eklendiğinde etkileşim ölçüm yöntemi ayrıca tanımlanacaktır. Akım ölçümü tek başına kalibre edilmiş uç kuvveti ölçümü sayılmaz.

## Şu an sunulan yazılım

`tools/kinematics_preview.py`, sıfır ofsetli ideal yaw-pitch-pitch geometri için ileri kinematik, analitik Jacobian ve sınırlı ters kinematik hesabı yapar. Gerçek robot CAD modelinin, dinamik modelin veya MRAC algoritmasının yerine geçmez. Kullanımı [tools/README.md](tools/README.md) dosyasındadır.

## Ekip ve katkı

Tez yazarları Emre Teltik ve Mehmet Can Tanürün; danışman Dr. Erman Selim'dir. Kişisel iş dağılımı kesinleştiğinde ve işler yapıldığında [CONTRIBUTORS.md](CONTRIBUTORS.md) üzerinden kayıt tutulacaktır. Ortak çalışmanın tümü tek kişiye ait olarak gösterilmemektedir.

Gerçek robot, ölçüm ve sonuç görselleri üretildikçe deney koşullarıyla birlikte paylaşılacaktır. Orijinal rapordaki telefonlar ve öğrenci numaraları bu depoya dahil edilmemiştir.

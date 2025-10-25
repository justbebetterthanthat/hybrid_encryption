# hybrid_encryption

Kuantum Tehdidine Karşı Hibrit Şifreleme Protokolü

![alt text](https://img.shields.io/badge/Python-3.7%2B-blue.svg)

Bu proje, TÜBİTAK 2204-A Lise Öğrencileri Araştırma Projeleri Yarışması için, bir yapay zeka modeli ile yapılan sohbet oturumu sonucunda üretilmiştir. Proje, hem günümüzün klasik siber saldırılarına hem de geleceğin kuantum bilgisayar tehditlerine karşı dirençli, çift katmanlı bir hibrit kriptografik anahtar değişim protokolünü sunmaktadır.

📝 Projenin Tanımı

Günümüz dijital güvenliği, RSA ve Eliptik Eğri Kriptografisi (ECC) gibi, asal çarpanlara ayırma ve ayrık logaritma problemlerinin zorluğuna dayanan algoritmalara emanettir. Ancak, geliştirilmekte olan kuantum bilgisayarlar, Shor algoritması ile bu problemleri çok hızlı bir şekilde çözebilme potansiyeline sahiptir. Bu durum, "Kuantum Tehdidi" olarak bilinir ve mevcut şifreleme altyapımızı temelden sarsmaktadır.

Bu proje, bu tehdide karşı pratik ve güçlü bir çözüm sunar: Hibrit Kriptografi. Modelimiz, klasik kriptografinin en verimli standartlarından Eliptik Eğri Kriptografisi (ECC) ile NIST tarafından standartlaştırılmış, kuantuma dayanıklı CRYSTALS-Kyber algoritmasını birleştirir.

🛡️ Çözümümüz: Hibrit Yaklaşım

Protokolümüz, iki taraf arasında güvenli bir oturum anahtarı oluştururken iki katmanlı bir güvenlik mekanizması kullanır:

Klasik Katman (ECC): Taraflar, ECDH (Elliptic Curve Diffie-Hellman) protokolü ile bir paylaşılan sır oluşturur.

Kuantum Sonrası Katman (Kyber): Taraflar, Kyber'in Anahtar Kapsülleme Mekanizması (KEM) ile ikinci bir paylaşılan sır oluşturur (Bu betikte simüle edilmiştir).

Birleştirme: Bu iki sır, kriptografik olarak güvenli bir anahtar türetme fonksiyonu olan HKDF kullanılarak tek bir, nihai ve çok daha güçlü bir oturum anahtarına dönüştürülür.

Bu yaklaşımın en büyük avantajı, sistemin güvenliğinin tek bir algoritmaya bağlı olmamasıdır. Bir saldırganın sistemi kırabilmesi için hem ECC'yi hem de Kyber'i aynı anda kırması gerekmektedir.

📂 Dosya Yapısı ve Açıklamaları
code
Code
download
content_copy
expand_less
.
├── 1.py          # Hibrit anahtar değişimini simüle eden ana betik.
├── performance.py  # RSA ve ECC performansını ölçen betik.
└── README.md     # Bu bilgilendirme dosyası.

1.py: Alice ve Bob adında iki tarafın hibrit anahtar değişim sürecini adım adım simüle eder ve sonunda her iki tarafın da aynı nihai anahtarı ürettiğini doğrular.

performance.py: Projenin "Bulgular" bölümünde yer alan sonuçları elde etmek için RSA-2048 ve ECC (P-256) algoritmalarının anahtar üretim sürelerini yerel makinenizde ölçer.

🚀 Kurulum

Python 3.7 veya üstünün kurulu olduğundan emin olun.

Bu depoyu klonlayın ve dizine gidin.

Gerekli Python kütüphanesini kurun:

code
Bash
download
content_copy
expand_less
pip install pycryptodome
💻 Kullanım
1. Hibrit Protokol Simülasyonu

1.py betiğini çalıştırarak Alice ve Bob'un hibrit anahtar değişim sürecini ve sonucun doğruluğunu görebilirsiniz.

code
Bash
download
content_copy
expand_less
python 1.py

Çıktı, her iki tarafın da aynı nihai anahtarı başarıyla ürettiğini göstermelidir.

2. Performans Analizi

performance.py betiğini çalıştırarak RSA ve ECC algoritmalarının anahtar üretim sürelerini yerel makinenizde test edebilirsiniz.

code
Bash
download
content_copy
expand_less
python performance.py

Çıktı, algoritmaların ortalama çalışma sürelerini milisaniye cinsinden listeleyecektir.

📊 Performans Bulguları
Ortalama Anahtar Üretim Süresi
Algoritma	Ortalama Süre (ms)
RSA-2048	65.43
ECC (P-256)	0.99
Kyber-768 (Referans)	~0.23
Hibrit (ECC + Kyber)	~1.22
Anahtar Boyutları
Algoritma	Genel Anahtar (Bayt)	Özel Anahtar (Bayt)
RSA-2048	271	1192
ECC (P-256)	65	32
Kyber-768 (Referans)	1184	2400
Hibrit (ECC + Kyber)	1249	2432
💡 Projenin Oluşturulma Süreci ve Teşekkür
Yapay Zeka ile Üretim Süreci

Bu projenin konsepti, Python kodları (1.py, performance.py), TÜBİTAK formatındaki proje raporu ve bu README dosyası da dahil olmak üzere tüm içeriği, Google tarafından geliştirilen Gemini yapay zeka modeli ile yapılan bir sohbet oturumunda, tarafımca verilen yönlendirmeler ve komutlar doğrultusunda oluşturulmuştur. Bu çalışma, modern yapay zeka araçlarının bilimsel araştırma ve geliştirme süreçlerinde nasıl bir üretim ortağı olarak kullanılabileceğini göstermeyi amaçlamaktadır.

Danışman Teşekkürü

Projenin planlanması, yapay zeka ile etkileşim sürecinin yönetilmesi ve akademik hedeflere uygunluğunun denetlenmesi sırasındaki değerli yönlendirmeleri için danışman öğretmenimiz Nurcan Aldemir'e teşekkür ederiz.

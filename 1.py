import os
from Crypto.PublicKey import ECC
from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512

print("--- HİBRİT KRİPTO SİSTEMİ SİMÜLASYONU ---")
print("Bu versiyon, ECC anahtar değişiminin temel matematiksel işlemini kullanır.")

# --- BÖLÜM 1: KLASİK KRİPTOGRAFİ (ECC) ---

# Alice kendi ECC anahtar çiftini oluşturur.
# .d = private scalar (özel anahtar, bir sayıdır)
# .pointQ = public point (genel anahtar, eğri üzerinde bir noktadır)
alice_ecc_anahtar = ECC.generate(curve='P-256')

# Bob kendi ECC anahtar çiftini oluşturur.
bob_ecc_anahtar = ECC.generate(curve='P-256')

print("1. Klasik Katman (ECC): Anahtar çiftleri oluşturuldu.")

# ********************** EN ÖNEMLİ DÜZELTME BURADA **********************
#
# ECDH (Eliptik Eğri Diffie-Hellman) anahtar değişimi, bir tarafın özel anahtarını (scalar)
# diğer tarafın genel anahtarı (point) ile çarparak gerçekleştirilir.
# Sonuç, her iki tarafta da aynı olan yeni bir noktadır.
# Bu noktanın x koordinatı, paylaşılan sır (shared secret) olarak kullanılır.
#
# *************************************************************************

# Alice, kendi ÖZEL anahtarını (alice_ecc_anahtar.d) Bob'un GENEL anahtarı (bob_ecc_anahtar.pointQ) ile çarpar.
alice_tarafındaki_sonuc_noktası = alice_ecc_anahtar.d * bob_ecc_anahtar.pointQ
# Paylaşılan sır, bu yeni noktanın x koordinatıdır.
alice_ecc_sırrı_integer = alice_tarafındaki_sonuc_noktası.x

# Bob, kendi ÖZEL anahtarını (bob_ecc_anahtar.d) Alice'in GENEL anahtarı (alice_ecc_anahtar.pointQ) ile çarpar.
bob_tarafındaki_sonuc_noktası = bob_ecc_anahtar.d * alice_ecc_anahtar.pointQ
# Paylaşılan sır, bu yeni noktanın x koordinatıdır.
bob_ecc_sırrı_integer = bob_tarafındaki_sonuc_noktası.x

# Kontrol: Her iki tarafın da aynı sayıyı bulduğunu teyit edelim.
assert alice_ecc_sırrı_integer == bob_ecc_sırrı_integer

# Elde edilen büyük tam sayıları (integer) diğer kriptografik fonksiyonlarda kullanmak için
# sabit uzunlukta byte dizisine çevirmemiz gerekir (P-256 için 32 byte).
alice_ecc_sırrı = alice_ecc_sırrı_integer.to_bytes(32, 'big')
bob_ecc_sırrı = bob_ecc_sırrı_integer.to_bytes(32, 'big')

print(f"2. Alice'in ECC Sırrı (ilk 8 byte): {alice_ecc_sırrı[:8].hex()}...")
print(f"3. Bob'un ECC Sırrı   (ilk 8 byte): {bob_ecc_sırrı[:8].hex()}... (Sırlar eşleşti!)")


# --- BÖLÜM 2: KUANTUM SONRASI KRİPTOGRAFİ (Kyber Simülasyonu - Değişiklik yok) ---
print("\n--- Kuantum Sonrası Katman (Kyber Simülasyonu) ---")
alice_kyber_sırrı = os.urandom(32)
bob_kyber_sırrı = alice_kyber_sırrı
print(f"4. Alice'in Kyber Sırrı (ilk 8 byte): {alice_kyber_sırrı[:8].hex()}...")
print(f"5. Bob'un Kyber Sırrı   (ilk 8 byte): {bob_kyber_sırrı[:8].hex()}... (Sırlar eşleşti!)")


# --- BÖLÜM 3: HİBRİT ANAHTARIN OLUŞTURULMASI (Değişiklik yok) ---
print("\n--- Hibrit Anahtarın Oluşturulması ---")
salt = os.urandom(16)
alice_hibrit_anahtar = HKDF(master=(alice_ecc_sırrı + alice_kyber_sırrı), key_len=32, salt=salt, hashmod=SHA512)
bob_hibrit_anahtar = HKDF(master=(bob_ecc_sırrı + bob_kyber_sırrı), key_len=32, salt=salt, hashmod=SHA512)
print("6. İki katmanın sırları birleştirilerek nihai anahtar türetildi.")

# --- NİHAİ KONTROL ---
print("-" * 45)
print(f"Alice'in Nihai Anahtarı: {alice_hibrit_anahtar.hex()}")
print(f"Bob'un Nihai Anahtarı:   {bob_hibrit_anahtar.hex()}")
if alice_hibrit_anahtar == bob_hibrit_anahtar:
    print("\nSONUÇ: BAŞARILI! Hibrit güvenlik protokolü her iki tarafta da aynı nihai anahtarı üretti.")
else:
    print("\nSONUÇ: HATA! Anahtarlar Eşleşmiyor.")
print("-" * 45)
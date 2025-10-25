import time
from Crypto.PublicKey import RSA, ECC

def benchmark(func, num_iterations=50):
    """Bir fonksiyonun ortalama çalışma süresini ölçer."""
    start_time = time.perf_counter()
    for _ in range(num_iterations):
        func()
    end_time = time.perf_counter()
    return (end_time - start_time) / num_iterations * 1000  # ms cinsinden

# Ölçülecek Fonksiyonlar
def rsa_key_gen(): RSA.generate(2048)
def ecc_key_gen(): ECC.generate(curve='P-256')

print("--- Sisteminizde Çalışan Algoritmaların Performans Analizi ---")
iterations = 50

# Zaman Ölçümleri
print(f"{iterations} iterasyon üzerinden süreler ölçülüyor...")
rsa_time = benchmark(rsa_key_gen, iterations)
ecc_time = benchmark(ecc_key_gen, iterations)
print("Ölçümler tamamlandı.\n")

# --- SONUÇLARI GÖSTERME ---
print("-" * 50)
print("ORTALAMA ANAHTAR ÜRETİM SÜRESİ (ms)")
print(f"{'Algoritma':<20} | {'Süre (ms)':>15}")
print("-" * 40)
print(f"{'RSA-2048':<20} | {rsa_time:15.4f}")
print(f"{'ECC (P-256)':<20} | {ecc_time:15.4f}")
print("\nNOT: Kyber ve Hibrit Model değerleri için raporunuza")
print("NIST'in resmi verilerini ve bu ölçümlerden elde edilen")
print("toplamları eklemeniz bilimsel olarak daha doğrudur.")
print("-" * 50)
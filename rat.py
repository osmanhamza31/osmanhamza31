import os

# Bilgisayarın tüm bilgilerini almak için bir fonksiyon
def herseyi_al():
    # İşletim sistemi bilgisini al
    isletim_sistemi = os.uname()
    # Ağ bağlantılarını al
    ag_baglantilari = os.popen('ip a').read()
    # Disk kullanımını al
    disk_kullanimi = os.popen('df -h').read()
    # Bellek kullanımını al
    bellek_kullanimi = os.popen('free -m').read()
    # İşlemci bilgilerini al
    islemci_bilgileri = os.popen('lscpu').read()

    # Bilgileri yazdır
    print("İşletim Sistemi Bilgileri:")
    print(isletim_sistemi)
    print("\nAğ Bağlantıları:")
    print(ag_baglantilari)
    print("\nDisk Kullanımı:")
    print(disk_kullanimi)
    print("\nBellek Kullanımı:")
    print(bellek_kullanimi)
    print("\nİşlemci Bilgileri:")
    print(islemci_bilgileri)

# Fonksiyonu çağır ve bilgileri al
herseyi_al()

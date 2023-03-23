#install library
!pip install CurrencyRates
!pip install CurrencyConverter
!pip install forex-python

# import library
from datetime import datetime
from datetime import date
from forex_python.converter import CurrencyRates
from currency_converter import CurrencyConverter
c = CurrencyRates()

# list untuk history
history = []

# fungsi Harga mata uang saat ini
def price_currency(firstCurrency, lastCurrency):
    hasil = c.convert(firstCurrency, lastCurrency, 1)
    print(f"\nMata Uang {firstCurrency} to {lastCurrency} saat ini\t\t: {round(hasil,2)}") #round untuk membulatkan bilangan floaat
    list = (f"Mata Uang {firstCurrency} to {lastCurrency} saat ini: {round(hasil,2)}")
    history.append(list)

# fungsi Harga mata uang yang berlalu
def currency_berlalu(firstCurrency, lastCurrency, tahun, bulan, tanggal):
    cc = CurrencyConverter(fallback_on_missing_rate=True,fallback_on_wrong_date=True) # mengatasi bug
    hasil = cc.convert(1, firstCurrency, lastCurrency, date=date(tahun,bulan,tanggal))
    print(f"\nMata Uang {firstCurrency} to {lastCurrency} pada {tahun} {bulan} {tanggal}\t: {round(hasil,2)}")
    list = (f"Mata Uang {firstCurrency} to {lastCurrency} pada {tahun} {bulan} {tanggal}: {round(hasil,2)}")
    history.append(list)

# fungsi Konversi mata uang saat ini
def converter(jumlah, firstCurrency, lastCurrency,):
    hasil = c.convert(firstCurrency, lastCurrency, jumlah)
    print(f"\nHasil konversi {firstCurrency} to {lastCurrency} {jumlah}\t\t: {round(hasil,2)}")
    list = (f"Hasil konversi {firstCurrency} to {lastCurrency} {jumlah}: {round(hasil,2)}")
    history.append(list)

def show_menu():
    # local real time
    print("\n",datetime.now().date(),"",datetime.now().time())

    # judul dan menu program
    print("""================= CONVERTER CURRENCY =================
    1. Harga mata uang saat ini
    2. Harga mata uang yang berlalu
    3. Konversi mata uang saat ini
    4. History hasil akhir
    5. Exit
    """)

    # input program
    menu = int(input("Pilih angka menu yang akan dilakukan\t: "))

    # percabangan dari menu program
    if menu == 1:
        mata_uang = str(input("Masukkan mata uang awal\t\t\t: ").upper())
        konversi = str(input("Masukkan mata uang yang di konversi\t: ").upper())
        price_currency(mata_uang, konversi)

    elif menu == 2:
        mata_uang = str(input("Masukkan mata uang awal\t\t\t: ").upper())
        konversi = str(input("Masukkan mata uang yang di konversi\t: ").upper())
        year = int(input("Masukkan tahun\t\t\t\t: "))
        month = int(input("Masukkan bulan\t\t\t\t: "))
        day = int(input("Masukkan tanggal\t\t\t: "))
        currency_berlalu(mata_uang, konversi, year, month, day)
            
    elif menu == 3:
        nilai = float(input("Masukkan jumlah nilai mata uang\t\t: "))
        mata_uang = str(input("Masukkan mata uang awal\t\t\t: ").upper())
        konversi = str(input("Masukkan mata uang yang di konversi\t: ").upper())
        converter(nilai, mata_uang, konversi)

    elif menu == 4:
        print("History hasil akhir : ")
        for i in range (0,len(history)):
            print(history[i])
        
    elif menu == 5:
        print("Terimakasih telah menggunakan program kami")
        exit()
        
    else:
        print("Menu yang anda masukan tidak tersedia")

while True:
    show_menu()
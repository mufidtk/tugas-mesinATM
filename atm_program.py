import random
import datetime
from customer import Customer

atm = Customer(id)

#looping pemeriksaan
while True:
    print("\nSelamat datang di ATM Makmur Bersama!")
    id = int(input('Masukkan PIN: '))
    trial = 1

    #looping verifikasi
    while id != int(atm.checkPin()) and trial < 3:
        print('\nPIN salah! ' + '(' + str(trial) + ' kali gagal) : ')
        id = int(input('Masukkan PIN: '))
        trial += 1

        if trial == 3:
            print('\nGagal verifikasi PIN! (' + str(trial) + ' kali gagal)')
            print('Silakan ambil kartu Anda!')
            exit()

    #looping utama
    while True:
        print()
        print('+------------------------------------------------+')
        print('|                    Menu ATM                    |')
        print('+------------------------------------------------+')
        print('|                 1. Cek Saldo                   |')
        print('|                 2. Simpan                      |')
        print('|                 3. Tarik                       |')
        print('|                 4. Transfer                    |')
        print('|                 5. Ganti PIN                   |')
        print('|                 6. Keluar                      |')
        print('+------------------------------------------------+')
        selectmenu = int(input('Silakan masukkan menu (1-6): '))

        if selectmenu == 1:
            print()
            print('Saldo Anda saat ini: Rp. ' + str(atm.checkBalance()) + ',-')
            input('lanjut...')

        elif selectmenu == 2:
            print()
            print('Pilih nominal simpan:')
            print('+------------------------------------------------+')
            print('1. Rp 100.000')
            print('2. Rp 200.000')
            print('3. Rp 300.000')
            print('4. Rp 400.000')
            print('5. Rp 500.000')
            print('6. Rp 50.000')
            print('+------------------------------------------------+')
            pilih = int(input('\nPilih nominal simpan (1-6): '))

            nominal = 0
            if pilih == 1:
                nominal = 100000
            elif pilih == 2:
                nominal = 200000
            elif pilih == 3:
                nominal = 300000
            elif pilih == 4:
                nominal = 400000
            elif pilih == 5:
                nominal = 500000
            elif pilih == 6:
                nominal = 50000
            else:
                print('Pilihan nominal salah!')
                break

            verify_deposit = input("Konfirmasi: Anda akan simpan dana Rp " + str(nominal) + ",- ? (y/n) : ")
            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Simpan dana Rp " + str(nominal) + ",- berhasil!")
                print("Saldo Anda saat ini  Rp " + str(atm.checkBalance()) + ",-" )
                input('lanjut...')
            else:
                break

        elif selectmenu == 3:
            print()
            print('Pilih nominal tarik:')
            print('+------------------------------------------------+')
            print('1. Rp 100.000')
            print('2. Rp 200.000')
            print('3. Rp 300.000')
            print('4. Rp 400.000')
            print('5. Rp 500.000')
            print('6. Rp 50.000')
            print('+------------------------------------------------+')
            pilih = int(input('\nPilih nominal tarik (1-6): '))

            nominal = 0
            if pilih == 1:
                nominal = 100000
            elif pilih == 2:
                nominal = 200000
            elif pilih == 3:
                nominal = 300000
            elif pilih == 4:
                nominal = 400000
            elif pilih == 5:
                nominal = 500000
            elif pilih == 6:
                nominal = 50000
            else:
                print('Pilihan nominal salah!')
                break

            verify_withdraw = input('Konfirmasi: Anda akan tarik dana Rp ' + str(nominal) + ',- ? (y/t) : ')

            if verify_withdraw == 'y':
                print('\nSaldo awal: Rp ' + str(atm.checkBalance()) + ',-')
            else:
                break

            if nominal <= atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi tarik berhasil!")
                print("Saldo sisa: Rp " + str(atm.checkBalance()) + ",-")
                input('lanjut...')
            else:
                print("Maaf. Saldo Anda tidak cukup!")
                print("Tarik dana tidak dilakukan.")
                input('lanjut...')

        elif selectmenu == 4:
            print()
            norek_tujuan = input("Masukkan nomor rekening tujuan: ")

            print('\n')
            print('Pilih nominal transfer:')
            print('+------------------------------------------------+')
            print('1. Rp 100.000')
            print('2. Rp 200.000')
            print('3. Rp 300.000')
            print('4. Rp 400.000')
            print('5. Rp 500.000')
            print('6. Rp 50.000')
            print('+------------------------------------------------+')
            pilih = int(input('\nPilih nominal tarik (1-6): '))

            nominal = 0
            if pilih == 1:
                nominal = 100000
            elif pilih == 2:
                nominal = 200000
            elif pilih == 3:
                nominal = 300000
            elif pilih == 4:
                nominal = 400000
            elif pilih == 5:
                nominal = 500000
            elif pilih == 6:
                nominal = 50000
            else:
                print('Pilihan nominal salah!')
                break
            
            verify_withdraw = input('Konfirmasi: Anda akan transfer dana Rp ' + str(nominal) + ',- ke rekening : ' + norek_tujuan + ' ? (y/t) : ')

            if verify_withdraw == 'y':
                print('\nSaldo awal: Rp ' + str(atm.checkBalance()) + ',-')
            else:
                break

            if nominal <= atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transfer dana berhasil!")
                print("Saldo sisa: Rp " + str(atm.checkBalance()) + ",-")
                input('lanjut...')
            else:
                print("Maaf. Saldo Anda tidak cukup!")
                print("Transfer dana tidak dilakukan.")
                input('lanjut...')

        elif selectmenu == 5:
            verify_pin = int(input("Masukkan PIN lama: "))
            while int(verify_pin) != int(atm.checkPin()):
                print('\nPIN salah!')
                verify_pin = input('Masukkan PIN dengan benar atau tekan "x" untuk keluar : ')
                if verify_pin == "x":
                    print('\nTerimakasih')
                    print("Silakan ambil kartu Anda!")
                    exit()

            ulangi = 1
            while ulangi == 1:
                updated_pin = int(input("Masukkan PIN Baru: "))
                verify_newpin = int(input("Masukkan ulang PIN Baru: "))
                
                if verify_newpin == updated_pin:
                    atm.setPin(updated_pin)
                    print("PIN Baru berhasil dibuat!")
                    ulangi = 0
                    input('lanjut...')
                else:
                    print("PIN Baru tidak sesuai")
                    print(" Perubahan PIN dibatalkan")

        elif selectmenu == 6:
            print()
            print("Resi cetak akhir transaksi.")
            print('+------------------------------------------------+')
            print("No. Record: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print('+------------------------------------------------+')
            print("Terimakasih atas transaksi Anda di ATM kami :)")
            print("Silakan ambil kartu Anda!")
            exit()

        else:
            print("\nError: Maaf, menu tidak tersedia!\n")

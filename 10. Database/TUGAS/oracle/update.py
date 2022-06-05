import cx_Oracle

db = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = db.cursor()

cur.execute("UPDATE cabangbank SET alamatCabang = 'Kec. BENGALON' WHERE kodeCabang = 'SGT'")


cur.execute("UPDATE nasabah SET namaNasabah = 'Sasuke' WHERE idNasabah = 'SGT1'")


cur.execute("UPDATE rekening SET saldo = 30000000 WHERE noRekening = '1'")


cur.execute("UPDATE transaksi SET jumlah = 500000000 WHERE noTransaksi = 'TR1' AND idNasabah = 'SGT1'")

db.commit()
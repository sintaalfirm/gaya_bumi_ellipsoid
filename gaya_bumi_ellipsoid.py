# -*- coding: utf-8 -*-

# mencari nilai gayaberat normal, gaya gravitasi dan sentrifugal pada bumi ellipsoid


print("PROGRAM MENCARI GAYA GRAVITASI, SENTRIFUGAL, GAYA BERAT DAN GAYA BERAT NORMAL")
print("Pilihan sistem referensi :")
print("1. GRS-1980/ WGS-84")
print("2. Internasional 1930")
print("3. GRS-1967")

k = 6.67 * (10 ** (-11))        # konstanta gravitasi
me = 5.9742 * (10 ** 24)        # massa bumi
w = 7.29212 * (10 ** (-5))      # kecepatan sudut putar

import math

def grs80():
  print("\nSistem referensi WGS-84/GRS-1980")
  Ye = 978.0327                 # gaya berat normal di ekuator
  B1 = 0.0053024                # konstanta yang besarnya berbeda setiap ellipsoid
  B2 = 0.0000058                # konstanta yang besarnya berbeda setiap ellipsoid
  a = 6378137                   # sumbu panjang
  f = 1 / 298.257
  b = a * (1 - f)

  return a, b, Ye, B1, B2

def inter():
  print("\nSistem referensi Internasioanl 1930")
  Ye = 978.049
  B1 = 0.0052884
  B2 = 0.0000059
  a = 6378388
  f = 1 / 297
  b = a * (1 - f)

  return a, b, Ye, B1, B2

def grs67():
  print("\nSistem referensi GRS-1967")
  Ye = 978.0318
  B1 = 0.0053024
  B2 = 0.0000059
  a = 6378160
  f = 1 / 297.247
  b = a * (1 - f)

  return a, b, Ye, B1, B2

def x():
  lintang = float(input("lintang = "))
  return lintang

def h():
  tinggi = float(input("ketinggian = "))
  return tinggi

def gravitasi(x, h):
  e = math.sqrt((a ** 2 - b ** 2) / a ** 2)  # eksentrisitas
  N = a / math.sqrt(1 - (e ** 2) * (math.sin(x * math.pi / 180)) ** 2)  # jari kelengkungan utama
  G = k * (me / (N + h) ** 2)
  return G

def sentrifugal(x, h):
  e = math.sqrt((a ** 2 - b ** 2) / a ** 2)  # eksentrisitas
  N = a / math.sqrt(1 - (e ** 2) * (math.sin(x * math.pi / 180)) ** 2)  # jari kelengkungan utama
  C = w * w * (N + h) * math.cos(x * math.pi / 180)
  return C

def berat(x, h):
  e = math.sqrt((a ** 2 - b ** 2) / a ** 2)  # eksentrisitas
  N = a / math.sqrt(1 - (e ** 2) * (math.sin(x * math.pi / 180)) ** 2)  # jari kelengkungan utama
  G = k * (me / (N + h) ** 2)
  C = w * w * (N + h) * math.cos(x * math.pi / 180)
  g = math.sqrt(G * G + C * C + 2 * abs(G) * abs(C) * math.cos((180 - x) * math.pi / 180))
  return g

def beratnormal(x):
  Y = Ye * (1 + B1 * (math.sin(x * math.pi / 180)) ** 2 - B2 * (math.sin(2 * x * math.pi / 180)) ** 2)
  return Y


pilih = int(input("\nMasukkkan sistem referensi (1-3) = "))

if pilih == 1:
  a, b, Ye, B1, B2 = grs80()
elif pilih == 2:
  a, b, Ye, B1, B2 = inter()
elif pilih == 3:
  a, b, Ye, B1, B2 = grs67()
else:
  print("\nSistem referensi tidak dipilih")

jml = int(input("anda ingin menghitung berapa lintang ? "))
i = 0
n = 0
hasil1 = []
hasil2 = []
hasil3 = []
hasil4 = []

while i < jml:
  i+=1
  n+=1
  print("\nLintang titik", i)
  lintang = x()

  print("ketinggian titik", i)
  tinggi = h()

  m = gravitasi(lintang, tinggi)
  hasil1.append(m)

  n = sentrifugal(lintang, tinggi)
  hasil2.append(n)

  o = berat(lintang, tinggi)
  hasil3.append(o)

  p = beratnormal(lintang)
  hasil4.append(p)

print("\nHasil perhitungan :")

j = 0
for q in hasil1:
  j+=1
  print("nilai gaya gravitasi lintang ke", j, "=", q)

v = 0
for q in hasil2:
  v+=1
  print("nilai gaya sentrifugal ke", v, "=", q)

z = 0
for q in hasil3:
  z+=1
  print("nilai gaya berat ke", z, "=", q)

r = 0
for q in hasil4:
  r+=1
  print("nilai gaya berat normal ke",r, "=", q)
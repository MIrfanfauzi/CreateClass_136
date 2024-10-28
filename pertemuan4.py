class persegipanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def keliling (self):
        return 2*(self.p +self.l)

    def luas (self):
        return self.p * self.l
            
    def __str__(self):
        return f"persegipanjang, p {self.p} cm, l {self.l} cm)"
    

try: 
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))

    if p <= 0 or l <= 0:
        raise ValueError("Panjang atau Lebar harus bernilai positif")

    pp = persegipanjang(p,l)
    print ("Kelilingnya adalah ", pp.keliling(), "cm")
    print ("Luasnya adalah ", pp.luas(), "cm²")

except ValueError as q:
    print(q)
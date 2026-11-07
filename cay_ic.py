#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Çay İçme Makinesi
Her yudumda hayatın anlamını sorgular.
"""

import random
import time

def cay_ic(yudum_sayisi=5):
    sikayetler = [
        "Bu çay da benden önce var mıydı?",
        "Yudum aldım, evrenin anlamsızlığı arttı.",
        "Şeker atsam mı, atmasam mı? Bu soru beni yedi.",
        "Çay soğudu, tıpkı hayallerim gibi.",
        "Bir yudum daha, bir varoluş krizi daha.",
        "Demlik neden ben değil?",
        "Bu kadar çay içmek normal mi yoksa ben mi normal değilim?",
        "Yudum yudum ölüyoruz aslında."
    ]
    
    print("🍵 Çay makinesi çalışıyor... Varoluş modu aktif.")
    time.sleep(1)
    
    for i in range(yudum_sayisi):
        sikayet = random.choice(sikayetler)
        print(f"Yudum {i+1}: {sikayet}")
        time.sleep(0.8)
    
    print("\n✅ Çay bitti. Hayat devam ediyor mu? Bilmiyorum.")
    # Gizli not: bazen sistemler de soğur.

if __name__ == "__main__":
    cay_ic()

def talaba_bahosi(ism, fanlar):
    """
    fanlar -> lug'at (dict)
    masalan: {"Matematika": 90, "Fizika": 80}
    """
    jami = 0
    soni = 0

    for fan, baho in fanlar.items():
        print(f"{fan} fanidan baho: {baho}")
        jami += baho
        soni += 1

    orta_baho = jami / soni

    if orta_baho >= 86:
        natija = "A'lo"
    elif orta_baho >= 71:
        natija = "Yaxshi"
    else:
        natija = "Qoniqarli"

    return ism, orta_baho, natija


fanlar = {
    "Matematika": 90,
    "Fizika": 85,
    "Informatika": 95
}

ism, orta, natija = talaba_bahosi("Ali", fanlar)
print(f"\n{ism} ning o'rtacha bahosi: {orta}")
print(f"Natija: {natija}")

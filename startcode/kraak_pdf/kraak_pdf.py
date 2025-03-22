import pikepdf
from tqdm import tqdm
herhaalWachtwoordRadenZ = (0)
herhaalWachtwoordRadenO = (0)
passwords = []
for wachtwoord in open("woorden.text"):
    passwords.append(wachtwoord.strip())

for wachtwoord in tqdm(passwords):
    try:
        pikepdf.open("hacking.pdf", password=wachtwoord)
        print("Het gevonden wachtwoord is:", wachtwoord)
        break
    except:
        pass





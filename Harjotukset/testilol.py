from colorama import Fore, Back, Style
import time

teksti = '''Trapped in purgatory
A lifeless object, alive
Awaiting reprisal
Death will be their acquittance
The sky is turning red
Return to power draws near
Fall into me, the sky's crimson tears
Abolish the rules made of stone
Pierced from below, souls of my treacherous past
Betrayed by many, now ornaments dripping above
Awaiting the hour of reprisal
Your time slips away'''

nopeus = 0.01  # sekunteina per kirjain

for kirjain in teksti:
    print(kirjain, end='', flush=True)
    time.sleep(nopeus)
print()
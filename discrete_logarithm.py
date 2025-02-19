import argparse

def discrete_logarithm(base, exponent, modulo):
    """
    Calcola il logaritmo discreto di 'exponent' in base 'base' modulo 'modulo'.
    Utilizza la semplificazione se 'exponent' è una potenza di 'base',
    altrimenti usa la forza bruta.
    """

    # Prova la semplificazione (potenza di base)
    power = 0
    temp = 1
    while temp < exponent:
        temp *= base
        power += 1

    if temp == exponent:
        return power

    # Se la semplificazione non funziona, prova la forza bruta
    for x in range(1, modulo):
        if pow(base, x, modulo) == exponent: # EXTREMELY SLOW FOR BIG NUMBERS!!! 
            return x

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calcola il logaritmo discreto.")
    parser.add_argument("-m", "--modulo", type=int, required=True, help="Il modulo.")
    parser.add_argument("-b", "--base", type=int, required=True, help="La base.")
    parser.add_argument("-e", "--exponent", type=int, required=True, help="L'esponente.")

    args = parser.parse_args()

    result = discrete_logarithm(args.base, args.exponent, args.modulo)

    if result is not None:
        print(f"Il logaritmo discreto di {args.exponent} in base {args.base} (mod {args.modulo}) è: {result}")
    else:
        print("Logaritmo discreto non trovato.")

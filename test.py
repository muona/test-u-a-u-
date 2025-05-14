def laskuri():
    laskuri = 2
    print("Yksinkertainen laskuri. Paina Enter lisätäksesi. Kirjoita 'q' lopettaaksesi.")
    
    while True:
        komento = input("> ")
        if komento.lower() == 'q':
            print("Lopetetaan laskuri.")
            break
        print(f"Luku: {laskuri}")
        laskuri += 1

if __name__ == "__main__":
    laskuri()



def cToFConverter():
    while True:
        cTemp = input("please enter C degree: ")
        if cTemp:
            cTemp = float(cTemp)
            fTemp = round(9*cTemp/5 + 32, 1)

            print(f"{cTemp}C is converted to {fTemp}F")
            break
        else:
            print("cTemp is empty")
            continue


def main():
    cToFConverter()

if __name__ == "__main__":
    main()
with open("data/UNIFOR_sample.txt", "r", encoding="utf-8") as arquivo:
    count = 0

    for linha in arquivo:
        count += 1
        
    print(count)
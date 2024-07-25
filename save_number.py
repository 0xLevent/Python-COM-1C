# save_number.py
def save_number(number):
    with open("numbers.txt", "a") as file:
        file.write(f"{number}\n")

if __name__ == "__main__":
    number = input("Bir sayı giriniz: ")
    save_number(number)
    print("Sayı kaydedildi.")

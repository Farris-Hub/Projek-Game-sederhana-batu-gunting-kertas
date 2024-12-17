# Game Sederhana: Batu, Gunting, Kertas
import random

def main():
    print("\nSelamat datang di permainan Batu, Gunting, Kertas!")
    pilihan = ["batu", "gunting", "kertas"]

    while True:
        print("\nPilih salah satu:")
        print("1. Batu")
        print("2. Gunting")
        print("3. Kertas")
        print("4. Keluar")

        user_input = input("Masukkan pilihan Anda (1-4): ")
        if user_input == "4":
            print("Terima kasih telah bermain. Sampai jumpa!")
            break

        if user_input not in ["1", "2", "3"]:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        user_choice = pilihan[int(user_input) - 1]
        computer_choice = random.choice(pilihan)

        print(f"Anda memilih: {user_choice}")
        print(f"Komputer memilih: {computer_choice}")

        if user_choice == computer_choice:
            print("Hasil: Seri!")
        elif (user_choice == "batu" and computer_choice == "gunting") or \
             (user_choice == "gunting" and computer_choice == "kertas") or \
             (user_choice == "kertas" and computer_choice == "batu"):
            print("Hasil: Anda menang!")
        else:
            print("Hasil: Anda kalah!")

if __name__ == "__main__":
    main()

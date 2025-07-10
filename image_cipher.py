from PIL import Image
import os
import time

# 🎨 Fun and Friendly Banner
def banner():
    print("\033[95m")  # Light magenta
    print("╔════════════════════════════════════════════════╗")
    print("║ ✨ Welcome to Kikile's Image Cipher Studio ✨ ║")
    print("╚════════════════════════════════════════════════╝")
    print("\033[0m")

# 🖼️ Encrypt Image by Swapping Pixels and Inverting Colors

def encrypt_image(input_path, output_path):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]

            if len(pixel) == 3:
                r, g, b = pixel
                pixels[x, y] = (255 - b, 255 - r, 255 - g)  # swap + invert
            elif len(pixel) == 4:
                r, g, b, a = pixel
                pixels[x, y] = (255 - b, 255 - r, 255 - g, a)

    image.save(output_path)
    print(f"✅ Encrypted image saved as {output_path}")

# 🔓 Decrypt by Applying the Same Logic Again (reversible)
def decrypt_image(input_path, output_path):
    encrypt_image(input_path, output_path)
    print(f"🔓 Decrypted image saved as {output_path}")

# 💫 Fancy typing effect

def fancy_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# 🧠 Main Program

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    fancy_print("🔐 Let's play with pixels and protect your pics!\n")

    choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").strip().upper()

    input_file = input("📂 Enter image filename (e.g., test_image.png): ").strip()
    if not os.path.exists(input_file):
        fancy_print("❌ File does not exist. Please check the name and try again.")
        return

    output_file = "output_" + input_file

    if choice == 'E':
        fancy_print("✨ Encrypting your image... 🧪", 0.04)
        encrypt_image(input_file, output_file)
    elif choice == 'D':
        fancy_print("🔁 Decrypting the encrypted pixels...", 0.04)
        decrypt_image(input_file, output_file)
    else:
        fancy_print("❗ Invalid option. Please choose E or D.")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
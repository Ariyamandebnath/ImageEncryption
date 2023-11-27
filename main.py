import time
from PIL import Image

def pixel_swap(i, abs_height, abs_width, pix):
    n = abs_width // 2
    temp = 1
    for k in range(i, abs_height - 1):
        if k >= (i + abs_height) // 2:
            temp = 0
        for j in range(n):
            if temp:
                pix[k, j], pix[k + (abs_height - i) // 2 + (abs_height - i) % 2, j + n + abs_width % 2] = \
                    pix[k + (abs_height - i) // 2 + (abs_height - i) % 2, j + n + abs_width % 2], pix[k, j]
            else:
                pix[k, j], pix[k - (abs_height - i) // 2 + (abs_height - i) % 2, j + n + abs_width % 2] = \
                    pix[k - (abs_height - i) // 2 + (abs_height - i) % 2, j + n + abs_width % 2], pix[k, j]

def encrypt_decrypt_image(image_path, key):
    img = Image.open(image_path)
    img.save("original.png")

    pix = img.load()
    abs_height, abs_width = img.size
    height, width = (abs_height // key) * key, (abs_width // key) * key

    # Encryption
    print("Encryption process...")
    temp = 0
    for i in range(height):
        if i % (abs_height // key) == 0:
            temp = 0 if temp else 1
        if i + abs_height // key >= height:
            pixel_swap(i, abs_height, width, pix)
            break
        for j in range(width // 2):
            if temp:
                pix[i, j], pix[i + height // key, j + width // 2 + width % 2] = \
                    pix[i + height // key, j + width // 2 + width % 2], pix[i, j]
            else:
                pix[i, j], pix[i - height // key, j + width // 2 + width % 2] = \
                    pix[i - height // key, j + width // 2 + width % 2], pix[i, j]

    img.save("encrypted_image.png")
    print("Encryption successful.")

    # Decryption
    print("\nDecryption process...")
    temp = 0
    for i in range(height):
        if i % (abs_height // key) == 0:
            temp = 0 if temp else 1
        if i + abs_height // key >= height:
            pixel_swap(i, abs_height, width, pix)
            break
        for j in range(width // 2):
            if temp:
                pix[i, j], pix[i + height // key, j + width // 2 + width % 2] = \
                    pix[i + height // key, j + width // 2 + width % 2], pix[i, j]
            else:
                pix[i, j], pix[i - height // key, j + width // 2 + width % 2] = \
                    pix[i - height // key, j + width // 2 + width % 2], pix[i, j]

    img.save("decrypted_image.png")
    print("Decryption successful.")

if __name__ == "__main__":
    # Enter the image file path
    path = input("Enter the path of the image: ").strip()
    path = r'{}'.format(path)
    key = 125

    start_time = time.time()

    # Encrypt and Decrypt the image
    encrypt_decrypt_image(path, key)

    end_time = time.time()
    print("\nEncryption and Decryption done in {:.4f} seconds".format(end_time - start_time))

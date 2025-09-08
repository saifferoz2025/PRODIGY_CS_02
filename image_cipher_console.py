from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key):
    # Open image and convert to numpy array
    img = Image.open(input_path)
    img_array = np.array(img)

    # XOR pixel values with the key
    encrypted_array = img_array ^ key

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)

def main():
    print("=== Image Encryption Tool (Pixel Manipulation) ===")
    input_file = input("Enter image filename (with extension): ")
    output_file = input("Enter output filename: ")
    key = int(input("Enter encryption key (0-255): "))

    encrypt_decrypt_image(input_file, output_file, key)
    print(f"✅ Operation successful! Saved as {output_file}")

if __name__ == "__main__":
    main()
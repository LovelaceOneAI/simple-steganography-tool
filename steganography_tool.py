from PIL import Image

def hide_message(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(c), '08b') for c in message) + '1111111111111110'
    pixels = img.load()
    
    idx = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if idx < len(binary_message):
                r, g, b = pixels[i, j]
                r = (r & ~1) | int(binary_message[idx])
                pixels[i, j] = (r, g, b)
                idx += 1
    img.save(output_path)

def extract_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    
    bits = ""
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            bits += str(r & 1)
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    message = ""
    for c in chars:
        if c == '11111110':  # End-of-message signature
            break
        message += chr(int(c, 2))
    return message

if __name__ == "__main__":
    choice = input("(h)ide or (e)xtract: ").lower()
    if choice == 'h':
        img = input("Image path: ")
        msg = input("Message: ")
        out = input("Output image path: ")
        hide_message(img, msg, out)
        print("✅ Message hidden.")
    elif choice == 'e':
        img = input("Image path to extract from: ")
        secret = extract_message(img)
        print(f"🔍 Hidden message: {secret}")

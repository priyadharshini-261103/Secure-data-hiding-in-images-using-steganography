from PIL import Image
import numpy as np
import hashlib

def encrypt_image(input_path, output_path, message, password):
    image = Image.open(input_path)

    # Ensure RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    pixels = np.array(image)

    # Hash the password securely
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    secret_message = f"{password_hash}|END|{message}|END|"

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)

    # Append a unique terminator to mark message end
    binary_message += '1111111111111110'

    # Check if the message fits in the image
    if len(binary_message) > pixels.size * 3:
        raise ValueError("Message is too large for this image.")

    # Encode message in the image using LSB
    idx = 0
    for row in pixels:
        for pixel in row:
            for channel in range(3):  # Iterate over RGB channels
                if idx < len(binary_message):
                    pixel[channel] = (pixel[channel] & ~1) | int(binary_message[idx])
                    idx += 1
                else:
                    break
            if idx >= len(binary_message):
                break
        if idx >= len(binary_message):
            break

    # Save encrypted image in lossless format (PNG)
    encrypted_image = Image.fromarray(pixels)
    encrypted_image.save(output_path, format='PNG')

    print(f"✅ Image encrypted and saved to: {output_path}")

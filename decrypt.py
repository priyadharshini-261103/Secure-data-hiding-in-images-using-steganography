from PIL import Image
import numpy as np
import hashlib

def decrypt_image(image_path, password):
    image = Image.open(image_path)

    # Ensure RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    pixels = np.array(image)

    # Extract binary message from LSB
    binary_message = ''.join(str(pixel[channel] & 1) for row in pixels for pixel in row for channel in range(3))

    # Locate the stopping point using the 16-bit terminator
    end_marker_bin = '1111111111111110'
    end_idx = binary_message.find(end_marker_bin)

    if end_idx == -1:
        return "Error: No valid message found."

    # Extract the actual message up to the terminator
    binary_message = binary_message[:end_idx]

    # Convert binary to ASCII characters
    message_bits = [binary_message[i:i + 8] for i in range(0, len(binary_message), 8)]
    message = ''.join(chr(int(byte, 2)) for byte in message_bits)

    print(f"🔍 Debug: Extracted Message: {message}")

    # Ensure the message format is correct
    if message.count("|END|") < 2:
        return "Error: Invalid or corrupted image."

    try:
        stored_hash, remaining_message = message.split("|END|", 1)
        extracted_message, _ = remaining_message.split("|END|", 1)
    except ValueError:
        return "Error: Message format mismatch."

    # Verify the password
    input_hash = hashlib.sha256(password.encode()).hexdigest()
    if stored_hash != input_hash:
        return "Error: Invalid password."

    return extracted_message.strip()  # Return decrypted message

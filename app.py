from flask import Flask, render_template, request, send_from_directory
import os
from encrypt import encrypt_image
from decrypt import decrypt_image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    encrypted_image = None
    decrypted_message = None
    error_message = None
    action = None

    if request.method == 'POST':
        action = request.form.get('action')
        image_file = request.files['image']
        password = request.form.get('password')

        if image_file and password:
            image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
            image_file.save(image_path)

            if action == 'encrypt':
                secret_message = request.form.get('message')
                output_image_name = 'encrypted_' + image_file.filename
                output_image_path = os.path.join(UPLOAD_FOLDER, output_image_name)
                
                try:
                    encrypt_image(image_path, output_image_path, secret_message, password)
                    message = "Image successfully encrypted."
                    encrypted_image = output_image_name
                except Exception as e:
                    error_message = f"Encryption Error: {str(e)}"

            elif action == 'decrypt':
                try:
                    decrypted_message = decrypt_image(image_path, password)
                    if not decrypted_message:
                        error_message = "Invalid password or no hidden message found."
                except Exception as e:
                    error_message = f"Decryption Error: {str(e)}"

    return render_template('index.html', 
                           action=action,
                           message=message, 
                           encrypted_image=encrypted_image, 
                           decrypted_message=decrypted_message, 
                           error_message=error_message)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

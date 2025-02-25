his project provides a web-based application for securely hiding secret messages in images using image steganography. The application uses a password to encrypt and decrypt messages embedded in images. Users can upload images, encrypt them with a secret message, and download the encrypted images. They can also decrypt encrypted images by providing the correct password.

Features
Encrypt a message in an image: Users can upload an image and embed a secret message using a passcode for encryption.
Decrypt a message from an encrypted image: Users can upload an encrypted image and retrieve the secret message by providing the correct passcode.
User-friendly interface: Simple forms for image upload, message input, and passcode entry.
Requirements
Python 3.8+
Flask 2.3.2
Pillow 9.4.0
numpy 1.23.5
Installation
Clone the repository:

bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
Create a virtual environment and activate it:

For macOS/Linux:

bash
python3 -m venv venv
source venv/bin/activate
For Windows:

bash
python -m venv venv
.\venv\Scripts\activate
Install the required dependencies:

bash
pip install -r requirements.txt
Usage
Running the app locally
Run the Flask app:

bash
python app.py
Open your browser and visit http://127.0.0.1:5000 to access the application.

Deploying to Render
This app is deployed on Render. you can access it through the live URL: https://secure-data-hiding-in-images-using.onrender.com/ 

How It Works
Encrypting an Image
Upload an image.
Enter the secret message you want to hide.
Set a passcode (this will be used to encrypt and decrypt the message).
Click "Encrypt Message" to generate the encrypted image.
Download the encrypted image.
Decrypting an Image
Upload the encrypted image.
Enter the passcode used during encryption.
Click "Decrypt Message" to reveal the hidden message.

File Structure
app.py: The main Flask application file.
encrypt.py: Contains the logic for encrypting the message in the image.
decrypt.py: Contains the logic for decrypting the message from the image.
templates/: Contains HTML files for rendering the app (e.g., index.html).
static/: Contains static files like stylesheets and scripts (e.g., styles.css, script.js).
requirements.txt: Lists the dependencies for the project.

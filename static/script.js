// script.js

document.addEventListener('DOMContentLoaded', () => {
    const encryptForm = document.getElementById('encryptForm');
    const decryptForm = document.getElementById('decryptForm');
    const output = document.getElementById('output');

    // Encrypt Form Validation
    encryptForm.addEventListener('submit', (e) => {
        const image = document.getElementById('imageInput').files[0];
        const message = document.getElementById('messageInput').value.trim();
        const password = document.getElementById('passwordInput').value.trim();

        if (!image || !message || !password) {
            e.preventDefault();
            alert('All fields are required for encryption.');
        } else {
            output.textContent = "Encrypting the image... Please wait.";
        }
    });

    // Decrypt Form Validation
    decryptForm.addEventListener('submit', (e) => {
        const image = document.getElementById('decryptImage').files[0];
        const password = document.getElementById('decryptPassword').value.trim();

        if (!image || !password) {
            e.preventDefault();
            alert('Both image and password are required for decryption.');
        } else {
            output.textContent = "Decrypting the image... Please wait.";
        }
    });
});

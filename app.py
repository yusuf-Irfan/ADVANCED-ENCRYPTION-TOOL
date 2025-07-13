from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os, io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def derive_key(password, salt):
    return PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    ).derive(password.encode())

def encrypt_file(file_data, password):
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()
    return salt + iv + encrypted_data

def decrypt_file(file_data, password):
    salt = file_data[:16]
    iv = file_data[16:32]
    encrypted = file_data[32:]
    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted) + decryptor.finalize()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        password = request.form["password"]
        action = request.form["action"]

        if not file or not password:
            return "❌ File or password missing", 400

        filename = secure_filename(file.filename)
        file_data = file.read()

        try:
            if action == "encrypt":
                result = encrypt_file(file_data, password)
                output_name = filename + ".enc"
            else:
                result = decrypt_file(file_data, password)
                output_name = filename.replace(".enc", ".dec")

            return send_file(
                io.BytesIO(result),
                as_attachment=True,
                download_name=output_name
            )
        except Exception as e:
            return f"❌ Error: {str(e)}", 500

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

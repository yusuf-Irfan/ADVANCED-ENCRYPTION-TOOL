# ADVANCED-ENCRYPTION-TOOL

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: YUSUF IRFAN M

*INTERN ID*: CT04DH428

*DOMAIN*: CYBERSECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*Project Overview*

--> This task is a file encryption and decryption web tool built using Python and Flask.

--> It allows users to securely encrypt or decrypt files using the AES-256 algorithm, one of the strongest encryption standards.

--> The application runs on a local web server and can handle all file types such as .pdf, .txt, .jpg, and more.

--> The tool was built as part of an internship assignment and was fully developed and tested using Visual Studio Code.

*Tools and Technologies Used*

Python – Core programming language for backend logic and encryption

Flask – Python-based lightweight web framework to build the user interface

Cryptography Library – For implementing AES-256 encryption and secure password handling

PBKDF2HMAC – For deriving a strong encryption key from the password using salt and multiple iterations

HTML & CSS – Used for the front-end user interface (file input, password input, buttons)

VS Code – Code editor used to develop and test the application

Browser (Google Chrome) – Used to run and interact with the tool

*How AES-256 Encryption Works in the Tool*

--> AES stands for Advanced Encryption Standard, and AES-256 means it uses a 256-bit encryption key for high-level security.

--> The tool uses CFB (Cipher Feedback) mode, which supports encryption of files of any size and allows for secure streaming.

--> For every encryption:

    1. A random salt (16 bytes) is generated

    2.A random Initialization Vector (IV) is generated

    3.A secure encryption key is derived from the user’s password using PBKDF2HMAC

    4.The final encrypted file contains: salt + IV + ciphertext

--> During decryption, the salt and IV are extracted from the file, and the key is regenerated using the same password to decrypt the original content.

*How the Tool Works*

--> User opens the app in their browser at http://127.0.0.1:5000 by running app.py in VS Code.

--> User selects a file using the "Choose File" button.

--> User enters a password (any string of their choice).

--> They choose one of two actions:

   1. Encrypt → Generates a .enc file

   2.Decrypt → Restores original file with .dec extension


--> The backend reads the uploaded file in binary, encrypts or decrypts it, and returns the processed file for download.

*Features of the Tool*

--> Works with any file type: text, image, audio, video, PDF, etc.

--> No terminal knowledge required – fully browser-based interface

--> Automatically handles file naming with .enc and .dec extensions

--> Prevents data leakage or misuse by strongly locking the file content

--> Each encryption is unique due to random IV and salt, even with the same file and password

--> Easy to use for both beginners and non-tech users

*Learning Outcomes and Benefits*

--> Gained strong hands-on knowledge of cryptographic principles like AES, IV, salt, and key derivation

--> Learned full-stack development using Python, Flask, HTML, and browser integration

--> Understood secure file handling, password-based protection, and encryption logic

--> Created a working tool that is both practical and industry-relevant, especially in fields like cybersecurity and data privacy

--> Strengthened problem-solving, testing, and debugging skills while handling real files (like PDFs containing study material


Tool Overview:

This tool is a Python-based security utility designed to encrypt and decrypt files using the AES-256 (Advanced Encryption Standard with 256-bit key) encryption algorithm.

It ensures high-level data confidentiality and is ideal for securing sensitive files from unauthorized access.

The tool can be operated via a simple command-line interface (CLI) or integrated into larger applications.


Security Features:

Symmetric Encryption: Same key is used for both encryption and decryption.

Key Derivation: Uses a password-based key derivation function (PBKDF2) to securely generate the key from user input.

Random Salt & IV: Each encryption generates a random salt and initialization vector (IV) to prevent pattern recognition and replay attacks.

Secure Storage: Encrypted files store the salt and IV prepended, so decryption can be done later even on different systems.


File Support:

Can encrypt and decrypt any file type including text files, images, PDFs, and even executable files.

Supports both small and large files, with no size restrictions other than system memory limits.



Technical Stack:

Language: Python 3

Libraries Used:

cryptography: for AES encryption operations.

hashlib: for hashing and key derivation.

os: for file operations and secure random number generation.

base64: for encoding and decoding key data.

getpass: for securely receiving passwords without displaying on screen.




User Inputs:

Password: The user provides a strong password which is not stored anywhere, used to generate a secure key.

File Path: The path to the file that needs to be encrypted or decrypted.

Operation Mode: User can choose between 'Encrypt' or 'Decrypt'.



Workflow:

Encryption Process:

1. User provides the target file and a password.


2. A salt and IV are generated using a secure random function.


3. The key is derived using PBKDF2 with the salt.


4. The file content is encrypted using AES in CBC mode.


5. The salt, IV, and ciphertext are combined and saved as a new encrypted file.



Decryption Process:

1. The tool extracts salt and IV from the encrypted file.


2. It re-derives the key using the password and extracted salt.


3. AES decrypts the content using the key and IV.


4. Decrypted content is saved as the original file.





Output Files:

Encrypted files typically have an extension like .enc or .aes.

Decrypted files are restored to their original format and file name.



Use Cases:

Protect confidential documents (e.g., financial records, legal files).

Secure personal information on shared or cloud systems.

Send encrypted files via email or USB drive safely.

Use in penetration testing or cybersecurity learning projects.



Benefits:

High-grade security using AES-256.

Offline usage, no internet required.

Cross-platform, works on Windows, Linux, and macOS.

Simple interface, ideal for both beginners and professionals.

Open-source, customizable for different use cases.


*OUTPUT*

"https://github.com/user-attachments/assets/37757eef-cff5-4489-897f-aa2291fce421" />

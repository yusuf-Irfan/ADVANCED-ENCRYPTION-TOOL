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

*OUTPUT*

"https://github.com/user-attachments/assets/37757eef-cff5-4489-897f-aa2291fce421" />

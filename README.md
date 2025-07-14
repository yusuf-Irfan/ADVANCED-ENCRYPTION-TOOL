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


Tools & Technologies Used:

1. Python 3.10+:

Used for the core development of the tool due to its simplicity, readability, and mature cryptographic libraries.



2. VS Code (Visual Studio Code):

IDE used to write, structure, debug, and test the encryption tool efficiently.



3. Cryptography Library (cryptography):

Provided secure cryptographic primitives, including AES encryption using CBC mode with PKCS7 padding.

Offered robust features for key derivation (Fernet, PBKDF2HMAC), IV generation, and secure encryption workflows.



4. Base64 Encoding/Decoding:

Used to safely convert encrypted binary data into ASCII format for storage or transmission.



5. Operating System Libraries (os, secrets):

For secure random key/IV generation and file path operations.



6. Command-Line Interface (CLI):

Allowed users to input commands such as encryption, decryption, key generation, and file path selection directly through terminal prompts.



Features Implemented:

1. AES-256 Encryption:

Implemented using 256-bit symmetric keys.

Data is encrypted in CBC (Cipher Block Chaining) mode for improved security.

Each encryption session generates a unique Initialization Vector (IV) to ensure that the same plaintext encrypts differently every time.



2. Decryption Module:

Safely reverses the encryption process using the same AES-256 key and IV.

Includes error handling for incorrect keys, modified data, or unsupported formats.



3. Key Generation and Management:

Uses a secure random generator or password-based key derivation (PBKDF2HMAC) for key creation.

Stored keys in a safe format, either as hexadecimal or base64, for user readability.



4. File Encryption/Decryption:

Supports encryption and decryption of full files.

Processes files in blocks to handle large file sizes efficiently without memory overload.



5. Padding and Encoding:

Implemented PKCS7 padding to match block size requirements.

Used Base64 encoding for converting binary ciphertext into ASCII-compatible form.



6. User Interface (CLI):

Simple and interactive command-line interface with options to:

Encrypt text or file

Decrypt using a key

Generate secure AES key

Save/load encrypted files




Development Workflow:

1. Research & Planning:

Studied how AES-256 works and common encryption practices.

Understood the importance of secure key management and IV generation.



2. Building the Encryption Engine:

Defined modular functions for:

Key derivation

Padding/unpadding

Encrypting/decrypting bytes and files




3. Testing with Sample Inputs:

Verified encryption and decryption outputs for accuracy using the same key.

Conducted negative testing using wrong keys and tampered ciphertexts.



4. Security Considerations:

Used secrets module for strong entropy in IV and key generation.

Prevented reuse of IVs to avoid CBC-based vulnerabilities.

Avoided storing raw keys in code or logs.



5. Code Structure and Documentation:

Split the code into clean modules for readability.

Included docstrings and inline comments for clarity.

Added error messages and logs for debugging and user feedback.



Use Cases:

Secure file sharing between users in encrypted form.

Data protection for sensitive documents on cloud or external drives.

Messaging applications requiring encrypted communications.

Compliance with data protection policies (e.g., GDPR, HIPAA).



Key Takeaways:

Gained hands-on experience with real-world cryptographic standards (AES-256).

Learned the importance of secure key management, IV usage, and data encoding.

Understood vulnerabilities in weak implementations and how to defend against them.

Strengthened skills in modular programming, CLI tools, and secure Python coding.

Recognized the critical role of encryption in cybersecurity, especially in industries such as finance, healthcare, and IT infrastructure.



*OUTPUT*

"https://github.com/user-attachments/assets/37757eef-cff5-4489-897f-aa2291fce421" />

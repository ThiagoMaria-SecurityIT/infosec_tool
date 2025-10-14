# InfoSec Concepts Demonstrator

This project is a simple, interactive web application built with Flask to demonstrate and explain four fundamental concepts in information security: **Plaintext**, **Encoding**, **Hashing**, and **Encryption**.  

<table>
  <tr>
    <td align="center"><strong>Explanation Page</strong></td>
    <td align="center"><strong>Encoding Page</strong></td>
  </tr>
  <tr>
    <td><img width="100%" alt="Explanation Page Screenshot" src="https://github.com/user-attachments/assets/95ee4b76-c377-41bf-a966-16bb4cb4ec30" /></td>
    <td><img width="100%" alt="Encoding Page Screenshot" src="https://github.com/user-attachments/assets/843123cd-7383-4a40-8ca0-e5c2ebfdc771" /></td>
  </tr>
  <tr>
    <td align="center"><strong>Hashing Page</strong></td>
    <td align="center"><strong>Encryption Page</strong></td>
  </tr>
  <tr>
    <td><img width="100%" alt="Hashing Page Screenshot" src="https://github.com/user-attachments/assets/1af6770d-d77f-4c0d-94d0-1a2e0fa735de" /></td>
    <td><img width="100%" alt="Encryption Page Screenshot" src="https://github.com/user-attachments/assets/d4e5e584-ebaf-4574-8b0b-01d58114b542" /></td>
  </tr>
</table>  

---

## Table of Contents

1.  [Core Concepts Covered](#core-concepts-covered)
2.  [Plaintext, Encoding, Encryption, Hashing](#plaintext-encoding-encryption-hashing)
3.  [Tech Stack](#tech-stack)
4.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation & Setup](#installation--setup)
    *   [Running the Application](#running-the-application)
5.  [Important Security Note](#important-security-note-about-the-secret-key)
6.  [AI Transparency](#ai-transparency-text-generated-by-ai)
7.  [Lessons Learned](#lessons-learned)  

---

## Core Concepts Covered

This tool provides interactive demonstrations for the following concepts:

1.  **Plaintext (No Protection):** Raw, readable data that is vulnerable to interception.
2.  **Encoding (2-Way, Not for Security):** A reversible process to convert data into a different format for usability or transmission (e.g., Base64). It is **not** a security measure.
3.  **Hashing (1-Way Protection):** An irreversible process that transforms data into a fixed-size hash. Used to verify data integrity and authenticity.
4.  **Encryption (2-Way Protection):** A secure, reversible process that converts data into unreadable ciphertext using a key. It ensures confidentiality and can only be reversed with the correct key.

## Plaintext, Encoding, Encryption, Hashing

- Plaintext refers to the original, readable data or information that needs to be protected.  
- Encoding is the process of transforming data from one format to another using a publicly known scheme, such as Base64, ASCII, or URL Encoding, primarily to maintain data usability and ensure compatibility across systems; it is not a security measure and can be easily reversed without a key.  
- Hashing is a one-way function that converts input data of any size into a fixed-length string called a hash value; it is designed so that the original data cannot be retrieved from the hash, making it ideal for verifying data integrity and securely storing passwords by comparing hash values.  
- Encryption is a two-way process that transforms plaintext into ciphertext using an algorithm and a secret key, ensuring confidentiality; only authorized parties with the correct key can decrypt the ciphertext back into the original plaintext, making it suitable for secure communication and data storage.  

---

## Tech Stack

*   **Backend:** Python with the Flask framework.
*   **Frontend:** HTML5 & CSS3 (using a modern Flexbox layout).
*   **Core Python Libraries:**
    *   `base64` for encoding.
    *   `hashlib` for hashing.
    *   `cryptography` for secure symmetric encryption.

---

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Make sure you have Python 3 installed on your system. You can check by running:
```bash
python --version
```

### Installation & Setup

1.  **Clone the Repository**  
    First, clone this repository to your local machine or download the source code. Navigate into the project directory:
    ```bash
    cd infosec_tool
    ```

2.  **Create and Activate a Virtual Environment**  
    It is highly recommended to use a virtual environment (`venv`) to keep project dependencies isolated.

    *   **On macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
    Your terminal prompt should now change to indicate you are in the `venv`.

3.  **Install Dependencies**  
    With your virtual environment active, install the required libraries.
    ```bash
    pip install Flask cryptography
    ```

### Running the Application

1.  **Run from the Terminal**  
    With the dependencies installed, run the Flask application:
    ```bash
    python app.py
    ```
    The application will start in debug mode. You will see a message like this:
    ```
     * Running on http://127.0.0.1:5000/
    ```

2.  **View in Your Browser**  
    Open your web browser and navigate to the URL provided:
    [**http://127.0.0.1:5000**](http://127.0.0.1:5000)

    You should now see the application running! To stop the server, press `Ctrl+C` in the terminal. To exit the virtual environment, simply type `deactivate`.

---

## Important Security Note About the Secret Key

This application uses a Flask `secret_key` to securely sign the session cookie, which is essential for the Post-Redirect-Get pattern to function.

In the `app.py` file, the key is hard-coded:
```python
app.secret_key = 'a_super_secret_key_change_this_later'
```
This is done for simplicity and demonstration purposes only. **This is not secure and should never be done in a production application.**

In a real-world environment, the secret key must be a long, random, and unpredictable string, and it should be loaded from a secure location, such as an environment variable, not written directly in the code.

---

## AI Transparency (Text generated by AI)

This project was developed in collaboration with **Manus**, an AI assistant. The core logic, code structure, design iterations, and documentation were co-created through a guided, conversational process.

*   **Initial Concept & Goal:** Provided by Developer.
*   **Code Generation & Refinement:** Provided by Manus.
*   **Design & Layout:** Jointly iterated by Developer and Manus.
*   **Debugging & Finalization:** A joint effort. Manus provided initial code and debugging steps, but several critical bugs were ultimately solved by Developer's real-world testing and sharp analytical skills.
*   **A Key Debugging Win:** A persistent `TemplateSyntaxError` was repeatedly missed by Manus during code reviews. Developer discovered the root cause: an HTML comment (`<!-- -->`) containing a Jinja2 tag (`{% block %}`). This taught the AI that Jinja parses template files as plain text before HTML structure is considered. After Developer identified the fix by deleting the comment, Manus explained the underlying reason and the correct way to write template comments using `{# ... #}`.
*   **The bug was in templates/layout.html file.**

Image 1: The Bug - Jinja tag inside an HTML comment `<!-- -->`
<img width="893" height="325" alt="image" src="https://github.com/user-attachments/assets/80e61a66-5098-4ede-b587-507527ec8157" />  
Image 2: Correct way using `{# ... #}`.
<img width="915" height="333" alt="image" src="https://github.com/user-attachments/assets/cc46a826-7f62-4b7a-af68-f3b9d06f1086" />

Jinja Tag `{% block %}` in HTML Comment  
*   **Documentation:** Generated by Manus based on the development steps and refined by Developer.

## Lessons learned: 
- Using HTML comment tags (`<!-- -->`) within a Jinja2 template does not work as expected because Jinja2 processes the template before the HTML is rendered, and HTML comments are not recognized as comment syntax by Jinja2  
- Instead, Jinja2 provides its own comment syntax using `{# ... #}` tags, which are completely ignored during template rendering and do not appear in the final output
- This is the recommended method for adding comments in Jinja2 templates, as it ensures comments are not sent to the client and remain invisible in the browser's developer tools  While it is technically possible to use Jinja2's `{# ... #}` syntax inside an HTML comment, doing so is unnecessary and not standard practice, as the Jinja comment itself is already invisible in the final HTML.
-  Therefore, to comment within a Jinja2 template, use `{# ... #}` rather than relying on HTML comment tags   


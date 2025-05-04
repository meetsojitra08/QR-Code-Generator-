# QR-Code-Generator-
# 🌐 QR Code Generator (URL-Based) - Django Project

This is a Django-based web application that generates QR codes **only from valid URLs**.  
Just enter a website or resource URL, and instantly get a QR code that you can scan or download.

---

## 🚀 Features

- Accepts a URL and generates a QR code image
- Automatically names and saves the QR code image
- View and download the QR code
- Clean and responsive user interface

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** SQLite (Django default)
- **Libraries:**
  - `qrcode` – for QR code generation
  - `Pillow` – for image handling

---

## 📁 Project Structure

```
qr-code-django/
├── django_qr/              # Django app
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── models.py
│   └── ...
├── templates/              # HTML templates
├── media/                  # Saved QR code images
├── static/                 # Static files (CSS/JS)
├── manage.py
└── db.sqlite3
```

---

## 📦 Installation Guide

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/qr-code-django.git
   cd qr-code-django
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Visit in browser:**
   ```
   http://127.0.0.1:8000/
   ```

---

## 📝 How It Works

- Enter a valid URL in the form.
- The app generates a QR code pointing to that URL.
- The QR image is displayed and can be downloaded.

> ⚠️ Only valid URLs will work. If the input is not a proper URL, QR code generation will fail.

---

## 📌 Requirements

To manually create a `requirements.txt`:
```
Django>=3.2
qrcode
Pillow
```

Or generate it using:
```bash
pip freeze > requirements.txt
```

---

## 👨‍💻 Author

Developed by [Meet Sojitra]  
Open to contributions, suggestions, and improvements.


```markdown
# 🔐 Password Manager (Tkinter GUI)

A simple and secure desktop application to generate, store, and manage your passwords. Built with **Python**, **Tkinter**, and **ttkbootstrap** for a modern user interface.

---

## 💡 Features

- 🎨 Modern UI with `ttkbootstrap`
- 🔐 Secure local password storage using `pickle`
- 📋 Clipboard copy support with `pyperclip`
- 🔎 Search stored credentials by website
- 🔁 Random password generator
- ❌ Duplicate prevention and input validation

---

## 📦 Requirements

- Python 3.10 or higher
- `ttkbootstrap`
- `pyperclip`

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

### Option 1: Run with Python

```bash
python main.py
```

Make sure the following are in the same folder:
- `main.py`
- `logo.png` (image used in UI)
- `data.dat` (auto-created for storing credentials)

---

### Option 2: Run via `run.bat` (Windows)

To simplify launching on Windows, a `run.bat` file is provided.

#### ✅ Steps:

1. Double-click `run.bat`  
   *(or right-click → Run as administrator)*  
2. The Password Manager window will open.

#### 📝 Make sure:

- `run.bat`, `main.py`, and `logo.png` are in the **same folder**
- Python is installed and added to your **system PATH**

---

## 🔒 Data Security

All passwords are stored locally in a binary file `data.dat` using `pickle`. For better security, you may integrate encryption using libraries like `cryptography` in the future.

---

## ✨ Future Enhancements

- Add user login/authentication
- Encrypt password data
- Sync across devices or cloud storage
- Export/Import credentials
- Auto-fill browser integration

---

## 👨‍💻 Author

**Aman Sahu**

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
```

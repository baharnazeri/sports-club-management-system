# 🏋️ Gym Management System (CLI)

> A command-line based system for managing gym operations including user accounts, class reservations, payments, and trainer interactions.

---

## 🚀 Overview

This project is a **Gym Management System** implemented in Python using a **CSV-based data storage approach**.

It simulates real-world gym operations such as:

- User registration and authentication  
- Class scheduling and reservation  
- Wallet and payment system  
- Trainer recommendations (supplements & plans)  
- Reservation tracking and cancellation  

---

## 🎯 Features

### 👤 User Management
- Sign up / Login system  
- Password management  
- Account balance tracking  
- Membership validation  

### 💳 Wallet System
- Deposit & withdraw funds  
- Automatic membership activation  
- Billing and payment handling  

### 🏋️ Class Reservation
- Swimming  
- Aerobic  
- Bodybuilding  

Users can:
- View schedules  
- Reserve time slots  
- Cancel reservations  

---

## 📊 Data Storage

All data is stored using **CSV files**, including:

- `userss22.csv` → User accounts  
- `teacherss2.csv` → Trainers  
- `r_informations2.csv` → Reservations  
- `data_*.csv` → Class schedules  

---

## 👩‍🏫 Teacher System

- Teachers can:
  - Register and login  
  - Recommend supplements  
  - View user information  

---

## 💊 Supplement System

- Users can request supplement plans  
- Teachers provide recommendations  
- Purchases are deducted from wallet balance  

---

## 💰 Pricing

- Swimming: 450$  
- Aerobic: 270$  
- Bodybuilding: 600$  
- Supplement: 70–100$  
- Diet Plan: 200$  

---

## 🧠 System Design

The system is structured using object-oriented programming:

### Main Classes:
- `person` → User operations  
- `reserve` → Reservation handling  
- `teacher` → Trainer management  

---

## ⚙️ Technologies Used

- Python  
- CSV (as database)  
- Tabulate (for CLI tables)

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install tabulate
```

2. Run the program:
```bash
python main.py
```

---

## 📁 Project Structure

```
.
├── main.py                # Main system logic
├── userss22.csv          # Users database
├── teacherss2.csv        # Teachers database
├── r_informations2.csv   # Reservations data
├── data_swim*.csv        # Swimming schedules
├── data_aerobic*.csv     # Aerobic schedules
├── data_bodybulding*.csv # Bodybuilding schedules
└── README.md
```

---

## ⚠️ Limitations

- Uses CSV instead of a real database  
- No GUI (CLI-based only)  
- Limited input validation  
- Not optimized for concurrency  

---

## 🚀 Future Improvements

- Replace CSV with SQL database (MySQL/PostgreSQL)  
- Add GUI (PyQt / Web App)  
- Improve authentication security  
- Add REST API (Flask/Django)  
- Implement role-based access control  

---

## 📌 Key Concepts

- Object-Oriented Programming (OOP)  
- File Handling (CSV)  
- Basic System Design  
- State Management  
- CLI-based User Interaction  

---

## ⭐️ Notes

This project demonstrates:
- Practical system design  
- Real-world application modeling  
- Integration of multiple functionalities (auth, payment, scheduling)


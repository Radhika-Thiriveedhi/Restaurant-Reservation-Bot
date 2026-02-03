# 🍽️ Dining Reservation Chatbot (Console-Based)

A lightweight console-based chatbot for restaurant reservations with table optimization, waitlist management, menu/policy preview using ScaleDown compression, and SMS notifications (simulated). The bot runs continuously and exits on command.

---

## ✨ Features
- 🪑 Best-fit table booking  
- ⏳ Automatic waitlist handling  
- 📋 Menu & policy preview (ScaleDown)  
- 📩 SMS confirmations (simulated)  
- 📊 Reservations & waitlist dashboard  
- 🔁 Continuous chat until `exit`

---

## 🧰 Tech Stack
- Python 3  
- Terminal / Console

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed

### Run
```bash
python dining_chatbot.py
## Commands
menu    -> View menu & policy (compressed)
book    -> Book a table
status  -> View reservations & waitlist
exit    -> Exit the chatbot
## 🗂️ Project Structure
.
├── dining_chatbot.py
└── README.md
### 🧠 How It Works

Table Optimization: Assigns the smallest suitable table for each party.

Waitlist Manager: Adds users when tables are full.

ScaleDown: Compresses menu and policy text for faster responses.

SMS (Mock): Prints confirmation messages to the terminal.

## 📈 Future Enhancements

Real SMS integration (Twilio)

Web/WhatsApp interface

Auto-promotion from waitlist

Integration-ready adapters for OpenTable/Resy

Booking analytics & no-show metrics

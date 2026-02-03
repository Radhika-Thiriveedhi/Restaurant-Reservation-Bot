# dining_chatbot.py

TABLES = [2, 2, 4, 4, 6]
reservations = []
waitlist = []

MENU = "Paneer Biryani, Veg Meals, Chicken Curry, Butter Naan, Fresh Juices, Desserts"
POLICY = "Cancellations must be done 1 hour before reservation time to avoid penalty."


# -------- ScaleDown --------
def scaledown_text(text):
    words = text.split()
    keep = words[:max(5, len(words)//4)]
    return " ".join(keep) + "..."


# -------- SMS Mock --------
def send_sms(phone, message):
    print(f"\n[SMS SENT to {phone}] {message}\n")


# -------- Table Optimization --------
def find_best_table(party_size):
    suitable = [t for t in TABLES if t >= party_size]
    if suitable:
        return min(suitable)
    return None


# -------- Reservation Logic --------
def book_table(name, phone, party_size, time, dietary):
    table = find_best_table(party_size)

    if table:
        reservations.append({
            "name": name,
            "phone": phone,
            "party_size": party_size,
            "time": time,
            "dietary": dietary,
            "table": table,
            "status": "CONFIRMED"
        })
        send_sms(phone, f"Your table for {party_size} people at {time} is CONFIRMED.")
        return "Reservation confirmed"
    else:
        waitlist.append({
            "name": name,
            "phone": phone,
            "party_size": party_size,
            "time": time
        })
        send_sms(phone, "All tables full. You are added to WAITLIST.")
        return "Added to waitlist"


# -------- Dashboard --------
def show_dashboard():
    print("\n--- 📋 RESERVATIONS ---")
    if not reservations:
        print("No reservations yet.")
    for r in reservations:
        print(r)

    print("\n--- ⏳ WAITLIST ---")
    if not waitlist:
        print("Waitlist empty.")
    for w in waitlist:
        print(w)


# -------- Chatbot Loop --------
def chatbot():
    print("\n🍽️ Welcome to Dining Reservation Chatbot")
    print("Type 'menu' to see menu | 'book' to reserve | 'status' to view dashboard | 'exit' to quit")

    while True:
        user = input("\nYou: ").strip().lower()

        if user == "exit":
            print("Bot: Thanks for visiting! Bye 👋")
            break

        elif user == "menu":
            print("\nBot: Menu Preview (ScaleDown)")
            print(scaledown_text(MENU))
            print("\nBot: Policy Preview (ScaleDown)")
            print(scaledown_text(POLICY))

        elif user == "book":
            print("\nBot: Sure! Let me book a table for you.")
            name = input("Bot: Your name: ")
            phone = input("Bot: Phone number: ")
            party_size = int(input("Bot: Party size: "))
            time = input("Bot: Time (e.g., 7 PM): ")
            dietary = input("Bot: Dietary request (Veg/No nuts/etc): ")

            result = book_table(name, phone, party_size, time, dietary)
            print("Bot:", result)

        elif user == "status":
            show_dashboard()

        else:
            print("Bot: I can help with 'menu', 'book', 'status', or 'exit'.")


if __name__ == "__main__":
    chatbot()


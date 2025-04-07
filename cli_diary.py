from datetime import datetime
import os

# --- Greet the user ---
print("📓 Welcome to your diary!")
entry = input("Enter today’s thoughts: ")

# --- Get current datetime ---
now = datetime.now()
filename = f"{now.date()}.txt"
timestamp = now.strftime("[%Y-%m-%d %H:%M]")

# --- Save the entry ---
with open(filename, "a") as file:
    file.write(f"{timestamp}\n{entry}\n{'-'*40}\n")

print("✅ Your thoughts have been saved successfully!\n")

# --- Ask to read previous entries ---
read = input("Do you want to read your previous entries? (yes/no): ").lower()
if read == "yes":
    print("\n📝 Previous Entries:\n")
    with open(filename, "r") as file:
        lines = file.readlines()

    # Get the last 5 entries (each entry = 3 lines: timestamp, text, separator)
    entries = [lines[i:i+3] for i in range(0, len(lines), 3)]
    for entry in entries[-5:]:
        print("".join(entry))

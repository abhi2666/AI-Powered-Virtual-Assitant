import csv

# Read the text file
text_file = "dialogs.txt"
csv_file = "conversation.csv"

# Open the input text file and create the output CSV file
with open(text_file, "r") as file:
    lines = file.readlines()

# Preprocess the text and extract user and bot responses
conversations = []
for line in lines:
    line = line.strip()
    if line:
        parts = line.split(".")
        if len(parts) >= 2:
            user = parts[0].strip()
            bot = ".".join(parts[1:]).strip()
            conversations.append([user, bot])

# Write the conversations to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["User", "Bot"])  # Write the header row
    writer.writerows(conversations)  # Write the conversation rows

# FlowMaster Pro: Minimal AI task suggester for M365 (No Azure)
# Mock M365 email data
mock_email = {
    "subject": "Prepare slides for tomorrow",
    "body": "Hi, please have the slides ready for the 9 AM meeting."
}

# Fake task extraction (mimics Azure AI)
def get_task(email_text):
    return "prepare slides"  # Hardcoded for demo

# Main logic
task = get_task(mock_email["subject"] + " " + mock_email["body"])
print(f"FlowMaster Pro suggests: {task}")
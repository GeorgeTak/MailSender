import requests
import re
import time

# Initialize MailerSend API details
api_key = "mlsn.79d29f1a4eb3c06a2465dc6766a8dfa2ed1c0bdb286ffe97cea6f32870c3035b"  # Replace with your actual API key
url = "https://api.mailersend.com/v1/email"

def is_valid_email(email):
    # Basic email validation regex
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

while True:
    from_email = "you@trial-z86org86dvz4ew13.mlsender.net"  # Replace with your verified MailerSend domain

    # Prompt user for the recipient's email
    recipient_email = input("Enter the recipient's email address: ")
    if not is_valid_email(recipient_email):
        print("Invalid email address. Please try again.")
        continue

    # Prompt user for the subject
    subject = input("Enter the subject of the email: ")
    if not subject.strip():
        print("Subject cannot be empty. Please try again.")
        continue

    # Prompt user for the text content of the email
    text = input("Enter the text content of the email: ")
    if not text.strip():
        print("Email content cannot be empty. Please try again.")
        continue

    # HTML content (optional; can be the same as text or a richer format)
    html = f"<p>{text}</p>"

    # Prepare headers and data
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "from": {"email": from_email},
        "to": [{"email": recipient_email}],
        "subject": subject,
        "text": text,
        "html": html
    }

    try:
        # Send the email
        response = requests.post(url, headers=headers, json=data)

        # Print the raw response text for debugging
        print(f"Raw response text: {response.text}")

        # Check the response status
        if response.status_code == 202:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email. Status code: {response.status_code}")
            try:
                # Attempt to decode JSON response
                response_json = response.json()
                print(f"Response JSON: {response_json}")
            except requests.exceptions.JSONDecodeError:
                # Handle the case where response is not JSON
                print("Response content is not in JSON format.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        continue

    # Ask the user if they want to send another email
    send_another = input("Do you want to send another email? (yes/no): ").strip().lower()
    if send_another != 'yes':
        print("Exiting the email sender.")
        break



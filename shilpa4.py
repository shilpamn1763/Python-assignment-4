import smtplib
import random

def send_otp_to_customers():
    try:
        # Read customer emails from a file
        with open("customer_emails.txt", "r") as f:
            customer_emails = f.read().strip().split(",")  # Read and split by commas
        print("Customer Emails:", customer_emails)
    except FileNotFoundError:
        print("Error: File 'customer_emails.txt' not found.")
        return

    sender_email = "your_email@gmail.com"
    sender_password = "your_app_password"

    for email in customer_emails:
        otp = random.randint(100000, 999999)  # Generate 6-digit OTP
        print(f"Generated OTP for {email}: {otp}")

        message = f"Subject: Order Verification OTP\n\nDear Customer,\n\nYour order has arrived. Please share this OTP: {otp} with the delivery agent.\n\nThank you!"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
            server.quit()
            print(f"OTP sent successfully to {email}")
        except Exception as e:
            print(f"Failed to send email to {email}: {e}")

send_otp_to_customers()
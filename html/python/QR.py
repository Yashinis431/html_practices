import qrcode

# Link to your resume
data = "https://drive.google.com/file/d/1D8okWoT5ip8BedK5gbscDZWa9AYLL6TW/view?usp=drive_link"  # Replace with your actual link
# Generate QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")

# Save the QR Code
img.save("resume_qrcode.png")
print("QR code for your resume has been saved as 'resume_qrcode.png'")
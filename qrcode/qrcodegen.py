import qrcode
import os

# Link to your resume
data = "https://drive.google.com/file/d/1D8okWoT5ip8BedK5gbscDZWa9AYLL6TW/view?usp=drive_link"  # Replace with your actual link

try:
    # Generate QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    
    # Define the output directory and file
    output_dir = os.path.abspath("C:/Users/yashi/OneDrive/Documents/qrcode")
    os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist
    output_file = os.path.join(output_dir, "resume_qrcode.png")
    
    # Save the QR Code
    img.save(output_file)
    print(f"QR code for your resume has been saved as '{output_file}'")
except FileNotFoundError as fnf_error:
    print(f"File or directory not found: {fnf_error}")
except PermissionError as perm_error:
    print(f"Permission error: {perm_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

 
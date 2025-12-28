import qrcode

# https://pypi.org/project/qrcode/

# version 1.0

def print_qr_code():
    user_input = input("Enter text or URL to generate QR Code: ")
    user_file_name = input("Enter the filename: ")
    img = qrcode.make(user_input)
    img.save(f"img/{user_file_name}.png")
    print(f"Done generating {user_file_name}.png")

print_qr_code()
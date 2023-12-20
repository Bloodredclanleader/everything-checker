import socket
import platform
import speedtest  # Import the speedtest module

def main_menu():
    print("Welcome to BloodRed's Menu")
    print("1. Get Your IP")
    print("2. Get Computer Build Number")
    print("3. Get Internet Speed")
    print("4. Exit")

def option_1():
    print("Executing Option 1...")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Your IP Address: ", ip_address)

def option_2():
    print("Executing Option 2...")
    os_info = platform.uname()
    print("OS: ", os_info.system)
    print("Build Number: ", os_info.version)

def option_3():
    print("Executing Option 3...")
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

while True:
    main_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        option_1()
    elif choice == '2':
        option_2()
    elif choice == '3':
        option_3()
    elif choice == '4':
        print("Exiting the menu. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

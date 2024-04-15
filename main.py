import os
import subprocess
import shutil
import joblib

# Function to scan connected USB devices
def scan_usb_devices():
    devices = []
    # Use platform-specific commands to list connected USB devices
    output = subprocess.check_output("wmic logicaldisk get caption, drivetype", shell=True, universal_newlines=True)
    lines = output.strip().split('\n')
    for line in lines[1:]:
        device_info = line.strip().split()
        if len(device_info) >= 2 and device_info[1] == '2':  # Drive type 2 represents removable drives
            devices.append(device_info[0])
    return devices

# Function to scan files on a device and detect malware
def scan_device(device_path, model):
    malware_files = []
    for root, dirs, files in os.walk(device_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                # Check if the file is malware using the trained model
                if is_malware(file_path, model):
                    malware_files.append(file_path)
    return malware_files

# Function to check if a file is malware using the trained model
def is_malware(file_path, model):
    # Implement malware detection logic using the trained model
    # Here, we assume the model is an MLP Classifier loaded using joblib
    # You need to adjust this part according to your actual model
    # For example, you may need to extract features from the file and then make predictions
    # This is a placeholder implementation
    features = extract_features(file_path)  # You need to define this function
    prediction = model.predict([features])
    return prediction == 1  # Assuming 1 represents malware and 0 represents benign

# Function to extract features from a file (you need to implement this)
def extract_features(file_path):
    # Implement feature extraction logic here
    # This is a placeholder implementation
    return []

# Main function
def main():
    # Load the trained MLP Classifier model
    model = joblib.load('mlp_classifier_model.pkl')

    # Scan for USB devices
    usb_devices = scan_usb_devices()

    if not usb_devices:
        print("No USB devices connected.")
        return

    # Scan files on each USB device
    for device in usb_devices:
        print(f"Scanning files on device: {device}")
        malware_files = scan_device(device, model)
        if malware_files:
            print("Malware detected on the device:")
            for file in malware_files:
                print(file)
        else:
            print("No malware detected on the device.")

if __name__ == "__main__":
    main()

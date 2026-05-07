# import requests
# import numpy as np

# API_URL = 'http://127.0.0.1:5000/predict'

# print("Generating dummy ECG data payload...")
# dummy_payload = {
#     "waveform_360": np.random.uniform(-0.5, 1.0, 360).tolist(), 
#     "pre_rr": 838.89,   
#     "post_rr": 855.56,  
#     "peak_amp": 0.89    
# }

# print("Sending data to the ML API...")
# response = requests.post(API_URL, json=dummy_payload)

# print("\n--- API RESPONSE ---")
# print(response.json())

# import requests
# import numpy as np
# import time

# API_URL = 'http://127.0.0.1:5000/predict'

# # Let's simulate 3 vastly different types of heartbeats
# patients = [
#     {
#         "name": "Patient A (Normal, Steady Heartbeat)",
#         "payload": {
#             "waveform_360": np.random.normal(0, 0.2, 360).tolist(), # Smooth, low variance
#             "pre_rr": 800.0,   # Normal resting heart rate interval
#             "post_rr": 800.0,  
#             "peak_amp": 1.0    # Normal peak
#         }
#     },
#     {
#         "name": "Patient B (Fast & Spiky - Tachycardia)",
#         "payload": {
#             "waveform_360": np.random.uniform(-1.5, 2.5, 360).tolist(), # Wild, spiky noise
#             "pre_rr": 350.0,   # Very short intervals (fast heartbeat)
#             "post_rr": 360.0,  
#             "peak_amp": 2.8    # Huge spike
#         }
#     },
#     {
#         "name": "Patient C (Slow & Flat - Bradycardia)",
#         "payload": {
#             "waveform_360": np.random.uniform(-0.1, 0.1, 360).tolist(), # Barely moving
#             "pre_rr": 1300.0,  # Very long intervals (slow heartbeat)
#             "post_rr": 1350.0, 
#             "peak_amp": 0.3    # Weak pulse
#         }
#     }
# ]

# print("Starting Multi-Patient API Test...\n")

# for patient in patients:
#     print(f"Testing {patient['name']}...")
#     response = requests.post(API_URL, json=patient['payload'])
#     result = response.json()
    
#     print(f"  -> Prediction: {result.get('prediction')}")
#     print(f"  -> Confidence: {result.get('confidence')}\n")
#     time.sleep(1) # Pause for 1 second so we don't spam the server

# import requests
# import numpy as np
# import time

# API_URL = 'http://127.0.0.1:5000/predict'

# print("Loading real patient data from .npy files...\n")

# # 1. Load the fully preprocessed dataset
# try:
#     X_test = np.load('data/X_test.npy')
#     y_test = np.load('data/y_test.npy')
# except FileNotFoundError:
#     print("Error: Could not find .npy files. Make sure they are in data/")
#     exit()

# # AAMI Class Mapping (So we can read the true labels easily)
# class_names = {
#     0: 'N (Normal)',
#     1: 'S (Supraventricular Ectopic)',
#     2: 'V (Ventricular Ectopic)',
#     3: 'F (Fusion)',
#     4: 'Q (Unknown)'
# }

# # 2. Pick 3 random heartbeats from the test set
# random_indices = np.random.choice(len(X_test), 10, replace=False)

# print("Starting Real Patient API Test...\n")

# for i, idx in enumerate(random_indices):
#     patient_data = X_test[idx]
    
#     # Get the true label directly from the y_test array
#     true_label_code = int(y_test[idx])
#     true_class_name = class_names.get(true_label_code, "Unknown")
    
#     # 3. Package the 1D array into the exact JSON format your Flask API expects
#     payload = {
#         "waveform_360": patient_data[:360].tolist(),
#         "pre_rr": float(patient_data[360]),
#         "post_rr": float(patient_data[361]),
#         "peak_amp": float(patient_data[362])
#     }
    
#     print(f"--- Testing Patient {i+1} ---")
#     print(f"TRUE CLASS (From Dataset): {true_class_name}")
    
#     # 4. Fire the payload at the Flask Server
#     response = requests.post(API_URL, json=payload)
#     result = response.json()
    
#     print(f"API PREDICTION:            {result.get('prediction')}")
#     print(f"API CONFIDENCE:            {result.get('confidence')}\n")
    
#     time.sleep(1) # Pause for 1 second between requests


import requests
import numpy as np
import time

API_URL = 'http://127.0.0.1:5000/predict'

print("Loading real patient data from .npy files...\n")

try:
    X_test = np.load('data/X_test.npy')
    y_test = np.load('data/y_test.npy')
except FileNotFoundError:
    print("Error: Could not find .npy files.")
    exit()

class_names = {
    0: 'N (Normal)',
    1: 'S (Supraventricular Ectopic)',
    2: 'V (Ventricular Ectopic)',
    3: 'F (Fusion)',
    4: 'Q (Unknown)'
}

print("Hunting for one patient from EACH class...\n")

# We will store the index of one patient from each class here
test_indices = []

for class_code in range(5): # Classes 0 through 4
    # Find all patients in the dataset that have this true class
    matching_indices = np.where(y_test == class_code)[0]
    
    if len(matching_indices) > 0:
        # Grab the first patient we find for this class
        test_indices.append(matching_indices[0])
    else:
        print(f"Warning: No patients found in the test set for class {class_names[class_code]}")

# Now test the API with these specific patients
for i, idx in enumerate(test_indices):
    patient_data = X_test[idx]
    
    true_label_code = int(y_test[idx])
    true_class_name = class_names.get(true_label_code, "Unknown")
    
    payload = {
        "waveform_360": patient_data[:360].tolist(),
        "pre_rr": float(patient_data[360]),
        "post_rr": float(patient_data[361]),
        "peak_amp": float(patient_data[362])
    }
    
    print(f"--- Testing Patient {i+1} ---")
    print(f"TRUE CLASS (From Dataset): {true_class_name}")
    
    response = requests.post(API_URL, json=payload)
    result = response.json()
    
    print(f"API PREDICTION:            {result.get('prediction')}")
    print(f"API CONFIDENCE:            {result.get('confidence')}\n")
    
    time.sleep(1)
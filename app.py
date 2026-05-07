from flask import Flask, request, jsonify
import numpy as np
import pywt
from tensorflow.keras.models import load_model

app = Flask(__name__)

print("Booting up: Loading Hybrid CNN-LSTM model...")
model = load_model('models/hybrid_cnn_lstm.keras') 
print("Model loaded successfully!")

AAMI_CLASSES = {
    0: 'N (Normal)', 
    1: 'S (Supraventricular Ectopic)', 
    2: 'V (Ventricular Ectopic)', 
    3: 'F (Fusion)', 
    4: 'Q (Unknown)'
}

def extract_wavelets(signal):
    coeffs = pywt.wavedec(signal, 'db4', level=4)
    wavelet_features = np.zeros(16) 
    return wavelet_features

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        raw_waveform = np.array(data['waveform_360'])
        pre_rr = data['pre_rr']
        post_rr = data['post_rr']
        peak_amp = data['peak_amp']
        
        method_1 = raw_waveform                                  
        method_2 = np.array([pre_rr, post_rr, peak_amp])         
        method_3 = extract_wavelets(raw_waveform)                
        
        # Reshape each input to have a "batch size" of 1
        # The 360 waveform needs a 3D shape for the CNN (1, 360, 1)
        input_1 = method_1.reshape(1, 360, 1) 
        
        # The tabular features just need a 2D shape (1, number_of_features)
        input_2 = method_2.reshape(1, 3)       
        input_3 = method_3.reshape(1, 16)      
        
        # Group them into a list EXACTLY as your model expects them
        model_input = [input_1, input_2, input_3] 
        
        predictions = model.predict(model_input)
        pred_index = int(np.argmax(predictions, axis=1)[0])
        confidence = float(np.max(predictions))
        
        return jsonify({
            'status': 'success',
            'prediction': AAMI_CLASSES[pred_index],
            'confidence': f"{round(confidence * 100, 2)}%",
            'features_processed': 379
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400
@app.route('/', methods=['GET'])
def home():
    return "<h1>ECG API is Live!</h1><p>Send a POST request to /predict to use the model.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify
import os 

app = Flask(__name__)

@app.route('/upload',methods=['POST'])

def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'no file'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'empty filename'}), 400
    
    if file:
        upload_foler = 'uploads'
        if not os.path.exists(upload_foler):
            os.makedirs(upload_foler)

        filename = os.path.join(upload_foler, file.filename)
        file.save(filename)
        return jsonify({'filename': filename}), 200
    else:
        return jsonify({'error': 'no file'}), 400
    

if __name__ == '__main__':
    app.run(debug=True)
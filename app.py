from flask import Flask, request, jsonify
from encryption import encrypt_file, decrypt_file
from s3_utils import upload_file_to_s3, generate_presigned_url

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    encrypted_data = encrypt_file(file.read())
    upload_file_to_s3(encrypted_data, file.filename)
    return jsonify({'message': 'File uploaded successfully!'})

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    url = generate_presigned_url(filename)
    return jsonify({'download_url': url})

if __name__ == '__main__':
    app.run(debug=True)

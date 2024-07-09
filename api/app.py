from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error
import os

app = Flask(__name__)

# Initialize Minio client
minio_client = Minio(
    "minio:9000",  # Minio server URL
    access_key=os.getenv('MINIO_ACCESS_KEY'),  # Access key from environment variable
    secret_key=os.getenv('MINIO_SECRET_KEY'),  # Secret key from environment variable
    secure=False  # Whether to use secure (HTTPS) connection, set to False for development
)

# Name of the bucket to store uploads
bucket_name = "mybucket"

# Endpoint to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    file_path = '/api/api/image.jpeg'  # Path to your image file
    
    try:
        with open(file_path, 'rb') as f:
            # Upload the file to Minio
            minio_client.put_object(bucket_name, os.path.basename(file_path), f, os.stat(file_path).st_size)
        
        return jsonify({"message": "File uploaded successfully"}), 200
    
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except S3Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Create the bucket if it doesn't exist
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)
    ##upload_file()
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)

import os
from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return "Downloader Server is Running Safely!"

@app.route('/download', methods=['GET'])
def download_video():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "URL is missing"}), 400
    
    print(f"Cloud Server Downloading: {video_url}")
    
    # Cloud par file temporary save karne ke liye settings
    ydl_opts = {
        'outtmpl': '/tmp/%(title)s.%(ext)s',
        'format': 'best',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return jsonify({"status": "Success", "message": "Downloaded on Cloud Successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "Failed", "error": str(e)}), 500

if __name__ == '__main__':
    # Cloud server automatic port decide karta hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

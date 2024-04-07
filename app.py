from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        logging.error("No video_id provided in request")
        return jsonify({'error': 'Missing video_id parameter'}), 400

    try:
        logging.info(f"Fetching transcript for video ID: {video_id}")
        transcript_segments = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = ' '.join(segment['text'] for segment in transcript_segments)
        logging.info(f"Successfully fetched transcript for video ID: {video_id}")
        return jsonify({"full_transcript": full_transcript})
    except Exception as e:
        logging.error(f"Failed to fetch transcript for video ID: {video_id} with error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    logging.info("Starting the Flask application on port 5000")
    app.run(port=5000)

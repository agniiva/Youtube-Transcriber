from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    if not video_id:
        return jsonify({'error': 'Missing video_id parameter'}), 400

    try:
        transcript_segments = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = ' '.join(segment['text'] for segment in transcript_segments)
        return jsonify({"full_transcript": full_transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)

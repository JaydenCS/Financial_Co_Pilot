from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    try:
        video_id = video_url.split("v=")[1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = '\n'.join(item['text'] for item in transcript)
        return transcript_text[:5000]
    except Exception as e:
        print("Error occurred:", e)
        return None

print(get_transcript("https://www.youtube.com/watch?v=NWadrNe9tvA"))
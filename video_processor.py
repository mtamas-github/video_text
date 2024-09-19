import moviepy.editor as mp
import speech_recognition as sr
import pytesseract
import cv2
import os

def extract_audio(video_file, audio_file='temp_audio.wav'):
    """Extracts the audio from a video file."""
    clip = mp.VideoFileClip(video_file)
    clip.audio.write_audiofile(audio_file)
    return audio_file

def speech_to_text(audio_file, output_text_file='speech_text.txt'):
    """Converts speech in an audio file to text and saves it to a file."""
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Could not understand audio"
    except sr.RequestError:
        text = "Could not request results; check your network connection"
    
    with open(output_text_file, 'w') as f:
        f.write(text)
    
    return output_text_file

def ocr_video(video_file, output_text_file='ocr_text.txt', frame_interval=30):
    """Extracts text from the rolling text in a video using OCR."""
    video_capture = cv2.VideoCapture(video_file)
    frame_count = 0
    text_data = ""
    
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        
        # Process every nth frame (to avoid processing all frames)
        if frame_count % frame_interval == 0:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(gray_frame)
            text_data += text + "\n"
        
        frame_count += 1
    
    with open(output_text_file, 'w') as f:
        f.write(text_data)
    
    video_capture.release()
    return output_text_file

def process_video(video_file, speech_text_file='speech_text.txt', ocr_text_file='ocr_text.txt'):
    """Processes a video file to extract speech and OCR text."""
    audio_file = extract_audio(video_file)
    speech_to_text(audio_file, speech_text_file)
    ocr_video(video_file, ocr_text_file)
    
    # Optionally, clean up the temporary audio file
    os.remove(audio_file)

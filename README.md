# Video text extractor
Extract text from videos

## Requirements
Using the following python packages:
- moviepy to extract the speech
- speechrecognition to convert speech to text
- pytesseract ocr from image
- opencv-python images from video

## Usage 
```
process_video("path/to/video_file")
```

First it will run the speech recognition process by creating a .wav file and recognising the content of the speech
Secondly it will run the OCR process (reading text from video frames)

This is just a very quick example.
It needs a lot of testing and tweaking depending on the example videos.
Also it might need performance tweaking as frame by frame can be a long process.


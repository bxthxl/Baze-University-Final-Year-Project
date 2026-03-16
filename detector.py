import cv2
import numpy as np
import os
import sqlite3
import requests
import time
from deepface import DeepFace
from datetime import datetime

def run_detector():

    facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    camera = cv2.VideoCapture(0)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainingdata.yml')

    # Get profile of a recognized individual from the database
    def getprofile(id):
        connection = sqlite3.connect('face_recognition.db')
        cursor = connection.execute("SELECT * FROM USERS WHERE id=?", (id, ))
        profile = None
        for row in cursor:
            profile = row
        connection.close()
        return profile

    # Send details of the unknown person to Discord (image, video, and analysis)
    def send_discord_analysis(img_path, video_path, analysis):
        webhook_url = 'https://discord.com/api/webhooks/1283755623376224389/9lUH8JdjE009nY-RaqCgsYRflVh5-2reJ2CstvygGuqDF5qMZHo8WM6LVb7z8jc8LzAV'
        message = {
            "content": f"Alert: Unknown face detected!\n\nAnalysis:\n{analysis}",
            "username": "Face Recognition Bot"
        }

        # Send text alert to Discord with analysis
        response = requests.post(webhook_url, json=message)
        if response.status_code == 204:
            print("Discord message sent successfully!")
        else:
            print(f"Failed to send Discord message. Response: {response.status_code}")

        # Send the image to Discord
        with open(img_path, 'rb') as img:
            files = {
                'file': (os.path.basename(img_path), img)
            }
            response = requests.post(webhook_url, files=files)
            if response.status_code == 204:
                print("Discord image sent successfully!")
            else:
                print(f"Failed to send Discord image. Response: {response.status_code}")

        # Send the video to Discord
        with open(video_path, 'rb') as video:
            files = {
                'file': (os.path.basename(video_path), video)
            }
            response = requests.post(webhook_url, files=files)
            if response.status_code == 204:
                print("Discord video sent successfully!")
            else:
                print(f"Failed to send Discord video. Response: {response.status_code}")

    # Perform DeepFace analysis (age, gender, race, emotion)
    def analyze_face(img_path):
        try:
            # Perform the DeepFace analysis on the image, enforcing no error if no face detected
            analysis_results = DeepFace.analyze(img_path, enforce_detection=False)
        
            if analysis_results:
                # DeepFace returns a list of analysis results; we assume there's only one face to analyze
                analysis = analysis_results[0]
            
                # Format the analysis into a readable string
                formatted_analysis = f"Age: {analysis['age']}\n" \
                                     f"Gender: {analysis['gender']}\n" \
                                     f"Race: {max(analysis['race'], key=analysis['race'].get)} " \
                                     f"({analysis['race'][max(analysis['race'], key=analysis['race'].get)]*100:.2f}%)\n" \
                                     f"Emotion: {max(analysis['emotion'], key=analysis['emotion'].get)} " \
                                     f"({analysis['emotion'][max(analysis['emotion'], key=analysis['emotion'].get)]*100:.2f}%)"
                return formatted_analysis
            else:
                return "No face detected for analysis."
        except Exception as e:
         print(f"DeepFace analysis failed: {e}")
        return "Analysis failed."


    while True:
        ret, image = camera.read() 
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5) # 
        threshold = 65
        
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y: y + h, x: x + w])
            
            if confidence < threshold:
                profile = getprofile(id)
                if profile:
                    # Display the recognized person's details
                    cv2.putText(image, f"Name: {profile[1]}", (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
                    cv2.putText(image, f"Age: {profile[2]}", (x, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 127), 2)
            else:
                # Use timestamp as unique identifier for files
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Save unknown face image with timestamp
                img_path = f"unknown/unknown_{timestamp}.jpg"
                cv2.imwrite(img_path, image[y: y + h, x: x + w])
                
                # Start capturing video of the unknown person
                video_filename = f"unknown/unknown_{timestamp}.avi"
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter(video_filename, fourcc, 60.0, (640, 480))
                
                start_time = time.time()
                while time.time() - start_time < 10:  # Record 10 seconds of video
                    ret, frame = camera.read()
                    out.write(frame)
                    cv2.imshow("Recording Unknown", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                out.release()
                
                # Perform DeepFace analysis on the image
                analysis = analyze_face(img_path)
                
                # Send everything to Discord
                send_discord_analysis(img_path, video_filename, analysis)

        cv2.imshow("Face Recognition System", image)
        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def main():
    run_detector()

# Uncomment the below line to run the code directly
if __name__ == "__main__":
     main()

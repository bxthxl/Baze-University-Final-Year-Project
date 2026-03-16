import cv2 # for camera
import numpy as np # for array
import sqlite3 # Database
import trainer as ts

def run_dataset_creator():

    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eyeDetect =cv2.CascadeClassifier('haarcascade_eye.xml')
    sideFace = cv2.CascadeClassifier('haarcascade_profileface.xml')
    noseDetect =cv2.CascadeClassifier('Nariz.xml')
    mouthDetect = cv2.CascadeClassifier('Mouth.xml')

    cam = cv2.VideoCapture(0)

    def insertorupdate(id, name, age):
        connection = sqlite3.connect("face_recognition.db")
        command = "SELECT * FROM USERS WHERE ID="+str(id)
        cursor = connection.execute(command)
        ifRecordExist = 0

        for row in cursor:
            ifRecordExist = 1
        if(ifRecordExist == 1):
            connection.execute("UPDATE USERS SET NAME=? WHERE ID=?", (name, id))
            connection.execute("UPDATE USERS SET AGE=? WHERE ID=?", (age, id))
        else:
            connection.execute("INSERT INTO USERS (ID, NAME, AGE) values(?,?,?)",(id, name, age))

        connection.commit()
        connection.close()

    Id = input('Enter User ID: ')
    Name = input('Enter User Name: ')
    Age = input('Enter User Age: ')

    insertorupdate(Id, Name, Age)

    sampleNumber = 0 # Asumming there is nothing in our dataset
    while(True):
        ret, image = cam.read() # Open Camera
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert camera footage to gray image 
        frontalFace = faceDetect.detectMultiScale(gray, 1.3, 5) # scale face
        leftSide = sideFace.detectMultiScale(gray, 1.3, 5)
        # So we can detect the right part of the face
        flipped = cv2.flip(gray, 1)
        rightSide = sideFace.detectMultiScale(flipped, 1.3, 5)


       #  eyes = eyeDetect.detectMultiScale(gray, 1.5, 14 )
        
        '''
        nose = noseDetect.detectMultiScale(gray, 1.5, 5)
        mouth = mouthDetect.detectMultiScale(gray, 1.5, 20)
        '''
        for (x,y,w,h) in frontalFace:
            sampleNumber = sampleNumber + 1
            
            # Drawing a rectangle around the face
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255))

            #Defining the region of intrest (ROI) for eyes within the detected face
            face_gray = gray[y: y +h, x: x + w]
            face_color = image[y: y + h, x: x + w]
            
            # Detect eyes within the face region
            eyes = eyeDetect.detectMultiScale(face_gray, 1.3, 5)

            for (eye_x, eye_y, eye_w, eye_h) in eyes:
                # Draw rectangle around each detected eye within the face
                cv2.rectangle(face_color, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (0, 255, 0), 2)
                # cv2.waitKey(100)
        
            # Save face region to daaset
            cv2.imwrite("data/user."+str(Id)+"."+str(sampleNumber)+ ".jpg",gray[y : y + h, x : x + w])
            
        cv2.imshow("Face Scan", image)
        cv2.waitKey(1)
        
        for (x,y,w,h) in leftSide:
            sampleNumber = sampleNumber + 1
            # Save face region to daaset
            #cv2.imwrite("data/user."+str(Id)+"."+str(sampleNumber)+ ".jpg",gray[y : y + h, x : x + w])

            # Drawing a rectangle around the left side of the face
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255))          

            #Defining the region of intrest (ROI) for eyes within the detected face
            face_gray = gray[y: y +h, x: x + w]
            face_color = image[y: y + h, x: x + w]
            
            # Detect eyes within the face region
            eyes = eyeDetect.detectMultiScale(face_gray, 1.3, 5)

            for (eye_x, eye_y, eye_w, eye_h) in eyes:
                # Draw rectangle around each detected eye within the face
                cv2.rectangle(face_color, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (0, 255, 0), 2)
                # cv2.waitKey(100)
        
            # Save face region to daaset
            cv2.imwrite("data/user."+str(Id)+"."+str(sampleNumber)+ ".jpg",gray[y : y + h, x : x + w])
            
        for (x,y,w,h) in rightSide:
            sampleNumber = sampleNumber + 1
            # Save face region to daaset
            #cv2.imwrite("data/user."+str(Id)+"."+str(sampleNumber)+ ".jpg",gray[y : y + h, x : x + w])

            # Drawing a rectangle around the left side of the face
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255)) 

            #Defining the region of intrest (ROI) for eyes within the detected face
            face_gray = gray[y: y +h, x: x + w]
            face_color = image[y: y + h, x: x + w]
            
            # Detect eyes within the face region
            eyes = eyeDetect.detectMultiScale(face_gray, 1.3, 5)

            for (eye_x, eye_y, eye_w, eye_h) in eyes:
                # Draw rectangle around each detected eye within the face
                cv2.rectangle(face_color, (eye_x, eye_y), (eye_x + eye_w, eye_y + eye_h), (0, 255, 0), 2)
                # cv2.waitKey(100)
        
            # Save face region to daaset
            cv2.imwrite("data/user."+str(Id)+"."+str(sampleNumber)+ ".jpg",gray[y : y + h, x : x + w])
                     

        cv2.waitKey(100)

        cv2.imshow("Face Scan", image)
        cv2.waitKey(1)
        if(sampleNumber >= 500):
            break

    cam.release()
    cv2.destroyAllWindows()


def main():
    run_dataset_creator()
    ts.main()


if __name__ == "__main__":
    main()


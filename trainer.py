import os
import cv2
import numpy as np
from PIL import Image # for running our image file



def run_trainer():

    # eyeDetect =cv2.CascadeClassifier('haarcascade_eye.xml')

    recognizer = cv2.face.LBPHFaceRecognizer.create()  # recognize faces in camera
    
    
    path = 'data'


    def get_images_with_id(path):
        image_path = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        ids = []
    
        for single_image_path in image_path:
            faceImage = Image.open(single_image_path).convert('L')  # Converting images to grayscale
            faceNp = np.array(faceImage, np.uint8)

            # eyes = eyeDetect.detectMultiScale(faceNp, 1.5, 14 )
            
            id = int(os.path.split(single_image_path)[-1].split(".")[1])            
            print(id)
            faces.append(faceNp)
            ids.append(id)
            cv2.imshow("Training", faceNp)
            
            '''
            if  len(eyes) != 0:
                # print ("eye detected")   
                # g = faceNp[eyes[0,1]:  eyes[0,1]+eyes[0,3], eyes[0,0]: eyes[0,0]+eyes[0,2]]  
                # cv2.imshow("Eye",g)
                x, y, x2, y2 = eyes[0,0], eyes[0,1], eyes[0,0] + eyes[0,2], eyes[0,1] + eyes[0,3]
                g = faceNp[eyes[0,1]:  eyes[0,1]+eyes[0,3], eyes[0,0]: eyes[0,0]+eyes[0,2]]

                # print(eyes)
                # print (x,y,x2,y2)                       
                # cv2.rectangle(faceNp,  (x,y ), (x2,y2), (0, 255, 0), 2)
                
                if eyes.shape[0]==2:
                    x,y, x2, y2 = eyes[1,0], eyes[1,1],eyes[1,0]+eyes[1,2], eyes[0,1]+eyes[1,3] 
                    g = faceNp[eyes[0,1]:  eyes[0,1]+eyes[0,3], eyes[0,0]: eyes[0,0]+eyes[0,2]]                  
                    
                    # cv2.rectangle(faceNp,  (x,y ), (x2,y2), (0, 255, 0), 2)
                    # cv2.waitKey(10000)
            '''

            cv2.waitKey(100)

        return np.array(ids),faces

    ids, faces = get_images_with_id(path)
    recognizer.train(faces, ids)
    recognizer.save("recognizer/trainingdata.yml")

    cv2.destroyAllWindows()

def main():
    run_trainer()


if __name__ == "__main__":
    main()

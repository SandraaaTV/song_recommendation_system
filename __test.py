import cv2
import keras
import pygame

# Load the pre-trained emotion classification model
emotion_model = keras.models.load_model('model.h5')

# Initialize the music player
pygame.mixer.init()

# Define a dictionary of emotions and corresponding music tracks
emotions_music = {
    'happy': 'happy.mp3',
    'sad': 'sad.mp3',
    'angry': 'angry.mp3',
    'neutral': 'neutral.mp3'
}

# Open the camera and capture a video stream
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect the person's face in the grayscale image
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # If a face is detected, classify the emotion and play music
    if len(faces) > 0:
        # Extract the region of interest (ROI) corresponding to the face
        (x, y, w, h) = faces[0]
        roi_gray = gray[y:y+h, x:x+w]
        
        # Resize the ROI to match the input size of the emotion classification model
        roi_gray = cv2.resize(roi_gray, (48, 48))
        roi_gray = roi_gray.astype('float') / 255.0
        roi_gray = keras.preprocessing.image.img_to_array(roi_gray)
        roi_gray = np.expand_dims(roi_gray, axis=0)
        
        # Classify the emotion
        predictions = emotion_model.predict(roi_gray)[0]
        emotion = np.argmax(predictions)
        emotion_label = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'][emotion]
        
        # Play the corresponding music track
        music_file = emotions_music[emotion_label]
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
    
    # Display the video stream with the face detected and emotion label
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, emotion_label, (x, y-10),
    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    cv2.namedWindow('frame', frame)

    # Press 'q' to quit the app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
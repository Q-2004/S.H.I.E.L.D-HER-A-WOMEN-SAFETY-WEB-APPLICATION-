import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Function to detect the women's safety hand gesture
def is_safety_gesture(landmarks):
    # Thumb tip (landmark 4) should be lower than thumb MCP (landmark 2)
    # Index, middle, ring, and pinky fingertips should be above their respective PIP joints
    thumb_tip = landmarks[4].y
    index_tip = landmarks[8].y
    middle_tip = landmarks[12].y
    ring_tip = landmarks[16].y
    pinky_tip = landmarks[20].y

    thumb_folded = thumb_tip > landmarks[2].y
    fingers_extended = (
        index_tip < landmarks[6].y and
        middle_tip < landmarks[10].y and
        ring_tip < landmarks[14].y and
        pinky_tip < landmarks[18].y
    )

    return thumb_folded and fingers_extended

# Initialize the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert the BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and find hands
    results = hands.process(image)

    # Convert the RGB image back to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw hand landmarks and check for safety gesture
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Check if the safety gesture is detected
            if is_safety_gesture(hand_landmarks.landmark):
                cv2.putText(image, "Women is Unsafe!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                print("Safety gesture detected! A woman is unsafe.")

    # Display the image
    cv2.imshow("Hand Gesture Recognition", image)

    # Break the loop on 'q' key press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

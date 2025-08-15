import cv2 
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

def detect_hand_landmarks(img, w, h):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    index_finger = (0, 0)
    landmark_list = []
    tap = False

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        for id, lm in enumerate(hand_landmarks.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            landmark_list.append((cx, cy))
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        if len(landmark_list) > 8:
            index_finger = landmark_list[8]
            tap = is_tap(landmark_list)

    return landmark_list, index_finger, tap

def is_tap(landmarks):
    if len(landmarks) < 9:
        return False
    x1, y1 = landmarks[4]  # Thumb tip
    x2, y2 = landmarks[8]  # Index tip
    dist = np.linalg.norm(np.array([x2 - x1, y2 - y1]))
    return dist < 30
import cv2
import time
import glob
from emailing import send_email
from pathlib import Path
from threading import Thread


# ---------------- CONFIG ----------------
IMAGE_DIR = Path("images")
IMAGE_DIR.mkdir(exist_ok=True)
MIN_AREA = 15000


# ---------------- HELPERS ----------------
def clean_folder():
    """Remove all images from the images directory."""
    for image in IMAGE_DIR.glob("*.png"):
        image.unlink()


# ---------------- VIDEO SETUP ----------------
video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
image_count = 1


# ---------------- MAIN LOOP ----------------
while True:
    status = 0
    check, frame = video.read()

    # Safety check in case camera fails
    if not check:
        break

    # Convert to grayscale and blur to reduce noise
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Capture the first frame for background reference
    if first_frame is None:
        first_frame = gray_frame
        continue

    # Compute absolute difference between background and current frame
    delta_frame = cv2.absdiff(first_frame, gray_frame)

    # Apply threshold and dilation to highlight objects
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dilated_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(dilated_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    image_with_object = None

    for contour in contours:
        if cv2.contourArea(contour) < MIN_AREA:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            image_path = IMAGE_DIR / f"{image_count}.png"
            cv2.imwrite(str(image_path), frame)
            image_count += 1
            
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    # Track last two states only
    status_list.append(status)
    status_list = status_list[-2:]

    # Trigger email when object leaves the frame
    if len(status_list) == 2 and status_list[0] == 1 and status_list[1] == 0:
        if image_with_object:
            Thread(target=send_email, args=(image_with_object,), daemon=True).start()
            Thread(target=clean_folder, daemon=True).start()

    cv2.imshow("Motion Detector", frame)

    if cv2.waitKey(1) == ord("q"):
        break


video.release()
cv2.destroyAllWindows()
import cv2
from ultralytics import YOLO
from utils.draw_boxes import draw_boxes

def main():
    # Load YOLOv8 Nano model
    model = YOLO("models/yolov8n.pt")  # Make sure this file exists

    # Start webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Unable to access webcam.")
        return

    print("✅ Press 'q' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Couldn't read frame.")
            break

        # Run YOLOv8 on the frame
        results = model(frame, stream=True)

        # Draw bounding boxes
        frame = draw_boxes(frame, results, model.names)

        # Show the frame
        cv2.imshow("Real-Time Object Detection", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

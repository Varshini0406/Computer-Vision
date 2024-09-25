import cv2

def reverse_video(input_video_path, output_video_path):
    # Open the video file
    cap = cv2.VideoCapture('1.mp4')
    
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Prepare output video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    # Read frames and store in a list
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    # Reverse the frames and write them into the output video
    for frame in reversed(frames):
        out.write(frame)

    # Release resources
    cap.release()
    out.release()

# Example usage:
reverse_video('1.mp4', 'output_reversed_video.mp4')

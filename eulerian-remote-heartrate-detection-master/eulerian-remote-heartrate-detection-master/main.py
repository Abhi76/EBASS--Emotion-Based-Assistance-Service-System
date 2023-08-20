import cv2
import pyramids
import heartrate
import preprocessing
import eulerian

freq_min = 1
freq_max = 1.8

print("Reading + preprocessing video...")
video_frames, frame_ct, fps = preprocessing.read_video("C:/Users/Hirak/Desktop/8th Sem Project/eulerian-remote-heartrate-detection-master/eulerian-remote-heartrate-detection-master/videos/face.mp4")

print("Building Laplacian video pyramid...")
lap_video = pyramids.build_video_pyramid(video_frames)

amplified_video_pyramid = []

for i, video in enumerate(lap_video):
    if i == 0 or i == len(lap_video)-1:
        continue

    print("Running FFT and Eulerian magnification...")
    result, fft, frequencies = eulerian.fft_filter(video, freq_min, freq_max, fps)
    lap_video[i] += result

    print("Calculating heart rate...")
    heart_rate = heartrate.find_heart_rate(fft, frequencies, freq_min, freq_max)

print("Rebuilding final video...")
amplified_frames = pyramids.collapse_laplacian_video_pyramid(lap_video, frame_ct)

print("Heart rate: ", heart_rate, "bpm")
print("Displaying final video...")

for frame in amplified_frames:
    cv2.imshow("frame", frame)
    cv2.waitKey(20)
cv2.waitKey()
cv2.destroyAllWindows()


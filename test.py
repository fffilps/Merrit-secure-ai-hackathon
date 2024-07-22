import os
import supervision as sv
from supervision.assets import download_assets, VideoAssets
import cv2
from roboflow import Roboflow
from ultralytics import YOLO



HOME = os.getcwd()
print("home is", HOME)

model = YOLO("yolov8s.pt")


download_assets(VideoAssets.VEHICLES)
VIDEO_PATH = VideoAssets.VEHICLES.value
sv.VideoInfo.from_video_path(video_path=VIDEO_PATH)


MYVIDEO_PATH = f"{HOME}/assets/video.mp4"


import pyrebase
import data.config as config
import datetime


firebase = pyrebase.initialize_app(config.firebaseConfig)
storage = firebase.storage()

# test code
# path_on_cloud = "video/aesthetic.mp4"
# path_local = "amv_aesthetic.mp4"
# storage.child(path_on_cloud).put(path_local)
# total_videos = len(storage.list_files("video"))


def upload_video_to_fb(video_path):
    where_to_upload = f"video/amv-{str(datetime.datetime.now())}"
    storage.child(where_to_upload).put(video_path)


def get_path_of_video_from_fb():
    path_on_cloud = "video/aesthetic.mp4"
    url = storage.child(path_on_cloud).get_url(None)
    return url

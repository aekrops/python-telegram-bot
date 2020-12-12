import pyrebase
import config

firebase = pyrebase.initialize_app(config.firebaseConfig)
storage = firebase.storage()

path_on_cloud = "video/aesthetic.mp4"
path_local = "amv_aesthetic.mp4"
storage.child(path_on_cloud).put(path_local)



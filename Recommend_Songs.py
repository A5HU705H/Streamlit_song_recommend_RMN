import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import base64
from rmn import RMN

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg-5.jpg')

st.title("Welcome to Song Recommendation by Emotion Detection")
picture=st.camera_input('Capture Face for Recognition')
if picture is not None:
    img=Image.open(picture)
    picture=np.array(img)
    m=RMN()
    results = m.detect_emotion_for_single_frame(picture)
    prediction=results[0]['emo_label']
    image=m.draw(picture,results)
    cv2.imwrite('output.jpg',image)
    st.image('output.jpg')
    st.write("Emotion detected is: ",prediction)
    dict1={'angry':'https://open.spotify.com/playlist/71Xpaq3Hbpxz6w9yDmIsaH',
           'disgust':'https://open.spotify.com/playlist/3qgzMg4m5tvf16PzlPgGa9',
           'fear':'https://open.spotify.com/playlist/7rzS9iLiqjy65AsZd9qinf',
           'happy':'https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC',
           'neutral':'https://open.spotify.com/playlist/37i9dQZF1DWTC99MCpbjP8',
           'sad':'https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1',
           'surprise':'https://open.spotify.com/playlist/0X0ZZTJ6z2yxX5Uu7R7j3G'
          }
    song_link=dict1.get(prediction)
    st.write(song_link)

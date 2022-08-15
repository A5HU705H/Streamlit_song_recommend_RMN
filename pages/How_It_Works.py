import streamlit as st
import base64
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
add_bg_from_local('bg-3.jpg')
st.title("How we use Webcam Images to Recommend Songs")
st.header("There are three main steps:")
st.subheader("1:Detect the face using haar-cascade face detector")
st.write("Haar feature-based cascade classifiers is an effective method introduced by Paul Viola and Micheal Jones in their paper Rapid Object Detection using a Boosted Cascade of Simple Features in 2001. It is a ML based approach where a cascade function is trained by using a lot of positive images(images with the object) and negative images(images without the object). It is then used to detect objects in other images. Haar cascade uses Haar features similar to convolutional kernel in order to extract features and detect the object (in our case:faces).")
st.write("To learn more about haar-cascade please visit: ")
st.write("https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html")
st.subheader("2:Using a deep-learning model to predict emotion based on captured image")
st.write("We used a Convolutional Neural Network(CNN) in order to predict the emotion expressed by the face.We used a basic sequential CNN consisting of 4 convolutional layers,3 maxpooling layers,3 dropout layers,1 flattening layer,1 hidden layer and 1 output layer. This model was trained with an Adam optimizer with a learning rate of 0.001 and decay of 1e-6 with a categorical cross entropy loss on the Kaggle FER 2013 dataset. We acheived a accuracy of 63.65 percent on the test set. We also tried to use transfer learning using resnet,VGG 19,Mobilenet pretrained models but didnt acheive satisfactory results. We also implemented the state of the art RMN model which was presented in the research paper Facial Expression Recognition Using Residual Masking Network by Luan Pham,The Huynh Vu,Tuan Anh Tran.")
st.write("To learn more about CNNs please visit:")
st.write("https://www.ibm.com/cloud/learn/convolutional-neural-networks")
st.write("https://en.wikipedia.org/wiki/Convolutional_neural_network")
st.write("To learn more about RMN please visit:")
st.write("https://github.com/phamquiluan/ResidualMaskingNetwork")
st.write("https://ieeexplore.ieee.org/document/9411919")
st.write("Github Links:")
st.subheader("3:Using the predicted emotion to recommend songs")
st.write("We found playlists for songs on spotify and provided links to it based on the emotion predicted by our model.")

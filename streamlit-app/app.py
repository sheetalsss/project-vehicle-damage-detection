import streamlit as st
from model_helper import predict

st.title("Car Damage Detection")

upload_file = st.file_uploader("Upload car image", type=["jpg", "jpeg", "png" ])

if upload_file:
    image_path = 'temp_file.jpg'
    with open(image_path, 'wb') as f:
        f.write(upload_file.getbuffer())
        prediction = predict(image_path)
        st.image(upload_file, caption='Uploaded Image' , use_column_width=True)
        st.info(f"Predicted class is : {prediction}")
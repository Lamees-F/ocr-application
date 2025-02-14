import streamlit as st
import easyocr
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="OCR mini project")


reader = easyocr.Reader(['en','ar'])  

st.title("📸 OCR App - Extract Text using EasyOCR")

st.write("Upload an image or take a picture using the camera to extract text.")

option = st.radio("Choose an input method:", ("Upload an Image", "Capture from Camera"))

if option == "Upload an Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)

elif option == "Capture from Camera":
    captured_image = st.camera_input("Take a picture")
    if captured_image is not None:
        image = Image.open(captured_image)

if 'image' in locals():
    img_np = np.array(image)
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

    st.image(image, caption="Original Image", use_container_width=True)

    extracted_text = reader.readtext(gray, detail=0)  

    st.subheader("Extracted Text")
    st.text_area("Text Output", "\n".join(extracted_text), height=200)

    if extracted_text:
        st.download_button(
            label="Download Text",
            data="\n".join(extracted_text),
            file_name="extracted_text.txt",
            mime="text/plain"
        )

import streamlit as st
from cv2 import GaussianBlur, bilateralFilter, filter2D, imdecode, IMREAD_COLOR
import numpy as np
from io import BytesIO

import matplotlib
matplotlib.use('Agg')

versionNumber = '0.1'

def blur(img, blur_amount=5):
    if blur_amount == 7:
        dst2 = GaussianBlur(img, (7, 7), 0)
        dst = bilateralFilter(dst2, 7, 80, 80)
    else:
        dst2 = GaussianBlur(img, (5, 5), 0)
        dst = bilateralFilter(dst2, 7, 10 * blur_amount, 80)
    return dst

def sharp(img, sharp_point, sharp_low):
    s_kernel = np.array([[0, sharp_low, 0], [sharp_low, sharp_point, sharp_low], [0, sharp_low, 0]])
    sharpened = filter2D(img, -1, s_kernel)
    return sharpened

def remove_screentones(input_image, blur_amount=2, sh_point=5.56, sh_low=-1.14):
    img_array = np.asarray(bytearray(input_image.read()), dtype=np.uint8)
    img = imdecode(img_array, IMREAD_COLOR)
    blurred = blur(img, blur_amount)
    ret = sharp(blurred, sh_point, sh_low)
    return ret

def main():
    st.title("Dr. Screentone v." + versionNumber)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Removing Screentone...")

        output_image = remove_screentones(uploaded_file, blur_amount=2, sh_point=5.56, sh_low=-1.14)

        st.image(output_image, caption="Processed Image.", use_column_width=True)
        st.write("")

if __name__ == "__main__":
    main()

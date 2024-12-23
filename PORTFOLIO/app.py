import streamlit as st
import os
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Anusha's Portfolio", layout="wide")

# Add simple inline CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e; /* Dark mode background */
            color: white; /* Text color for dark mode */
        }
        .main-header {
            font-size: 28px;
            font-weight: bold;
            color: #4CAF50; /* Green heading */
        }
        .sub-text {
            font-size: 16px;
            color: white;
            margin-top: 5px;
        }
        .section-header {
            font-size: 22px;
            font-weight: bold;
            color: #4CAF50; /* Green heading */
            margin-top: 20px;
        }
        .text-box {
            margin-bottom: 15px;
        }
        .education-container, .project-container {
            margin-bottom: 20px;
            padding: 15px;
            background-color: #2e2e2e; /* Slightly lighter dark mode box */
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        os.path.join(os.getcwd(), "assests", "anndy.png"),
        width=200,
        caption="Anusha"
    )

with col2:
    st.markdown('<div class="main-header">Anusha Portfolio</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Full Stack Python Developer</div>', unsafe_allow_html=True)
    st.write("""
        As a fresher, I am working on improving my skills professionally. 
        I am committed to delivering results and striving for excellence continuously.
    """)

    # Resume download button
    resume_path = "assests/resume.pdf"
    with open(resume_path, "rb") as resume_file:
        st.download_button(
            label="Download Resume",
            data=resume_file,
            file_name="resume.pdf",
            mime="application/pdf"
        )

# About Me Section
st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
st.write("""
    I am a passionate software developer with a focus on Full Stack development and AI technologies. 
    I enjoy solving complex problems and building efficient, scalable solutions.
""")

# Education Section
st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="education-container">
        <b>B.Sc. Computer Science</b><br>
        Government Arts and Science College for Women, Puliakulam<br>
        <i>Percentage:</i> 77%<br>
        <i>2021 - 2024</i>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="education-container">
        <b>XII - Standard</b><br>
        CMS Matriculation Higher Secondary School, Ganapathy<br>
        <i>Percentage:</i> 87%<br>
        <i>2020 - 2021</i>
    </div>
""", unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        os.path.join(os.getcwd(), "assests", "1.png"),
        caption="proj1"
    )
    st.markdown("""
        <div class="project-container">
            <p>A Web Application for Visually Impaired Low Vision People</p>
            <p>01/2024 - 05/2024, Coimbatore, India</p>
            Developed using Python.<br>
            EYE-C is a real-time object detection system developed with Python, OpenCV, and YOLOV5.<br>
            It assists users with low vision or blindness by providing a voice assistant and text-to-speech functionality.
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(
        os.path.join(os.getcwd(), "assests", "2.png"),
        caption="proj2"
    )
    st.markdown("""
        <br>
        <div class="project-container">
            <p>Responsive Educational Website</p>
            <p>08/2024, Coimbatore, India</p>
            Implemented a responsive educational website using HTML, CSS, and JavaScript, ensuring a user-friendly experience
            across various devices and enhancing accessibility to learning resources.
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.image(
        os.path.join(os.getcwd(), "assests", "3.png"),
        caption="proj3"
    )
    st.markdown("""
        <br>
        <div class="project-container">
            <p>Responsive Furniture Decoration Website</p>
            <p>10/2024, Coimbatore, India</p>
            Designed and implemented a multi-page furniture decoration website using HTML, CSS, JavaScript, and Bootstrap,
            highlighting modern design principles and enhancing user experience through interactive elements and a visually
            appealing layout.
        </div>
    """, unsafe_allow_html=True)



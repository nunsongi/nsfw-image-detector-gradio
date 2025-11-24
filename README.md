# 🛡️ Safe Content Classifier (NSFW Detector)

A Computer Vision application that automatically detects whether an image contains explicit content (NSFW) or is safe for public viewing (Normal).

Built with **Python**, **Hugging Face Transformers**, and **Gradio**.

[![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/nunsongi/detector-seguridad-demo)

## 🚀 Project Overview

This project leverages a pre-trained Deep Learning model to analyze images in real-time. It serves as a content moderation tool, useful for platforms that need to filter user-generated content automatically.

**Key Features:**
* **Image Classification:** Categorizes images into 'Normal' or 'NSFW'.
* **Confidence Score:** Provides a probability percentage for the prediction.
* **User Interface:** Simple web interface built with Gradio.

## 📺 Video Demo

Watch the full 1-minute demonstration of how the classifier works:

[![Watch the video](https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg)](https://youtu.be/izr9VzMsoh0)

## 📓 Research & Experimentation

Before building the app, I tested the model and logic using Google Colab. You can view the experimentation process here:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](nsfw_image_detector_gradio.ipynb)

*Check the file `nsfw_image_detector_gradio.ipynb` in this repository to see the testing phase.*

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **ML Library:** Transformers (Hugging Face)
* **Interface:** Gradio SDK
* **Model:** [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection)

## 📦 Installation & Usage

To run this project locally on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/nunsongi/nsfw-image-detector-gradio](https://github.com/nunsongi/nsfw-image-detector-gradio)
    cd nsfw-image-detector-gradio
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    python app.py
    ```

4.  Open your browser at the URL provided in the terminal (usually `http://127.0.0.1:7860`).

## 📄 File Structure

* `app.py`: Main application logic and UI definition.
* `requirements.txt`: List of Python dependencies.
* `README.md`: Project documentation.

## 🤝 Credits

* Model by [Falconsai](https://huggingface.co/Falconsai).
* Powered by [Hugging Face](https://huggingface.co/).

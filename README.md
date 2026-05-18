# AI-Based Mental Health Conversational Chatbot

An AI-powered conversational chatbot that implicitly detects signs of anxiety, depression, and mood variations through natural conversations — without directly asking the user about their mental state.

The project combines Natural Language Processing (NLP) and Computer Vision techniques to build a privacy-focused multimodal mental health assistance system suitable for real-time interaction.

---

## Features

- Implicit mental health detection
- Multi-turn conversation analysis
- DistilBERT + BiLSTM architecture
- Facial emotion recognition
- Multimodal fusion pipeline
- Privacy-preserving inference
- Real-time conversational analysis
- Lightweight and efficient model pipeline

---

## Tech Stack

- Python
- DistilBERT
- BiLSTM
- DeepFace
- OpenCV
- PyTorch / TensorFlow
- Hugging Face Transformers

---

## System Architecture

User Input → DistilBERT → BiLSTM → Mood Analysis  
                        ↘  
                DeepFace Emotion Detection  
                        ↘  
                 Late Fusion → Final Prediction

### Fusion Strategy
- 70% Text Signal
- 30% Visual Signal

---

## Dataset Used

- FER2013 (Facial Emotion Recognition Dataset)
- Custom conversational text dataset
- Emotion-labelled dialogue datasets

---

## Installation

```bash
git clone https://github.com/your-username/project-name.git
cd project-name
pip install -r requirements.txt
```

---

## Usage

```bash
python app.py
```

Run the chatbot interface and start interacting naturally with the system.

---

## Project Structure

```bash
project/
│── models/
│── datasets/
│── chatbot/
│── vision_module/
│── fusion/
│── app.py
│── requirements.txt
│── README.md
```

---

## Privacy & Ethics

- No raw conversations are stored
- Personally Identifiable Information (PII) is removed before processing
- Supports local on-device inference
- Designed for supportive analysis, not clinical diagnosis

---

## Research Contribution

This project extends existing research on mental health NLP systems by enabling:

- Real-time multi-turn dialogue analysis
- Mood drift detection across conversations
- Multimodal emotional inference
- Privacy-preserving local processing

The work is inspired by and extends:
- Aggarwal et al. (arXiv 2025)

---

## Future Improvements

- Speech emotion recognition
- Real-time voice interaction
- Personalized emotional adaptation
- Reinforcement learning-based empathetic responses
- Mobile and edge-device deployment

---

## Demo

Add screenshots or demo images here.

```markdown
![Chatbot Demo](images/demo.png)
```

---

## Disclaimer

This project is intended for academic and research purposes only. It is not a replacement for professional mental health diagnosis or treatment.

---

## Authors

- Pratik Sen #77
- Mohak Biswas #78
 
---

## License

This project is licensed under the MIT License.

---

## Keywords

Mental Health NLP, DistilBERT, BiLSTM, Multimodal Fusion, DeepFace, Privacy-by-Design, Empathetic Chatbot, Mood Drift Detection.

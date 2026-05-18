This B.Tech research project proposes a conversational AI chatbot that implicitly detects signs of anxiety, depression,
and mood states from natural user interactions — without ever asking the user directly. The system uses a fine-tuned
DistilBERT model (40% smaller, 60% faster than BERT, retaining 97% of its understanding) augmented with a
Bidirectional LSTM (BiLSTM) layer that captures mood drift across multi-turn dialogue. A secondary image-processing
module performs facial emotion analysis via DeepFace / FER2013 and is combined with the text signal through late
fusion (70% text + 30% visual), forming a fully multimodal mental health inference pipeline. Privacy is first-class: no raw
conversation text is stored, all inference runs locally on-device, and all data is PII-stripped before processing. This project
extends Aggarwal et al. (arXiv 2025) by shifting from static Reddit posts to real-time, privacy-preserving, multi-turn
dialogue analysis.

Keywords: Mental Health NLP, DistilBERT, BiLSTM, Multimodal Fusion, DeepFace, Privacy-by-Design, Empathetic
Chatbot, Mood Drift Detection.

Authors- Pratik Sen ,Mohak Biswas

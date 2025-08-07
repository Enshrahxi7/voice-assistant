# voice-assistant
 # Smart Arabic Voice Assistant

# Project Idea:
An intelligent Arabic voice assistant that quickly understands user speech, responds contextually, and replies with natural, human-like voices—all in a few seconds. Built with a modular Python structure and a modern web interface.

# Key Features:
 • Fast response time ( 6 seconds)
 • Realistic voice replies using ElevenLabs
 • Advanced Arabic understanding via Cohere NLP
 • Sleek and interactive web interface
 • Simple, modular, and scalable codebase

# Development Setup:
Developed using Python (Anaconda environment) with clean, extendable file organization.

 # Libraries Used in the Project
To build a fast and intelligent Arabic voice assistant, the following libraries were integrated, each serving a key function in the system:

# Audio Input & Output
 • sounddevice – captures live audio from the microphone
 • pygame – plays audio responses seamlessly
 • gTTS – generates Arabic speech from text using Google Text-to-Speech
 • io.BytesIO – enables in-memory audio streaming without saving files

# Speech Recognition & NLP
 • faster_whisper – performs quick and accurate Arabic speech-to-text
 • cohere – understands context and generates smart, Arabic-aware replies

# Core Utilities & Processing
 • numpy – processes and handles audio data efficiently
 • requests – sends and receives data from external APIs
 • flask – powers the web-based interface for user interaction
These tools form a cohesive and extensible system for real-time Arabic voice interaction.

 # Running the Project – Step-by-Step Guide
Here’s how to set up and launch the Arabic Voice Assistant on your machine:

1️⃣ Set Up the Environment
 • Make sure you have Anaconda installed.
 • Launch the Anaconda Prompt.

2️⃣ Create and Activate a Virtual Environment
conda create -n arabic_voice_assistant python=3.10  
conda activate arabic_voice_assistant

3️⃣ Install Required Libraries
Use pip to install all dependencies in one command:
pip install faster-whisper sounddevice numpy cohere requests pygame flask gTTS

4️⃣ Open the Project in VS Code
In the same terminal, navigate to the project folder (or clone it), then run:
code .

5️⃣ Run the Application
Make sure all project files are in place.

# Project Showcase
![ai](ai.mp4)

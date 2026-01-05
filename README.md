Friday AI – Modular Voice-Based Intelligent Assistant

Friday AI is a modular, voice-driven intelligent assistant framework built in Python that continuously listens for a wake word, interprets spoken commands, executes system-level actions, and generates intelligent spoken responses.

The project focuses on clean architecture, extensibility, and real-time human–computer interaction, making it suitable as a foundation for advanced assistant systems.

🚀 Key Capabilities

🎙️ Wake-word–based activation system

🗣️ Real-time speech-to-text command ingestion

🧠 Context-aware intelligent response generation

🔊 Natural-sounding text-to-speech output

🌐 Automated web navigation & system actions

🎵 Media playback via custom libraries

📰 Live information retrieval and summarization

🧩 Highly modular, extensible codebase

🏗️ Project Architecture
friday-ai/
│
├── main.py                  # Runtime entry point & control loop
├── client.py                # Intelligent inference client abstraction
├── musicLibrary.py          # Media mapping & playback configuration
│
├── assistant/
│   ├── __init__.py
│   ├── ai.py                # Cognitive response pipeline
│   ├── speech.py            # Speech synthesis engine
│   ├── listener.py          # Audio input & recognition layer
│   └── commands.py          # Intent routing & command execution
│
├── test_gemini.py           # Inference validation module
├── requirements.txt
└── README.md

🔹 Design Philosophy

Clear separation of concerns

Loosely coupled subsystems

Scalable for future enhancements

Production-style code organization

🧠 System Workflow

The assistant runs in a persistent listening loop

Activation occurs upon detecting a predefined wake phrase

Spoken input is converted into structured commands

Commands are routed through an intent-handling layer

Responses are dynamically generated or executed

Output is delivered via synthesized speech

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/friday-ai.git
cd friday-ai

2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Environment Configuration

The system relies on external services for inference and data retrieval.

Set required environment variables before running:

Windows (PowerShell)
setx GEMINI_API_KEY "your_key_here"

Linux / macOS
export GEMINI_API_KEY="your_key_here"


⚠️ API keys are intentionally not hardcoded for security and scalability.

▶️ Running the Assistant
python main.py


Expected startup message:

Initializing Friday


Say the wake word, followed by commands such as:

“Open YouTube”

“Play believer”

“Summarize today’s news”

“Explain machine learning”

🎵 Media Configuration

Custom media commands are defined in musicLibrary.py:

music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}

📰 Information Retrieval

Friday can fetch and vocalize real-time information such as headlines and summaries using external data sources.

Relevant credentials can be configured inside:

assistant/commands.py

🧪 System Validation

A standalone validation module is provided to test the inference pipeline:

python test_gemini.py

🛠️ Technology Stack

Python 3

Speech recognition & synthesis systems

Real-time audio processing

External inference APIs

Modular command routing architecture

(Specific implementations are abstracted for flexibility)

🔮 Planned Enhancements

Conversational memory & context tracking

Offline speech processing support

GUI-based interaction layer

Asynchronous execution pipeline

Plugin-based skill system

Voice authentication

🎯 Applications

Intelligent assistant research

Human–computer interaction projects

AI systems prototyping

Resume & internship portfolios

Hackathons & demos

👨‍💻 Author

Ayush Kumar Singh
B.Tech – Computer Science (AI)

Interests:
AI Systems • ML • Data Engineering • Intelligent Applications

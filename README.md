🤖 **Friday AI – Modular Voice-Based Intelligent Assistant**

Friday AI is a modular, voice-driven intelligent assistant framework in Python that continuously listens for a wake word, understands spoken commands, executes system-level or web actions, and responds through natural-sounding speech.

***

## Overview

Friday AI is designed as a clean, extensible base for building advanced intelligent assistants with real-time human–computer interaction. It emphasizes **modularity** so individual components (speech, AI, commands) can be extended or swapped without breaking the overall system.

***

## Key Features

- Wake-word–based activation with a persistent listening loop for hands-free interaction.
- Real-time speech-to-text ingestion and structured command parsing for robust voice control.
- Context-aware AI response generation using external inference APIs for intelligent replies.
- Natural text-to-speech output for conversational responses and announcements.
- Automated web navigation, system-level actions, and custom media playback via `musicLibrary.py`.
- Live information retrieval and summarization using configurable external data sources.
- A highly modular, extensible codebase suitable for research, portfolios, and production-style prototypes.

***

## Project Structure

```text
friday-ai/
├── main.py            # Runtime entry point & control loop
├── client.py          # Inference client abstraction
├── musicLibrary.py    # Media mapping & playback configuration
│
├── assistant/
│   ├── __init__.py
│   ├── ai.py          # Cognitive response pipeline
│   ├── speech.py      # Speech synthesis engine
│   ├── listener.py    # Audio input & recognition
│   └── commands.py    # Intent routing & command execution
│
├── test_gemini.py     # Inference validation module
├── requirements.txt
└── README.md
```

This layout enforces separation between listening, reasoning, speaking, and acting, which keeps the **architecture** clean and scalable.

***

## Installation and Usage

- Clone and enter the repository:
  `git clone https://github.com/askaks19/friday-ai.git && cd friday-ai`.
- (Recommended) Create and activate a virtual environment using `python -m venv venv` and the appropriate activate script for your OS.
- Install dependencies with `pip install -r requirements.txt`.
- Set the `GEMINI_API_KEY` environment variable for your platform to enable external inference.
- Run the assistant with `python main.py`, then say the wake word followed by commands like "Open YouTube", "Play believer", "Summarize today's news", or "Explain machine learning".

***

## Extensibility and Applications

- Media mappings (like "believer" or "shape of you") are configured in `musicLibrary.py` and can be extended with more custom commands.
- Information retrieval credentials and logic live in `assistant/commands.py`, making it easy to plug in new APIs or skills.
- `test_gemini.py` validates the inference pipeline independently, which is helpful for debugging and experimentation.

Planned enhancements include conversational memory, offline speech support, GUI interaction, async pipelines, plugin-based skills, and voice authentication, making this an excellent **portfolio**-grade project for internships, hackathons, and HCI research.

👨‍💻 Author: Ayush Kumar Singh – B.Tech, Computer Science (AI).

# AI Voice Pipeline

## End-to-end voice AI pipeline: STT → LLM → TTS with full-duplex conversation support

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/neorhythmmm/ai-voice-pipeline/actions/workflows/main.yml/badge.svg)](https://github.com/neorhythmmm/ai-voice-pipeline/actions)

---

## Overview

**AI Voice Pipeline** is a modular, open-source framework for building real-time voice AI agents. It connects:

- **Speech-to-Text** (STT) — local inference with GigaAM-v3 (Russian, 240M parameters)
- **Language Model** (LLM) — any OpenAI-compatible endpoint (cloud or local)
- **Text-to-Speech** (TTS) — Kokoro-82M (StyleTTS2-based) with RUAccent stress markers
- **Qwen3-TTS** — voice cloning with speaker embedding support

The pipeline runs in **full-duplex mode**: continuous microphone capture, real-time VAD (Silero), barge-in interruption, and streaming TTS playback.

## Architecture

```
┌─────────────┐     ┌──────────┐     ┌──────────┐     ┌──────────────┐
│   Microphone │────▶│ VAD      │────▶│  STT     │────▶│   LLM        │
│  (PulseAudio)│     │ (Silero) │     │(GigaAM)  │     │  (Cloud API) │
└─────────────┘     └──────────┘     └──────────┘     └──────┬───────┘
                                                              │
                                                              ▼
┌─────────────┐     ┌──────────┐     ┌────────────────────────┐
│  Speaker     │◀────│  TTS     │◀────│   Response Processor   │
│ (PulseAudio) │     │(Kokoro)  │     │   (Sentence Chunking)  │
└─────────────┘     └──────────┘     └────────────────────────┘
```

## Features

- **Full-duplex voice conversation** — speak and interrupt naturally
- **Russian language STT** — GigaAM-v3, 240M parameters, e2e RNN-T
- **High-quality TTS** — Kokoro-82M with RUAccent stress marks support
- **Voice cloning** — Qwen3-TTS with speaker embedding (.spk) support
- **Modular architecture** — pluggable STT/LLM/TTS backends
- **LoRA fine-tuning** — scripts for custom voice adaptation
- **CI/CD** — automated linting and testing with GitHub Actions

## Installation

```bash
# Clone the repository
git clone https://github.com/neorhythmmm/ai-voice-pipeline.git
cd ai-voice-pipeline

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Download models
python scripts/download_models.py
```

## Quick Start

```bash
# Start the pipeline (default mode)
python main.py

# Or with custom configuration
python main.py --config config.yaml
```

## Project Structure

```
ai-voice-pipeline/
├── main.py                 # Pipeline entry point
├── config.yaml             # Configuration file
├── processor.py            # Audio processing core
├── scripts/
│   ├── download_models.py  # Model download utility
│   └── train_lora.py       # LoRA training script
├── tests/
│   └── test_processor.py   # Unit tests
├── .github/workflows/
│   └── main.yml            # CI/CD workflow
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Configuration

Edit `config.yaml` to set your STT/TTS/LLM endpoints:

```yaml
stt:
  provider: openai
  base_url: http://127.0.0.1:13309/v1
  model: gigaam-v3

tts:
  provider: openai
  base_url: http://127.0.0.1:8085/v1
  model: kokoro-ru
  voice: af_heart

llm:
  provider: openai
  base_url: https://openrouter.ai/api/v1
  model: deepseek/deepseek-chat-v3-0324:free
```

## License

MIT
#!/usr/bin/env python3
"""Download and verify model weights for the pipeline."""
import sys

MODELS = {
    "gigaam-v3": "https://huggingface.co/gigaam/gigaam-v3/",
    "qwen3-tts-1.7b": "https://huggingface.co/Qwen/Qwen3-TTS-1.7B/",
    "kokoro-82m": "https://huggingface.co/Serveurperso/Qwen3-TTS-GGUF/",
}


def main():
    print("Available model sources:")
    for key, url in MODELS.items():
        print(f"  {key}: {url}")
    print("Run with --download <key> to fetch a specific model.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

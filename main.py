#!/usr/bin/env python3
"""
main.py — AI Voice Pipeline entry point.

Full-duplex voice conversation pipeline:
Microphone → VAD (Silero) → STT (GigaAM) → LLM → TTS (Kokoro) → Speaker

Usage: python main.py [--config config.yaml]
"""
import argparse
import asyncio
import logging
import sys
from pathlib import Path

import yaml

from processor import AudioProcessor, PipelineConfig

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("voice-pipeline")


def load_config(path: str = "config.yaml") -> PipelineConfig:
    with open(path, "r") as f:
        raw = yaml.safe_load(f)
    return PipelineConfig.from_dict(raw)


async def run_pipeline(cfg: PipelineConfig) -> None:
    processor = AudioProcessor(cfg)
    logger.info("Starting voice pipeline (full-duplex mode)")
    logger.info(f"STT: {cfg.stt.provider} ({cfg.stt.model})")
    logger.info(f"TTS: {cfg.tts.provider} ({cfg.tts.model})")
    logger.info(f"LLM: {cfg.llm.provider} ({cfg.llm.model})")

    try:
        await processor.run()
    except KeyboardInterrupt:
        logger.info("Shutdown requested")
    finally:
        await processor.cleanup()


def main():
    parser = argparse.ArgumentParser(description="AI Voice Pipeline")
    parser.add_argument("--config", default="config.yaml", help="Path to config file")
    args = parser.parse_args()

    if not Path(args.config).exists():
        logger.error(f"Config file not found: {args.config}")
        sys.exit(1)

    cfg = load_config(args.config)
    asyncio.run(run_pipeline(cfg))


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""test_processor.py — Minimal sanity test for audio pipeline."""
import sys
sys.path.insert(0, ".")

from processor import PipelineConfig, AudioProcessor


def test_config_default():
    cfg = PipelineConfig()
    assert cfg.sample_rate == 16000
    assert cfg.tts.voice == "af_heart"


def test_config_from_dict():
    cfg = PipelineConfig.from_dict({"stt": {"model": "test-model"}, "pipeline": {"sample_rate": 22050}})
    assert cfg.stt.model == "test-model"
    assert cfg.sample_rate == 22050


if __name__ == "__main__":
    test_config_default()
    test_config_from_dict()
    print("All tests passed.")

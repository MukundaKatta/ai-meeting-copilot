"""Tests for MeetingCopilot."""
import pytest
from src.meetingcopilot import MeetingCopilot

def test_init():
    obj = MeetingCopilot()
    stats = obj.get_stats()
    assert stats["total_ops"] == 0

def test_operation():
    obj = MeetingCopilot()
    result = obj.start_recording(input="test")
    assert result["processed"] is True
    assert result["operation"] == "start_recording"

def test_multiple_ops():
    obj = MeetingCopilot()
    for m in ['start_recording', 'transcribe_segment', 'extract_action_items']:
        getattr(obj, m)(data="test")
    assert obj.get_stats()["total_ops"] == 3

def test_caching():
    obj = MeetingCopilot()
    r1 = obj.start_recording(key="same")
    r2 = obj.start_recording(key="same")
    assert r2.get("cached") is True

def test_reset():
    obj = MeetingCopilot()
    obj.start_recording()
    obj.reset()
    assert obj.get_stats()["total_ops"] == 0

def test_stats():
    obj = MeetingCopilot()
    obj.start_recording(x=1)
    obj.transcribe_segment(y=2)
    stats = obj.get_stats()
    assert stats["total_ops"] == 2
    assert "ops_by_type" in stats

"""Tests for AiMeetingCopilot."""
from src.core import AiMeetingCopilot
def test_init(): assert AiMeetingCopilot().get_stats()["ops"] == 0
def test_op(): c = AiMeetingCopilot(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = AiMeetingCopilot(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = AiMeetingCopilot(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = AiMeetingCopilot(); r = c.process(); assert r["service"] == "ai-meeting-copilot"

"""CLI for ai-meeting-copilot."""
import sys, json, argparse
from .core import AiMeetingCopilot

def main():
    parser = argparse.ArgumentParser(description="Real-time meeting assistant — transcription, action items, and follow-up generation")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = AiMeetingCopilot()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"ai-meeting-copilot v0.1.0 — Real-time meeting assistant — transcription, action items, and follow-up generation")

if __name__ == "__main__":
    main()

"""Basic usage example for ai-meeting-copilot."""
from src.core import AiMeetingCopilot

def main():
    instance = AiMeetingCopilot(config={"verbose": True})

    print("=== ai-meeting-copilot Example ===\n")

    # Run primary operation
    result = instance.process(input="example data", mode="demo")
    print(f"Result: {result}")

    # Run multiple operations
    ops = ["process", "analyze", "transform]
    for op in ops:
        r = getattr(instance, op)(source="example")
        print(f"  {op}: {"✓" if r.get("ok") else "✗"}")

    # Check stats
    print(f"\nStats: {instance.get_stats()}")

if __name__ == "__main__":
    main()

from pathlib import Path


class Paths(object):
    root = Path(__file__).parent
    prompts = root / "prompts"
    generic_prompt = prompts / "dalle3_prompt.md"

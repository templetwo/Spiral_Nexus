#!/usr/bin/env python3
import os, zipfile, textwrap, pathlib

ROOT = pathlib.Path("/home/oai/share/living_spiral_nexus")
FILES = {
    "ingestion/__init__.py": "",
    "ingestion/main.py": textwrap.dedent("""
        \"\"\"FastAPI skeleton for scroll ingestion.\"\"\"
        from fastapi import FastAPI
        app = FastAPI(title="Living Spiral Nexus – Ingestion")

        @app.get("/health")
        def health():
            return {"status": "breathing"}
    """),
    "ingestion/embeddings.py": textwrap.dedent("""
        \"\"\"Tone‑vector placeholder embedding logic.\"\"\"
        def embed(text: str):
            # TODO: Replace with real Siamese model
            return [0.0] * 6
    """),
    "ingestion/models.py": textwrap.dedent("""
        \"\"\"Pydantic data models for Scroll & Mirror.\"\"\"
        from pydantic import BaseModel
        class Scroll(BaseModel):
            id: str
            content: str
            tone_vector: list[float]
            visibility: str
    """),
    "ingestion/tests/test_health.py": textwrap.dedent("""
        from ingestion.main import app
        from fastapi.testclient import TestClient
        client = TestClient(app)
        def test_health():
            assert client.get('/health').json() == {'status': 'breathing'}
    """),
    "scheduler/__init__.py": "",
    "scheduler/heartbeat.py": textwrap.dedent("""
        \"\"\"APScheduler stub for daily reflections.\"\"\"
        def breathe():
            print("✨ Nexus inhales… exhales…")
    """),
    "plugins/discord_bot/bot.py": textwrap.dedent("""
        \"\"\"Minimal Discord bot stub for !glyph command.\"\"\"
        import os, discord, asyncio
        class SpiralBot(discord.Client):
            async def on_ready(self):
                print(f'Logged in as {self.user}')
            async def on_message(self, msg):
                if msg.content.startswith('!glyph'):
                    await msg.channel.send('🔍 Resonance not yet implemented.')
        if __name__ == '__main__':
            token = os.getenv('DISCORD_TOKEN', 'replace-me')
            SpiralBot(intents=discord.Intents.default()).run(token)
    """),
    "plugins/local_llm/mirror.py": textwrap.dedent("""
        \"\"\"Local LLM mirror stub.\"\"\"
        def pull_scrolls():
            pass
        def push_echo():
            pass
    """),
    "ui/README.md": "# UI placeholder – SvelteKit constellation coming soon\n",
    "docs/nexus_blueprint.md": "",  # Will be copied from existing blueprint later
    ".gitignore": "venv/\n__pycache__/\n*.pyc\n.env\n",
    "README.md": "# Living Spiral Nexus – Seed\n",
    "requirements.txt": "fastapi\nuvicorn\npydantic\napscheduler\ndiscord.py\nqdrant-client\n",
    "pyproject.toml": textwrap.dedent("""
        [tool.poetry]
        name = "living-spiral-nexus"
        version = "0.1.0"
        description = "Breathing archive of scrolls and glyphs"
        authors = ["Spiral Core"]
        [tool.poetry.dependencies]
        python = "^3.11"
        fastapi = "*"
        uvicorn = "*"
        pydantic = "*"
        apscheduler = "*"
        discord.py = "*"
        qdrant-client = "*"
    """),
}

def main():
    # 1. Create directories & files
    for path, content in FILES.items():
        file_path = ROOT / path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if content:
            file_path.write_text(content.strip() + "\n")
        else:
            file_path.touch()
    # 2. Copy blueprint into docs
    blueprint_src = pathlib.Path("/home/oai/share/docs/nexus_blueprint.md")
    if blueprint_src.exists():
        blueprint_dst = ROOT / "docs/nexus_blueprint.md"
        blueprint_dst.write_text(blueprint_src.read_text())
    # 3. Zip everything
    zip_path = pathlib.Path("/home/oai/share/living_spiral_nexus_seed.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in ROOT.rglob("*"):
            zf.write(file, file.relative_to(ROOT.parent))
    print(f"✅ Seed created at {zip_path}")

if __name__ == "__main__":
    main()
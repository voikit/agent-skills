"""Helpers shared by the repo scripts. Standard library only."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")

# shared/<file>  -> copied into skills/<skill>/references/<file>
# templates/<file> -> copied into skills/<skill>/assets/<file>
# shared/scripts/<file> -> copied into skills/<skill>/scripts/<file>
# "*" means every skill.
SYNC_MAP = {
    "shared/operating-rules.md": ("references", "*"),
    "shared/answering-modes.md": (
        "references",
        [
            "voikit-onboarding",
            "voikit-call-center",
            "voikit-industry-playbooks",
            "voikit-premium-scenario-design",
        ],
    ),
    "shared/panel-only.md": (
        "references",
        [
            "voikit-mcp",
            "voikit-onboarding",
            "voikit-call-center",
            "voikit-conversations",
            "voikit-support",
            "voikit-premium-onboarding",
            "voikit-premium-scenario-design",
        ],
    ),
    "shared/scripts/text_check.py": (
        "scripts",
        ["voikit-ai-agents", "voikit-business-memory", "voikit-instagram-automation"],
    ),
    "templates/business-brief.md": (
        "assets",
        ["voikit-onboarding", "voikit-premium-onboarding", "voikit-premium-intake"],
    ),
    "templates/proposal.md": ("assets", ["voikit-premium-scenario-design"]),
    "templates/handover.md": ("assets", ["voikit-premium-handover"]),
    "templates/golive-checklist.md": (
        "assets",
        ["voikit-qa-testing", "voikit-onboarding", "voikit-premium-handover"],
    ),
}


def skill_names():
    return sorted(
        d
        for d in os.listdir(SKILLS_DIR)
        if os.path.isfile(os.path.join(SKILLS_DIR, d, "SKILL.md"))
    )


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_frontmatter(text):
    """Minimal YAML subset: `key: value`, folded `key: >-` blocks, one-level maps."""
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    raw, body = text[4:end], text[end + 5 :]
    data, key, mode = {}, None, None
    for line in raw.split("\n"):
        if not line.strip():
            continue
        if line[0] not in " \t":
            k, _, v = line.partition(":")
            k, v = k.strip(), v.strip()
            if v in (">-", ">", "|", "|-"):
                data[k], key, mode = "", k, "text"
            elif v == "":
                data[k], key, mode = {}, k, "map"
            else:
                data[k], key, mode = v.strip("\"'"), None, None
        elif key and mode == "text":
            data[key] = (data[key] + " " + line.strip()).strip()
        elif key and mode == "map":
            k, _, v = line.strip().partition(":")
            data[key][k.strip()] = v.strip().strip("\"'")
    return data, body

# Releasing

A release gives people one file, `voikit.zip`, at an address that never changes:

    https://github.com/voikit/agent-skills/releases/latest/download/voikit.zip

Everything else on this page exists so that file always installs cleanly.

## What is automatic

`scripts/build_release.py` builds the zip and refuses to finish when:

- the lint fails (tool names, shared copies, ASCII, banned terms);
- the zip does not have exactly one top-level folder and exactly one `SKILL.md`;
- the skill name, the description or a frontmatter key would be refused by an upload page;
- a file sits outside the standard folders (`references/`, `assets/`, `scripts/`, `agents/`);
- with `--tag`: the tag is not the version in `.claude-plugin/plugin.json`, or `CHANGELOG.md` has no dated section for it.

The release workflow runs that script for every `v*` tag and attaches only the files listed in `dist/RELEASE_ASSETS.txt`. The validate workflow runs it on every push and pull request, so a change that would break the zip is caught before a release.

## What a person does (ten minutes)

1. **Version.** Set `"version"` in `.claude-plugin/plugin.json`. Add a `## X.Y.Z - YYYY-MM-DD` section to `CHANGELOG.md`, written for the people who use the skills.
2. **Build.** `python3 scripts/build_release.py --tag vX.Y.Z`
3. **Try the real file** in each app you name in the README. Automatic checks cover the shape of the zip; only an upload proves the app takes it.

   | App | Do | Pass when |
   |---|---|---|
   | Claude | Upload `dist/voikit.zip` in the skills settings | The preview shows one skill named `voikit`, no error |
   | ChatGPT | Skills, Create, Upload from your computer | The skill is installed and can be picked in a chat |
   | Both | New chat: "Connect my Voikit account" | It asks which address you sign in with and goes one step at a time |
   | Both, connected | "Check my connection and tell me what you can do" | It calls `capabilities` and offers the numbered choices |

   If an app refuses the zip, read the message, fix the cause in `scripts/build_release.py` (add the rule to `check_zip` so it can never ship again), and rebuild.
4. **Publish.** Commit, push, then:

       git tag vX.Y.Z && git push origin vX.Y.Z

5. **Confirm.** Open the release: it shows `voikit.zip` and `SHA256SUMS.txt`. Download from the latest address above and compare the checksum.

## Rules that keep releases boring

- One download for everybody. Do not attach other zips to a release: people pick the wrong one. Single-skill zips are built into `dist/single-skills/` for whoever needs them.
- Never rename `voikit.zip` or the skill `voikit`: the latest address, the README and installed copies depend on the name.
- Never re-tag a published version. Fix forward with the next patch version.
- A zip of the repository (GitHub's "Source code") is not installable; the release notes say so at the top.
- Workflow files live in `docs/ci/`. After changing one, copy it again: `cp docs/ci/*.yml .github/workflows/`.

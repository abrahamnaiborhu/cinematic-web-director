#!/usr/bin/env python3
"""Build a reproducible, versioned skill ZIP and SHA-256 manifest offline."""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import tempfile
import zipfile
from pathlib import Path


RELEASE_FILES = (
    'README.md', 'SKILL.md', 'TUTORIAL.md', 'CHANGELOG.md',
    'references/CREATIVE_WORKFLOW.md', 'references/PREFLIGHT_PROTOCOL.md',
    'references/DESIGN_DIRECTION.md', 'evaluations/DESIGN_DIRECTION.md',
    'templates/PROJECT_SCRIPT.md', 'templates/CONTINUITY_BIBLE.md',
    'templates/SCENE_TREATMENT.md', 'templates/ITERATION_LOG.md',
    'scripts/preflight.py', 'scripts/package_release.py',
    'tests/test_preflight.py', 'tests/test_package_release.py',
)


def build_release(root: Path, version: str, output: Path) -> tuple[Path, Path]:
    """Package only the explicit distribution files after validating version and inputs."""
    if not re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)', version):
        raise ValueError('Version must be three numeric components, for example 0.2.0, without v.')
    root = root.resolve()
    for name in RELEASE_FILES:
        source = root / name
        if not source.is_file() or source.is_symlink() or not source.resolve().is_relative_to(root):
            raise ValueError(f'Missing or unsafe release file: {name}')
    heading = (root / 'README.md').read_text(encoding='utf-8').splitlines()[0]
    if heading != f'# Cinematic Web Director (v{version})':
        raise ValueError('Requested version must match the README heading.')
    changelog = (root / 'CHANGELOG.md').read_text(encoding='utf-8')
    if not re.search(r'^## \[' + re.escape(version) + r'\](?:\s|$)', changelog, re.MULTILINE):
        raise ValueError('Requested version needs a changelog entry.')

    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    archive = output / f'cinematic-web-director-v{version}.zip'
    checksum = output / 'SHA256SUMS.txt'
    with tempfile.NamedTemporaryFile(prefix='.release-', suffix='.zip', dir=output, delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as package:
            for name in sorted(RELEASE_FILES):
                info = zipfile.ZipInfo('cinematic-web-director/' + name, date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.compress_type = zipfile.ZIP_DEFLATED
                mode = 0o100755 if name.startswith('scripts/') else 0o100644
                info.external_attr = mode << 16
                package.writestr(info, (root / name).read_bytes(), compresslevel=9)
        digest = hashlib.sha256(temporary.read_bytes()).hexdigest()
        os.replace(temporary, archive)
        checksum.write_text(f'{digest}  {archive.name}\n', encoding='utf-8')
    finally:
        temporary.unlink(missing_ok=True)
    return archive, checksum


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', required=True, help='Release version without v, for example 0.2.0')
    parser.add_argument('--out', type=Path, default=Path('dist'), help='Artifact directory (default: ./dist)')
    args = parser.parse_args()
    try:
        archive, checksum = build_release(Path(__file__).resolve().parents[1], args.version, args.out)
    except (ValueError, OSError, UnicodeError) as exc:
        parser.error(str(exc))
    print(archive)
    print(checksum)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

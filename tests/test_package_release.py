"""Behavior tests for the versioned distribution archive."""
import hashlib
import os
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from package_release import build_release


CONTENTS = (
    'README.md', 'SKILL.md', 'TUTORIAL.md', 'CHANGELOG.md',
    'references/CREATIVE_WORKFLOW.md', 'references/PREFLIGHT_PROTOCOL.md',
    'templates/PROJECT_SCRIPT.md', 'templates/CONTINUITY_BIBLE.md',
    'templates/SCENE_TREATMENT.md', 'templates/ITERATION_LOG.md',
    'scripts/preflight.py', 'scripts/package_release.py',
    'tests/test_preflight.py', 'tests/test_package_release.py',
)


class ReleasePackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'source'
        for name in CONTENTS:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f'Fixture for {name}\n')
        (self.root / 'README.md').write_text('# Cinematic Web Director (v0.2.0)\n')
        (self.root / 'CHANGELOG.md').write_text('# Changelog\n\n## [0.2.0] - 2026-10-14\n')
        self.output = self.base / 'artifacts'

    def test_archive_contains_complete_package_in_one_directory(self):
        archive, checksum = build_release(self.root, '0.2.0', self.output)
        self.assertEqual(archive.name, 'cinematic-web-director-v0.2.0.zip')
        with zipfile.ZipFile(archive) as package:
            self.assertEqual(set(package.namelist()), {'cinematic-web-director/' + name for name in CONTENTS})
            self.assertIsNone(package.testzip())
            self.assertEqual(package.read('cinematic-web-director/SKILL.md'), (self.root / 'SKILL.md').read_bytes())
        digest, filename = checksum.read_text().strip().split('  ')
        self.assertEqual(filename, archive.name)
        self.assertEqual(digest, hashlib.sha256(archive.read_bytes()).hexdigest())

    def test_private_and_generated_files_are_excluded(self):
        for name in ('.env', '.git/config', '.DS_Store', 'dist/old.zip', '__pycache__/old.pyc'):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('excluded fixture')
        archive, _ = build_release(self.root, '0.2.0', self.output)
        with zipfile.ZipFile(archive) as package:
            self.assertEqual(len(package.namelist()), len(CONTENTS))
            self.assertFalse(any('/.git/' in name or name.endswith('.env') for name in package.namelist()))

    def test_archive_is_reproducible_across_source_mtime_changes(self):
        first, _ = build_release(self.root, '0.2.0', self.output)
        expected = first.read_bytes()
        for name in CONTENTS:
            os.utime(self.root / name, (1700000000, 1700000000))
        second, _ = build_release(self.root, '0.2.0', self.base / 'second')
        self.assertEqual(expected, second.read_bytes())

    def test_missing_file_fails_before_creating_artifacts(self):
        (self.root / 'templates/CONTINUITY_BIBLE.md').unlink()
        with self.assertRaises(ValueError):
            build_release(self.root, '0.2.0', self.output)
        self.assertFalse(self.output.exists())

    def test_version_must_be_safe_and_match_documentation(self):
        for version in ('../escape', 'v0.2.0', '0.2', '01.2.0', '1.0.0'):
            with self.subTest(version=version), self.assertRaises(ValueError):
                build_release(self.root, version, self.output)
        self.assertFalse(self.output.exists())

    def test_changelog_entry_is_required(self):
        (self.root / 'CHANGELOG.md').write_text('# Changelog\n')
        with self.assertRaises(ValueError):
            build_release(self.root, '0.2.0', self.output)

    def test_symlinked_payload_is_not_followed(self):
        target = self.base / 'outside.md'
        target.write_text('outside fixture')
        source = self.root / 'TUTORIAL.md'
        source.unlink()
        source.symlink_to(target)
        with self.assertRaises(ValueError):
            build_release(self.root, '0.2.0', self.output)


if __name__ == '__main__':
    unittest.main()

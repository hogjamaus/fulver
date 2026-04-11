# Full Versioning Specification

"Full Versioninig" or "FulVer" builds on "Semantic Versioning" or "SemVer" with and additional version number for EXTRA versioning aspects such as highly important development operations changes and some lesser changes such as assets or similar. The change is intended for tags and changelogs, not application skews or semantic logic. You can find the full document in [fulver.md](./fulver.md) and make suggestions here under [issues](https://github.com/hogjamaus/fulver). Once you begin using Full Versioning the `fulver-compat.py` script can be run to find match your version number within your `CHANGELOG.md` or `CHANGELOG.txt` for example and match the first fulver note it finds such as `1.2.3.1-beta-4635+build-2026.04.10` to create a `semver.txt` and `fulver.txt` so the developer can have each for other scripts if needed.

# Semantic Versioning Specification

"Semantic Versioning" or "SemVer" contains a set of rules and requirements that dictate how version numbers are assigned and incremented. You can find the full document in [semver.md](./semver.md) or visit our official website [semver.org](https://semver.org) to find previous versions and localized specifications.

Changes to the document are published to the website by a [GitHub Actions workflow](https://github.com/semver/semver.org/blob/gh-pages/.github/workflows/sync.yml) which runs once each day.

## Contributing

See the [contribution guide](./CONTRIBUTING.md).

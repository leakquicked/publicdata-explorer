# Public Data Explorer

Inspect a local CSV header for potentially sensitive columns.

## Usage
```bash
python publicdata_explorer.py sample.txt
python publicdata_explorer.py sample.txt --output report.json
```

Python 3.10+; standard library only. Reads only a local UTF-8 text file. No network access, scraping, or source-file modification.

## Detection rules
- `email`: review heuristic
- `location`: info heuristic
- `identifier`: review heuristic

Results are heuristic and require human validation. Use only public information or data you are authorized to review. Avoid committing personal or confidential data.

## Tests
`python -m unittest discover -s tests -v`

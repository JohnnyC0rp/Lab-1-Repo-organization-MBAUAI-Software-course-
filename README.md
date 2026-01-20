# Lab 1: Receipt Extraction CLI

This project processes a directory of receipt images, calls an OpenAI model to
extract structured fields (date, amount, vendor, category), and prints the
results as JSON.

## Project Structure
- `src/receipt_extractor/`: core package
- `receipts/`: sample receipt images (ignored by git)
- `docs/`: generated documentation (ignored by git)

## Setup
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running
Set your OpenAI API key, then run the CLI:
```bash
export OPENAI_API_KEY="your_key_here"
PYTHONPATH=src python -m receipt_extractor.main --print receipts
```

Or use the Makefile:
```bash
make run RECEIPTS_DIR=receipts
```

## Documentation
Generate API docs with:
```bash
pdoc src/receipt_extractor -o docs
```

## Notes
- The amount field is normalized to a float if it includes a `$` symbol.

## Git Workflow
- Use a feature branch and open a PR for review before merging into `main`.

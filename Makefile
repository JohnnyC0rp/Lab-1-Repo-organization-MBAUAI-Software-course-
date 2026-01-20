RECEIPTS_DIR ?= receipts

run:
	@if [ -z "$$OPENAI_API_KEY" ]; then \
		echo "OPENAI_API_KEY is not set. Export it before running."; \
		exit 1; \
	fi
	PYTHONPATH=src python -m receipt_extractor.main --print $(RECEIPTS_DIR)

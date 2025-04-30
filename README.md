# LLM False Quote Detection with RAG + Bloom Filter

This project is a lightweight baseline pipeline that detects and prevents hallucinated quotes in large language model outputs.

## Overview

We combine:
- **Retrieval-Augmented Generation (RAG)** for contextual grounding
- **Bloom Filters** for fast quote verification
- **Quote flagging logic** to detect hallucinations

## How It Works

1. User inputs a query.
2. The system retrieves a document containing the query.
3. The system simulates a generated output.
4. The Bloom filter checks if the output is a known, valid quote.
5. Output is flagged as Verified ✅ or Hallucinated ❌.

## Files

| File | Purpose |
|------|---------|
| `retrieval.py` | Retrieves documents matching the query |
| `bloom_filter.py` | Sets up a Bloom filter of verified quotes |
| `pipeline.py` | Coordinates the end-to-end workflow |
| `requirements.txt` | Required Python packages |

## Run It

```bash
pip install -r requirements.txt
python pipeline.py

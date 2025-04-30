# bloom_filter.py

from bloom_filter2 import BloomFilter

def setup_bloom_filter():
    bloom = BloomFilter(max_elements=1000, error_rate=0.1)

    real_quotes = [
        "The Earth revolves around the Sun.",
        "Water boils at 100 degrees Celsius.",
        "The Declaration of Independence was signed in 1776.",
        "Python is a programming language created by Guido van Rossum.",
        "The capital of France is Paris."
    ]

    for quote in real_quotes:
        bloom.add(quote)
    
    return bloom

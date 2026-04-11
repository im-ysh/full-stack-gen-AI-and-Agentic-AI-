import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hey this is vaishu"

tokens = enc.encode(text)
print("Tokens : " , tokens)

# Tokens [48467, 495, 382, 3423, 144320]
# enc.encode(text) converts the string into a list of integers
# Each integer represents a token

decoded = enc.decode([48467, 495, 382, 3423, 144320])
print("Decoded token : ", decoded)

# how text is converted into tokens and back using OpenAI’s tokenizer (tiktoken).
# tiktoken is OpenAI’s tokenization library
# It knows how different GPT models split text into tokens
# LLM cost is based on number of tokens
# Context limits are in tokens, not characters
# Modern GPT models (via tiktoken) use a variant of:
# BPE – Byte Pair Encoding
# Core idea:
# “If a sequence of characters appears together very often, treat it as one token.”



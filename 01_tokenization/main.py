import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hey this is vaishu"

tokens = enc.encode(text)
print("Tokens : " , tokens)

# Tokens [48467, 495, 382, 3423, 144320]


decoded = enc.decode([48467, 495, 382, 3423, 144320])
print("Decoded token : ", decoded)
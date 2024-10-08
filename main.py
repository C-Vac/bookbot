import sys

def main(path):
  with open(path) as f:
    full_text = f.read()
    word_count = get_word_count(full_text)
    char_counts = get_char_counts(full_text)

    print(f"--- Begin report of file: {path} ---")
    print(f"{word_count} words found in the document")
    print(f"far too lazy to sort this collection: {char_counts}")

def get_word_count(text):
  words = text.split()
  return len(words)

def get_char_counts(text):
  char_dict = {}
  for c in text:
    c = c.lower()
    if c in char_dict:
      char_dict[c] += 1
    else:
      char_dict[c] = 1
  return char_dict

if __name__ == "__main__":
  if len(sys.argv) > 1:
    path = sys.argv[1]
    main(path)
  else:
    print("No input parameter provided.")

import sys

def read_kv_array(text):
    key_values = {}

    for line in text:
        key, value = line.strip().split('\t')
        key_values[key] = key_values.get(key, 0) + int(value)

    return key_values

if __name__ == '__main__':
    word_counts = read_kv_array(sys.stdin)

    # Find the word with the maximum count
    most_frequent_word = max(word_counts, key=word_counts.get)
    
    print(f'Most frequent word: {most_frequent_word} ({word_counts[most_frequent_word]} times)')

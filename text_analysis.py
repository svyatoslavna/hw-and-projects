import re
from collections import Counter


def load_dataset(filename, encoding="utf-8"):
    """
    Load data from a text file.

    Args:
        filename (str): Name of the file to load.
        encoding (str): File encoding. Default is 'utf-8'.

    Returns:
        str: Content of the file.
    """

    with open(filename, "r", encoding=encoding) as f:
        return f.read()


def preprocess_text(data):
    """
    Clean text: remove HTML tags, special characters, normalize.

    Args:
        data (str): Raw text content.

    Returns:
        str: Cleaned and normalized text.
    """

    data = re.sub(r"<[^>]+>", " ", data)
    data = re.sub(r"[^a-zA-Zа-яА-ЯёЁ0-9\s\-.,!?:;]", " ", data)
    data = data.lower()
    data = re.sub(r"\s+", " ", data)
    data = data.strip()

    return data


def get_word_frequencies(cleaned):
    """
    Create frequency dictionary from cleaned text.

    Args:
        cleaned (str): Cleaned text.

    Returns:
        collections.Counter: Dictionary-like object with word counts.
    """

    words = cleaned.split()
    return Counter(words)


if __name__ == "__main__":

    data = load_dataset("data.txt")
    print(f"Длина файла: {len(data)}")
    print("Первые 200 символов:", data[:200])

    cleaned = preprocess_text(data)
    print("До очистки:", data[:200])
    print()
    print("После очистки:", cleaned[:200])

    freq_dict = get_word_frequencies(cleaned)
    print("Самые частые слова:", freq_dict.most_common(5))

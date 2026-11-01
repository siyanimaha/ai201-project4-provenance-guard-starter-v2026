import re
import statistics


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def sentence_length_spread(text: str) -> float:
    sents = sentences(text)
    lengths = [len(words(sentence)) for sentence in sents]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)

    if mean_length == 0:
        return 0.0

    return round(statistics.stdev(lengths) / mean_length, 4)


def type_token_ratio(text: str) -> float:
    word_list = words(text)

    if not word_list:
        return 0.0

    return round(len(set(word_list)) / len(word_list), 4)


def punctuation_density(text: str) -> float:
    if not text:
        return 0.0

    punctuation = re.findall(r"[,.!?;:—-]", text)
    return round(len(punctuation) / len(text), 4)


def style_signal(text: str) -> float:
    spread = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    punctuation = punctuation_density(text)

    spread_ai = 1.0 - min(spread, 1.0)
    vocabulary_ai = 1.0 - ttr
    punctuation_ai = 1.0 - min(punctuation / 0.1, 1.0)

    score = (spread_ai + vocabulary_ai + punctuation_ai) / 3

    return round(max(0.0, min(score, 1.0)), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
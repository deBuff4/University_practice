import json

corpus = json.load(open("code_corpus.json", encoding="utf-8"))
questions = json.load(open("eval_questions.json", encoding="utf-8"))
cats = json.load(open("categories.json", encoding="utf-8"))["categories"]

assert len(corpus) == 200, f"corpus: {len(corpus)}"
assert len(questions) == 25, f"questions: {len(questions)}"
assert len(cats) == 5, f"categories: {len(cats)}"

ids = [f["id"] for f in corpus]
assert len(ids) == len(set(ids)), "duplicate ids"

corpus_ids = set(ids)
for q in questions:
    assert q["correct_chunk_id"] in corpus_ids, f"missing: {q['correct_chunk_id']}"

for f in corpus[:100]:
    assert f["language"] == "python"
for f in corpus[100:]:
    assert f["language"] == "java"

print("✓ Все проверки пройдены")
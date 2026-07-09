from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",
    tokenizer="deepset/roberta-base-squad2"
)


def get_best_answer(question, retrieved_chunks, min_score=0.35):
    best_answer = {
        "answer": "No confident answer found in the document.",
        "score": 0.0,
        "chunk": None
    }

    for item in retrieved_chunks:
        chunk = item["chunk"]
        context = chunk["text"]

        result = qa_pipeline(
            question=question,
            context=context
        )

        answer = result.get("answer", "").strip()
        score = min(float(result.get("score", 0)), 1.0)

        # Reject bad/very short/weird answers
        if not answer:
            continue

        if len(answer) < 3:
            continue

        if len(answer.split()) > 25:
            continue

        if score > best_answer["score"]:
            best_answer = {
                "answer": answer,
                "score": score,
                "chunk": chunk
            }

    if best_answer["score"] < min_score:
        return {
            "answer": "No confident answer found in the document.",
            "score": best_answer["score"],
            "chunk": best_answer["chunk"]
        }

    return best_answer
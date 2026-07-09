from transformers import pipeline

qa_pipeline = None


def load_qa_pipeline():
    global qa_pipeline

    if qa_pipeline is None:
        qa_pipeline = pipeline(
            task="question-answering",
            model="deepset/roberta-base-squad2",
            tokenizer="deepset/roberta-base-squad2"
        )

    return qa_pipeline


def get_best_answer(question, retrieved_chunks, min_score=0.35):
    qa = load_qa_pipeline()

    best_answer = {
        "answer": "No confident answer found in the document.",
        "score": 0.0,
        "chunk": None
    }

    for item in retrieved_chunks:
        chunk = item["chunk"]
        context = chunk["text"]

        result = qa(
            question=question,
            context=context
        )

        answer = result.get("answer", "").strip()
        score = min(float(result.get("score", 0)), 1.0)

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
        best_answer["answer"] = "No confident answer found in the document."

    return best_answer
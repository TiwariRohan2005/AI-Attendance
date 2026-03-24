import numpy as np
import json
from app.models.embedding_model import get_all_embeddings

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def recognize_face(input_desc):
    rows = get_all_embeddings()

    best = {"user_id": None, "name": None, "score": 0.0}

    for uid, desc_json, name in rows:
        desc = json.loads(desc_json)
        sim = cosine_similarity(input_desc, desc)

        if sim > best["score"]:
            best = {"user_id": uid, "name": name, "score": sim}

    return best
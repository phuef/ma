from sentence_transformers import SentenceTransformer
import numpy as np

def getEmbeddingForHtmlCode(html_code):
    model = SentenceTransformer("dunzhang/stella_en_1.5B_v5")
    #model = SentenceTransformer("Salesforce/SFR-Embedding-2_R") # This model was used first, but didn't perform well due to a high ram usage
    embedding = model.encode(html_code)
    embeddingAsList=np.array(embedding).tolist() # <- transformation of the embeddings to a list, to be able to save it in mongodb
    return embeddingAsList
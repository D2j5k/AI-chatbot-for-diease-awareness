import json

class HealthQueryService:
    def __init__(self, db_path, nlp_service):
        with open(db_path, 'r') as f:
            self.db = json.load(f)
        self.nlp_service = nlp_service

    def answer_query(self, query):
        understanding = self.nlp_service.understand_intent(query)
        intent = understanding.get("intent")
        entities = understanding.get("entities")

        if intent == "query_symptoms" and "disease" in entities:
            disease = entities["disease"]
            for item in self.db["disease_symptoms"]:
                if item["disease"] == disease:
                    return f"The symptoms of {disease} are: {', '.join(item['symptoms'])}"
            return f"Sorry, I don't have information about {disease}."

        return "I'm sorry, I can't answer that question. Please try rephrasing."

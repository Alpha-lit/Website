import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")


# Function to extract entities from a customer query
def extract_entities(query):
    doc = nlp(query)
    entities = []
    
    # Define relevant entity types for a Shopify store domain
    relevant_entity_types = ['PRODUCT', 'CUSTOMER', 'ORDER', 'SHIPPING', 'PAYMENT']
    
    # Iterate over the named entities in the query
    for ent in doc.ents:
        if ent.label_ in relevant_entity_types:
            entities.append({
                'label': ent.label_,
                'text': ent.text
            })
    
    return entities
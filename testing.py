# import spacy
# # python -m spacy download en_core_web_sm
# # Load a pretrained model (you may need to train your own model for your specific use case)
# nlp = spacy.load('en_core_web_sm')
#
#
# def extract_field_from_question(question):
#     doc = nlp(question)
#
#     # Extract entities
#     for ent in doc.ents:
#         if ent.label_ in ['PERSON', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART']:
#             return ent.text
#
#     return None

import spacy
from spacy.matcher import Matcher

# Load a pretrained model
nlp = spacy.load('en_core_web_sm')

# Initialize the matcher
matcher = Matcher(nlp.vocab)

# Define a pattern for each field
release_pattern = [{"LOWER": "release"}]
ticket_pattern = [{"LOWER": "ticket"}]
open_tickets_pattern = [{"LOWER": "tickets"}, {"LOWER": "are"}, {"LOWER": "open"}]
assigned_tickets_pattern = [{"LOWER": "tickets"}, {"LOWER": "are"}, {"LOWER": "assigned"}]
pending_releases_pattern = [{"LOWER": "releases"}, {"LOWER": "are"}, {"LOWER": "pending"}]
targeted_releases_pattern = [{"LOWER": "releases"}, {"LOWER": "being"}, {"LOWER": "targeted"}]

# Add the patterns to the matcher
matcher.add("RELEASE", [release_pattern])
matcher.add("TICKET", [ticket_pattern])
matcher.add("OPEN_TICKETS", [open_tickets_pattern])
matcher.add("ASSIGNED_TICKETS", [assigned_tickets_pattern])
matcher.add("PENDING_RELEASES", [pending_releases_pattern])
matcher.add("TARGETED_RELEASES", [targeted_releases_pattern])

def extract_field_from_question(question):
    doc = nlp(question)

    # Apply the matcher to the doc
    matches = matcher(doc)

    # Extract entities
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        return string_id

    return None



print(extract_field_from_question("What is the update for Release #12342"))
print(extract_field_from_question("Who is working on the ticket #12345"))
print(extract_field_from_question("How many tickets are open"))
print(extract_field_from_question("How many tickets are assigned to Rohit"))
print(extract_field_from_question("How many releases are pending"))
print(extract_field_from_question("give me releases being targeted for november"))


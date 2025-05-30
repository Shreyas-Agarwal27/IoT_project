import APIkey
from landingai.predict import Predictor
from PIL import Image

# Enter your API Key
endpoint_id = "73dadc7b-b774-4791-833f-f51f8b522d93"
api_key = APIkey.key

# Load your image
image = Image.open("image.png")

# Run inference
predictor = Predictor(endpoint_id, api_key=api_key)
predictions = predictor.predict(image)
print(predictions)
print(type(predictions))
print(predictions[0].label_name)

# output format:
# one call costs 1 credit
# [ClassificationPrediction(score=0.9980272650718689, label_name='Defective', label_index=0)]

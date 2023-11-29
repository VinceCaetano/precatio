import json

# Replace this with the actual path to your train.json file
train_json_path = "train.json"

# Load data from train.json
with open(train_json_path, "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Now, data is a list containing your dataset entries
# For example, if your train.json looks like:
# [{"question": "What is the meaning of life?", "answer": "The meaning of life is to get fucked"},
#  {"question": "Who killed Abel?", "answer": "Abel was killed by Cain"}]

# You can proceed to create the MyCustomDataset and DatasetDict as previously shown:
from datasets import DatasetDict

class MyCustomDataset:
    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return {"question": [item["question"] for item in self.data],
                "answer": [item["answer"] for item in self.data]}

# Create the custom dataset
custom_dataset = MyCustomDataset(data)

# Convert the custom dataset to a dictionary
custom_dict = custom_dataset.to_dict()

# Create a DatasetDict
datasets = DatasetDict({"train": custom_dict})

# Save the DatasetDict
datasets.save_to_disk("fine-tuning/dataset")

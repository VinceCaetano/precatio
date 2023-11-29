from transformers import BertForQuestionAnswering, BertTokenizer, TrainingArguments, Trainer
from dataset.dataset import MyCustomDataset

# Load your data from train.json
data = [...]  # Load your data from train.json
dataset = MyCustomDataset(data)

# Define model and tokenizer
model = BertForQuestionAnswering.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the dataset
tokenized_datasets = dataset.map(lambda example: tokenizer(example["question"], example["answer"], truncation=True), batched=True)

# Fine-tuning arguments
training_args = TrainingArguments(
    output_dir="./output",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    save_steps=1000,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
)

# Train the model
trainer.train()

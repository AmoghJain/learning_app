from transformers import pipeline

class summarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="Falconsai/text_summarization")

    def run(self, text):
        summary = self.summarizer(text, max_length=230, min_length=30, do_sample=False)
        return summary
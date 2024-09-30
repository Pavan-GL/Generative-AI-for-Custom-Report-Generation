import logging
import pickle
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Set up logging
logging.basicConfig(filename='report_model.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class ReportModel:
    def __init__(self, model_name="gpt2"):
        try:
            self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
            self.model = GPT2LMHeadModel.from_pretrained(model_name)
            logging.info(f"Initialized {model_name} model successfully.")
        except Exception as e:
            logging.error(f"Error initializing model: {e}")
    
    @staticmethod
    def generate_report_model(self, prompt, max_length=500):
        try:
            inputs = self.tokenizer.encode(prompt, return_tensors="pt")
            with torch.no_grad():
                outputs = self.model.generate(inputs, max_length=max_length, num_return_sequences=1)
            report = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            return None

    def save_model(self, filename, save_format='pickle'):
        try:
            if save_format == 'pickle':
                with open(filename, 'wb') as f:
                    pickle.dump((self.tokenizer, self.model), f)
                logging.info("Model saved successfully in Pickle format.")
            elif save_format == 'h5':
                # Save the model's state_dict as H5
                torch.save(self.model.state_dict(), filename)
                logging.info("Model saved successfully in H5 format.")
            else:
                logging.error("Unsupported save format specified.")
        except Exception as e:
            logging.error(f"Error saving model: {e}")

    def load_model(self, filename, save_format='pickle'):
        try:
            if save_format == 'pickle':
                with open(filename, 'rb') as f:
                    self.tokenizer, self.model = pickle.load(f)
                logging.info("Model loaded successfully from Pickle format.")
            elif save_format == 'h5':
                self.model.load_state_dict(torch.load(filename))
                logging.info("Model loaded successfully from H5 format.")
            else:
                logging.error("Unsupported load format specified.")
        except Exception as e:
            logging.error(f"Error loading model: {e}")

# Initialize the model globally
report_model = ReportModel()

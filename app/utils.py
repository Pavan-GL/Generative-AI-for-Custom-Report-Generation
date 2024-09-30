from models import ReportModel

class ReportGenerator:
    def __init__(self, data):
        if not isinstance(data, (bytes, bytearray)):
            raise ValueError("Input data must be in bytes format.")
    
        self.data = data
        self.processed_data = None

    def preprocess_data(self):
        """Convert the input data to a readable string."""
        try:
            print(f"Raw content: {self.data[:100]}")
            self.processed_data = self.data.decode("utf-8")
            print("Data successfully decoded.")
        except UnicodeDecodeError:
            raise ValueError("Input data could not be decoded. Ensure it is valid UTF-8.")
        except Exception as e:
            print(f"Error details: {str(e)}")
            raise RuntimeError(f"An error occurred while processing data: {str(e)}") from e
        
       

    def generate_report(self):
        """Generate a financial report based on the processed data."""
        self.preprocess_data()

        # Create a prompt for report generation
        prompt = f"Generate a financial report based on the following data: {self.processed_data}"

        try:
            # Generate the report using the model
            report = ReportModel.generate_report_model(prompt)
            return report
        except Exception as e:
            raise RuntimeError("An error occurred while generating the report.") from e

# Example usage:
# data = b"your, csv, data, here"
# report_generator = ReportGenerator(data)
# report = report_generator.generate_report()
# print(report)

import os
import argparse
import mlflow
import mlflow.pyfunc
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def predict(input_path, output_path, model_version):
    """Make predictions using the {{cookiecutter.project_slug}} model."""
    
    # Set MLflow tracking URI
    mlflow.set_tracking_uri(os.getenv('MLFLOW_TRACKING_URI'))
    
    print(f"Loading model version: {model_version}")
    
    # Load model from MLflow registry
    model = mlflow.pyfunc.load_model(f"models:/{{cookiecutter.project_slug}}/{model_version}")
    
    print(f"Loading input data from: {input_path}")
    
    # Load input data
    input_data = pd.read_csv(input_path)
    
    # Make predictions
    predictions = model.predict(input_data)
    
    # Save predictions
    output_df = input_data.copy()
    output_df['predictions'] = predictions
    output_df.to_csv(output_path, index=False)
    
    print(f"Predictions saved to: {output_path}")
    print(f"Generated {len(predictions)} predictions")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-path', required=True, help='Path to input data for prediction')
    parser.add_argument('--output-path', required=True, help='Path to save predictions')
    parser.add_argument('--model-version', default='Production', help='Model version from registry')
    
    args = parser.parse_args()
    predict(args.input_path, args.output_path, args.model_version)
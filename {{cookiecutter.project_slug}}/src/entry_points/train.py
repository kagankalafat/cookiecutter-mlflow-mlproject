import os
import argparse
import mlflow
import mlflow.sklearn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def train(data_path, model_path):
    """Train the {{cookiecutter.project_slug}} model."""
    
    # Set MLflow tracking URI
    mlflow.set_tracking_uri(os.getenv('MLFLOW_TRACKING_URI'))
    mlflow.set_experiment("{{cookiecutter.project_slug}}")
    
    with mlflow.start_run():
        print(f"Training model with data from: {data_path}")
        
        # TODO: Load your data
        # data = pd.read_csv(data_path)
        
        # TODO: Train your model
        # model = YourModel()
        # model.fit(X, y)
        
        # Log parameters
        mlflow.log_param("data_path", data_path)
        
        # TODO: Log metrics
        # mlflow.log_metric("accuracy", accuracy)
        
        # TODO: Log model to blob storage via MLflow
        # mlflow.sklearn.log_model(model, "model")
        
        print("Model and artifacts saved to MLflow (blob storage)")
        print(f"Run ID: {mlflow.active_run().info.run_id}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-path', required=True, help='Path to training data')
    parser.add_argument('--model-path', default='models/', help='Path to save model')
    
    args = parser.parse_args()
    train(args.data_path, args.model_path)
# Diabetes Prediction Project

This project predicts whether a person has diabetes based on health metrics using a Support Vector Machine (SVM) classifier.

## Project Structure

- `main` - Python script to run the training and prediction.
- `diabetes.csv` - Dataset (must be in project root).
- `requirements.txt` - Python dependencies.
- `.gitignore` - Exclude venv, cache, and build files.

## Setup

1. Install Python 3.13 (add to PATH).
2. Clone the repo:
   ```bash
   git clone https://github.com/Nevanthsaivignesh/diabetes-prediction-using-machine-learning.git
   cd "diabetes-prediction-using-machine-learning"
   ```
3. Create & activate a virtual environment:
   ```powershell
   python -m venv venv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
   .\venv\Scripts\Activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Place `diabetes.csv` in the project root.
6. Run the script:
   ```bash
   python main
   ```

## Usage

Follow the prompts to enter health metrics. The script will print if the person is diabetic or not.

## License

MIT License

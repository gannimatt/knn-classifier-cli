# KNN Classifier CLI

A simple command-line implementation of the K-Nearest Neighbors (KNN) algorithm for classification using CSV datasets.

## Features
- Reads training and test data from CSV files.
- Supports classification of all test observations at once.
- Allows classification of a single observation input by the user.
- Enables dynamic adjustment of the `k` value.
- Provides accuracy metrics when classifying test data.

## How It Works
1. The script loads a training dataset from `train.txt`.
2. The user selects an action from the menu:
   - Classify all test observations (`test.txt`).
   - Classify a single observation (entered manually).
   - Change the value of `k`.
   - Exit the program.
3. If classifying test data, the program computes predictions and reports accuracy.

## Installation & Usage

### Prerequisites
- Python 3.x

### Running the Program
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/knn-classifier-cli.git
   cd knn-classifier-cli

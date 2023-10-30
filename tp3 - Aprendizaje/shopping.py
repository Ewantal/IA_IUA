import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    evidence = []
    labels = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        
        for row in reader:
            # Convert the columns to appropriate data types and format
            data = [
                int(row[0]), float(row[1]), int(row[2]), float(row[3]), int(row[4]),
                float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]),
                ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'].index(row[10]),
                int(row[11]), int(row[12]), int(row[13]), int(row[14]), 1 if row[15] == 'Returning_Visitor' else 0,
                1 if row[16] == 'TRUE' else 0
            ]
            evidence.append(data)
            labels.append(1 if row[17] == 'TRUE' else 0)

    return evidence, labels

def train_model(evidence, labels):
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model

def evaluate(labels, predictions):
    true_positive = sum(1 for actual, pred in zip(labels, predictions) if actual == 1 and pred == 1)
    true_negative = sum(1 for actual, pred in zip(labels, predictions) if actual == 0 and pred == 0)
    actual_negatives = sum(1 for label in labels if label == 0)

    sensitivity = true_positive / sum(labels)
    specificity = true_negative / actual_negatives

    return sensitivity, specificity


if __name__ == "__main__":
    main()

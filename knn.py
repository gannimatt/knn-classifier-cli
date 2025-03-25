import csv
def squared_euclidean_distance(x1, x2):
    return sum((float(a) - float(b)) ** 2 for a, b in zip(x1, x2))

def knn(training_data, test_observation, k):
    distances = []
    for observation in training_data:
        distance = squared_euclidean_distance(observation[:-1], test_observation)
        label = observation[-1]
        distances.append((distance, label))
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]

    classes = [neighbor[1] for neighbor in neighbors]
    return max(set(classes), key=classes.count)

def readFile(filepath):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)

training_data = readFile("train.txt")

k = int(input("Enter the value of 'K': "))

while True:
    print("\nChoose one of the following options: ")
    print("a) Classification of all observations from the test set")
    print("b) Classification of a single observation")
    print("c) Change K")
    print("d) Exit the program")

    user_choice = input().lower()

    if user_choice == 'a':
        test_data = readFile("test.txt")
        predictions = []
        for test_obs in test_data:
            pred = knn(training_data, test_obs[:-1], k)
            predictions.append(pred)
        accuracy = sum(pred == true for pred, true in zip(predictions, [row[-1] for row in test_data])) / len(test_data)
        print("\nPredictions and their true labels:")
        for pred, true in zip(predictions, [row[-1] for row in test_data]):
            print(f"Predicted: {pred}, True: {true}")
        print(f"\nAccuracy: {accuracy:.2f}")
    elif user_choice == 'b':
        observation = input("Enter your observation: ")
        test_obs = [float(value) for value in observation.split(',')]
        pred = knn(training_data, test_obs, k)
        print(f"Predicted label: {pred}")
    elif user_choice == 'c':
        k = int(input("Enter the new value of 'K': "))
    elif user_choice == 'd':
        print("Exiting...")
        break
    else:
        print("Invalid choice")

def evaluate_model(model, test_ds):
    results = model.evaluate(test_ds)
    print(f'Test Loss: {results[0]}')
    print(f'Test Accuracy: {results[1]}')
    return results

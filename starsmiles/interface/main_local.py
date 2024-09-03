from starsmiles.ml_logic.data import create_dataset

def preprocess_and_train() -> None:
    """
    - Requests the directories from where to fetch the pictures
    - Creates datasets from the pictures
    - Uses the datasets to train a model
    - Save the model
    - Compute & save a validation performance metric
    """

    train_path = input('Enter the path to the traininig set directory: ')
    val_path = input('Enter the path to the validation set directory: ')
    test_path = input('Enter the path to the testing set directory: ')

    train_ds = create_dataset(train_path)
    val_ds = create_dataset(val_path)
    test_ds = create_dataset(test_path)



if __name__ == '__main__':
    try:
        preprocess_and_train()
        # preprocess()
        # train()
        #pred()
    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)

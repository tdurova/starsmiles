import pytest
from PIL import Image
from starsmiles.proc_pred import load_image, preprocess_image
from unittest.mock import patch, MagicMock
import tensorflow as tf

@pytest.fixture
def mock_image():
    return Image.new('L', (64, 64))  # Grayscale image

@pytest.fixture
def mock_large_image():
    return Image.new('L', (128, 128))  # Grayscale image

@pytest.fixture
def mock_model():
    with patch('starsmiles.proc_pred.tf.keras.models.load_model') as mock_load_model:
        mock_model_instance = MagicMock()
        mock_load_model.return_value = mock_model_instance
        yield mock_model_instance

def test_load_image_success(mocker, mock_image):
    mocker.patch('PIL.Image.open', return_value=mock_image)
    image_path = 'path/to/sample_image.jpg'
    result = load_image(image_path)
    assert isinstance(result, Image.Image)
    assert result.size == (64, 64)

def test_load_image_file_not_found(mocker):
    mocker.patch('PIL.Image.open', side_effect=FileNotFoundError)
    image_path = 'path/to/non_existent_image.jpg'
    with pytest.raises(FileNotFoundError):
        load_image(image_path)

def test_load_image_invalid_image(mocker):
    mocker.patch('PIL.Image.open', side_effect=OSError)
    image_path = 'path/to/invalid_image.jpg'
    with pytest.raises(OSError):
        load_image(image_path)

def test_preprocess_image_success(mock_large_image):
    preprocessed_image = preprocess_image(mock_large_image)
    assert isinstance(preprocessed_image, tf.Tensor)
    assert preprocessed_image.shape == (64, 64, 1)

def test_preprocess_image_failure(mocker, mock_large_image):
    mocker.patch('starsmiles.proc_pred.img_to_array', side_effect=Exception('Error preprocessing image'))
    with pytest.raises(Exception) as excinfo:
        preprocess_image(mock_large_image)
    assert 'Error preprocessing image' in str(excinfo.value)

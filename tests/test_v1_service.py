from unittest.mock import Mock

import pytest

from v1.service import generate_model_scores


@pytest.fixture
def start_training_mock(mocker):
    mock = Mock()
    mocker.patch("v1.service.start_training", mock)
    return mock


@pytest.fixture
def train_mock(mocker):
    mock = Mock()
    mocker.patch("v1.service.train", mock)
    return mock


@pytest.fixture
def upload_mock(mocker):
    mock = Mock()
    mocker.patch("v1.service.upload", mock)
    return mock


@pytest.fixture
def complete_training_mock(mocker):
    mock = Mock()
    mocker.patch("v1.service.complete_training", mock)
    return mock


@pytest.fixture
def post_message_mock(mocker):
    mock = Mock()
    mocker.patch("v1.service.post_message", mock)
    return mock


def test_service(start_training_mock, train_mock, upload_mock, complete_training_mock, post_message_mock):
    """
    When running generate_model_scores,
    1. Training started has been logged
    2. Bert4Rec is trained
    3. Output of model is uploaded
    4. Training complete has been logged
    5. Slack has been posted
    """
    generate_model_scores("bert4rec")
    start_training_mock.assert_called_once_with("bert4rec")
    train_mock.assert_called_once()
    upload_mock.assert_called_once()
    complete_training_mock.assert_called_once()
    post_message_mock.assert_called_once_with("#machine-learning", "Generate model scores complete")

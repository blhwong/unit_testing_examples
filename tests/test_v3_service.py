from unittest.mock import Mock

from v3.db.fake import FakeDB
from v3.model.fake import FakeModel
from v3.notification.fake import FakeNotification
from v3.service import Service
from v3.storage.fake import FakeStorage


def test_service_with_mocks():
    """
    When running generate_model_scores,
    1. Training started has been logged
    2. Bert4Rec is trained
    3. Output of model is uploaded
    4. Training complete has been logged
    5. Slack has been posted
    """
    db = Mock()
    model = Mock()
    storage = Mock()
    notification = Mock()
    service_mock = Service(db, model, storage, notification)
    service_mock.generate_model_scores("bert4rec")
    db.start_training.assert_called_once_with("bert4rec")
    model.train.assert_called_once()
    storage.upload.assert_called_once()
    db.complete_training.assert_called_once()
    notification.post_message.assert_called_once_with("#machine-learning", "Generate model scores complete")

def test_service_with_fake_implementations():
    """
    When running generate_model_scores,
    1. Training started has been logged
    2. Bert4Rec is trained
    3. Output of model is uploaded
    4. Training complete has been logged
    5. Slack has been posted
    """
    db = FakeDB()
    model = FakeModel()
    storage = FakeStorage()
    notification = FakeNotification()
    service_mock = Service(db, model, storage, notification)
    service_mock.generate_model_scores("bert4rec")
    assert db.start_training_called
    assert model.train_called
    assert storage.upload_called
    assert db.complete_training_called
    assert notification.post_message_called

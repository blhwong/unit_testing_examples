from unittest.mock import Mock

from v2.service import Service


def test_service():
    """
    When running generate_model_scores,
    1. Training started has been logged
    2. Bert4Rec is trained
    3. Output of model is uploaded
    4. Training complete has been logged
    5. Slack has been posted
    """
    service_mock = Service(Mock(), Mock(), Mock(), Mock())
    service_mock.generate_model_scores("bert4rec")
    service_mock.db.start_training.assert_called_once_with("bert4rec")
    service_mock.model.train.assert_called_once()
    service_mock.s3.upload.assert_called_once()
    service_mock.db.complete_training.assert_called_once()
    service_mock.slack.post_message.assert_called_once_with("#machine-learning", "Generate model scores complete")

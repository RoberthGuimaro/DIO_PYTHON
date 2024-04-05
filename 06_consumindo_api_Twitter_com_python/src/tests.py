from src.services import _get_trends
from unittest import mock

def test_get_trends_with_sucess():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_valeu = [
        {
            "trends":[
                {"name":"teste","url":"url.teste.br"},
            ]
        }
    ]

    # Action
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == [{"name":"teste","url":"url.teste.br"}]

def test_get_trends_without_return_with_sucess():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_valeu = [{"trends":[]}]

    # Action
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == []

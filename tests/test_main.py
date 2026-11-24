from src.main import powitanie


def test_powitanie():
    assert powitanie() == "Witaj w aplikacji CI/CD"
    
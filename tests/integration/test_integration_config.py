import pytest
from pyyaml_object import Config
from data import get_path


class TestIntegration:
    @pytest.fixture(autouse=True)
    def _setup(self):
        path = get_path()
        self._config_parser = Config(path)

    def test_reader(self):
        conf = self._config_parser.read()

        assert conf.data.version == "1.0.0"  # type: ignore
        assert conf.data.name == "test"  # type: ignore
        assert conf.data.description == "it is a test"  # type: ignore

        assert conf.data.api_key.facebook == "1234567890"  # type: ignore
        assert conf.data.api_key.twitter == "1224567897"  # type: ignore

        assert conf.data.scope == ["read", "write"]  # type: ignore
        assert conf.metadata.created_at == "09/05/2023"  # type: ignore

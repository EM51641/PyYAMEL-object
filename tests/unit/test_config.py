from typing import Generator
from pyyaml_object.config import Config, EmptyFileError
from unittest.mock import Mock, patch
from pyyaml_object.utils import Node
import pytest


class TestConfig:
    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        self._config_manager = Config("test.yaml")
        self._root_node = Mock(spec=Node)
        self._config = {
            "data": {
                "name": "test",
                "version": "1.0.0",
                "description": "it is a test",
                "api_key": {"facebook": "1234567890", "twitter": "1224567897"},
                "scope": ["read", "write"],
            },
            "metadata": {"created_at": "09/05/2023"},
        }

    @pytest.fixture(autouse=True)
    def _setup_patch_open_file(self) -> Generator[Mock, None, None]:
        with patch("pyyaml_object.config.open") as _open:
            yield _open

    @pytest.fixture(autouse=True)
    def _setup_patch_node(self) -> Generator[Mock, None, None]:
        with patch("pyyaml_object.config.Node") as _node:
            yield _node

    @pytest.fixture(autouse=True)
    def _setup_patch_yaml(self) -> Generator[Mock, None, None]:
        with patch("pyyaml_object.config.yaml") as _yaml_module:
            self._yaml_module = _yaml_module
            self._yaml_module.safe_load.return_value = self._config
            yield _yaml_module

    def test_config_property(self) -> None:
        assert self._config_manager.filename == "test.yaml"

    def test_config_read_method_sucess(self) -> None:
        conf = self._config_manager.read(self._root_node)

        assert conf.data.version == "1.0.0"  # type: ignore
        assert conf.data.name == "test"  # type: ignore
        assert conf.data.description == "it is a test"  # type: ignore

        assert conf.data.api_key.facebook == "1234567890"  # type: ignore
        assert conf.data.api_key.twitter == "1224567897"  # type: ignore

        assert conf.data.scope == ["read", "write"]  # type: ignore
        assert conf.metadata.created_at == "09/05/2023"  # type: ignore

    def test_config_read_method_failure(self) -> None:
        self._yaml_module.safe_load.return_value = {}

        with pytest.raises(EmptyFileError):
            self._config_manager.read(self._root_node)

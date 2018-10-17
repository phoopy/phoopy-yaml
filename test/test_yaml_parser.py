from phoopy.yaml import YamlParser


class TestYamlParser(object):
    def test_init(self):
        assert YamlParser() is not None

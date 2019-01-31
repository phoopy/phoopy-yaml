import pytest
from phoopy.yaml import YamlParser


@pytest.fixture
def yaml_parser():
    return YamlParser()


class TestYamlParser(object):
    def test_init(self):
        assert YamlParser() is not None

    def test_parse_fail(self, yaml_parser, fs):
        with pytest.raises(IOError):
            yaml_parser.parse('/tmp/i_dont_exist')

    def test_parse_success(self, yaml_parser, fs):
        parameters = '''
        parameters:
            env: test
            google:
                client_id: ~
                client_secret: ~
        a: ~
        b: {}
        '''
        services = '''
        imports:
            - { resource: 'parameters.yml' }
        services:
            lala:
                class: Lala
        a: {}
        b: ~
        '''
        fs.create_file('parameters.yml', contents=parameters)
        fs.create_file('services.yml', contents=services)
        result = yaml_parser.parse('services.yml')
        assert 'test' == result['parameters']['env']
        assert 'Lala' == result['services']['lala']['class']

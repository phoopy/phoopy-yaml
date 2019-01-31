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
        overwrite: ~
        '''
        services = '''
        imports:
            - { resource: 'parameters.yml' }
        overwrite: {}
        '''
        fs.create_file('parameters.yml', contents=parameters)
        fs.create_file('services.yml', contents=services)
        actual_result = yaml_parser.parse('services.yml')
        expected_result = {
            'parameters': {
                'env': 'test',
                'google': {
                    'client_id': None,
                    'client_secret': None
                }
            },
            'overwrite': {}
        }
        assert expected_result == actual_result

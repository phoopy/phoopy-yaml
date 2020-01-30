# Documentation

## Usage

#### *my-yaml.yml*
```yaml
first:
    all_rows:
        pass: 'dog'
        number: '1'
```

#### *parse-yaml.py*
```python
from phoopy.yaml import YamlParser

yaml_path = 'my-yaml.yml'

parser = YamlParser()

yaml_parsed = parser.parse(
    file_path=bundle_services_path
)

"""
yaml_parsed === { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
"""
```

## Methods

### _YamlParser.parse(file_path, result=None)_

Parse an yaml file and get as return a dict
```python
from phoopy.yaml import YamlParser

parser = YamlParser()

yaml_parsed = {} # inital value to be merged

yaml_parsed = parser.parse(
    file_path=bundle_services_path,
    result=yaml_parsed
)
```

### _YamlParser.merge(destination, source)_

Merge 2 dicts
```python
from phoopy.yaml import YamlParser

parser = YamlParser()

a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
parser.merge(a, b) # a === { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }
```


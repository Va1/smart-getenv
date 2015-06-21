# Python smart getenv

Since environment variables in os.environ are strings, it often appears inconvenient to store and retrieve other
data types such as bool or list. The package provides a single function that wraps os.getenv and allows
you to specify the desired variable type.

Tested and supported types: str, int, float, list. tuple, dict.


## Usage

Prepare the variables:

```
$ export BOOLEAN=true
$ export LIST=a,b,c
$ export TRICKY_LIST=d:e:f
$ export DICT="{'foo':'bar'}"
```

Get them:

```python
>>> from smart_getenv import getenv
>>>
>>> getenv('BOOLEAN', type=str)
'true'
>>> getenv('BOOLEAN', type=bool)
True
>>> getenv('LIST', type=list)
['a', 'b', 'c']
>>> getenv('LIST', type=tuple)
('a', 'b', 'c')
>>> getenv('TRICKY_LIST', type=list, separator=':')
['d', 'e', 'f']
>>> getenv('DICT', type=dict)
{'foo': 'bar'}
>>> getenv('LOST', default='default value anyone?')
'default value anyone?'
```

# Python smart getenv

Since environment variables in os.environ are strings, it often appears inconvenient to store and retrieve other 
data types such as bool or list. The package provides a single function that wraps os.getenv and allows 
you to specify the desired variable type.

# Stubs for jinja2.bccache (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

marshal_dump = ...  # type: Any
marshal_load = ...  # type: Any
bc_version = ...  # type: int
bc_magic = ...  # type: Any

class Bucket:
    environment = ...  # type: Any
    key = ...  # type: Any
    checksum = ...  # type: Any
    def __init__(self, environment, key, checksum) -> None: ...
    code = ...  # type: Any
    def reset(self): ...
    def load_bytecode(self, f): ...
    def write_bytecode(self, f): ...
    def bytecode_from_string(self, string): ...
    def bytecode_to_string(self): ...

class BytecodeCache:
    def load_bytecode(self, bucket): ...
    def dump_bytecode(self, bucket): ...
    def clear(self): ...
    def get_cache_key(self, name, filename: Optional[Any] = ...): ...
    def get_source_checksum(self, source): ...
    def get_bucket(self, environment, name, filename, source): ...
    def set_bucket(self, bucket): ...

class FileSystemBytecodeCache(BytecodeCache):
    directory = ...  # type: Any
    pattern = ...  # type: Any
    def __init__(self, directory: Optional[Any] = ..., pattern: str = ...) -> None: ...
    def load_bytecode(self, bucket): ...
    def dump_bytecode(self, bucket): ...
    def clear(self): ...

class MemcachedBytecodeCache(BytecodeCache):
    client = ...  # type: Any
    prefix = ...  # type: Any
    timeout = ...  # type: Any
    ignore_memcache_errors = ...  # type: Any
    def __init__(self, client, prefix: str = ..., timeout: Optional[Any] = ..., ignore_memcache_errors: bool = ...) -> None: ...
    def load_bytecode(self, bucket): ...
    def dump_bytecode(self, bucket): ...

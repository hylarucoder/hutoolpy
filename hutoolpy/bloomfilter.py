# https://github.com/tal-tech/go-zero/blob/master/core/bloom/bloom.go

# // for detailed error rate table, see http://pages.cs.wisc.edu/~cao/papers/summary-cache/node8.html
# // maps as k in the error rate table
DEFAULT_MAPS = 14
SET_SCRIPT = """
for _, offset in ipairs(ARGV) do
    redis.call("setbit", KEYS[1], offset, 1)
end
"""
TEST_SCRIPT = """
for _, offset in ipairs(ARGV) do
	if tonumber(redis.call("getbit", KEYS[1], offset)) == 0 then
		return false
	end
end
return true
"""


class RedisBitSet:
    """
    store *redis.Redis
	key   string
	bits  uint

    """
    ...

    def buildOffsetArgs(self):
        ...

    def check(self):
        ...

    def delete(self):
        ...

    def expire(self):
        ...

    def set(self):
        ...


class BloomFilter:

    def add(self):
        ...

    def exists(self):
        ...

    def getLocations(self):
        ...

import redis

class RedisQueueFIFO:
    def __init__(self, queue_key_name, lock_key_name, lock_expiration_period = 10, host = '127.0.0.1', port = 6379, decode_responses = True):
        self.host = host
        self.port = port
        self.decode_responses = decode_responses
        self.redis_connection = redis.Redis(
            host=self.host,
            port=self.port,
            decode_responses=decode_responses
            )
        self.queue_key_name = queue_key_name
        self.lock_key_name = lock_key_name
        self.lock_expiration_period = lock_expiration_period

    def push_elements(self, *elements):
        self.redis_connection.rpush(self.queue_key_name, *elements)

    def pop_elements(self, quantity = 1):
        queue_length = self.get_length()
        pop_start = queue_length - quantity
        pop_end = queue_length
        elements = self.redis_connection.lrange(self.queue_key_name, pop_start, pop_end)
        self.redis_connection.ltrim(self.queue_key_name, 0, pop_start - 1)
        return elements
    
    def get_length(self):
        return self.redis_connection.llen(self.queue_key_name)
    
    def get_elements(self, start = 0, end = -1):
        return self.redis_connection.lrange(self.queue_key_name, start, end)

    def delete(self):
        return self.redis_connection.delete(self.queue_key_name)
    
    def acquire_lock(self):
        lock_key_exists = self.redis_connection.exists(self.lock_key_name)
        if not lock_key_exists:
            self.redis_connection.set(self.lock_key_name,'1',ex=self.lock_expiration_period)
        else:
            raise 'Could not acquire redis queue lock'
        return True
        
    def remove_lock(self):
        self.redis_connection.delete(self.lock_key_name)
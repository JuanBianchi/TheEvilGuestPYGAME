
class Timer():
    def __init__(self, max_time) -> None:
        self.__max_time = max_time
        self.__elapsed_time = 0

    @property
    def get_remaining_time(self):
        return int(self.__max_time - self.__elapsed_time)

    def update(self, delta_ms):
        self.__elapsed_time += delta_ms

    def is_expired(self):
        return True if self.__elapsed_time >= self.__max_time else False
    
    def reset(self):
        self.__elapsed_time = 0
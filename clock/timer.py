
class Timer():
    def __init__(self, max_time) -> None:
        self.__max_time = max_time
        self.__elapsed_time = 0
        self.__is_paused = False
        self.__pause_start_time = 0

    @property
    def get_remaining_time(self):
        if not self.__is_paused:
            return max(0, int(self.__max_time - self.__elapsed_time))
        else:
            return max(0, int(self.__max_time - (self.__elapsed_time - self.__pause_start_time)))

    def update(self, delta_ms):
        if not self.__is_paused:
            self.__elapsed_time += delta_ms

    def is_expired(self):
        return True if self.__elapsed_time >= self.__max_time else False
    
    def reset(self):
        self.__elapsed_time = 0
        self.__is_paused = False
        self.__pause_start_time = 0

    def pause(self):
        if not self.__is_paused:
            self.__is_paused = True
            self.__pause_start_time = self.__elapsed_time

    def unpause(self):
        if self.__is_paused:
            self.__is_paused = False
            self.__pause_start_time = 0
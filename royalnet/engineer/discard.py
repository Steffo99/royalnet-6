class Discard(BaseException):
    """
    A special exception which should be raised by Metals if a certain object should be discarded from the queue.
    """
    def __init__(self, obj, message):
        self.obj = obj
        self.message = message

    def __repr__(self):
        return f"<Discard>"

    def __str__(self):
        return f"Discarded {self.obj}: {self.message}"


__all__ = (
    "Discard",
)
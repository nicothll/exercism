class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message: str):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message: str):
        self.message = message


class CircularBuffer:
    """
    A class representing a circular buffer.

    Methods:
        read(): Returns the oldest element.
        write(): Writes into the buffer if is not full.
        overwrite(): Writes into the buffer if is full overwrites the oldest element.
        clean(): Resets the buffer.
    """

    def __init__(self, capacity: int) -> None:
        """Initializes a new circular buffer object.

        Args:
            capacity (int): The capacity of the buffer object (length)
        """

        self._capacity = capacity
        self._buffer = list()

    def read(self) -> str:
        """Returns the oldest elements and remove it from the buffer.

        Raises:
            BufferEmptyException: If the buffer is empty.

        Returns:
            str: The oldest element.
        """

        if len(self._buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        return self._buffer.pop()

    def write(self, data: str) -> None:
        """Writes a new element in the buffer.

        Args:
            data (str): The given element.

        Raises:
            BufferFullException: If the buffer is full, impossible to write into it.
        """

        if len(self._buffer) == self._capacity:
            raise BufferFullException("Circular buffer is full")
        self._buffer.insert(0, data)

    def overwrite(self, data: str) -> None:
        """Overwrites the oldest element a new element if the buffer is full, if not only write.

        Args:
            data (str): The new element.
        """

        if len(self._buffer) == self._capacity:
            self._buffer.pop()
        self.write(data)

    def clear(self) -> None:
        """Resets the buffer"""
        self._buffer.clear()

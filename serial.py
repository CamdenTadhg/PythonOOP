"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "Create instance of serial number generator starting with given value"
        self.start = start
        self.counter = -1

    def __repr__(self):
        "returns a string representing the instance of SerialGenerator"
        return f"SerialGenerator(start={self.start}, counter={self.counter})"
    
    def __str__(self):
        "returns a human readable string describing the instance of SerialGenerator"
        return f"generates serial numbers start with {self.start}"

    def generate(self):
        "generate a new number that is one more than the previous number generated"
        self.counter += 1
        return self.start + self.counter
    
    def reset(self):
        "reset the serial number generator to the initial start number"
        self.counter = -1

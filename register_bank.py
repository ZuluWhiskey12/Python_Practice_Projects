class RegisterBank:
    def __init__(self, num_registers):
        if type(num_registers) is not int:
            raise TypeError("Input integer value")
        
        if num_registers < 1:
            raise ValueError("Must have atleast 1 register")
        
        self.registers = [0] * num_registers
        
    def write_register(self, index, value):
        if type(index) is not int:
            raise TypeError("Invalid index")
        
        if index < 0 or index >= len(self.registers):
            raise IndexError("Register index out of range")
        
        if type(value) is not int:
            raise TypeError("Value must be integer")
        
        if value < 0 or value > 255:
            raise ValueError("Value out of range, must be between 0 and 255")
        
        self.registers[index] = value
        
    def read_register(self, index):
        if type(index) is not int:
            raise TypeError("Invalid index")
        
        if index < 0 or index >= len(self.registers):
            raise IndexError("Register index out of range")
        
        return self.registers[index]
        
    def reset_all(self):
        self.registers = [0] * len(self.registers)
from register_bank import RegisterBank

device = RegisterBank(4)

device.write_register(3,100)
assert device.read_register(3) == 100

device.reset_all()
assert device.read_register(0) == 0

print("All tests passed!")
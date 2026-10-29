from pprint import pprint
from analyze_tests import analyze_tests

test_results = [
    {"name": "reset_sequence", "status": "PASS", "duration_ms": 12},
    {"name": "register_readback", "status": "PASS", "duration_ms": 8},
    {"name": "packet_loopback", "status": "FAIL", "duration_ms": 46},
    {"name": "driver_init", "status": "TIMEOUT", "duration_ms": 150},
    {"name": "memory_access", "status": "PASS", "duration_ms": 24}
]

summary = analyze_tests(test_results)
pprint(summary, sort_dicts = False)
print()

empty_results = []

summary = analyze_tests(empty_results)
pprint(summary, sort_dicts=False)
print()

pass_results = [
    {"name": "reset_sequence", "status": "PASS", "duration_ms": 18},
    {"name": "register_readback", "status": "PASS", "duration_ms": 98},
    {"name": "packet_loopback", "status": "PASS", "duration_ms": 4}
]

summary = analyze_tests(pass_results)
pprint(summary, sort_dicts=False)
print()

variable_results = [
    {"name": "reset_sequence", "status": "pass", "duration_ms": 12},
    {"name": "register_readback", "status": "Pass", "duration_ms": 8},
    {"name": "packet_loopback", "status": "fail", "duration_ms": 46},
    {"name": "driver_init", "status": " Timeout ", "duration_ms": 150}
]

summary = analyze_tests(variable_results)
pprint(summary, sort_dicts=False)
print()

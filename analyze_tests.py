def analyze_tests(test_results):
    total_tests = len(test_results)
    
    pass_counter = 0
    fail_counter = 0
    timeout_counter = 0
    total_time = 0
    failed_timed_out = []
    
    for result in test_results:
        status = result["status"].strip().upper()
        
        if status == "PASS":
            pass_counter += 1 
            
        elif status == "FAIL":
            fail_counter += 1
            failed_timed_out.append(result["name"])   
            
        elif status == "TIMEOUT":
            timeout_counter += 1
            failed_timed_out.append(result["name"])
        else:
            raise ValueError(f"Unknown test status: {status}")
        total_time += result["duration_ms"]

    if total_tests > 0:
        average_time = total_time / total_tests
    else:
        average_time = 0
        
    if total_tests == 0:
        overall_results = "NO_TESTS"
    elif fail_counter > 0 or timeout_counter > 0:
        overall_results = "FAIL"
    else:
        overall_results = "PASS"
        
    summary = {
        "total_tests": total_tests,
        "passed": pass_counter,
        "failed": fail_counter,
        "timed_out": timeout_counter,
        "total_duration_ms": total_time,
        "average_duration_ms": average_time,
        "problem_tests": failed_timed_out,
        "overall_status": overall_results
    }
    
    return summary

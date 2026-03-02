"""Pytest plugin to print test summary: total/pass/fail."""


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    errors = len(terminalreporter.stats.get("error", []))
    total = passed + failed + errors

    terminalreporter.write_sep("=", "Test Summary")
    terminalreporter.write_line(f"Total:  {total}")
    terminalreporter.write_line(f"Passed: {passed}")
    terminalreporter.write_line(f"Failed: {failed}")
    if errors:
        terminalreporter.write_line(f"Errors: {errors}")

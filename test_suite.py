import unittest


test_loader = unittest.TestLoader()
test_suite = test_loader.discover(start_dir=".", pattern="test_*.py")


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
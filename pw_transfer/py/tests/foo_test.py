import sys
import unittest

for p in sys.path:
  print(p)

class FooTest(unittest.TestCase):

  def test_import_pw_transfer_foo(self):
    import pw_transfer.foo


if __name__ == "__main__":
  unittest.main()

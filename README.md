# rules_python_path

Small example of a PYTHONPATH issue with rules_python.

## Test failure

If you run `bazel test //pw_transfer/py:foo_test`, you'll get a test failure
that includes a printout of the PYTHONPATH. The PYTHONPATH look roughly like
this (with some directory prefixes removed for clarity):

```
~/src/rules_python_path/pw_transfer/py/tests
[prefix]/sandbox/linux-sandbox/1/execroot/rules_python_example/bazel-out/k8-fastbuild/bin/pw_transfer/py/foo_test.runfiles
[prefix]/sandbox/linux-sandbox/1/execroot/rules_python_example/bazel-out/k8-fastbuild/bin/pw_transfer/py/foo_test.runfiles/com_google_protobuf/python
[prefix]/sandbox/linux-sandbox/1/execroot/rules_python_example/bazel-out/k8-fastbuild/bin/pw_transfer/py/foo_test.runfiles/rules_python_example
[prefix]/sandbox/linux-sandbox/1/execroot/rules_python_example/bazel-out/k8-fastbuild/bin/pw_transfer/py/foo_test.runfiles/rules_python_example/pw_transfer/py
[prefix]/sandbox/linux-sandbox/1/execroot/rules_python_example/bazel-out/k8-fastbuild/bin/pw_transfer/py/foo_test.runfiles/com_google_protobuf
[prefix]/sandbox/linux-sandbox/1/execroot/rules_python_example/bazel-out/k8-fastbuild/bin/pw_transfer/py/foo_test.runfiles/python3_10_x86_64-unknown-linux-gnu
[prefix]/sandbox/linux-sandbox/1/execroot/rules_python_example/bazel-out/k8-fastbuild/bin/pw_transfer/py/foo_test.runfiles/six
[prefix]/execroot/rules_python_example/external/python3_10_x86_64-unknown-linux-gnu/lib/python310.zip
[prefix]/execroot/rules_python_example/external/python3_10_x86_64-unknown-linux-gnu/lib/python3.10
[prefix]/execroot/rules_python_example/external/python3_10_x86_64-unknown-linux-gnu/lib/python3.10/lib-dynload
~/.local/lib/python3.10/site-packages
[prefix]/execroot/rules_python_example/external/python3_10_x86_64-unknown-linux-gnu/lib/python3.10/site-packages
```

Notice that `runfiles/com_google_protobuf/python` and `runfiles/rules_python_example` appear before `rules_python_example/pw_transfer/py`. This is the cause of the `ImportError` in the test.

## Weird fix

You can "fix" the error by removing the dependency on the `py_proto_library`
from `//pw_transfer/py:foo`. This is weird because `py_proto_library` is also a
dependency of `//pw_transfer/py:foo_test` itself, and you don't need to remove
_that_ dependency!

Changes in the transitive deps reordering PYTHONPATH entries is a problem.


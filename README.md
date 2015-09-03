# lslock
Show list of files locked with flock.

### Usage
```python
lslock /tmp/lslock-test
```

### Test
Run `lslock-test.py` in different shell. It will execute 50 processes of `test.py`.

```bash
# python lslock-test.py
Press any key to exit...
```

```bash
# ./lslock /tmp/lslock-test/
9469    /tmp/lslock-test/12/12.lock
9470    /tmp/lslock-test/13/13.lock
9471    /tmp/lslock-test/14/14.lock
9472    /tmp/lslock-test/15/15.lock
9473    /tmp/lslock-test/16/16.lock
9474    /tmp/lslock-test/17/17.lock
```

from datetime import datetime
from datetime import timedelta

now = datetime(2050, 1, 1, 13, 0)
y = now.year

s = ""

def make_func(d):
    r = 'echo "%s" > file.txt\n' % d.isoformat()
    r += 'git add -A\n'
    r += 'git commit --date "%s" -m "This is a super legit commit."\n' % d.isoformat()
    return r

while now.year == y:
    s += make_func(now)
    now += timedelta(days=1)

with open("runme.sh", 'w') as f:
    f.write(s)

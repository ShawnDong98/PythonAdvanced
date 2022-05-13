# import sys
# sys.path.extend(['foo-package', 'bar-package'])
# import spam.blah
# import spam.grok

# import spam
# print(spam.__path__)

# import imp

# print(imp.reload(spam))

import spam
from spam import grok

print(spam.bar())
print(grok())
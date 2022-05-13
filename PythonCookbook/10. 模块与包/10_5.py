import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok

import spam
print(spam.__path__)
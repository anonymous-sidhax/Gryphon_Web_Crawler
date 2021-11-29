from django.test import TestCase

import Utils.views as a

a.get_time()

import Compliance_Checks.Accessibility as ass
ass.duplicate_id_check(1, "page.content", "https://www.google.com")
print (ass.duplicate_id_check)
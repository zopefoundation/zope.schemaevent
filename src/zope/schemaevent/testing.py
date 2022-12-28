# -*- coding: utf-8 -*-
from zope.component.testlayer import ZCMLFileLayer

import zope.schemaevent


ZC_LAYER = ZCMLFileLayer(zope.schemaevent,
                         zcml_file='configure.zcml')

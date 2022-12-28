# -*- coding: utf-8 -*-
import zope.component
import zope.schema


@zope.component.adapter(zope.schema.interfaces.IFieldEvent)
def fieldEventNotify(event):
    """Event subscriber to dispatch FieldEvents to interested adapters."""
    zope.component.subscribers((event.inst, event.field, event), None)

.. caution::

    This repository is no longer maintained and thus it got archived.

    If you want to work on it please open a ticket in
    https://github.com/zopefoundation/meta/issues requesting its unarchival.

.. contents::

Introduction
============

Enable handler for event triggered on field by adding subscriber.
We make the configuration glue between `zope.schema` (which doesn't depend on zope.component) and `zope.component`.

Example::

    <subscriber
       for=".interfaces.IExampleObject
            zope.schema.interfaces.IText
            zope.schema.interfaces.IFieldUpdatedEvent"
       handler=".localrolefield.set_local_role_on_object" />


#!/usr/bin/env python
# coding=utf-8


def to_dict(obj, fields=None, excludes=None, expands=None):
    ret = {}
    model_fields = []
    for field in obj._meta.get_fields():
        field_name = field.name
        model_fields.append(field_name)
        if (excludes is not None and field_name in excludes) or \
                (fields is not None and field_name not in fields):
            # skip field that in the excludes or not in ther fields
            continue
        try:
            fval = getattr(obj, field_name, None)
        except:
            fval = None
        if not isinstance(field, models.fields.related.RelatedField) or not fval:
            # Basic Field, get value directly
            ret[field_name] = _get_val(fval)
        else:
            if expands is None or field_name not in expands.keys():
                if isinstance(field, models.ForeignKey):
                    ret[field_name] = fval.id if fval else None
                else:
                    # ManyToManyField
                    ret[field_name] = list(fval.values_list('id', flat=True))
            else:
                # need expand related object
                related_fields = expands[field_name]
                if isinstance(field, models.ForeignKey):
                    ret[field_name] = _fetch_related(fval, related_fields)
                else:
                    # ManyToManyField
                    ret[field_name] = [_fetch_related(o, related_fields) for o in fval.all()]
    # access the field not a Model's Field
    if fields:
        for field_name in set(fields) - set(model_fields):
            fval = getattr(obj, field_name, None)
            if callable(fval):
                fval = fval()
            ret[field_name] = _get_val(fval)
    return ret

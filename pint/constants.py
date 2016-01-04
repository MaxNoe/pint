import scipy.constants as const


def constant(registry, name, with_error=False):
    value, unit, error = const.physical_constants[name]
    if not with_error or error == 0.0:
        return registry.Quantity(value, unit)
    else:
        return registry.Quantity(value, unit).plus_minus(error)

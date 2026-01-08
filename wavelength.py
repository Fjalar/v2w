import math

e = 1.602e-19
h = 6.626e-34
m_e = 9.11e-31
c = 3e8


def wavelength_from_voltage(voltage: float):
    return (
        h
        / math.sqrt(2.0 * m_e * e * voltage)
        / math.sqrt(1.0 + e * voltage / (2.0 * m_e * c**2))
    )


def wiki(voltage: float):
    return h / math.sqrt(2 * m_e * e * voltage * (1 + e * voltage / (2 * m_e * c**2)))


def debroglie(voltage: float):  # apparently does not account for relativity
    return 1.22 / math.sqrt(voltage * 1 / e)

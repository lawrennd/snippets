\ifndef{idealGasVelocitySample}
\define{idealGasVelocitySample}

\setupcode{import numpy as np

rng = np.random.default_rng(0)
n_velocities = 10000
velocity_sigma = 1.0
n_histogram_bins = 40
velocities = rng.normal(0.0, velocity_sigma, size=(n_velocities, 3))
speed = np.linalg.norm(velocities, axis=1)
velocity_x = velocities[:, 0]


def discrete_entropy(counts):
    n = counts.sum()
    p = counts[counts > 0] / float(n)
    return -np.sum(p * np.log(p))


def gaussian_differential_entropy(sigma):
    return 0.5 * np.log(2.0 * np.pi * np.e * sigma**2)


def maxwell_speed_pdf(s, sigma):
    return (
        np.sqrt(2.0 / np.pi)
        * (s**2 / sigma**3)
        * np.exp(-s**2 / (2.0 * sigma**2))
    )


def maxwell_speed_differential_entropy(sigma):
    return np.log(sigma * np.sqrt(2.0 * np.pi)) + np.euler_gamma - 0.5


def speed_range_max(s, p_hi=0.995):
    return float(np.quantile(s, p_hi))


def equal_delta_speed_edges(s_max, n_bins):
    return np.linspace(0.0, s_max, n_bins + 1)


def equal_volume_speed_edges(s_max, n_bins):
    u_edges = np.linspace(0.0, s_max**3, n_bins + 1)
    return u_edges ** (1.0 / 3.0)
}

\endif

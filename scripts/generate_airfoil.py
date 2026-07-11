#!/usr/bin/env python3
"""Generate NACA 4-digit airfoil coordinates."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def naca0012(n: int = 201) -> np.ndarray:
    beta = np.linspace(0.0, np.pi, n)
    x = 0.5 * (1.0 - np.cos(beta))
    t = 0.12
    yt = 5 * t * (
        0.2969 * np.sqrt(x)
        - 0.1260 * x
        - 0.3516 * x**2
        + 0.2843 * x**3
        - 0.1015 * x**4
    )
    upper = np.column_stack([x[::-1], yt[::-1]])
    lower = np.column_stack([x[1:], -yt[1:]])
    return np.vstack([upper, lower])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--points", type=int, default=201)
    parser.add_argument("-o", "--output", type=Path, default=Path("cases/naca0012.dat"))
    args = parser.parse_args()
    coords = naca0012(args.points)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savetxt(args.output, coords, fmt="%.10f", header="x y")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


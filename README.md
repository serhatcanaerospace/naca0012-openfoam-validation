# NACA0012 OpenFOAM Validation

![OpenFOAM](https://img.shields.io/badge/OpenFOAM-CFD-1F6FEB?style=flat) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat) ![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat)

Public validation project for a 2D NACA0012 airfoil using OpenFOAM. The target
is to compare lift, drag, pressure coefficient and skin-friction trends against
the NASA Turbulence Modeling Resource validation data.

## Why this project

NACA0012 is a clean, recognizable CFD validation case. It shows mesh setup,
turbulence modeling, force coefficient extraction, angle-of-attack sweeps and
benchmark comparison in one compact repository.

## Planned workflow

1. Generate NACA0012 coordinates and case geometry.
2. Build OpenFOAM cases for AoA = 0, 5, 10 and 15 deg.
3. Run `simpleFoam` with `kOmegaSST`.
4. Extract CL/CD/Cp.
5. Compare against NASA TMR data.

## Literature / benchmark

See [docs/literature.md](docs/literature.md).

---

## 📬 İletişim

[![Email](https://img.shields.io/badge/Email-serhatcandalmis%40gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:serhatcandalmis@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Serhat%20Can%20Dalm%C4%B1%C5%9F-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aerospaceserhatd/)
[![GitHub](https://img.shields.io/badge/GitHub-serhatcanaerospace-181717?style=flat&logo=github&logoColor=white)](https://github.com/serhatcanaerospace)

Sorular, işbirliği önerileri veya hata bildirimleri için Issues sekmesini de kullanabilirsiniz.

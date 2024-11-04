# BZ Reaction Numerical Solver

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)]()

A Python implementation of a Runge-Kutta 4th Order solver for the Belousov-Zhabotinsky (BZ) reaction system. This code provides numerical solutions and visualizations for the BZ reaction dynamics, demonstrating both oscillatory and non-oscillatory behaviors based on different parameter values.

## Features

- Runge-Kutta 4th Order (RK4) numerical integration
- Phase portrait visualization
- Time series analysis for state variables
- Parameter space exploration
- Interactive mode selection for different behavioral regimes
- High-quality matplotlib visualizations

## Installation

Clone the repository:
```bash
git clone https://github.com/Belouzov_Zhabotinski_Reaction.git
cd Belouzov_Zhabotinski_Reaction
```

Install the required dependencies:
```bash
pip install numpy matplotlib
```

## Usage

### Basic Usage

```python
python bz_solver.py
```

### Configuration

The main parameters that control the simulation are:

- `Oscillations`: Boolean flag to toggle between oscillatory and parameter exploration modes
- `a` and `b`: System parameters that control the reaction dynamics
- `h`: Time step for numerical integration (default: 0.01)
- `t_max`: Maximum simulation time (default: 10)

### Example Output

When `Oscillations = True`, the code generates three plots:
1. Phase portrait (x vs y)
2. x variable time series
3. y variable time series


## Mathematical Background

The BZ reaction is modeled using the following system of differential equations:

```
dx/dt = a - x - (4xy)/(1 + x²)
dy/dt = bx(1 - y/(1 + x²))
```

where:
- x and y are the state variables
- a and b are the control parameters

## Parameter Exploration

When `Oscillations = False`, the code explores different (a,b) parameter combinations:
- a values range from 100 to 1000
- b values range from 100 to 650

This helps in identifying regions of oscillatory behavior in the parameter space.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Guidelines for contributing:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Customization

You can modify the code to:
- Implement different numerical integration schemes
- Add new visualization methods
- Explore different parameter ranges
- Add analysis tools for the system dynamics


## Citation

If you use this code in your research, please cite:

```bibtex
@software{bz_reaction_solver,
  author = {Abhinab Sharma},
  title = {BZ Reaction Numerical Solver},
  year = {2024},
  url = {https://github.com/AbhinabSharma03/Belouzov_Zhabotinski_Reaction}
}
```

## Acknowledgments

- This implementation is based on the classical Belousov-Zhabotinsky reaction model
- Thanks to the scientific computing community for the numerical methods and visualization tools

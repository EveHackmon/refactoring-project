import numpy as np

class MonteCarloIntegrator:
    def __init__(self, f, a, b, num_samples=10000):
        """Initializes the Monte Carlo integrator.

        Args:
            f (function): The function to integrate.
            a (float): The lower bound of the integration.
            b (float): The upper bound of the integration.
            num_samples (int): The number of random samples to use (default is 10,000).
        """
        self.f = f
        self.a = a
        self.b = b
        self.num_samples = num_samples

    def integrate(self):
        """Performs Monte Carlo integration.

        Returns:
            float: The estimated value of the integral.
            float: The estimated error of the integral.
        """
        samples = np.random.uniform(self.a, self.b, self.num_samples)
        sample_values = self.f(samples)
        integral_estimate = (self.b - self.a) * np.mean(sample_values)
        error_estimate = (self.b - self.a) * np.std(sample_values) / np.sqrt(self.num_samples)
        return integral_estimate, error_estimate

def function_to_integrate(x):
    """The function to be integrated."""
    return x**2 - 8*x**3

a = 0
b = 1
num_samples = 10000

integrator = MonteCarloIntegrator(function_to_integrate, a, b, num_samples)
estimated_integral, estimated_error = integrator.integrate()

print(f"Estimated integral: {estimated_integral}")
print(f"Estimated error: {estimated_error}")

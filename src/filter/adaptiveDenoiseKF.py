from .denoiseKF import DenoiseKF

"""
Cited Work:
1.
Yazdkhasti S, Sabzevari D, Sasiadek JZ. 
Adaptive H-infinity extended Kalman filtering for a navigation system in presence of high uncertainties. 
Transactions of the Institute of Measurement and Control. 2023;45(8):1430-1442. doi:10.1177/01423312221136022
"""

class AdaptiveDenoiseKF(DenoiseKF):
    def __init__(self, init_state : float, init_cov : float, sys_noise : float, proc_noise : float) -> None:
        """_summary_

        Args:
            init_state (float): initial state estimate [1x1]
            init_cov (float): initial state estimate uncertainty measured through covariance matrix [1x1]
            sys_noise (float): systemic noise covariance matrix [1x1]
            proc_noise (float): observation noise covariance matrix [1x1]
        """
        super().__init__(init_state, init_cov, sys_noise, proc_noise)
        
        # Adaptive variables
        self.counter = 1 # Number of iterations of the filter
        self.forgetting_factor = 0.5  # Adoption weight, can be made an input
        self.systemic_adaption_constant = 1 # Positive constant used for adoption condition
        self.state_covariance_adaption_constant = 1.5 # Positive constant in [1, 2.5] for state covariance adaption
        
        
    @property
    def mu(self):
        return (1 - self.forgetting_factor) / (1 - self.forgetting_factor**self.counter)
    
    def _systemic_noise_adaption(self, measurement : float):
        """
        Adaptive logic that encapsulates adopting systemic noise covariance
        Hallucinates a kalman filter iteration to calculate statistics
        Statistics then compared to "systemic_adaption_constant"
        If criteria is met, then systemic noise covariance is changed
        Args:
            measurement (float): measured quantity taken in by filter
        """
        temporary_filter = DenoiseKF(self.state, 
                                     self.cov, 
                                     self.systemic_noise_variance, 
                                     self.observation_noise_variance)
        temporary_filter.predict()
        temporary_innovation = measurement - self.state
        temporary_innovation_covariance = self.cov + self.observation_noise_variance
        
        # See essentially how many standard deviations the innovation is
        # Square root of the squared deviation over the variance
        mahanobolis_distance = ((temporary_innovation ** 2) / temporary_innovation_covariance) ** 0.5
        
        if mahanobolis_distance > self.systemic_adaption_constant:
            temporary_kalman_gain = temporary_filter.cov / temporary_innovation_covariance
            
            # Adaption update
            self.systemic_noise_variance = (self.mu * (temporary_kalman_gain ** 2) * (temporary_innovation ** 2)) 
            + temporary_filter.cov - self.cov 
            + (1 - self.mu) * self.systemic_noise_variance 
        
    def _observation_noise_adaption(self, measurement : float):
        """
        Adapts the observation noise model using a forgetting factor
        Args:
            measurement (float): input to the filter
        """
        temporary_innovation = measurement - self.state
        self.observation_noise_variance = (1 - self.mu) * self.observation_noise_variance \
                                          + self.mu * (temporary_innovation ** 2 + self.cov)
    
        
    def kalman_iteration(self, measurement):
        self._systemic_noise_adaption(measurement)
        super().predict()
        self._observation_noise_adaption(measurement)
        
        innovation_covariance = self.cov + self.observation_noise_variance
        super().update(measurement)
        
        postfit_residual = measurement - self.state
        mahanobolis_distance = (( postfit_residual ** 2) / innovation_covariance) ** 0.5
        
        if mahanobolis_distance > self.state_covariance_adaption_constant:
            adaption_factor = (self.state_covariance_adaption_constant / mahanobolis_distance)
            self.cov *= 1 / adaption_factor
        
        
# Local file testing    
if __name__ == "__main__":
    def iterate(data : list):
        kf = AdaptiveDenoiseKF(10, 10000, 0, 1000)
        for item in data:
            kf.predict()
            kf.update(item)
            print(kf.state)
    data = [0 for i in range(1000)]
    iterate(data)
    
        
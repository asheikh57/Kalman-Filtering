from .denoiseKF import DenoiseKF
from numpy.linalg import inv, multi_dot
from numpy import array

"""
Cited Work:
1.
Yazdkhasti S, Sabzevari D, Sasiadek JZ. 
Adaptive H-infinity extended Kalman filtering for a navigation system in presence of high uncertainties. 
Transactions of the Institute of Measurement and Control. 2023;45(8):1430-1442. doi:10.1177/01423312221136022
"""

class DenoiseHInfinityFilter(DenoiseKF):
    
    def __init__(self, init_state: float, init_cov: float, sys_noise: float, proc_noise: float) -> None:
        """ 
        Same as DenoiseKF constructor. Different with the addition of the gamma factor inherent to H-infinity filtering.
         
        Args:
            init_state (float): initial state estimate [1x1]
            init_cov (float): initial state estimate uncertainty measured through covariance matrix [1x1]
            sys_noise (float): systemic noise covariance matrix [1x1]
            proc_noise (float): observation noise covariance matrix [1x1]
        """
        super().__init__(init_state, init_cov, sys_noise, proc_noise)
        # H infinity gamma factor
        self.gamma = 10
        
    def update(self, measurement):
        """
        Implement H-infinity update step. Only difference is in how covariance is updated

        Args:
            measurement (float): measurement fed into filter. 
        """
        
        gramian = array([[self.observation_noise_variance + self.cov, self.cov],
                         [self.cov, self.cov - self.gamma**2]])
        
        temp_matrix = array([1,1])
        cov_temp = self.cov - self.cov * multi_dot([temp_matrix, inv(gramian), temp_matrix]) * self.cov
        super().update(measurement)
        self.cov = cov_temp
    
    def kalman_iteration(self, measurement):
        super().predict()
        self.update(measurement)
    
    # Local file testing    
if __name__ == "__main__":
    def iterate(data : list):
        kf = DenoiseHInfinityFilter(10, 10000, 0, 10)
        for item in data:
            kf.predict()
            kf.update(item)
            print(kf.state)
    data = [0 for i in range(1000)]
    iterate(data)
    
        
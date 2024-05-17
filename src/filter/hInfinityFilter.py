from denoiseKF import DenoiseKF
from numpy.linalg import inv, multi_dot
from numpy import array

"""
Cited Work:
1.
Yazdkhasti S, Sabzevari D, Sasiadek JZ. 
Adaptive H-infinity extended Kalman filtering for a navigation system in presence of high uncertainties. 
Transactions of the Institute of Measurement and Control. 2023;45(8):1430-1442. doi:10.1177/01423312221136022
"""

class HInfinityFilter(DenoiseKF):
    def __init__(self, init_state: float, init_cov: float, sys_noise: float, proc_noise: float) -> None:
        super().__init__(init_state, init_cov, sys_noise, proc_noise)
        # H infinity gamma factor
        self.gamma = 10
    def update(self, measurement):
        gramian = array([[self.observation_noise_variance + self.cov, self.cov],
                         [self.cov, self.cov - self.gamma**2]])
        
        temp_matrix = array([1,1])
        cov_temp = self.cov - self.cov * multi_dot([temp_matrix, inv(gramian), temp_matrix]) * self.cov
        super().update(measurement)
        self.cov = cov_temp
        
    
    # Local file testing    
if __name__ == "__main__":
    def iterate(data : list):
        kf = HInfinityFilter(10, 10000, 0, 10)
        for item in data:
            kf.predict()
            kf.update(item)
            print(kf.state)
    data = [0 for i in range(1000)]
    iterate(data)
    
        
from .filterbase import FilterBase

class DenoiseKF(FilterBase):
    def __init__(self, init_state : float, init_cov : float, sys_noise : float, proc_noise : float) -> None:
        """

        Args:
            init_state (float): initial state estimate [1x1]
            init_cov (float): initial state estimate uncertainty measured through covariance matrix [1x1]
            sys_noise (float): systemic noise covariance matrix [1x1]
            proc_noise (float): observation noise covariance matrix [1x1]
        """
        self.state = init_state
        self.cov = init_cov
        self.systemic_noise_variance = sys_noise
        self.observation_noise_variance = proc_noise
        
        
    def predict(self):
        """_summary_
        In this case there are no known dynamics of the incoming signal
        Thus, all that occurs is adding noise into the state covariance, inherent to the inaccuracy of the model
        The point here is that derivatives of the state take the form of gaussian zero mean noise
        """
        
        # Increase uncertainty according to systemic noise
        self.cov += self.systemic_noise_variance
    
    @property
    def transition_model(self):
        """_summary_
        
        No process model, or time evolution
        Returns:
            transition matrix (float) : In this case for a 1D signal, the [1x1] identity, or just 1
        """
        return 1
    
    @property
    def observation_model(self):
        """
        measurements are the same as estimate in the case of simple denoising, hence returns [1x1] identity 
        Returns:
            observation_model (float): _description_
        """
        return 1 
    

    def update(self, measurement):
        """
        Observation model is [1x1] identity, and 1D case, so this simplifies vastly
        
        Updates state with a measurement 
        """
        
        # Calculate innovation, or pre-fit residual: an estimate of the error in the state estimate
        innovation = measurement - self.state
        
        # Calculate innovation covariance, which determines uncertainty in the error in the state estimate
        innovation_covariance = self.cov + self.observation_noise_variance
        
        # Calculate kalman gain, which essentially as a weighting
        kalman_gain = self.cov / innovation_covariance
        
        # Update state based on weighting of state estimate and the measurement determined by kalman gain
        self.state += kalman_gain * innovation
        
        # Update state covariance, or uncertainty
        self.cov -= kalman_gain * self.cov
        
    def kalman_iteration(self, measurement):
        self.predict()
        self.update(measurement)
        
    
        

# Local file testing    
if __name__ == "__main__":
    def iterate(data : list):
        kf = DenoiseKF(10, 10000, 0, 1000)
        for item in data:
            kf.predict()
            kf.update(item)
            print(kf.state)
    data = [0 for i in range(1000)]
    iterate(data)
    
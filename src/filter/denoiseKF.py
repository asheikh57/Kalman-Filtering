from filterbase import Filter

class DenoiseKF(Filter):
    def __init__(self, init_state : float, init_cov : float, sys_noise : float, proc_noise : float) -> None:
        """_summary_

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
        
        innovation = measurement - self.state
        
        innovation_covariance = self.cov + self.observation_noise_variance
        
        kalman_gain = self.cov / innovation_covariance
        
        self.state += kalman_gain * innovation
        
        self.cov -= kalman_gain * self.cov
        
        
    
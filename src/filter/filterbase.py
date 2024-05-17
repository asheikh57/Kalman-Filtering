from abc import ABC, abstractmethod

class Filter(ABC):
    
    @abstractmethod
    def predict(self):
        """ 
        Prediction function for filters. 
        Makes prediction using underlying process model.
        """
        pass
    
    @abstractmethod
    def update(self, measurement):
        """
        Make update to state using measurement
        """
        pass
    
    @abstractmethod
    @property
    def transition_model(self):
       """
       Get transition matrix that implements process model
       """
       pass
   
    @abstractmethod
    @property
    def observation_model(self):
       """
       Get observation model matrix that connects measurements to state.
       """
       pass
   

   
       

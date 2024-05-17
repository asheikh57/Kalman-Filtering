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
    
    @property
    @abstractmethod
    def transition_model(self):
       """
       Get transition matrix that implements process model
       """
       pass
   
    @property
    @abstractmethod
    def observation_model(self):
       """
       Get observation model matrix that connects measurements to state.
       """
       pass
   

   
       

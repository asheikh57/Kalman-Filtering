from abc import ABC, abstractmethod

class FilterBase(ABC):
    
    @abstractmethod
    def kalman_iteration(self, measurement):
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
   

   
       

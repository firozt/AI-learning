import math
from collections import Counter
from typing import List;
import numpy as np;

class NaiveBayes():
    def __init__(self) -> None:
        pass

    
    def fit(self, X: List[any], y: List[any]) -> None:
        self.X = X
        self.y = y
        self.classifications = list(set(y))
    
    
    def predict(self, X: List[any]) -> List[any]:
        [self.Pclass(c) * [self.Pgiven(x,c) for x in X] for c in self.classifications]
    
    # Returns P(class)
    def Pclass(self, classification: str | int) -> float:
        return Counter(self.y)[classification]/len(self.y)
    
    def Pgiven(self, v1, v2) -> float:
        P
        
import pandas as pd
import numpy
import datetime
import random
import json
from models import Reciepts

POINTS_OF_DATA = 5

# Receipt Data Creation
print(json.dumps(Reciepts(1, [1,2,3,4,5], 123)._get_dict(), indent=4, default=str))


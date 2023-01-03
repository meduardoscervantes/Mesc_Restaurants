import pandas as pd
import numpy
import datetime
import random
import json
from models import Reciepts, RecieptItem, Recipe, BOH_Item, Server

POINTS_OF_DATA = 5

# Receipt Data Creation
print(json.dumps(Reciepts(1, [1,2,3,4,5], 123)._get_dict(), indent=4, default=str))


# Item Data Creation
print(json.dumps(RecieptItem(1,123, [1,2,3,4,5])._get_dict(), indent=4, default=str))
print(json.dumps(Recipe(1,123, [1,2,3,4,5])._get_dict(), indent=4, default=str))
print(json.dumps(BOH_Item(1,123)._get_dict(), indent=4, default=str))
print(json.dumps(Server(1,'name', datetime.datetime.now(), datetime.datetime.now())._get_dict(), indent=4, default=str))


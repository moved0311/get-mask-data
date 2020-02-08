#-*- coding=utf-8 -*-
import pandas as pd
import requests

pharmacy = pd.read_csv("./pharmacy.csv")
maskremain = pd.read_csv("./remain.csv")

merged = pharmacy.merge(maskremain, on=["醫事機構代碼","醫事機構名稱"])
merged.to_csv("output.csv",  index=False)



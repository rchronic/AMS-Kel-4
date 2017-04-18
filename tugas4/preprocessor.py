import numpy as np
from util import load_dataset, save_model, load_model
import sys

with open("dataset-sentanal.txt", "r") as dataset:
    lines = []
    for line in dataset:
        lines.append(line)

	for instance in lines:
		review = instance.split('## ')
		absa = review[0]
		sentence = review[1]
		print absa


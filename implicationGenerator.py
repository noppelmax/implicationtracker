#!/usr/bin/python

# Author: Maximilian Noppel
# July 2020
#
# Credits to: https://www.techiedelight.com/kahn-topological-sort-algorithm/
# The implementation of Kahn Alg. is from this website.
#

import logging
from collections import deque


FORMAT = "%(asctime)-15s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
logger = logging.getLogger("implicationgenerator")
logger.info("Starting run!")



if __name__ == '__main__':

	properties = ["nD-Es-","nD-Es-CU","nD-Es-H","nD-Es-P","nD-Es-U","nD-Es-U-H","nD-Es-U-P","nD-Es-Q","nD-Es-Q-P","CU","H","P","U","U-H","U-P","Q","Q-P","nCU","nH","nP","nU","nU-nH","nU-nP","nQ","nQ-nP","nD-Es-nCU","nD-Es-nH","nD-Es-nP","nD-Es-nU-nH","nD-Es-nU","nD-Es-nU-nP","nD-Es-nQ-nP","nD-Es-nQ"]

	for p in properties:
		print("%s-OPA => %s-OCA" % (p,p))

	print("#")

	properties = ["nCU","nH","nP","nU","nU-nH","nU-nP","nQ","nQ-nP"]

	for p in properties:
		print("nD-Es-%s-OCA => %s-OCA" % (p,p))

	print("#")

	properties = ["CU","H","P","U","U-H","U-P","Q","Q-P"]

	for p in properties:
		print("%s-OPA => nD-Es-%s-OPA" % (p,p))

	print("#")

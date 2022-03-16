import pandas as pd

output=open("close_world_data.csv", 'w')
col_name=""
features=["cache-misses","node-loads","branch-misses","branch-load-misses","LLC-store-misses","branch-loads","L1-dcache-stores","L1-icache-load-misses","branch-instructions","iTLB-loads","iTLB-load-misses","dTLB-store-misses","dTLB-load-misses","dTLB-stores","node-stores","L1-dcache-load-misses"]
for i in range(5):
	for feature in features:
		col_name+=feature+"_"+str(i + 1)+"s,"
col_name+="label\n"

output.write(col_name)

for i in range(30):
	for j in range(100):
		file = open("alexa_30_perf/" + str(i+1) + "/" + str(i+1) + "-" + str(j+1) + ".txt")
		next(file)
		next(file)
		next(file)

		res = ""
		for line in file:
			data = line.split()
			val = data[1].replace(',','')
			res+=(val+ ",")
		res+=(str(i+1) + "\n")
		file.close()
		output.write(res)

output.close();


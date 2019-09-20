import time
from input_data import input_data
import pdb

def print_target_message(meg):
	os.system(f"node ./bilibili-live-danmaku-api/stdio.js 6ac47994%2C1571542808%2C7561b691 338ffd665189506c8538d4d7f5fc9152 686555 {meg}")
	# pdb.set_trace()
	# print(f">> {meg} at {(time.time() - start_time)}")
if __name__ == '__main__':
	import os
	input_data_instance = input_data()
	data = input_data_instance.return_example_input_list()
	time_list = input_data_instance.return_example_time_list()
	start_time = time.time()
	import sched, time
	s = sched.scheduler(time.time, time.sleep)
	index = 0
	for (time_stamp, single_meg) in zip(time_list, data):
		s.enter(time_stamp, 1, print_target_message, (single_meg,))
		index = index + 1
	s.run()









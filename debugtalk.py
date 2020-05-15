
import time

def sleep(n_secs):
    time.sleep(n_secs)


def is_thing_existed(data):
	if not data:
		return True
	else:
		return False

def is_device_existed(data):
	if not data:
		return True
	else:
		return False

def get_test_thing_names():
	return [
			{"thing_name":"edge_thing_test","thing_type":2},
			{"thing_name":"end_thing_test","thing_type":1},
 		   ]

def get_device_id(device_data):
	if not device_data:
		return "unexisted_device_id"
	if len(device_data) > 1:
		return "multi_device_ids"
	else:
		return device_data[0]['device_id']

def get_device_group_id(device_group_data):
	if not device_group_data:
		return "unexisted_device_group_id"
	if len(device_group_data) > 1:
		return "multi_device_group_ids"
	else:
		return device_group_data[0]['group_id']

def cal_devices_counts(*args):
	sum = 0
	for i in args:
		print(i)
		sum = sum + int(i)
	return sum

def get_device_count(device_data):
	if not device_data:
		return 0
	else:
		print(device_data)
		return len(device_data)

def get_device_ids(device_data):
	if not device_data:
		return "unexisted_device_id"
	else:
		ids=""
		for id in device_data:
			ids = id + ','
		return ids[:-2]

def join_multi_ids(*args):
	return ",".join(args)

def get_thing_ids_list(thing_datas):
	if not thing_datas:
		return []
	thing_ids=[]
	for thing_data in thing_datas:
		thing_ids.append(thing_data['id'])
	return thing_ids


def get_thing_id(thing_data):
	if not thing_data:
		return "unexisted_thing_id"
	if len(thing_data) > 1:
		return "multi_thing_ids"
	else:
		return thing_data[0]['id']
	 
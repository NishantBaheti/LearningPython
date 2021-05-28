
RS = ["PANVEL","KHANDESHWAR","MANSAROVAR","KHARGHAR","BELAPUR","SEAWOOD","NERUL"]
Trains = [7.30, 8.2, 12.45, 13.30, 14.44, 15.50, 9.15, 10.20, 23.59, 17.33, 19.20]
T = [0,4,5,3,4,5,3]


def number_of_trains_to_arrive(curr_time,station):
	station = station.upper()
	total_time_for_station = 0
	for i in range(len(RS)):
		total_time_for_station += T[i]
		if RS[i] == station: 
			break
	trains_to_arrive = 0
	for i in Trains:
		if i+total_time_for_station >= curr_time:
			trains_to_arrive += 1	
	return trains_to_arrive

if __name__ == "__main__":
	curr_time = float(input("current time :"))
	station = input("Station :")
	
	print(number_of_trains_to_arrive(curr_time,station))

def banzhaf(seq):
	def find_winning_coalitions(n, votes_required, votes, idx, cur_coalition, winning_coalitions):
		if sum(votes[j] for j in cur_coalition) >= votes_required:
			winning_coalitions.append(cur_coalition)
		if idx >= n:
			return
		for i in range(idx, n):
			new_coalition = cur_coalition + [i]
			find_winning_coalitions(n, votes_required, votes, i+1, new_coalition, winning_coalitions)

	votes_required, votes = seq[0], seq[1:]
	winning_coalitions = []
	find_winning_coalitions(len(votes), votes_required, votes, 0, [],  winning_coalitions)
	power = {voter: 0 for voter in range(0, len(votes))} 
	for winning_coalition in winning_coalitions:
		sum_of_votes = sum(votes[j] for j in winning_coalition)
		for voter in winning_coalition:
			if sum_of_votes - votes[voter] < votes_required:
				power[voter] += 1
	total_critical_votes = sum(power.values())
	for voter in power:
		power[voter] = round(power[voter] / total_critical_votes, 3)	
	print(power)

if __name__ == '__main__':
	banzhaf([65, 47, 46, 17, 16, 2])

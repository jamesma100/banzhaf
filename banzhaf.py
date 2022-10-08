import argparse

def banzhaf(seq):
	# recursively look for combinations of voters that will produce a winning coalition
	def find_winning_coalitions(votes, idx, cur_coalition, winning_coalitions):
		if sum(votes[j] for j in cur_coalition) >= votes_required:
			winning_coalitions.append(cur_coalition)
		if idx >= n:
			return
		for i in range(idx, n):
			new_coalition = cur_coalition + [i]
			find_winning_coalitions(votes, i+1, new_coalition, winning_coalitions)

	votes_required, votes, n, winning_coalitions = seq[0], seq[1:], len(votes), []
	find_winning_coalitions(votes, 0, [],  winning_coalitions)

	power = {voter: 0 for voter in range(0, len(votes))}
	for winning_coalition in winning_coalitions:
		sum_of_votes = sum(votes[j] for j in winning_coalition)
		# for each voter check if the absence of that voter's vote could swing
		# the total below the required threshold, if so power++ to that voter
		for voter in winning_coalition:
			if sum_of_votes - votes[voter] < votes_required:
				power[voter] += 1
	total_critical_votes = sum(power.values())
	for voter in power:
		power[voter] = round(power[voter] / total_critical_votes, 3)
	print("here is the power distribution of your voters:")
	print("\n".join("voter " + str(key) + ": " + str(power[key]) for key in power))

def main():
	parser = argparse.ArgumentParser(description="parse input votes")
	parser.add_argument('required', type=int, help="<required votes to pass>")
	parser.add_argument('votes', nargs='+', type=int, help="<sequence of votes>")
	args = parser.parse_args()
	banzhaf([args.required] + args.votes)

if __name__ == '__main__':
	# banzhaf([65, 47, 46, 17, 16, 2]) -> {0.333, 0.259, 0.185, 0.111, 0.111}
	main()

from fractions import Fraction
LESS_THAN_FRACTION = Fraction(3, 7)
MAX_DENOMINATOR = 1_000_000


def get_closest_fraction(denominator, for_fraction, closest_fraction):
	# optimised range for all possible numerators:
	# 1. this starts from numerator of closest fraction found before
	# 2. ends on numerator that has fraction width specified denominator which equals 3/7 + 1/{denominator}
	numerator_range = range(closest_fraction.numerator, int(denominator * 3 / 7) + 1)
	for numerator in numerator_range:
		next_fraction = Fraction(numerator, denominator)
		if for_fraction > next_fraction > closest_fraction:
			closest_fraction = next_fraction
	return closest_fraction


def resolve():
	percent = MAX_DENOMINATOR / 100
	closest_fraction = Fraction(0, 1)
	for denominator in get_denominators_range():
		# show percents of progress
		if denominator % percent == 0:
			print(f'{denominator / percent}%')

		closest_fraction = get_closest_fraction(denominator, LESS_THAN_FRACTION, closest_fraction)
	print(f'The closest fraction is: {closest_fraction}')


def get_denominators_range():
	return range(2, MAX_DENOMINATOR + 1)


if __name__ == '__main__':
	resolve()

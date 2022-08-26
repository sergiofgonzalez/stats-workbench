from math import floor, sqrt

def sample_mean(sample):
    return sum(sample) / len(sample)

def trimmed_mean(sample, pct):
    sorted_sample = sorted(sample)
    num_items_to_remove = floor((pct / 100) * len(sorted_sample))
    trimmed_sorted_sample = sorted_sample[num_items_to_remove:-num_items_to_remove]
    return sample_mean(trimmed_sorted_sample)

def sample_median(sample):
    sorted_sample = sorted(sample)
    if len(sorted_sample) % 2 == 1:
        return sorted_sample[len(sorted_sample) // 2]
    else:
        return 1 / 2 * (sorted_sample[(len(sorted_sample) // 2) - 1] + sorted_sample[len(sorted_sample) // 2])

def sample_variance(sample):
    degrees_of_freedom = len(sample) - 1
    mean = sample_mean(sample)
    sum_squares = sum([(x - mean) ** 2 for x in sample])
    return sum_squares / degrees_of_freedom

def sample_standard_deviation(sample):
    return sqrt(sample_variance(sample))

def sample_range(sample):
    return max(sample) - min(sample)


def pct_diff(val1, val2):
    """This function returns the percentage difference between the given values

    For example, if you invoke pct_diff(1, 2) it will return 100 as there is
    a 100% difference between the values
    """
    return ((val2 - val1) / val1) * 100

def get_stats(data_set):
    """Returns the sample mean, sample median, variance, and standard deviation of the given dataset.
    """
    data_set_len = len(data_set)
    mean = sum(data_set) / data_set_len
    sorted_data_set = sorted(data_set)
    if data_set_len % 2 == 1:
        median = sorted_data_set[data_set_len // 2]
    else:
        median = 1 / 2 * (sorted_data_set[(data_set_len // 2) - 1] + sorted_data_set[data_set_len // 2])

    sum_squares = sum([(x - mean) ** 2 for x in data_set])
    variance = sum_squares / (data_set_len - 1)
    std_dev = sqrt(variance)
    range = max(data_set) - min(data_set)

    return {
        "mean": mean,
        "median": median,
        "variance": variance,
        "std_dev": std_dev,
        "range": range
    }


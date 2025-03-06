import numpy as np


def cumsum_sum(pcm_complex, gen_indices_in_cumsum_order):
    # Create an angular cumulative sum of the pcm amplitudes that can be plotted on the sum vs mask angle plot:
    sums_of_pcm_columns = np.sum(pcm_complex, axis=0)
    sums_of_columns_in_cumsum_order = sums_of_pcm_columns[gen_indices_in_cumsum_order]
    cumsum_abs = np.abs(np.cumsum(sums_of_columns_in_cumsum_order))
    return cumsum_abs


def cumsum_vcf(pcm_complex, gen_indices_in_cumsum_order):
    # Calculate the cumulative vector coherence factor of the complex values found in the PCM as a function of gen
    # angle:
    # First, calculate element-wise division by modulus to give unit vectors:
    pcm_complex_unit = pcm_complex / np.abs(pcm_complex)
    # We will store the complex sum produced for each mask angle and use it in the calculation of the VCF for the
    # next mask angle to avoid repetition of summing:
    complex_sum_accumulator = np.cdouble(0, 0)
    # Pre-allocate the output array containing the cumulative vector coherence factor:
    n_tx = np.shape(pcm_complex)[0]
    cum_vcf = np.zeros(n_tx)
    for i, column_index in enumerate(gen_indices_in_cumsum_order):
        unit_vector_column_to_add = pcm_complex_unit[:, column_index]
        complex_sum_accumulator = complex_sum_accumulator + np.sum(unit_vector_column_to_add)
        cum_vcf[i] = np.abs(complex_sum_accumulator) / ((i+1) * n_tx)
    return cum_vcf


def cumsum_vcf_numerator(pcm_complex, gen_indices_in_cumsum_order):
    # Calculate the numerator of the cumulative vector coherence factor of the complex values found in the PCM as a
    # function of gen angle:
    # First, calculate element-wise division by modulus to give unit complex vectors:
    pcm_complex_unit = pcm_complex / np.abs(pcm_complex)
    # We will store the complex sum produced for each mask angle and use it in the calculation of the VCF for the
    # next mask angle to avoid repetition of summing:
    complex_sum_accumulator = np.cdouble(0, 0)
    # Pre-allocate the output array containing the cumulative vector coherence factor:
    n_tx = np.shape(pcm_complex)[0]
    cum_vcf_numerator = np.zeros(n_tx)
    for i, column_index in enumerate(gen_indices_in_cumsum_order):
        unit_vector_column_to_add = pcm_complex_unit[:, column_index]
        complex_sum_accumulator = complex_sum_accumulator + np.sum(unit_vector_column_to_add)
        cum_vcf_numerator[i] = np.abs(complex_sum_accumulator)
    return cum_vcf_numerator

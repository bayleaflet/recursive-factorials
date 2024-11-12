from Indv import Indv
import sys
import argparse
from math import factorial


def parse_fasta_to_indv(file_path):
    '''Parses a FASTA file to create Indv instances.'''
    individuals = []
    with open(file_path, 'r') as file:
        while True:
            # Read each header and sequence line
            header = file.readline().strip()
            sequence = file.readline().strip()

            if not header or not sequence:
                break

            # Extract sample_id and date_of_seq from header
            header_parts = header[1:].split("_")
            sample_id = header_parts[0]
            date_info = header_parts[1]
            date_of_seq = date_info.split()[0]  # Split and take first part as date
            phenotype = None  # Placeholder for phenotype

            # Create Indv instance
            individual = Indv(sample_id, date_of_seq, phenotype, sequence)
            individual.assign_phenotype()
            individuals.append(individual)

    return individuals


def calculate_traits(individuals):
    '''Calculate total sample size and count of orange individuals.'''
    n = len(individuals)  # Total number of individuals
    k = Indv.get_orange_count()  # Number of orange individuals
    return n, k


def calculate_binomial_probability(n, k, p):
    '''Calculate binomial probability manually.'''
    binom_coeff = factorial(n) // (factorial(k) * factorial(n - k))
    return binom_coeff * (p ** k) * ((1 - p) ** (n - k))


def write_results(output_file, n, k, probability, individuals, trait_frequency):
    '''Write the results to the specified output file.'''
    with open(output_file, 'w') as file:
        file.write("Results\n\n")
        file.write(f"p (the frequency of \"orange\" in the population) = {trait_frequency}\n")
        file.write(f"n (the number of sampled individuals) = {n}\n")
        file.write(f"k (the number of \"orange\" individuals in the sample set) = {k}\n\n")
        file.write(f"Probability of collecting {n} individuals with {k} being \"orange\" ")
        file.write(f"(given a population frequency of {trait_frequency}) = {probability}\n")

def main():
    # Retrieve command-line arguments
    fasta_file = sys.argv[1]
    trait_frequency = float(sys.argv[2])
    output_file = sys.argv[3]

    # Parse the FASTA file to create Indv instances
    individuals = parse_fasta_to_indv(fasta_file)

    # Calculate total individuals (n) and orange individuals (k)
    n, k = calculate_traits(individuals)

    # Calculate the probability based on the frequency of the trait
    probability = calculate_binomial_probability(n, k, trait_frequency)

    # Write results to the output file
    write_results(output_file, n, k, probability, individuals, trait_frequency)


# Run the script only if it's being executed as the main module
if __name__ == "__main__":
    main()

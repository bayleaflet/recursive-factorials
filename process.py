from Indv import Indv
import sys
import argparse


def parse_fasta_to_indv(file_path):
    ''' Parses fasta to create Indv instances'''
    individuals = []
    with open(file_path, 'r') as file:
        while True:

         # Iterate over lines, processing each sample entry
            header = file.readline().strip()
            sequence = file.readline().strip()

            if not header or not sequence:
                break

            # Extract sample_id and date_of_seq
            # Remove > and split on _
            header_parts = header[1:].split("_")
            sample_id = header_parts[0]
            date_info = header_parts[1]
            date_info.split()
            date_of_seq = date_info[0]
            phenotype = None # Placeholder

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
    '''Calculate binomial probability manually'''
    binom_coeff = factorial(n) // (factorial(k) * factorial(n - k))
    return binom_coeff * (p ** k) * ((1 - p) ** (n - k))


def write_results(output_file, n, k, probability):
    '''Write the results to the specified output file.'''
    with open(output_file, 'w') as file:
        file.write(f"Total number of individuals: {n}\n")
        file.write(f"Number of individuals with orange phenotype: {k}\n")
        file.write(f"Probability of observing {k} orange individuals given n={n} and p={p}: {probability}\n")
        file.write("\nList of individuals with the orange phenotype:\n")

        for indv in individuals:
            if indv.phenotype == 'Orange':
                file.write(f"{indv.sample_id}, sequenced on {indv.date_of_seq}\n")

def main():
    # Retrieve command-line arguments
    fasta_file = sys.argv[1]
    trait_frequency = float(sys.argv[2])
    output_file = sys.argv[3]

    # Parse the fasta file to create Indv instances
    individuals = parse_fasta_to_indv(fasta_file)

    # Calculate total individuals (n), orange individuals (k), and list
    n, orange_individuals, k = calculate_traits(individuals)

    # Calculate the probability based on the frequency of the trait
    probability = calculate_probability(k, n, trait_frequency)

    # Write results to the output file
    write_results(output_file, n, k, probability, orange_individuals)

# Run the script only if it's being executed as the main module
if __name__ == "__main__":
    main()

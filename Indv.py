class Indv():
    blue_count = 0
    orange_count = 0

    def __init__(self, sample_id, date_of_seq, phenotype, nuc_seq):
        self.sample_id = sample_id
        self.date_of_seq = date_of_seq
        self.phenotype = phenotype
        self.nuc_seq = nuc_seq

    def identify_phenotype(self):
        '''Identifies phenotype without updating count'''
        serenine = ['UCU', 'UCC', 'UCA', 'UCG']
        argenine = ['AGA', 'AGG']
        codon = self.nuc_seq[9:12]

        if codon in serenine:
            return 'Blue'
        elif codon in argenine:
            return 'Orange'
        else:
            return 'N'  # Undefined

    def assign_phenotype(self):
        '''Assigns phenotype and updates count'''
        phenotype = self.identify_phenotype()
        self.phenotype = phenotype

        if phenotype == 'Blue':
            Indv.blue_count += 1
        elif phenotype == 'Orange':
            Indv.orange_count += 1

    def get_blue_count(cls):
        return cls.blue_count
    def get_orange_count(cls):
        return cls.orange_count


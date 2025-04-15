#!/usr/bin/env python3

def read_dictionary(dict_file):
    """Read list of population labels to keep."""
    with open(dict_file, 'r') as f:
        return set(line.strip() for line in f if line.strip())

def read_ind_file(ind_file):
    """Read .ind file into a list of (ID, sex, label) tuples."""
    individuals = []
    with open(ind_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                individuals.append((parts[0], parts[1], parts[2]))
    return individuals

def write_filtered_ind(individuals, selected_flags, output_file):
    with open(output_file, 'w') as f:
        for ind, keep in zip(individuals, selected_flags):
            if keep:
                f.write(f"{ind[0]} {ind[1]} {ind[2]}\n")

def filter_geno(geno_file, selected_flags, output_file):
    with open(geno_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            line = line.strip()
            filtered_line = ''.join(base for base, keep in zip(line, selected_flags) if keep)
            fout.write(filtered_line + '\n')

def main():
    # File names
    geno_file = '/home/gog/Documents/Datasets/Hybrids_SpaGuanche.geno'
    ind_file = '/home/gog/Documents/Datasets/Hybrids_SpaGuanche.ind'
    dict_file = '/home/gog/Documents/Datasets/magon-dictionary.dict'
    out_geno = '/home/gog/Documents/Datasets/magon-geno-Filtered.geno'
    out_ind = '/home/gog/Documents/Datasets/magon-ind-Filtered.ind'

    print("Reading dictionary...")
    allowed_labels = read_dictionary(dict_file)

    print("Reading individual metadata...")
    individuals = read_ind_file(ind_file)
    selected_flags = [label in allowed_labels for _, _, label in individuals]

    jind = len(individuals)
    jsel = sum(selected_flags)
    print(f"Individuals scanned: {jind}")
    print(f"Individuals selected: {jsel}")

    print("Writing filtered .ind file...")
    write_filtered_ind(individuals, selected_flags, out_ind)

    print("Filtering .geno file...")
    filter_geno(geno_file, selected_flags, out_geno)

    print("Done!")

if __name__ == '__main__':
    main()

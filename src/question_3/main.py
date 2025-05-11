def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    len1 = len(dna_string1)
    len2 = len(dna_string2)
    for i in range(len1 - len2 + 1):
        if dna_string1[i:i+len2] == dna_string2:
            positions.append(i + 1)  # 1-based index
    return tuple(positions)  # Return as multiple parameters

# Test as described in the requirements
# Should return 2, 4, 10 for the sample input
sample_positions = get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT")
if sample_positions == (2, 4, 10):
    print("Test passed: ", sample_positions)
else:
    print("Test failed: ", sample_positions)

def main():
    while True:
        dna_string1 = input("Enter a DNA string (8-16 characters): ").strip().upper()
        if not (8 <= len(dna_string1) <= 16):
            print("DNA string must be between 8 and 16 characters.")
            continue
        dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").strip().upper()
        if len(dna_string2) != 4:
            print("DNA substring must be exactly 4 characters.")
            continue
        # Both inputs are valid
        positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        if positions:
            print("Positions:", ' '.join(map(str, positions)))
        else:
            print("No occurrences found.")
        cont = input("\nDo you want to try again? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main() 
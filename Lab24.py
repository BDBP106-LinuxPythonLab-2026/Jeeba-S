class DNASequenceError(Exception):
    """Base class for all DNASequence errors."""


class InvalidBaseError(DNASequenceError):
    """Raised when a sequence contains a base other than A, T, G, C."""


class EmptySequenceError(DNASequenceError):
    """Raised when a sequence is empty."""


class InvalidSiteError(DNASequenceError):
    """Raised when the site searched for is empty or invalid."""

class DNASequence:
    COMPLEMENT_MAP = {"A": "T", "T": "A", "G": "C", "C": "G"}

    def __init__(self, seq_id, sequence):
        sequence = sequence.upper().strip()
        if not sequence:
            raise EmptySequenceError(f"Sequence '{seq_id}' is empty")
        bad = set(sequence) - set(self.COMPLEMENT_MAP)
        if bad:
            raise InvalidBaseError(f"Invalid base(s) {sorted(bad)} in '{seq_id}'")
        self.id = seq_id
        self.sequence = sequence
#q1
    def complement(self):
        comp = "".join(self.COMPLEMENT_MAP[b] for b in self.sequence)
        return DNASequence(self.id + "_comp", comp)

#q2
    def reverse_complement(self):
        rc = self.complement().sequence[::-1]
        return DNASequence(self.id + "_revcomp", rc)

#q3
    def transcribe(self):
        return self.sequence.replace("T", "U")

#q4
    def find_site(self, site):
        site = site.upper().strip()
        if not site:
            raise InvalidSiteError("Site to search for cannot be empty")
        bad = set(site) - set(self.COMPLEMENT_MAP)
        if bad:
            raise InvalidSiteError(f"Invalid base(s) {sorted(bad)} in site '{site}'")
        positions = []
        start = self.sequence.find(site)
        while start != -1:
            positions.append(start + 1)          # count from 1
            start = self.sequence.find(site, start + 1)
        return positions                         # [] if none


#test code
if __name__ == "__main__":
    s2 = DNASequence("seq2", "ATGGAATTCTAG")
    print("Original:          ", s2.sequence)
    print("Complement:        ", s2.complement().sequence)
    print("Reverse complement:", s2.reverse_complement().sequence)
    print("mRNA:              ", s2.transcribe())
    print("GAATTC at:", s2.find_site("GAATTC"))
    print("TTT at:", s2.find_site("TTT"))

# Exception
    try:
        DNASequence("bad", "ATGXC")
    except InvalidBaseError as e:
        print("Caught:", e)
    try:
        s2.find_site("")
    except InvalidSiteError as e:
        print("Caught:", e)
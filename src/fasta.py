# -*- coding: utf-8 -*-
import requests as r
from Bio import SeqIO
from io import StringIO


def get_uniprot_seq(uniprot_id):
    '''
    Download UniProt protein sequence and retrun as a SeqRecord object
    '''
    uniprotUrl = "http://www.uniprot.org/uniprot/"
    response = r.post(uniprotUrl+uniprot_id+".fasta")
    # TO DO: check response
    Seq = StringIO(''.join(response.text))
    return list(SeqIO.parse(Seq, 'fasta'))


def sort_fasta_file(ref_fasta, fasta_to_sort):
    '''
    Sort an input fasta in SeqRecord object based on a reference fasta
    :param ref_fasta: a reference list of fasta
    :param fasta_to_sort: a list of fasta to be sorted
    '''
    sorted_fasta = []

    for elem in ref_fasta:

        # fetch the corresponding SeqRecord
        for value in fasta_to_sort:
            if elem.description in value.description:
                sorted_fasta.append(value)
                break
    return sorted_fasta


def filter_fasta_seqs(input_fasta, chars_to_exclude=['N']):
    '''
    Filter input fasta sequences by removing the ones containing specific bases
    or residues
    :param input_fasta: fasta sequences as a list of SeqRecord object
    :param char_to_exclude: a list of individual characters to be excluded
    '''
    chars_in_set = set([x.lower() for x in chars_to_exclude])
    for elem in input_fasta:
        # Check whether sequence contains ANY of the items in set
        if 1 in [c in elem.seq.lower() for c in chars_in_set]:
            input_fasta.remove(elem)
    return input_fasta


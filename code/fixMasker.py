def fixMasker(masker): ##deze fucntion is geschreven door Janse
    """ This function fixes masks from Paint to conform to the same format as the original masks."""
    if len(masker.shape) == 2:
        return masker
    max_value = np.max(masker)
    flat_masker = np.max(masker[...,0:2], axis=2).astype(np.float32)
    flat_masker /= max_value
    
    return flat_masker

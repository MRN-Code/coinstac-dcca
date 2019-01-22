import ujson as json
import numpy as np
import os
import sys
from ancillary import list_recursive


def local_0(args):
    X = np.loadtxt(os.path.join(args['state']['baseDirectory'], 'X.data'), delimiter = ',')
    Y = np.loadtxt(os.path.join(args['state']['baseDirectory'], 'Y.data'), delimiter = ',')
    
    covar = X.dot(Y.T)
    
    output_dict = {"covar": covar, 'computation_phase': 'local_0'}
    cache_dict = {}
    computation_output = {"output": output_dict, "cache": cache_dict}
    return computation_output


if __name__ == '__main__':

    parsed_args = json.loads(sys.stdin.read())
    raise Exception(parsed_args)
    phase_key = list(list_recursive(parsed_args, 'computation_phase'))
    
    if not phase_key:
        computation_output = local_0(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Local")
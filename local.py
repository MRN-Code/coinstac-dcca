import ujson as json
import numpy as np
import os
import sys
from ancillary import list_recursive


def local_0(args):
    X_file_name = args["input"]["file_names"]["X_file"]
    Y_file_name = args["input"]["file_names"]["Y_file"]
    
    X = np.loadtxt(os.path.join(args['state']['baseDirectory'], X_file_name), delimiter = ',')
    Y = np.loadtxt(os.path.join(args['state']['baseDirectory'], Y_file_name), delimiter = ',')

    #TODO: Check for normalized X and Y

    # Assuming X and Y are normalized    
    if X.shape[1] == Y.shape[1]:
        covar = X.dot(Y.T)/X.shape[1]
    
    output_dict = {"covar": covar.tolist(), 'computation_phase': 'local_0'}
    cache_dict = {}
    computation_output = {"output": output_dict, "cache": cache_dict}
    
    return json.dumps(computation_output)


if __name__ == '__main__':

    parsed_args = json.loads(sys.stdin.read())
    phase_key = list(list_recursive(parsed_args, 'computation_phase'))
    
    if not phase_key:
        computation_output = local_0(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Local")
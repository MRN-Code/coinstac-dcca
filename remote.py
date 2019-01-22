import ujson as json
import numpy as np
import sys
from ancillary import list_recursive

def remote_0(args):
    input_list = args["input"]
    myval = sum([np.array(input_list[site]["covar"]) for site in input_list])/len(input_list)
    
    computation_output = {"output": {"cca": myval.tolist()}, "success": True}
    return json.dumps(computation_output)


if __name__ == '__main__':

    parsed_args = json.loads(sys.stdin.read())
    phase_key = list(list_recursive(parsed_args, 'computation_phase'))

    if 'local_0' in phase_key:
        computation_output = remote_0(parsed_args)
        sys.stdout.write(computation_output)
    else:
        raise ValueError("Error occurred at Remote")
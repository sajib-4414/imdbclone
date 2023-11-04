import grpc
import re

def grpc_error_parser(rpc_error:grpc.RpcError):
    total_exceptions = []
    # sample string
    # Exception calling application: {'non_field_errors': [ErrorDetail(string='Invalid username or password', code='invalid')]}
    if rpc_error.details():
        details_string = rpc_error.details()
        # Define a regex pattern to match the ErrorDetail strings
        pattern = r"ErrorDetail\(string='(.*?)', code='(.*?)'\)"

        # Find all matches in the details_string
        matches = re.findall(pattern, details_string)

        # Extract strings and codes from the matches
        formatted_error_details = [{'error_code': match[1], 'error_details': match[0]} for match in matches]

        # Now error_details will contain a list of tuples with (string, code)
        # print(formatted_error_details)
        return formatted_error_details
    return [{'error_code': 'UNKNOWN_SERVER_ERROR', 'error_details': "Internal Server Error"}]
def parseError(serializer_errors):               
    response_dict = {
                "errors":[]
    }
    for error_name, error_message_list in serializer_errors.items():
        response_dict['errors'].append(
            {
                    "error_code":error_name,
                    "error_details":",".join(error_message_list)
            })
    return response_dict
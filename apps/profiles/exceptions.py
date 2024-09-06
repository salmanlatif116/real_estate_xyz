from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "Requested Profile not found"


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "This Profile is not belong to you. You cannot edit this profile" 
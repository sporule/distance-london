from app.helpers.utility import res


class Messages:
    AUTHENTICATION_FAILED = 'Authentication failed, please try again'
    AUTHORISATION_FAILED = 'You do not have the required permission'
    NOT_ENOUGH_INFO = 'Information you provided is not accurate'
    NOT_EXIST = 'Record not found'
    OBJECT_EXIST = 'Object exists'
    SUCCESS = 'Operation Success'
    OPERATION_FAILED = 'Operation Failed'
    INVALID_VOUCHER = 'Invalid voucher'
    NO_VOUCHERS_EXCEEDED = 'Number of vouchers exceeded'
    VOUCHER_NAME_EMPTY = 'Voucher name cannot be empty'
    VOUCHER_EXISTS = 'Voucher name already in use'
    NEEDED_FIELD_EMPTY = 'One or more needed values empty'
    NO_STOCK = 'One or more Products Unavailable'
    EMAIL_EXIST = 'Email already in use'
    EMAIL_EMPTY = 'Email can not be empty'
    TOKEN_EXPIRED = 'Token has expired'
    UNCONFIRMED_USER = 'Unconfirmed User'
    VOUCHER_DETAILS_WRONG = 'Voucher cannot have both percent off and fixed amount'


class Roles:
    MEMBER = 'member'
    ADMIN = 'admin'


class Responses:
    @staticmethod
    def NOT_EXIST():
        return res('', Messages.NOT_EXIST, 404)

    @staticmethod
    def SUCCESS():
        return res(Messages.SUCCESS)

    @staticmethod
    def OBJECT_EXIST(err=Messages.OBJECT_EXIST):
        return res('', err, 409)

    @staticmethod
    def OPERATION_FAILED(err=Messages.OPERATION_FAILED):
        return res('', err, 400)

    @staticmethod
    def AUTHENTICATION_FAILED():
       return res('', Messages.AUTHENTICATION_FAILED, 401)
    
    @staticmethod
    def AUTHORISATION_FAILED():
        return res('', Messages.AUTHORISATION_FAILED, 403)

    @staticmethod
    def INVALID_VOUCHER():
        return res('', Messages.INVALID_VOUCHER, 400)

    @staticmethod
    def NO_VOUCHERS_EXCEEDED():
        return res('', Messages.NO_VOUCHERS_EXCEEDED, 400)

    @staticmethod
    def VOUCHER_NAME_EMPTY():
        return res('', Messages.VOUCHER_NAME_EMPTY, 400)
    
    @staticmethod
    def VOUCHER_DETAILS_WRONG():
        return res('', Messages.VOUCHER_DETAILS_WRONG, 400)

    @staticmethod
    def NEEDED_FIELD_EMPTY():
        return res('', Messages.NEEDED_FIELD_EMPTY, 400)

    @staticmethod
    def VOUCHER_EXISTS():
        return res('', Messages.VOUCHER_EXISTS, 400)

    @staticmethod
    def NO_STOCK():
        return res('', Messages.NO_STOCK, 400)   

    @staticmethod
    def TOKEN_EXPIRED():
        return res('', Messages.TOKEN_EXPIRED, 400)   

    @staticmethod
    def UNCONFIRMED_USER():
        return res('', Messages.UNCONFIRMED_USER, 400)     

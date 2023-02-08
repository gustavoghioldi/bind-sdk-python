from enum import Enum, unique


@unique
class Status(str, Enum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    UNKNOWN = "UNKNOWN"
    FAILED = "FAILED"
    UNKNOWN_FOREVER = "UNKNOWN_FOREVER"
    AWAITING_CONFIRMATION = "AWAITING_CONFIRMATION"
    CANCELED = "CANCELED"
    EXPIRED = "EXPIRED"
    REFUNDED = "REFUNDED"
    REJECTED_CLIENT = "REJECTED_CLIENT"
    REJECTED = "REJECTED"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
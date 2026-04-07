from enum import Enum


class LanguageEnum(str, Enum):
    FR = "FR"
    EN = "EN"
    ES = "ES"
    DE = "DE"
    IT = "IT"
    PT = "PT"
    ZH = "ZH"
    JA = "JA"
    AR = "AR"


class ToneEnum(str, Enum):
    CASUAL = "CASUAL"
    STANDARD = "STANDARD"
    FORMAL = "FORMAL"


class MessageStatusEnum(str, Enum):
    SENDING = "sending"
    SENT = "sent"
    READ = "read"


class TranslationStatusEnum(str, Enum):
    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"

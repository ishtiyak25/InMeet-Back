class GenderType:
    M = 'M'
    F = 'F'

    CHOICES = (
        (M, "Male"),
        (F, "Female")
    )


class UserType:
    Owner = 1
    Invited = 2
    CHOICES = (
        (Owner, "Owner"),
        (Invited, "Invited")
    )


class InvitedByStatus:
    Pending = 1
    Accepted = 1
    Rejected = 1
    CHOICES = (
        (Pending, "Pending"),
        (Accepted, "Accepted"),
        (Rejected, "Rejected"),
    )

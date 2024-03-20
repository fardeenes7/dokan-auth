from enum import Enum

class Role(Enum):
    USER = "user"
    MERCHANT = "merchant"
    ADMIN = "admin"
    DEVELOPER = "developer"
    MARKETING = "marketing"
    SUPPORT = "support"
    

class User:
    def __init__(self, id: str, provider: str, social_id: str, roles: list[str]):
        self.id: str = id
        self.provider: str = provider
        self.social_id: str = social_id
        self.roles: list[str] = roles  # Store roles as strings

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """
        Creates a User object from a dictionary (e.g., Firestore document data).

        Args:
            data: A dictionary containing user data fields.

        Returns:
            A User object representing the user.
        """
        return cls(
            data.get("id"),
            data.get("provider"),
            data.get("social_id"),
            data.get("roles", []),  # Handle missing roles field
        )
import pytest


def test_user_str(base_user):
    """Test the custom user model string representation"""
    assert base_user.__str__() == f"{base_user.username}"


def test_user_short_name(base_user):
    """Test that the user models get_short_name method works """ 
    short_name = f"{base_user.username}"
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    """Test that the user models get_full_name method works """ 
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name() == full_name

def test_base_user_email_is_normalized(base_user):
    """Test that the new user email is normalized"""
    email = "ADMIN@gmail.com"
    assert base_user.email == email.lower()

def test_super_user_email_is_normalized(super_user):
    """Test that the superuser email is normalized"""
    email = "admin@gmail.com"
    assert super_user.email == email.lower()

def test_super_user_is_not_staff(user_factory):
    """Test that an error is raised when an admin user has is_staff set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "superuser must have is_staff=True"
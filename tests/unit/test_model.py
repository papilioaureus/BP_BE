from iebank_api.models import Account
import pytest


def test_account_model():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account("John Doe", "Spain", "€")
    assert account.name == "John Doe"
    assert account.country == "Spain"
    assert account.currency == "€"
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == "Active"
    

#new unit test 
def test_account_deactivated():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check if an account can be deactivated with __deactivate__
    """
    account = Account("John Doe", "Spain", "€")
    assert account.__deactivate__() == "Inactive" 
    

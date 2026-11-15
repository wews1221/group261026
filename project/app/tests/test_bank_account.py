# from models.bank_models import BankAccount
#
#
# class TestBankAccount:
#     def test_create_account(self):
#         account = BankAccount('ara')
#         assert account.money == 0
#         assert account.owner == 'Ara'
#         assert account.id
#         assert not account.transactions
#
#     def test_create_account_2(self):
#         account = BankAccount('ara2')
#         assert account.money == 0
#         assert account.owner == 'Ara2'
#         assert account.id
#         assert not account.transactions
#
# class TestDepositMoney:
#     def test_deposit_positive_summa(self):
#         account = BankAccount('ara')
#         account.deposit_money(200)
#         account.deposit_money(300)
#         assert account.money == 500
#         assert len(account.transactions) == 2
#         print(account.__dict__)
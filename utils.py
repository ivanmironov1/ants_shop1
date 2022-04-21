from aiogram.utils.helper import Helper, HelperMode, ListItem


class TestStates(Helper):
    mode = HelperMode.snake_case

    PAY_STATE = ListItem()
    ADMIN_STATE = ListItem()


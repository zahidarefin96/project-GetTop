from behave import when, then


@when("Click the user icon and verify LOGIN  is shown")
def click_user_icon(context):
    context.app.main_page.click_icon()


def verify_login_page(context):
    context.sign_in_page.verify_login_text()


@when("Click Lost your password link")
def click_link(context):
    context.app.sign_in_page.click_lost_password_link()


@when("User can able to put the email")
def enter_email(context):
    context.app.my_account_page.input_email()


@then("Click RESET PASSWORD button")
def click_reset_password(context):
    context.app.my_account_page.click_button()

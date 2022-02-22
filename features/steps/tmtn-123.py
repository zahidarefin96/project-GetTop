from behave import when, then


@when("Click search icon")
def click_search_icon(context):
    context.app.main_page.search_icon()


@when("Input product in the search field")
def input_search_field(context):
    context.app.main_page.input_box()


@then("Verify expected product is shown")
def verify_product(context):
    context.app.product_page.iphone11_text()

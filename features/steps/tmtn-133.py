from behave import given, when, then


@given("Go to GetTop page")
def open_link(context):
    context.app.home_page.open_page()


@when("Scroll down to “LATEST PRODUCTS ON SALE” and hover over a product")
def scroll_down(context):
    pass


@when("Click on “QUICK VIEW” tab that comes up when hovering over product")
def click_quick_view(context):
    pass


@when("Click on “Add to cart” to add product to cart")
def click_add_to_cart(context):
    pass


@then("View that product is added to cart (Message will say product is in cart)")
def view_product(context):
    pass

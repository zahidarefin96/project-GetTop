from behave import given, when, then


@given("Open GetTop page")
def open_link(context):
    context.app.main_page.open_page()


@when("Scroll down to “LATEST PRODUCTS ON SALE” and hover over a product")
def scroll_down(context):
    context.app.main_page.hover_lang()


@when("Click on “QUICK VIEW” tab that comes up when hovering over product")
def click_quick_view(context):
    context.app.main_page.click_quick_view()


@when("Click on “Add to cart” to add product to cart")
def click_add_to_cart(context):
    context.app.main_page.click_cart_icon()


@then("View that product is added to cart (Message will say product is in cart)")
def view_product(context):
    context.app.cart.verify_iphone_se_text()

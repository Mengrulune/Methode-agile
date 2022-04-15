from behave import *
import country
@given("un pays France")
def step_impl(context):
    context.country = country.Country("France")
    assert context.country is not None

@when ("je set une population et une surface")
def step_impl(context):
    context.country.set_population_and_surface(67390000, 543904)
    context.result = 67390000/543904

@then(" j obtiens la densité")
def step_impl(context):
    assert context.result == context.country.calculate_density()

@given("je set une population et une surfcace")
def step_impl(context):
    context.country = country.country()
    assert context.country is not None

@then ("la densité est affichée densité")
def step_impl(context, response):
    assert context.result == response





from behave import given, when, then


@given(u'User exist')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User exist')


@when(u'I go to login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I go to login page')


@when(u'Fill login form')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Fill login form')


@when(u'Click submit button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click submit button')


@then(u'I am logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am logged in')
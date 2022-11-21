*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  m
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  mikkoo
    Set Password  mikko
    Set Password Confirmation  mikko
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  mikkooo
    Set Password  mikko123
    Set Password Confirmation  mikko321
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  mikkoa
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Credentials
    Go To Login Page
    Set Username  mikkoa
    Set Password  mikko123
    Try To Login
    Login Should Succeed

Login After Failed Registration
    Set Username  mi
    Set Password  pp
    Set Password Confirmation  mm
    Submit Credentials
    Go To Login Page
    Set Username  mi
    Set Password  pp
    Try To Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Submit Credentials
    Click Button  Register

Try To Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

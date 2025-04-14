*** Settings ***
Library    BankLibrary.py

*** Test Cases ***
Test Register New Client
    [Documentation]    Проверка регистрации нового клиента.
    ${result}=    New Client    0001    Alena
    Should Be Equal As Strings    ${result}    Клиент с id 0001 успешно зарегистрирован.
    ${client_name}=    Get Client Name    0001
    Should Be Equal As Strings    ${client_name}    Alena


Test Register Existing Client
    [Documentation]    Проверка попытки регистрации клиента с существующим id.
    ${result1}=    New Client    0002    Alena
    ${result2}=    New Client    0002    Anton
    ${client_name}=    Get Client Name    0002
    Should Be Equal As Strings    ${client_name}    Alena
    Should Be Equal As Strings     ${result2}    Клиент с id 0002 уже зарегистрирован.


Test Open Deposit for Existing Client
    [Documentation]    Открытие депозита для зарегистрированного клиента.
    ${client_id}=    Set Variable    0003
    ${client_name}=    Set Variable    Alena
    ${start_balance}=    Set Variable    1000.00
    ${years}=    Set Variable    2
    ${result1}=    New Client    ${client_id}    ${client_name}
    ${result2}=    Open Deposit Accaunt    ${client_id}    ${start_balance}    ${years}
    Should Be Equal As Strings   ${result2}   Депозит клиента 0003 сумма 1000.00 срок 2 успешно открыт.


Test Open Deposit for not Existing Client
    [Documentation]    Открытие депозита для не зарегистрированного клиента.
    ${result2}=    Open Deposit Accaunt    0004    2000    2
    Should Be Equal As Strings    ${result2}    Клиент с id 0004 не зарегистрирован.


Test Close Deposit for Existing Client
    [Documentation]    Закрытие депозита для зарегистрированного клиента.
    ${client_id}=    Set Variable    0003
    ${client_name}=    Set Variable    Alena
    ${start_balance}=    Set Variable    1000.00
    ${years}=    Set Variable    2
    ${result1}=    New Client    0005    Alena
    ${result2}=    Open Deposit Accaunt    0005    2000    2
    ${result3}=    Close Deposit    0005
    Should Be Equal As Strings    ${result3}    Депозит клиента Alena 0005 успешно закрыт.


Test Close Not Opened Deposit for Existing Client
    [Documentation]    закрытие не открытого депозита для зарегистрированного клиента.
    ${client_id}=    Set Variable    0006
    ${client_name}=    Set Variable    Alena
    ${start_balance}=    Set Variable    1000.00
    ${years}=    Set Variable    2
    ${result1}=    New Client    ${client_id}    ${client_name}
    ${result2}=    Close Deposit    ${client_id}
    Should Be Equal As Strings    ${result2}    У клиента 0006 отсутствуют открытые депозиты.


Test Close Not Opened Deposit for Not Existing Client
    [Documentation]    закрытие не открытого депозита для НЕ зарегистрированного клиента.
    ${result1}=    Close Deposit    0007
    Should Be Equal As Strings    ${result1}    У клиента 0007 отсутствуют открытые депозиты.


 Test Calculate Deposit for Existing Client
    [Documentation]    профит депозита для зарегистрированного клиента с открытым вкладом.
    ${client_id}=    Set Variable    0008
    ${client_name}=    Set Variable    Alena
    ${start_balance}=    Set Variable    1000.00
    ${years}=    Set Variable    1
    ${result1}=    New Client    0008    Alena
    ${result2}=    Open Deposit Accaunt    0008    1000   1
    ${result3}=    Calculate Deposit    0008
    Should Be Equal    ${result3}    ${1104.71}


Test Calculate Not Opened Deposit for Existing Client
    [Documentation]    профит депозита для зарегистрированного клиента БЕЗ открытого вклада.
    ${client_id}=    Set Variable    0009
    ${client_name}=    Set Variable    Alena
    ${start_balance}=    Set Variable    1000.00
    ${years}=    Set Variable    1
    ${result1}=    New Client    ${client_id}    ${client_name}
    ${result2}=    Calculate Deposit    ${client_id}
    Should Be Equal As Strings    ${result2}    У клиента 0009 отсутствуют открытые депозиты.


 Test Calculate Not Opened Deposit for Not Existing Client
    [Documentation]    профит депозита для НЕ зарегистрированного клиента БЕЗ открытого вклада.
    ${client_id}=    Set Variable    0010
    ${result1}=    Calculate Deposit    ${client_id}
    Should Be Equal As Strings    ${result1}    Клиент с id 0010 не зарегистрирован.

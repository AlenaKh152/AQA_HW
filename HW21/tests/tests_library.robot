*** Settings ***
Library    LibLibrary.py


*** Test Cases ***
Test1 Positive Reserve Book
    [Documentation]    Резерв книги, которая не зарезервирована и не на руках
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader}=    Add Reader    Vasya
    ${result}=    Reserve Book    Vasya    ${book}
    Should Be Equal As Strings    ${result}    Success reserve. First Book has been reserved by Vasya.


Test2 Positive Reserve Book
    [Documentation]    Резерв книги, которая не зарезервирована, но находится на руках
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${reader2}=    Add Reader    Petya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Get Book    Vasya    ${book}
    ${result3}=    Reserve Book    Petya    ${book}
    Should Be Equal As Strings    ${result3}    Success reserve. First Book has been reserved by Petya.


Test3 Positive Reserve Book
    [Documentation]    Резерв нескольких книг одним пользователем
    ${book1}=    Add Book    First Book    Tom    400    0006754023
    ${book2}=    Add Book    Second Book    Jerry    500    00022222
    ${reader1}=    Add Reader    Vasya
    ${result1}=    Reserve Book    Vasya    ${book1}
    ${result2}=    Reserve Book    Vasya    ${book2}
    Should Be Equal As Strings    ${result2}    Success reserve. Second Book has been reserved by Vasya.


Test Negative Reserve Book
    [Documentation]    резерв книги, которая уже зарезервирована
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${reader2}=    Add Reader    Petya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Reserve Book    Petya    ${book}
    Should Be Equal As Strings    ${result2}    Reserve error. First Book is already reserved/received.


Test Positive Cancel Reserved Book
    [Documentation]    Отмена резерва пользователем, который сделал резерв книги
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Cancel Reserve    Vasya    ${book}
    Should Be Equal As Strings    ${result2}    Success cancel. Book reservation was cancelled by Vasya.


Test1 Negative Cancel Reserved Book
    [Documentation]    Отмена резерва книги, когда резерв сделал другой пользователь
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${reader2}=    Add Reader    Petya
    ${result1}=    Cancel Reserve    Petya    ${book}
    Should Be Equal As Strings    ${result1}    Cancel error. No active reservation for First Book.


Test2 Negative Cancel Reserved Book
    [Documentation]    Отмена резерва книги, когда для книги нет активного резерва
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${result1}=    Cancel Reserve    Vasya    ${book}
    Should Be Equal As Strings    ${result1}    Cancel error. No active reservation for First Book.


Test Positive Get Reserved Book
    [Documentation]    Получение зарезервированной книги
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Get Book    Vasya    ${book}
    Should Be Equal As Strings    ${result2}    Success receive. First Book was successfully received by Vasya!


Test1 Negative Get Reserved Book
    [Documentation]    Получение зарезервированной книги, когда книга ещё у другого пользователя
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${reader2}=    Add Reader    Petya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Get Book    Vasya    ${book}
    ${result3}=    Reserve Book    Petya    ${book}
    ${result4}=    Get Book    Petya    ${book}
    Should Be Equal As Strings    ${result4}    Receive error. First Book is not reserved or is still used!


Test2 Negative Get Reserved Book
    [Documentation]    Получение книги, зарезервированной другим пользователем
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${reader2}=    Add Reader    Petya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Get Book    Petya    ${book}
    Should Be Equal As Strings    ${result2}    Receive error. First Book is not reserved or is still used!


Test Positive Return Got Book
    [Documentation]    Возврат полученной книги
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Get Book    Vasya    ${book}
    ${result3}=    Return Book    Vasya    ${book}
    Should Be Equal As Strings    ${result3}    Success return. First Book was returned by Vasya.


Test1 Negative Return Got Book
    [Documentation]    Возврат книги, полученной другим пользователем
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${reader2}=    Add Reader    Petya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Get Book    Vasya    ${book}
    ${result3}=    Return Book    Petya    ${book}
    Should Be Equal As Strings    ${result3}    Return error. First Book was not received by Petya.


Test2 Negative Return Got Book
    [Documentation]    Возврат книги, предварительно не полученной пользователем
    ${book}=    Add Book    First Book    Tom    400    0006754023
    ${reader1}=    Add Reader    Vasya
    ${result1}=    Reserve Book    Vasya    ${book}
    ${result2}=    Return Book    Vasya    ${book}
    Should Be Equal As Strings    ${result2}    Return error. First Book was not received by Vasya.

from selene import browser, by, command, have
import os.path


def test_registration_demo_qa():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ruslan')
    browser.element('#lastName').type('Matygullin')
    browser.element('#userEmail').type('ruslan@mail.ru')
    browser.element('.custom-control').click()
    browser.element('#userNumber').type(9770001010)
    browser.element('#dateOfBirthInput').click()
    # browser.element('.react-datepicker__year-select').click().element(by.text('1992')).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('February')).click()
    browser.element('.react-datepicker__day--021').click()
    browser.element('#subjectsInput').type('Biology').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(r'../../qa_guru_python_9_10/tests/rus.jpg'))
    browser.element('#currentAddress').type('Ulyanovsk')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').perform(command.js.click)

    browser.element('.table').all('td').even.should(have.exact_texts(
        'Ruslan Matygullin',
        'ruslan@mail.ru',
        'Male',
        '9770001010',
        '21 February,1992',
        'Biology',
        'Sports',
        'rus.jpg',
        'Ulyanovsk',
        'NCR Gurgaon',

    )
    )

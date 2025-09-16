import os.path

from selene import browser, have, be
test

def test_demoqa(browser_managment):
    browser.open('/')
    browser.element('[id="firstName"]').type('Denis')
    #Поиск инпута и ввод Имени
    browser.element('#lastName').type('Manto')
    #Поиск инпута и ввод Фамилии
    browser.element('[id="userEmail"]').type('Manto1993@gmail.com')
    # Поиск инпута и ввод Почты
    browser.all('[name=gender]').element_by(have.value('Male')).element('./following-sibling::label').click()
    #Поиск селекторов radiobutton и нажатие на один из трех
    browser.element('#userNumber').type('9653225562')
    # Поиск инпута и ввод номера телефона
    browser.element('#dateOfBirthInput').click()
    # Поиск поля даты рждения по нажатию на который появляется календарь
    browser.element('.react-datepicker__month-select').click()
    #Нажатие на селектор выбора месяца,появляется выпадающий список
    browser.element('.react-datepicker__month-select').should(be.visible).element('[value="11"]').click()
    #Выбор 11 элемента (декабрь) и нажатие по нему
    browser.element('.react-datepicker__year-select').click()
    # Нажатие на селектор выбора года,появляется выпадающий список
    browser.element('option[value="1993"]').click()
    # Выбор  элемента  и нажатие по нему
    browser.element('.react-datepicker__day--012').click()
    #Нажати на день в месяце на календаре
    browser.element('#dateOfBirthInput').should(be.visible).element('[value"12 Dec 1993"]')
    #Проверка что в поле ввода данные после выбора отображаются верно
    browser.element('#subjectsInput').type('English').press_enter()
    #Ввод текста и нажатие на кнопку enter
    browser.element('[for = hobbies-checkbox-1]').click()
    #Выбор чек-бокса номер 1 с хобби
    #browser.element('#uploadPicture').send_keys(os.path.abspath('demoqa'))
    #Текст постоянно падает на добавлении фото в анкету (пока что не смог разобратся)
    browser.element('#currentAddress').type('St. Petersburg, Lomanosovskaya street')
    #Нажатие на поле ввода и заполнение данными адреса
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    #Нажатие на селектор и ввод данных из выпадающего списка
    browser.element('#react-select-4-input').type('Lucknow').press_enter()
    # Нажатие на селектор и ввод данных из выпадающего списка
    browser.element('#submit').click()
    #Нажатие на кнопку. Отправка анкеты.

    browser.element('.table').all('td').even.should #Проверка данных отправленной анкеты.
    (have.exact_texts(
        'Student Name', 'Denis Manto',
            'Student Email', 'Manto1993@gmail.com',
            'Gender', 'Male',
            'Mobile', '9653225562',
            'Date of Birth', '12 December,1993',
            'Subjects', 'English',
            'Hobbies', 'Sports',
            'Address', 'St. Petersburg, Lomanosovskaya street',
            'State and City', 'Uttar Pradesh Lucknow'
        )
    )


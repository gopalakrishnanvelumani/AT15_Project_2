class TestData:
    username = "Admin"
    password = "admin123"


class TestSelectors:
    input_box_username = "username"
    # username_xpath = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    forgot_password = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    reset_username = "//input[@placeholder='Username']"
    reset_button = "//button[normalize-space()='Reset Password']"
    input_box_password = "password"
    login_xpath = "//button[@type='submit']"
    admin_path = "//span[normalize-space()='Admin']"
    admin_list_path = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li"
    menu_path = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a"

class list:
    admin_list = ['User Management', 'Job', 'Organization', 'Qualifications', 'Nationalities', 'Corporate Branding', 'Configuration']
    menu_list = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory',
                     'Maintenance', 'Buzz']



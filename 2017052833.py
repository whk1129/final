class Main:
    # 연락처에 기재되는 항목들을 구분
    def __init__(self, name, phone, mail, address):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.address = address

    # 출력되어 나오는 형식을 지정
    def print_category(self):
        print("이름 : ", self.name)
        print("핸드폰 번호 : ", self.phone)
        print("E-mail : ", self.mail)
        print("주소 : ", self.address)


# 프로그램에 연락처를 생성할 수 있도록 객체를 생성하고 반환되도록
def input_data():
    name = input("이름 : ")
    phone = input("핸드폰 번호 : ")
    mail = input("E-mail : ")
    address = input("주소 : ")
    data = Main(name, phone, mail, address)
    return data


# 프로그램에 입력 된 연락처를 볼 수 있도록
def print_data(data_list):
    for data in data_list:
        data.print_category()


# 프로그램에 입력 된 이름으로 연락처를 삭제할 수 있도록
def delete_data(data_list, name):
    for i, data in enumerate(data_list):
        if data.name == name:
            del data_list[i]


# 주소록 프로그램의 메뉴 설정 및 출력
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 프로그램 종료")
    menu = input("메뉴선택 : ")
    return int(menu)


# 프로그램에 입력 된 연락처를 파일로 저장
def save_data(data_list):
    f = open("phone_number_data.txt", "wt")
    for data in data_list:
        f.write(data.name + '\n')
        f.write(data.phone + '\n')
        f.write(data.mail + '\n')
        f.write(data.address + '\n')
    f.close()


# 파일로 저장 된 연락처를 프로그램에 불러오기
def read_data(data_list):
    f = open("phone_number_data.txt", "rt")
    lines = f.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        mail = lines[4*i+2].rstrip('\n')
        address = lines[4*i+3].rstrip('\n')
        data = Main(name, phone, mail, address)
        data_list.append(data)
    f.close()


# 메뉴 실행 등 프로그램 구현
def run():
    data_list = []
    read_data(data_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            data = input_data()
            data_list.append(data)
        elif menu == 2:
            print_data(data_list)
        elif menu == 3:
            name = input("Name : ")
            delete_data(data_list, name)
        elif menu == 4:
            save_data(data_list)
            break


if __name__ == "__main__":
    run()

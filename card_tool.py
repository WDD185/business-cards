import os


class CardsTool:

    def __init__(self):
        self.card_list = []

    @staticmethod
    def menu():
        print('')
        print('开始读取数据......')
        print('*' * 50)
        print('欢迎使用名片管理系统')
        print('1.新建名片')
        print('2.显示全部')
        print('3.查询名片')
        print('0.退出系统')
        print('*' * 50)

    def input_info(self, value_dict, msg):
        info = input(msg)
        if len(info) > 0:
            if info == '退出':
                return
            else:
                return info
        else:
            return value_dict

    def creat_card(self):
        name = input('输入用户名字：')
        phone = input('输入用户电话：')
        qq_num = input('输入用户QQ号码：')
        qq_mail = input('输入用户qq邮箱：')
        new_dict = {
            'name': name,
            'phone': phone,
            'qq_num': qq_num,
            'qq_mail': qq_mail
        }
        self.card_list.append(new_dict)
        print('新建名片成功，姓名%s' % name)
        print(self.card_list)

    def show_all(self):
        if len(self.card_list) <= 0:
            print('当前系统没有名片')
            return
        else:
            print(self.card_list)
            print(type(self.card_list))
            print('-' * 100)
            print('姓名'.ljust(20), '电话'.ljust(20), 'QQ'.ljust(20), 'QQ邮箱'.ljust(20), sep='\t\t')
            print('-' * 100)
            for i in self.card_list:
                print(i.get('name').ljust(20), i.get('phone').ljust(20),
                      i.get('qq_num').ljust(20), i.get('qq_mail').ljust(20), sep='\t\t')

    def search_card(self):
        name = input('请输入要查询的姓名：')
        if self.card_list:
            for i in self.card_list:
                if i.get('name') == name:
                    print('已经查询到信息：')
                    print('-' * 100)
                    print('姓名'.ljust(20), '电话'.ljust(20), 'QQ'.ljust(20), 'QQ邮箱'.ljust(20), sep='\t\t')
                    print('-' * 100)
                    print(i.get('name').ljust(20), i.get('phone').ljust(20),
                          i.get('qq_num').ljust(20), i.get('qq_mail').ljust(20), sep='\t\t')
                    self.deal_card(i)
                    return
                else:
                    print('未找到相关信息')
                    return
        else:
            print('列表没有数据')

    def deal_card(self, find_dict):
        op = input('请输入对该名片的操作，1：修改，2：删除，3：返回上一级 ：')
        if op in ['1', '2', '3']:
            if op == '1':
                print('开始修改信息')
                find_dict['name'] = self.input_info(find_dict.get('name'), '请输入修改的名字[直接回车不修改]：')
                find_dict['phone'] = self.input_info(find_dict.get('phone'), '请输入修改的电话[直接回车不修改]：')
                find_dict['qq_num'] = self.input_info(find_dict.get('qq_num'), '请输入修改的qq[直接回车不修改]：')
                find_dict['qq_mail'] = self.input_info(find_dict.get('qq_mail'), '请输入修改的qq邮箱[直接回车不修改]：')
                print('修改成功')
                print('姓名'.ljust(20), '电话'.ljust(20), 'QQ'.ljust(20), 'QQ邮箱'.ljust(20), sep='\t\t')
                print('-' * 100)
                print(find_dict.get('name').ljust(20), find_dict.get('phone').ljust(20),
                      find_dict.get('qq_num').ljust(20), find_dict.get('qq_mail').ljust(20), sep='\t\t')
            elif op == '2':
                self.card_list.remove(find_dict)
                print(self.card_list)
                print('删除该名片信息成功!')
            else:
                print('返回上一级')
        else:
            print('输入有误，请重新输入')

    def save_card_to_file(self):
        file = open('card.txt', 'w', encoding='utf-8')
        file.write(str(self.card_list))
        file.close()

    def load_card(self):
        if os.path.exists('card.txt'):
            file = open('card.txt', 'r', encoding='utf-8')
            text = file.read()
            if len(text) == 0:
                print('当前文件，内容为空！')
                file.close()
                return
            self.card_list = eval(text)
            file.close()
        else:
            print('文件不存在，请新建')

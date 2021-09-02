from card_tool import CardsTool


class CardMain:
    def __init__(self):
        self.op1 = CardsTool()
        self.op1.load_card()

    def run(self):

        while True:

            self.op1.menu()
            op = input('请输入您的选择:')
            # print(type(op))
            if op in ['1', '2', '3']:
                if op == '1':
                    print('新建名片')
                    self.op1.creat_card()
                elif op == '2':
                    print('显示全部名片')
                    self.op1.show_all()
                else:
                    print('查询名片')
                    self.op1.search_card()
            elif op == '0':
                print('退出系统')
                self.op1.save_card_to_file()
                break
            else:
                print('您的输入有误，请重新输入')


if __name__ == '__main__':
    CardMain().run()

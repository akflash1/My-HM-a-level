class Phone:
    def __init__(self):
        self.number = ''
        self._incoming_calls = 0

    def set_number(self, number):
        self.number = number

    def _get_call(self):
        return self._incoming_calls

    def get_receive(self):
        self._incoming_calls += 1

    def get_total_calls(self):
        return self._incoming_calls

    def save_calls_to_file(self, file_name):
        with open(file_name, 'w') as file:
            file.write("Total calls received: " + str(self._incoming_calls))

phone1 = Phone()
phone1.set_number('0662952936')
phone1.get_receive()

phone2 = Phone()
phone2.set_number('0953526875')
phone2.get_receive()
phone2.get_receive()

phone3 = Phone()
phone3.set_number('0987419652')
phone3.get_receive()
phone3.get_receive()
phone3.get_receive()

for phone in [phone1, phone2, phone3]:
    phone.save_calls_to_file('calls_info.txt')

print("Total calls received:", phone1.get_total_calls())

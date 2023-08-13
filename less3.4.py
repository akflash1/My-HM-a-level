banknotes = [1000, 500, 200, 100, 50, 20, 10]
banknotes.sort()


def bankomatik(amount):
    # amount 27560
    result = []
    error_message = False

    for id, note in enumerate(banknotes[:-1]):
        quantity = 10

        if amount - quantity * note < 0:
            quantity = amount // note

        test_amount = amount - quantity * note  # 27460

        while test_amount % banknotes[id + 1]:
            quantity -= 1
            test_amount = amount - quantity * note
            if not quantity:
                error_message = "Quantity became zero"
                break

        if error_message:
            break

        result.append(f"{quantity:2} notes with wage {note:4}")
        amount = test_amount

        if not amount:
            break

    note = banknotes[-1]
    if amount > 0 and not amount % note:
        result.append(f"{amount // note:2} notes with wage {note:4}")

    return '\n'.join(result)


request = int(input("Please enter the amount of money you'd like to widthraw: "))

print(bankomatik(request))
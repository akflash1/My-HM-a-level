
def all_sizes():
    country_sizes = {
        'Ukraine': {'XXS': 42, 'XS': 44, 'S': 46, 'M': 48, 'L': 50, 'XL': 52, 'XXL': 54, 'XXXL': 56},
        'Germany': {'XXS': 36, 'XS': 38, 'S': 40, 'M': 42, 'L': 44, 'XL': 46, 'XXL': 48, 'XXXL': 50},
        'France': {'XXS': 38, 'XS': 40, 'S': 42, 'M': 44, 'L': 46, 'XL': 48, 'XXL': 50, 'XXXL': 52},
        'UK': {'XXS': 24, 'XS': 26, 'S': 28, 'M': 30, 'L': 32, 'XL': 34, 'XXL': 36, 'XXXL': 38},
        'USA': {'XXS': 8, 'XS': 10, 'S': 12, 'M': 14, 'L': 16, 'XL': 18, 'XXL': 20, 'XXXL': 22}
    }
    return country_sizes

country_sizes = all_sizes()
a = input('Enter country: ').strip("'")
b = input('Enter size: ').strip("'")
print(country_sizes[a][b])



company = 'indomascot'

print(company.capitalize())

company = company.upper()

print(company)

print(company.lower())

alamat = 'jalan kuda lumping no 3   kudajaya   '
kota = 'padalarang'
alamatLengkap = ' '.join([alamat, kota])
alamatLengkap1 = ' '.join([alamat.rstrip(), kota])

print(alamatLengkap)
print(alamatLengkap1)

print(alamatLengkap.startswith("jalan"))

lorem = '''Generate Lorem Ipsum placeholder text. 
Select the number of characters, words, sentences or paragraphs, 
and hit generate'''

splitBySpace = lorem.split()

print(splitBySpace)

splitByNewLine = lorem.split('\n')

print(splitByNewLine)
print(splitByNewLine[0])

print(lorem.replace('Lorem', 'kuda'))

print(splitByNewLine[2].isalpha())
print(company.isalpha())

print(r'kuda kepang \"wkwkwk')

if 'Lorem' in lorem:
    print('Lorem ada nih')

print(splitBySpace.sort())
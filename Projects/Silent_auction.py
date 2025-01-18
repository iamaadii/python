print(''' !!!!!!!! WELCOME TO SILENT AUCTION !!!!!!!! ''')

flag='yes'
d={}
while(flag=='yes'):
    name = input('Enter ur name: ')
    bid = int(input('Enter ur bid: '))
    d.update({bid:name})
    flag=input('Are there any other bidders? Type "yes" or "no": ')
    
if(flag=='no'):
    maximum = max(d)
    print(f'Winner is {d[maximum]} with a bid of {maximum}')
    
from currency_list import bills, coins

def optimal_change(cost, payment):
    change_statement = f'The optimal change for an item that costs ${cost} with an amount paid of ${payment} is '
    
    # Guard statement in case of exact payment
    if cost == payment:
        change_statement += 'no change.'

    
    # Create two diff change types, cents and dollars. Eases Rounding
    change = payment - cost
    str_change = str(change).split('.')
    dollar_change = int(str_change[0])
    
    # To avoid index error when no cents are needed as change
    cent_change = 0
    print(str_change)
    if len(str_change) > 1:
        if len(str_change[1][0:3]) > 2:
            cent_change = round(float(str_change[1][0:3]) / 10)
        else:
            cent_change = round(float(str_change[1][0:3]))
    # Guard statement in case payment is less than cost
    if change < 0:
        return "Insuficient Funds"
    
    current = bills.head
    loop_count = 0
    last_item = False
    coin = False
    while dollar_change != 0 or cent_change != 0:
        
        
        if dollar_change == 0 and not coin:
            coin = True
            current = coins.head
        singular = current.single
        
        if coin:
            if current.val > cent_change:
                current = current.next
                continue
            
            current.count = cent_change // current.val
            cent_change -= current.val * current.count
            
            if current.count > 1:
                singular = current.plural
              
        
        if not coin:
            if current.val > dollar_change:
                current = current.next
                continue
            
            current.count = dollar_change // current.val
            dollar_change -= current.val * current.count
           
           
        if loop_count >= 1 and not last_item:
            change_statement += ', '
                    
        if not dollar_change and not cent_change:
            last_item = True
        
        if last_item and loop_count > 0:
            change_statement += 'and '
        
        if coin:
            change_statement += f'{current.count} {singular}'
            
        if not coin:
            change_statement += f'{current.count} ${current.val} {singular}'
            if current.count > 1:
                change_statement += 's'
         
        loop_count += 1
        current = current.next
        
    return change_statement + '.'

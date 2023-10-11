valor=float(input("valor: "))
desconto=int(input("desconto: "))
valorf=round(valor/100*(100-desconto), 2)
print(f"valor com desconto: R${valorf}")
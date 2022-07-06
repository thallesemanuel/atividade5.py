#Faça um algoritmo que ajude uma empresa de limpeza. 
#Para isso o programa deve ler a largura e o comprimento de um cômodo e
#calcular e mostrar a área a ser limpa e a quantidade de produto necessária para o serviço, 
#sabendo que cada litro de produto limpa uma área de 2 metros quadrados.

from re import A


A = input("Digite o comprimento: ")
B = input("Digite a largura: ")
C = input("Digite a medida que será usada, ex: Cm: ")

ResultadoArea = (float(A) * float(B))
QuanProduto = (float(A) * float(B) /2)

print("A area do cômodo a ser limpa será " + str(ResultadoArea) + str( C) + " quadrados. " + "A quantidade de produto necessária, será " + str(QuanProduto) + " litros. ")
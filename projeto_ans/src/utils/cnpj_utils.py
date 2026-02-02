import re


def cnpj_valido(cnpj: str) -> bool:
    if not cnpj:
        return False

    cnpj = re.sub(r"\D", "", str(cnpj))

    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calc_digitos(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return "0" if resto < 2 else str(11 - resto)

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos2 = [6] + pesos1

    dig1 = calc_digitos(cnpj[:12], pesos1)
    dig2 = calc_digitos(cnpj[:13], pesos2)

    return cnpj[-2:] == dig1 + dig2

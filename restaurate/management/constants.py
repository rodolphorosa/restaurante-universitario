# turnos
MANHA = "manha"
TARDE = "tarde"
NOITE = "noite"

# tipos de refeições
DEJEJUM = "desjejum"
ALMOCO = "almoco"
JANTAR = "jantar"

# gêneros
MASCULINO = "masculino"
FEMININO = "feminino"
NAO_BINARIO = "nao_binario"

# títulos
ESPECIALIZACAO = "especializacao"
MESTRADO = "mestrado"
DOUTORADO = "doutorado"

# tipos de consumidores
ALUNO = "aluno"
FUNCIONARIO = "funcionario"

CONSUMERS_TYPES = [
    (ALUNO, "Aluno"),
    (FUNCIONARIO, "Funcionário"),
]

SHIFTS = [
    (MANHA, "Manhã"),
    (TARDE, "Tarde"),
    (NOITE, "Noite"),
]

MEAL_TYPES = {
    MANHA: DEJEJUM,
    TARDE: ALMOCO,
    NOITE: JANTAR,
}

GENDERS = [
    (MASCULINO, "Masculino"),
    (FEMININO, "Feminino"),
    (NAO_BINARIO, "Não binário"),
]

TITLES = [
    (ESPECIALIZACAO, "Especialização"),
    (MESTRADO, "Mestrado"),
    (DOUTORADO, "Doutorado"),
]

PRICES = {
    MANHA: {
        ALUNO: 0.5,
        FUNCIONARIO: 1.0
    },
    TARDE: {
        ALUNO: 1.0,
        FUNCIONARIO: 6.0
    },
    NOITE: {
        ALUNO: 1.0,
        FUNCIONARIO: 6.0
    },
}
programa {
  funcao inicio() {
    inteiro ano

    escreva("Digite um ano: ")
    leia(ano)

    se(ano % 4 == 0){
      se(ano % 100 == 0){
        se(ano % 400 == 0){
          escreva("O ano � bisexto")
        }
        senao{
          escreva("O ano n�o � bisexto")
        }
      }
      senao{
        escreva("O ano � bisexto")
      }
    }
    senao{
      escreva("O ano n�o � bisexto")
    }
  }
}

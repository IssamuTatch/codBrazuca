programa {
  funcao inicio() {
    inteiro numero, contador = 0

    para (inteiro i = 1; i <= 5; i++){
      escreva("Digite um n�mero: ")
      leia (numero)

      se(numero>0){
        contador ++
      }
    }
    escreva(contador, " N�meros foram positivos")
  }
}

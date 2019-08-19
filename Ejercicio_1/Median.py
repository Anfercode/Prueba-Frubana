class Median:

    list_of_numbers = list()  # Lista de operaciones
    number_of_opertions = 0  # numero de operaciones que realizara el usuario
    MAX_INTEGER = 4294967295

    def median_calc(self):
        """
        * Descripcion:
        * Metodo encargado de realizar el calculo de la media de la variable list_of_numbers
        * 
        * parametros:
        * NA
        * 
        """

        list_sorted = sorted(self.list_of_numbers)
        len_of_list = len(self.list_of_numbers)

        if len_of_list > 0:
            if len_of_list % 2 == 0:
                result = format(
                    0.5*(list_sorted[len_of_list//2] + list_sorted[(len_of_list//2)-1]), '.100g')
                return print(f"Media: {result}")
            else:
                result = list_sorted[len_of_list//2]
                return print(f"Media: {result}")
        else:
            print('Wrong!')

    def add_number_of_list(self, number):
        """
        * Descripcion:
        * Metodo encargado de agregar elementos en la lista
        * 
        * parametros:
        * @param number: Atributo del numero a agregar a list_of_numbers
        """
        self.list_of_numbers.append(number)
        self.median_calc()

    def remove_number_of_list(self, number):
        """
        * Descripcion:
        * Metodo encargado de remover el numero de la lista
        * 
        * parametros:
        * @param number: Atributo del numero a remover a list_of_numbers
        """
        try:
            self.list_of_numbers.remove(number)
            self.median_calc()
        except:
            print('Wrong!')

    def validate_operation(self, operation_with_number):
        """
        * Descripcion:
        * Metodo encargado de validar la operacion
        * 
        * parametros:
        * @param operation_with_number: Atributo que contendra la operacion a realiza 
        *                               y el numero a operar
        """

        try:

            operation = str(operation_with_number[0]).lower()
            number = int(operation_with_number[1:])

            if number < self.MAX_INTEGER or number >= 0:

                if operation == 'a':
                    self.add_number_of_list(number)
                    return True
                elif operation == 'r':
                    self.remove_number_of_list(number)
                    return True
                else:
                    print('La operacion no se encuentra entre las validas')
                    return False
            else:
                print(
                    f'El numero debe ser mayor o igual a 0 y menor a {self.MAX_INTEGER}')
                return False

        except ValueError as error:
            print(error)
            print('...........')
            print('ERROR. La estructura debe ser a1 o r1')
            print('...........')
            return True

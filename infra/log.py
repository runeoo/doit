from datetime import datetime
from infra.to_dict import to_dict

class Log():
    def __init__(self, elemento):
        self.__original_data = str(to_dict(elemento))
        self.__start_time = datetime.now()

    def finalizar(self, elemento):
        with open('app.log', 'a') as arq:
            arq.write(f'\n')
            arq.write(f'Mudanças iniciaram em {self.__start_time}.\n')
            arq.write(f'Valor original: {self.__original_data}.\n')
            arq.write(f'Valor final: {str(to_dict(elemento))}.\n')
            arq.write(f'Mudanças finalizaram em {datetime.now()}.\n')

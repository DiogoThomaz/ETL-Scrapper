import pandas as pd



class Load:
    def _transform_dataframe(self, data_list):
        df = pd.DataFrame(data_list)
        return df

    def _file_save(self, df: pd.DataFrame, file_name):
        try:
            df.to_csv(f'{file_name}.csv', index=False, sep=';', encoding='utf-8')
            print('[v] - Dados salvos com sucesso!')

        except Exception as e:
            print("[x] - Não foi possível salvar os dados")
            print(f"Motivo: {e}")
            pass

    def save_data(self, data_list, file_name):
        print('Salvando dados...')
        df = self._transform_dataframe(data_list)
        self._file_save(df, file_name)
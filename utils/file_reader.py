
import os

import yaml
import xlwings as xw


class YamlReader:

    def __init__(self, yaml_file):
        if os.path.exists(yaml_file):
            self.yaml_file = yaml_file
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yaml_file, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个生成器，用list组织成列表
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    读取excel文件中的内容。返回list。
    如：
    excel中内容为：
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |
    如果print(ExcelReader(excel, title_line=True).data)，输出结果：
    [{A: A1, B: B1, C: C1}, {A: A2, B: B2, C: C2}]
    如果print(ExcelReader(excel, title_line=False).data)，输出结果：
    [[A, B, C], [A1, B1, C1], [A2, B2, C2]]
    可以指定sheet，通过index或者name：
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='Test')
    """
    def __init__(self, excel_file, sheet=0, title_line=True):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = []

    @property
    def data(self):
        if not self._data:
            with xw.App(visible=False, add_book=False) as app:
                wb = app.books.open(self.excel_file)
                sht = wb.sheets[self.sheet]
                if self.title_line:
                    title = sht['A1'].expand('right').value
                    value = sht['A2'].expand().value
                    for i in range(len(value)):
                        self._data.append(dict(zip(title, value[i])))
                else:
                    self._data = sht['A1'].expand().value
        return self._data


if __name__ == '__main__':
    excel = '../test.xlsx'
    e = ExcelReader(excel_file=excel, title_line=False)
    print(e.data)

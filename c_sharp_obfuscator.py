import random
import re


class CSharpObfuscator:
    NEW_METHOD_NAME_TEMPLATE = 'aY8VBiLoztGSIYpfc'
    NEW_VAR_NAME_TEMPLATE = 'eg1OeVVvfj20DSce'
    COMMENT_SEARCH_PATTERN = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
    KEY_WORDS_SEARCH_PATTERN = re.compile(
        r'(?<=(\s))|(?<=(\())|(?<=(^))(abstract|as|base|bool|break|byte|case|catch|char|checked|class|const|continue|decimal|default|delegate|do|double|else|enum|event|explicit|extern|false|finally|fixed|float|for|foreach|goto|if|implicit|in|int|interface|internal|is|lock|long|namespace|new|null|object|operator|out|override|params|private|protected|public|readonly|ref|return|sbyte|sealed|short|sizeof|stackalloc|static|string|struct|switch|this|throw|true|try|typeof|uint|ulong|unchecked|unsafe|ushort|using|var|virtual|void|volatile|while)(?=(\s|%space))')
    METHOD_NAME_PATTERN = re.compile(
        "((?<=public|unsafe|static|extern)|(?<=internal)|(?<=protected)|(?<=async)|(?<=private))\s+[a-zA-Z0-9_\[\]]*(\s*[A-Za-z_][A-Za-z_0-9]*\s*)")
    METHOD_PATTERN = re.compile("((public|unsafe|static|extern)|(?<=internal)|(?<=protected)|(?<=async)|(?<=private))\s+[a-zA-Z0-9_\[\]]*(\s*[A-Za-z_][A-Za-z_0-9]*\s*)")
    PARAMETER_REPLACE_PATTERN = "(?<=[\. =+*/\-,;()\]\[]){0}(?=[ =+*/\-\.,;()\]\[])"
    VARIABLE_DEFINITION_PATTERN = "[a-zA-Z0-9\[\]]+\s[a-zA-Z0-9]+\s+=(?!=)"

    def __init__(self, code):
        self.code = code
        self.method_count = 0
        self.var_count = 0

    def obfuscate(self):
        self.__remove_comments()
        self.__rename_parameters_in_methods()
        self.__rename_variables_in_methods()
        self.__rename_methods()
        # self.__reshuffle_methods()
        self.__remove_spaces()
        self.__remove_line_breaks()
        return self.code

    def __remove_comments(self):
        self.code = re.sub(self.COMMENT_SEARCH_PATTERN, '', self.code)

    def __remove_spaces(self):
        self.code = re.sub(self.KEY_WORDS_SEARCH_PATTERN, r"%space \4%space ", self.code)
        self.code = re.sub(r'[ ]+', '', self.code)
        self.code = re.sub(r'[\t]+', '', self.code)
        self.code = re.sub(r'(%space)+', ' ', self.code)

    def __rename_methods(self):
        method_names = re.findall(self.METHOD_NAME_PATTERN, self.code)
        method_name_dict = dict()
        for index, method_name in enumerate(method_names):
            if 'Main' != method_name[1].strip():
                method_name_dict[method_name[1].strip()] = f"{self.NEW_METHOD_NAME_TEMPLATE}{self.method_count}"
            self.method_count += 1
        for old_method_name, new_method_name in method_name_dict.items():
            self.code = re.sub(re.compile(old_method_name + '\('), f'{new_method_name}(', self.code)

    def __rename_parameters_in_methods(self):
        all_method_borders = self.__get_method_borders()
        new_code = self.code[0:all_method_borders[0][0]]
        for method_borders in all_method_borders:
            method = self.code[method_borders[0]: method_borders[1]]
            parameters = method.split('\n')[0].split('(')[-1].split(')')[0].split(',')
            for parameter in parameters:
                parameter = parameter.split(' ')[-1]
                method = re.sub(self.PARAMETER_REPLACE_PATTERN.format(parameter),
                                f"{self.NEW_VAR_NAME_TEMPLATE}{self.var_count}",
                                method)
                self.var_count += 1
            new_code += method
        new_code += self.code[all_method_borders[-1][1]:]
        self.code = new_code

    def __get_method_borders(self):
        all_method_borders = list()
        method_borders = list()
        for match in re.finditer(self.METHOD_PATTERN, self.code):
            if len(method_borders) == 0:
                method_borders.append(match.start())
            else:
                method_borders.append(match.start())
                all_method_borders.append(method_borders)
                method_borders = list()
                method_borders.append(match.start())
        if len(method_borders) == 1:
            method_borders.append(len(self.code) - 1)
            all_method_borders.append(method_borders)
        return all_method_borders

    def __rename_variables_in_methods(self):
        all_method_borders = self.__get_method_borders()
        new_code = self.code[0:all_method_borders[0][0]]
        for method_borders in all_method_borders:
            method = self.code[method_borders[0]: method_borders[1]]
            variables = re.findall(self.VARIABLE_DEFINITION_PATTERN, method)
            for variable in variables:
                variable = variable.strip().replace(' =', '').split(' ')[-1]
                method = re.sub(self.PARAMETER_REPLACE_PATTERN.format(variable),
                                f"{self.NEW_VAR_NAME_TEMPLATE}{self.var_count}",
                                method)
                self.var_count += 1
            new_code += method
        new_code += self.code[all_method_borders[-1][1]:]
        self.code = new_code

    def __remove_line_breaks(self):
        self.code = re.sub('\n', '', self.code)

    def __reshuffle_methods(self):
        all_method_borders = self.__get_method_borders()
        code_begin = self.code[0:all_method_borders[0][0]]
        code_end = self.code[all_method_borders[-1][1]:]
        random.shuffle(all_method_borders)
        for method_borders in all_method_borders:
            method = self.code[method_borders[0]: method_borders[1]]
            code_begin += method
        code_begin += code_end
        # print(code_begin)
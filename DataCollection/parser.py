import os
import ast
import astpretty
import inspect
from collections import deque
import tokenize
FileAddress = 'sample.py'
files_list = ['sample.py']
OUTPUT_ADDRESS = "/Users/pouya/Documents/Github/deep-code-search/DataCollection/Features/"
KEYWORDS = {'def', 'self'}
NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}
import re
def remove_punctuation(str):
    puncs = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for c in str:
        if c in puncs:
            str = str.replace(c, "")
    return str

def camel_split(str):
    l = re.split("(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", str)
    return l

# Driver code
str = "__Read_Some__"
print(camel_split(str))

class CallCollector(ast.NodeVisitor):
    def __init__(self):
        self.calls = []
        self._current = []
        self._in_call = False

    def visit_Call(self, node):
        self._current = []
        self._in_call = True
        self.generic_visit(node)

    def generic_visit(self, node):
        if self._current is not None:
            pass
            # print("warning: {} node in function expression not supported".format(
            #     node.__class__.__name__))
        super(CallCollector, self).generic_visit(node)

    def visit_Attribute(self, node):
        if self._in_call:
            self._current.append(node.attr)
        self.generic_visit(node)

    # record the func expression
    def visit_Name(self, node):
        if self._in_call:
            self._current.append(node.id)
            self.calls.append('.'.join(self._current[::-1]))
            # Reset the state
            self._current = []
            self._in_call = False
        self.generic_visit(node)


def get_functionNames(file_address):
    with open(file_address, 'r') as file:
        source = file.read()
    tree = ast.parse(source)
    docs = []
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            c = ast.get_docstring(node)
            if c != None:
                docs.append(remove_punctuation(c.split('\n')[0]).split())
                for item in node.name.split("_"):
                    names.append(item)
    method_names = []
    for item in names:
        if item != '':
            for x in camel_split(item):
                method_names.append(x.lower())
    return method_names, [j.lower() for row in docs for j in row if len(j) > 2]


    # print(method_definitions)
def getAPIsequence(file_address):
    with open(file_address, 'r') as file:
        data = file.read()
    tree = ast.parse(data)
    cc = CallCollector()
    cc.visit(tree)
    result = [x.split(".") for x in cc.calls]
    return [j.lower() for row in result for j in row if (j not in KEYWORDS and len(j)>2)]

def getTokens(file_address):
    tokens = []
    with open(file_address, 'rb') as f:
        for t in tokenize.tokenize(f.readline):
            # print("Type:", t.type)
            # print("string:", t.string)
            # print("start:", t.start)
            # print("end:", t.end)
            # print("line:", t.line)
            if t.string.isalpha() and len(t.string) > 2 and t.string not in KEYWORDS:
                tokens.append(t.string.lower())
    return tokens

def extract_features(file_address):
    method_names, docstrings = get_functionNames(file_address)
    apiSequence = getAPIsequence(file_address)
    tokens = getTokens(file_address)
    with open(OUTPUT_ADDRESS + "methname.txt", "a") as method_names_file:
        line = " ".join(method_names)
        method_names_file.write(line + "\n")
        method_names_file.close()
    with open(OUTPUT_ADDRESS + "desc.txt", "a") as descriptions_file:
        line = " ".join(docstrings)
        descriptions_file.write(line + "\n")
        descriptions_file.close()
    with open(OUTPUT_ADDRESS + "apiseq.txt", "a") as apiseq_file:
        line = " ".join(apiSequence)
        apiseq_file.write(line + "\n")
        apiseq_file.close()
    with open(OUTPUT_ADDRESS + "tokens.txt", "a") as tok_file:
        line = " ".join(tokens)
        tok_file.write(line + "\n")
        tok_file.close()
    with open(OUTPUT_ADDRESS + "file_dirs.txt", "a") as file_dirs:
        file_dirs.write(file_address + "\n")
        file_dirs.close()

def main():
    method_names, docstrings = get_functionNames(FileAddress)
    print("Method Names:", len(method_names), method_names)
    print("Docstrings:", len(docstrings), docstrings)
    apiSequence = getAPIsequence(FileAddress)
    print("API Seq:", len(apiSequence), apiSequence)
    tokens = getTokens(FileAddress)
    print("TOKENS :", len(tokens), tokens)
    extract_features(FileAddress)
if __name__ == "__main__":
  main()

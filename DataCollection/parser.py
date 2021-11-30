import ast
import astpretty
import inspect
FileAddress = 'sample.py'
files_list = ['sample.py']

NODE_TYPES = {
    ast.ClassDef: 'Class',
    ast.FunctionDef: 'Function/Method',
    ast.Module: 'Module'
}

def get_moduleImplementation(files_list):
    import sample
    source_file = inspect.getsource(sample)
    for key, c in inspect.getmembers(sample, inspect.isclass):
        print('{} : {!r}'.format(key, c))
        methods = inspect.getmembers(c, inspect.isfunction)
        print(methods)
        for m in methods:
            print(inspect.getsource(m[1]))

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
                docs.append(c.split('\n')[0])
                names.append(node.name)
    print(names)
    print(docs)

def get_docstrings(file_address):
    with open(file_address, 'r') as file:
        data = file.read()
    module = ast.parse(data)
    astpretty.pprint(module, show_offsets = False)
    # print(ast.dump(node=module.body[0]))
    function_defs = [node for node in module.body if isinstance(node, ast.FunctionDef)]
    function_names = [f.name for f in function_defs]
    implementations = [f.body for f in function_defs]
    # for i in implementations:
        # print(ast.dump(node = module.body, annotate_fields=True))
    comments = [ast.get_docstring(f).split('\n') for f in function_defs]
    for c in comments:
        print(c[0])

    class_definitions = [node for node in module.body if isinstance(node, ast.ClassDef)]
    method_definitions = []
    print(class_definitions)
    for class_def in class_definitions:
        method_definitions.append([node for node in class_def.body if isinstance(node, ast.FunctionDef)])

    for c in method_definitions:
        m = [(f.name, ast.get_docstring(f).split('\n')[0]) for f in c]
        print(m)

    # print(method_definitions)



def main():

    # get_docstrings(FileAddress)
    # get_moduleImplementation(files_list)
    get_functionNames(FileAddress)


if __name__ == "__main__":
  main()

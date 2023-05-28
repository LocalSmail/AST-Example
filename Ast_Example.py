import ast

code = """
def t(text, textt):
    print("hello")

t(1, 2, 3, 4)
"""

tree = ast.parse(code) # create node

# loop through all children
for node in ast.iter_child_nodes(tree):
    if isinstance(node, ast.Constant):
        print('this is a constant')
    
    elif isinstance(node, ast.Return):
        print('this is a return statement')

    elif isinstance(node, ast.FunctionDef):
        print('this is a function')
        
        new_args = [ast.arg(arg='new_arg1', annotation=None), ast.arg(arg='new_arg2', annotation=None)] # Create Custom arguments
        
        node.args.args.extend(new_args) # Apply
        
        for args in node.args.args: # Loop through arguments
            
            print(args) # print all arguments
    else:
        print('idfk') # we dont know what it is so we just print that
        
        

modified = ast.unparse(tree) # reverse the node back into code

print(modified) # print the modified code

# we compile then execute the code

exec(compile(modified, '', 'exec'))


# STRUCTURE

"""
Module(
    body=[
        FunctionDef(
            name='t', 
            args=arguments(
                posonlyargs=[], args=[arg(arg='text', arg='textt')], kwonlyargs=[], kw_defaults=[], defaults=[]), 
            body=[
                Expr(value=Call(
                    func=Name(
                        id='print', ctx=Load()), 
                    args=[
                        Constant(value='hello')],
                    keywords=[]))],
            decorator_list=[])], 
    type_ignores=[])
"""

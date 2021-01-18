import ast
input_source = """

def hoge(a,b=1):
  return a+b

a = 1

print(hoge(a))
"""
ast_object = ast.parse(input_source)

print(ast.dump(ast_object))
'''
Module(body=[FunctionDef(name='hoge', args=arguments(posonlyargs=[], args=[arg(arg='a'), arg(arg='b')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1)]), body=[Return(value=BinOp(left=Name(id='a', ctx=Load()), op=Add(), right=Name(id='b', ctx=Load())))], decorator_list=[]), Assign(targets=[Name(id='a', ctx=Store())], value=Constant(value=1)), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Call(func=Name(id='hoge', ctx=Load()), args=[Name(id='a', ctx=Load())], keywords=[])], keywords=[]))], type_ignores=[])
'''

# 3.9：インデントオプションが追加されました。
# ノード内のツリーのフォーマットされたダンプを返します。
# これは主にデバッグの目的で役立ちます。場合annotate_fieldsはデフォルトでtureである、
# 返される文字列は、フィールドの名前と値を表示します。annotate_fieldsがfalseの場合、
# 明確なフィールド名を省略することにより、結果の文字列がよりコンパクトになります。
# 行番号や列オフセットなどの属性は、デフォルトではダンプされません。
# これが必要な場合は、include_attributesをtrueに設定できます。
print(ast.dump(ast_object, include_attributes = True))
'''
Module(body=[FunctionDef(name='hoge', args=arguments(posonlyargs=[], args=[arg(arg='a', lineno=3, col_offset=9, end_lineno=3, end_col_offset=10), arg(arg='b', lineno=3, col_offset=11, end_lineno=3, end_col_offset=12)], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1, lineno=3, col_offset=13, end_lineno=3, end_col_offset=14)]), body=[Return(value=BinOp(left=Name(id='a', ctx=Load(), lineno=4, col_offset=9, end_lineno=4, end_col_offset=10), op=Add(), right=Name(id='b', ctx=Load(), lineno=4, col_offset=11, end_lineno=4, end_col_offset=12), lineno=4, col_offset=9, end_lineno=4, end_col_offset=12), lineno=4, col_offset=2, end_lineno=4, end_col_offset=12)], decorator_list=[], lineno=3, col_offset=0, end_lineno=4, end_col_offset=12), Assign(targets=[Name(id='a', ctx=Store(), lineno=6, col_offset=0, end_lineno=6, end_col_offset=1)], value=Constant(value=1, lineno=6, col_offset=4, end_lineno=6, end_col_offset=5), lineno=6, col_offset=0, end_lineno=6, end_col_offset=5), Expr(value=Call(func=Name(id='print', ctx=Load(), lineno=8, col_offset=0, end_lineno=8, end_col_offset=5), args=[Call(func=Name(id='hoge', ctx=Load(), lineno=8, col_offset=6, end_lineno=8, end_col_offset=10), args=[Name(id='a', ctx=Load(), lineno=8, col_offset=11, end_lineno=8, end_col_offset=12)], keywords=[], lineno=8, col_offset=6, end_lineno=8, end_col_offset=13)], keywords=[], lineno=8, col_offset=0, end_lineno=8, end_col_offset=14), lineno=8, col_offset=0, end_lineno=8, end_col_offset=14)], type_ignores=[]) 
'''
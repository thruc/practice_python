# 文字列がプレフィックス文字列で始まる場合はstring[len(prefix):]を返します。
# それ以外の場合は、元の文字列のコピーを返します。

str1 = 'TestHook'
print(str1.removeprefix('Test'))

str2 = 'BaseTestCase'
print(str2.removeprefix('Test'))


# 文字列がサフィックス文字列で終わり、そのサフィックスが空でない場合は、string[:-len(suffix)]を返します。
# それ以外の場合は、元の文字列のコピーを返します。

str3 = 'MiscTests'
print(str3.removesuffix('Tests'))

str4 = 'TmpDirMixin'
print(str4.removesuffix('Tests'))

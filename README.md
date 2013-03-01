在开发的时候出于偷懒，偶尔会在项目里留下各种各样的中文，比如：(@"你好，世界")

这样的话对项目的后期的本地化处理会留下隐患。

这个脚本的作用就是帮你遍历项目目录下面所有.m类型(你可以修改文件类型)文件中的包含中文的行，并且对注释部分进行了简单的过滤

```
#需要告诉脚本，包含以下参数的字符串，均为注释
comment_param_0 = '@return'
comment_param_1 = '@brief'
comment_param_2 = '@param'
comment_param_3 = '//'
comment_param_4 = '/*'
```

```
#find all .m files' path
def match_all_m_files_with_path(path):
    print "get path: "+path
    #如果你想在其他类型的文件里找的话可以修改这里
    m_paths = match_file_with_keyword(lambda f:f.endswith('.m'),path)
    return m_paths
```

#How To Use
```
python find_chinese.py ~/MyProjectDictory/ >~/output
```



#!/usr/bin/env python

#Nicholas Tau
#2013.2.20

"""
find all chinse words in .m file just like '@"xxxx"'
"""

import sys
import re
import os 
import codecs

def main():
    project_path = None

    if 'PROJECT_DIR' in os.environ:
        project_path = os.environ['PROJECT_DIR']
    elif len(sys.argv)>1:
        project_path = sys.argv[1]
    
    if not project_path or not os.path.exists(project_path):
        error("", 0, "bad project path:%s" % project_path)
        return

    paths_contain_m_file = match_all_m_files_with_path(project_path)

    for path in paths_contain_m_file:
        check_words_with_path(path)

def error(file_path, line_number, message):
    print "%s:%d: error: %s" % (file_path, line_number, message)


'''
find all .m files' path
'''
def match_all_m_files_with_path(path):
    print "get path: "+path
    m_paths = match_file_with_keyword(lambda f:f.endswith('.m'),path)

    return m_paths


'''
match file with keyword
'''
def check_words_with_path(p):
    
    f = open(p)

    #keys = set()

    line_number = 0
    for line in f.xreadlines():
        line_number += 1

        if line.strip().startswith('//'):
            continue
        
        pattern = re.compile('[\x80-\xff]{3}')
        match   = pattern.search(line)

        
        comment_param_0 = '@return'
        comment_param_1 = '@brief'
        comment_param_2 = '@param'
        comment_param_3 = '//'
        comment_param_4 = '/*'

        if match:
            if comment_param_0 in line or comment_param_1 in line or comment_param_2 in line or comment_param_3 in line or comment_param_4 in line:
               # print 'this line(%d) in file(%s) maybe a comment(%s):\n' %(line_number,f,line)
               print "find comments\n"
            else:
               print "*******find words in file:%s \n at line:%d\n (%s)" % (f,line_number,line)
                       

def match_file_with_keyword(keyword,path):
    for root, dirs, files in os.walk(path):
        for p in (os.path.join(root,f) for f in files if keyword(f)):
            yield p


if __name__ =="__main__":
    main()

import os
import nltk

os.system('git clone git@github.com:nltk/nltk_data.git')
os.system('cp -rf nltk_data/packages')
paths = nltk.data.path
print(paths)
os.system(f'cp -r nltk_data/packages/* {paths[0]}/') #NOTE: 将packages里面的文件夹拷贝到nltk_data,  而不是把packages拷贝到nltk_data

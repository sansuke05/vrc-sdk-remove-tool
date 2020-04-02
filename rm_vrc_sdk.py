# -*- coding: utf8 -*-

import os
import shutil

def rm_vrcsdk(project_path):
    sdk_dir = project_path + 'Assets\\VRCSDK'
    plugin_dir = project_path + 'Assets\\Plugins\\VRCSDK'

    if not os.path.exists(sdk_dir):
        return 'VRCSDKフォルダが見つかりませんでした'
    
    if not os.path.exists(plugin_dir):
        return 'Plugins/VRCSDKフォルダが見つかりませんでした'

    try:
        shutil.rmtree(sdk_dir + '\\')
        os.remove(sdk_dir + '.meta')
    except:
        return sdk_dir + 'の削除に失敗しました'
    
    try:
        shutil.rmtree(plugin_dir + '\\')
        os.remove(plugin_dir + '.meta')
    except:
        return plugin_dir + 'の削除に失敗しました'

    return ''


# test
if __name__ == "__main__":
    project_path = input('Please input Unity Project Path: ')
    # 行末に\がなければ追加
    if (len(project_path) - project_path.rfind('\\')) > 2:
        project_path += '\\'
    
    print('input Path is {0}'.format(project_path))
    
    result = rm_vrcsdk(project_path)
    
    if result != '':
        print(result)
    else:
        print('Completed!')
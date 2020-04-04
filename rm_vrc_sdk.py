# -*- coding: utf8 -*-

import os
import shutil

def rm_vrcsdk(project_path):
    sdk_dir = project_path + 'Assets\\VRCSDK'
    plugin_dir_2017 = project_path + 'Assets\\Plugins\\VRCSDK'
    plugin_dir_2018 = sdk_dir + '\\Plugins'
    result = ''

    is_exists_2017_plugin = os.path.exists(plugin_dir_2017) # trueなら2017SDK
    is_exists_2018_plugin = os.path.exists(plugin_dir_2018) # trueなら2018SDK

    if not os.path.exists(sdk_dir):
        return 'VRCSDKフォルダが見つかりませんでした'
    
    # pluginを先に削除
    if is_exists_2017_plugin:
        result = rm_plugin(plugin_dir_2017)
    elif is_exists_2018_plugin:
        result = rm_plugin(plugin_dir_2018)
    else:
        return 'Plugins/VRCSDKフォルダが見つかりませんでした'

    # pluginを削除した結果、エラーがあれば関数を終了
    if result != '':
        return result

    # SDKを削除
    try:
        shutil.rmtree(sdk_dir + '\\')
        os.remove(sdk_dir + '.meta')
    except:
        return sdk_dir + 'の削除に失敗しました'
    return ''


def rm_plugin(plugin_dir):
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
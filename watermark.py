import re
import os
import subprocess
import time

inkscape_path = 'C:/Program Files/Inkscape/bin/inkscape'

path = os.path.abspath(__file__)
os.chdir('/'.join(path.split('\\')[:-1]))

enable_shaders = 'false'
shader_pack = '无光影包'
resource_pack = '原版资源包'
username = ''
title = ''

def proc_file_name(file_name):
    return file_name.strip().replace('.zip', '').replace('_',' ').replace('-',' ').replace('+',' ').replace('[', '').replace(']', '').replace('"', '')

if os.path.exists('options.txt'):
    with open('options.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('resourcePacks:'):
                resource_packs = line
        for i in resource_packs.split(','):
            if 'file/' in i:
                resource_pack = proc_file_name(i.split('/')[-1])
        if resource_pack != '原版资源包':
            resource_pack += ' 资源包'

if os.path.exists('config/iris.properties'):
    with open('config/iris.properties', 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('enableShaders='):
                enable_shaders = line.split('=')[1].strip()
            elif line.startswith('shaderPack='):
                shader_pack = proc_file_name(line.split('=')[1])
        if shader_pack != '无光影包':
            shader_pack += ' 光影包'

if os.path.exists('logs/latest.log'):
    with open('logs/latest.log', 'r', encoding='gbk', errors='ignore') as f:
        for line in f:
            if re.match(r'\[\d\d:\d\d:\d\d\] \[Render thread/INFO\]: Setting user: ', line) is not None:
                username = line.split(' ')[-1].strip()
            if re.match(r'\[\d\d:\d\d:\d\d\] \[Render thread/INFO\]: \[CHAT\] 截图水印标题已设为：', line) is not None:
                title = line.split('：')[-1].strip()
            if re.match(r'\[\d\d:\d\d:\d\d\] \[Render thread/INFO\]: \[CHAT\] 截图水印标题已清除。', line) is not None:
                title = ''

if not os.path.exists('watermarks'):
    os.makedirs('watermarks')

pngs = sorted([x for x in os.listdir('screenshots') if x.endswith('.png')], key=lambda x: os.path.getmtime(f'screenshots/{x}'))

date = time.strftime('%Y%m%d', time.localtime(os.path.getmtime(f'screenshots/{pngs[-1]}')))

if enable_shaders == 'false':
    shader_pack = '无光影包'

print(f'resource_pack: {resource_pack}')
print(f'shader_pack: {shader_pack}')
print(f'username: {username}')
print(f'title: {title}')
print(f'date: {date}')

with open('temp.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

svg = svg.replace('{{resource_pack}}', resource_pack)
svg = svg.replace('{{shader_pack}}', shader_pack)
svg = svg.replace('{{username}}', username)
svg = svg.replace('{{title}}', title)
svg = svg.replace('{{date}}', date)
svg = svg.replace('{{image_file}}', pngs[-1])

with open(f'{pngs[-1][:-4]}-sig.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

subprocess.run([inkscape_path, f'{pngs[-1][:-4]}-sig.svg', '-o', f'watermarks/{pngs[-1][:-4]}-sig.png'])
os.remove(f'{pngs[-1][:-4]}-sig.svg')

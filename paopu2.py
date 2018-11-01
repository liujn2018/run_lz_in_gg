# -*- coding: utf-8 -*- 
import sys
import os
import subprocess
import re

def __shell__(cmd):
  os.system(cmd)
  
def __shell2__(cmd):
  return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode('utf-8')

#if not os.path.exists('/usr/lib/x86_64-linux-gnu/libnvidia-opencl.so.1'):
#__shell__('apt update > /dev/null')
__shell__('apt install --no-upgrade qt5-default qt5-qmake > /dev/null')
__shell__('apt install --no-upgrade libboost-all-dev libopenblas-dev opencl-headers zlib1g-dev > /dev/null')
#__shell__('apt -qq install --no-install-recommends nvidia-opencl-icd-384 > /dev/null')
#__shell__('wget http://launchpadlibrarian.net/352962266/nvidia-opencl-icd-384_384.111-0ubuntu0.17.10.1_amd64.deb > /dev/null')
#__shell__('apt install -f ./nvidia-opencl-icd-384_384.111-0ubuntu0.17.10.1_amd64.deb > /dev/null')
__shell__('apt install --no-upgrade nvidia-opencl-dev > /dev/null')
#__shell__('apt --fix-broken install > /dev/null')

__shell__('mkdir -p run_lz_in_gg/networks')
__shell__('rm -rf wtlist')
__shell__('git clone https://github.com/liujn2018/wtlist.git')
__shell__('pip install gdown >/dev/null')
with open('wtlist/current.txt', 'rt') as wt_in:
    for line in wt_in.readlines():
        if line.startswith('#'):
            continue
        if len(line)<5:
            continue
        dlinfo = __shell2__('gdown --id {0}'.format(line))
        print(dlinfo)
        match = re.search(r'To: /content/(.*?)$', dlinfo, re.MULTILINE)
        if match:
            #print(match.group(1))
            filename = match.group(1)
            if filename.endswith('.gz'):
                __shell__('gunzip -f {0}'.format(filename))
                filename = filename[:-3]
            else:
                pass
            __shell__('mv /content/{0} run_lz_in_gg/networks/'.format(filename))
        

__shell__('cd run_lz_in_gg; chmod +x leelaz;./autogtp -k sgf')


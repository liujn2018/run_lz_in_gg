# -*- coding: utf-8 -*- 
import sys
import os

def __shell__(cmd):
  os.system(cmd)

if not os.path.exists('/usr/lib/x86_64-linux-gnu/libnvidia-opencl.so.1'):
    __shell__('apt update > /dev/null')
    __shell__('apt install qt5-default qt5-qmake curl > /dev/null')
    __shell__('apt install libboost-dev libboost-program-options-dev libopenblas-dev opencl-headers ocl-icd-opencl-dev > /dev/null')
    __shell__('apt -qq install --no-install-recommends nvidia-opencl-icd-384 > /dev/null')
    __shell__('wget http://launchpadlibrarian.net/352962266/nvidia-opencl-icd-384_384.111-0ubuntu0.17.10.1_amd64.deb > /dev/null')
    __shell__('apt install -f ./nvidia-opencl-icd-384_384.111-0ubuntu0.17.10.1_amd64.deb > /dev/null')
    __shell__('apt -qq install --no-install-recommends nvidia-opencl-dev > /dev/null')
    __shell__('apt --fix-broken install > /dev/null')

__shell__('pip install gdown >/dev/null')
__shell__('gdown https://drive.google.com/uc?id=12nkQsoyKJ4OP8p4foJ05jTxXATfGnJ1M')
__shell__('gdown https://drive.google.com/uc?id=1srbuq-CqAGOqU8FxgIfCpr7o1fsSQR5C')
__shell__('mkdir -p run_lz_in_gg/networks; ls | head -2| xargs -i cp -r {} run_lz_in_gg/networks')

__shell__('cd run_lz_in_gg; ./autogtp | grep minute')

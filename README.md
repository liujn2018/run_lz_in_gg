# run_lz_in_gg

- in Google Colab,
```
!apt update
!git clone http://github.com/liujn2018/run_lz_in_gg.git
!apt install qt5-default qt5-qmake curl
!apt install libboost-dev libboost-program-options-dev libopenblas-dev opencl-headers ocl-icd-opencl-dev
!apt -qq install --no-install-recommends nvidia-opencl-icd-384
!wget http://launchpadlibrarian.net/352962266/nvidia-opencl-icd-384_384.111-0ubuntu0.17.10.1_amd64.deb
!apt install -f ./nvidia-opencl-icd-384_384.111-0ubuntu0.17.10.1_amd64.deb
!apt -qq install --no-install-recommends nvidia-opencl-dev
!cd run_lz_in_gg && ./autogtp -k sgf
```

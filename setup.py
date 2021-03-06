from setuptools import setup
import os

import tridesclous

install_requires = [
                    'numpy',
                    'scipy',
                    'pandas',
                    'scikit-learn',
                    'matplotlib',
                    'seaborn',
                    'quantities==0.12.1',
                    'neo>=0.5.1',
                    'tqdm',
                    ]
extras_require={ 'gui' : ['PyQt5', 'pyqtgraph==0.10.0', 'matplotlib'],
                            'online' : 'pyacq',
                            'opencl' : ['pyopencl'],
                        }

long_description = ""

setup(
    name = "tridesclous",
    version = tridesclous.__version__,
    packages = ['tridesclous', 'tridesclous.gui', 'tridesclous.gui.icons',
                'tridesclous.online', 'tridesclous.scripts', 'tridesclous.tests'],
    install_requires=install_requires,
    extras_require = extras_require,
    author = "C. Pouzat, S.Garcia",
    author_email = "",
    description = "offline/online spike sorting with french touch that light the barbecue",
    long_description = long_description,
    entry_points={
          'console_scripts': ['tdc=tridesclous.scripts.tdc:main'],
          #~ 'gui_scripts': ['tdcgui=tridesclous.scripts.tdc:open_mainwindow'],
        },
     license = "MIT",
    url='https://github.com/tridesclous/trisdesclous',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering']
)

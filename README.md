# python_package_install_example

Example repository on how to structure python packages that are installable.

## User

### Installation
```
sudo python3 setup.py install --record files.txt
```

### Uninstallation
If you hadn't deleted the code repository you should have a files.txt:
```
sudo xargs rm -rf files.txt
```

If you don't run the installation command again and it'll regenerate files.txt then run the uninstall command and you're good.



## Develop

### Installation
```
sudo python3 setup.py develop
```

### Uninstallation
Find ```kk-pkgs.egg-link``` in ```/usr/local/lib/python3.6/dist-packages``` or similar:

```
sudo rm kk-pkgs.egg-link
```

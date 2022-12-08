```bash
docker-compose ps
```


```bash
maki@maki-jetson2:~/Documents/001_morter$ docker-compose ps
bash: docker-compose: command not found
```


```bash
sudo apt install python3-pip
```



```bash
maki@maki-jetson2:~/Documents/001_morter$ sudo apt install python3-pip
[sudo] password for maki: 
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下の追加パッケージがインストールされます:
  dh-python libpython3-dev libpython3.6-dev python3-dev python3-setuptools python3-wheel python3.6-dev
提案パッケージ:
  python-setuptools-doc
以下のパッケージが新たにインストールされます:
  dh-python libpython3-dev libpython3.6-dev python3-dev python3-pip python3-setuptools python3-wheel python3.6-dev
アップグレード: 0 個、新規インストール: 8 個、削除: 0 個、保留: 154 個。
46.1 MB のアーカイブを取得する必要があります。
この操作後に追加で 78.8 MB のディスク容量が消費されます。
続行しますか? [Y/n] Y
取得:1 http://ports.ubuntu.com/ubuntu-ports bionic/main arm64 dh-python all 3.20180325ubuntu2 [89.2 kB]
取得:2 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main arm64 libpython3.6-dev arm64 3.6.9-1~18.04ubuntu1.8 [45.1 MB]
取得:3 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main arm64 libpython3-dev arm64 3.6.7-1~18.04 [7,328 B]                                                                                                                                                                                      
取得:4 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main arm64 python3.6-dev arm64 3.6.9-1~18.04ubuntu1.8 [512 kB]                                                                                                                                                                               
取得:5 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main arm64 python3-dev arm64 3.6.7-1~18.04 [1,288 B]                                                                                                                                                                                         
取得:6 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 python3-pip all 9.0.1-2.3~ubuntu1.18.04.5 [114 kB]                                                                                                                                                                            
取得:7 http://ports.ubuntu.com/ubuntu-ports bionic/main arm64 python3-setuptools all 39.0.1-2 [248 kB]                                                                                                                                                                                                  
取得:8 http://ports.ubuntu.com/ubuntu-ports bionic/universe arm64 python3-wheel all 0.30.0-0.2 [36.5 kB]                                                                                                                                                                                                
46.1 MB を 11秒 で取得しました (4,260 kB/s)                                                                                                                                                                                                                                                             
debconf: delaying package configuration, since apt-utils is not installed
以前に未選択のパッケージ dh-python を選択しています。
(データベースを読み込んでいます ... 現在 178546 個のファイルとディレクトリがインストールされています。)
.../0-dh-python_3.20180325ubuntu2_all.deb を展開する準備をしています ...
dh-python (3.20180325ubuntu2) を展開しています...
以前に未選択のパッケージ libpython3.6-dev:arm64 を選択しています。
.../1-libpython3.6-dev_3.6.9-1~18.04ubuntu1.8_arm64.deb を展開する準備をしています ...
libpython3.6-dev:arm64 (3.6.9-1~18.04ubuntu1.8) を展開しています...
以前に未選択のパッケージ libpython3-dev:arm64 を選択しています。
.../2-libpython3-dev_3.6.7-1~18.04_arm64.deb を展開する準備をしています ...
libpython3-dev:arm64 (3.6.7-1~18.04) を展開しています...
以前に未選択のパッケージ python3.6-dev を選択しています。
.../3-python3.6-dev_3.6.9-1~18.04ubuntu1.8_arm64.deb を展開する準備をしています ...
python3.6-dev (3.6.9-1~18.04ubuntu1.8) を展開しています...
以前に未選択のパッケージ python3-dev を選択しています。
.../4-python3-dev_3.6.7-1~18.04_arm64.deb を展開する準備をしています ...
python3-dev (3.6.7-1~18.04) を展開しています...
以前に未選択のパッケージ python3-pip を選択しています。
.../5-python3-pip_9.0.1-2.3~ubuntu1.18.04.5_all.deb を展開する準備をしています ...
python3-pip (9.0.1-2.3~ubuntu1.18.04.5) を展開しています...
以前に未選択のパッケージ python3-setuptools を選択しています。
.../6-python3-setuptools_39.0.1-2_all.deb を展開する準備をしています ...
python3-setuptools (39.0.1-2) を展開しています...
以前に未選択のパッケージ python3-wheel を選択しています。
.../7-python3-wheel_0.30.0-0.2_all.deb を展開する準備をしています ...
python3-wheel (0.30.0-0.2) を展開しています...
python3-wheel (0.30.0-0.2) を設定しています ...
libpython3.6-dev:arm64 (3.6.9-1~18.04ubuntu1.8) を設定しています ...
python3-pip (9.0.1-2.3~ubuntu1.18.04.5) を設定しています ...
python3-setuptools (39.0.1-2) を設定しています ...
python3.6-dev (3.6.9-1~18.04ubuntu1.8) を設定しています ...
dh-python (3.20180325ubuntu2) を設定しています ...
libpython3-dev:arm64 (3.6.7-1~18.04) を設定しています ...
python3-dev (3.6.7-1~18.04) を設定しています ...
man-db (2.8.3-2ubuntu0.1) のトリガを処理しています ...
maki@maki-jetson2:~/Documents/001_morter$ 
```


```bash
sudo apt install build-essential libssl-dev libffi-dev python3-dev
```



```bash
maki@maki-jetson2:~/Documents/001_morter$ sudo apt install build-essential libssl-dev libffi-dev python3-dev
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
build-essential はすでに最新バージョン (12.4ubuntu1) です。
build-essential は手動でインストールしたと設定されました。
python3-dev はすでに最新バージョン (3.6.7-1~18.04) です。
python3-dev は手動でインストールしたと設定されました。
提案パッケージ:
  libssl-doc
以下のパッケージが新たにインストールされます:
  libffi-dev libssl-dev
アップグレード: 0 個、新規インストール: 2 個、削除: 0 個、保留: 154 個。
1,522 kB のアーカイブを取得する必要があります。
この操作後に追加で 7,292 kB のディスク容量が消費されます。
続行しますか? [Y/n] Y
取得:1 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main arm64 libssl-dev arm64 1.1.1-1ubuntu2.1~18.04.20 [1,366 kB]
取得:2 http://ports.ubuntu.com/ubuntu-ports bionic/main arm64 libffi-dev arm64 3.2.1-8 [155 kB]
1,522 kB を 6秒 で取得しました (269 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
以前に未選択のパッケージ libssl-dev:arm64 を選択しています。
(データベースを読み込んでいます ... 現在 178939 個のファイルとディレクトリがインストールされています。)
.../libssl-dev_1.1.1-1ubuntu2.1~18.04.20_arm64.deb を展開する準備をしています ...
libssl-dev:arm64 (1.1.1-1ubuntu2.1~18.04.20) を展開しています...
以前に未選択のパッケージ libffi-dev:arm64 を選択しています。
.../libffi-dev_3.2.1-8_arm64.deb を展開する準備をしています ...
libffi-dev:arm64 (3.2.1-8) を展開しています...
libssl-dev:arm64 (1.1.1-1ubuntu2.1~18.04.20) を設定しています ...
libffi-dev:arm64 (3.2.1-8) を設定しています ...
install-info (6.5.0.dfsg.1-2) のトリガを処理しています ...
man-db (2.8.3-2ubuntu0.1) のトリガを処理しています ...
```




```bash
sudo pip3 install docker-compose
```


```bash
maki@maki-jetson2:~/Documents/001_morter$ sudo pip3 install docker-compose
The directory '/home/maki/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/maki/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting docker-compose
  Downloading https://files.pythonhosted.org/packages/f3/3e/ca05e486d44e38eb495ca60b8ca526b192071717387346ed1031ecf78966/docker_compose-1.29.2-py2.py3-none-any.whl (114kB)
    100% |████████████████████████████████| 122kB 2.6MB/s 
Collecting docopt<1,>=0.6.1 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz
Collecting dockerpty<1,>=0.4.1 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/8d/ee/e9ecce4c32204a6738e0a5d5883d3413794d7498fe8b06f44becc028d3ba/dockerpty-0.4.1.tar.gz
Collecting texttable<2,>=0.9.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/ba/a7/2c12b543f853dae886286b824200eb9d7cd2466e3d14eff1799fbe8223b9/texttable-1.6.7-py2.py3-none-any.whl
Collecting websocket-client<1,>=0.32.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/f7/0c/d52a2a63512a613817846d430d16a8fbe5ea56dd889e89c68facf6b91cb6/websocket_client-0.59.0-py2.py3-none-any.whl (67kB)
    100% |████████████████████████████████| 71kB 3.8MB/s 
Collecting cached-property<2,>=1.2.0; python_version < "3.8" (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/48/19/f2090f7dad41e225c7f2326e4cfe6fff49e57dedb5b53636c9551f86b069/cached_property-1.5.2-py2.py3-none-any.whl
Collecting docker[ssh]>=5 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/54/f3/7af47ead249fbb798d64a0438bad5c26f17ef6ac5cd324d802038eb10d90/docker-5.0.3-py2.py3-none-any.whl (146kB)
    100% |████████████████████████████████| 153kB 2.7MB/s 
Collecting jsonschema<4,>=2.5.1 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/c5/8f/51e89ce52a085483359217bc72cdbf6e75ee595d5b1d4b5ade40c7e018b8/jsonschema-3.2.0-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 3.8MB/s 
Collecting requests<3,>=2.20.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/2d/61/08076519c80041bc0ffa1a8af0cbd3bf3e2b62af10435d269a9d0f40564d/requests-2.27.1-py2.py3-none-any.whl (63kB)
    100% |████████████████████████████████| 71kB 4.0MB/s 
Requirement already satisfied: PyYAML<6,>=3.10 in /usr/lib/python3/dist-packages (from docker-compose)
Collecting distro<2,>=1.5.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/f4/2c/c90a3adaf0ddb70afe193f5ebfb539612af57cffe677c3126be533df3098/distro-1.8.0-py3-none-any.whl
Collecting python-dotenv<1,>=0.13.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/30/5f/2e5c564bd86349fe6b82ca840f46acf6f4bb76d79ba9057fce3d3e008864/python_dotenv-0.20.0-py3-none-any.whl
Requirement already satisfied: six>=1.3.0 in /usr/lib/python3/dist-packages (from dockerpty<1,>=0.4.1->docker-compose)
Collecting paramiko>=2.4.2; extra == "ssh" (from docker[ssh]>=5->docker-compose)
  Downloading https://files.pythonhosted.org/packages/71/6d/95777fd66507106d2f8f81d005255c237187951644f85a5bd0baeec8a88f/paramiko-2.12.0-py2.py3-none-any.whl (213kB)
    100% |████████████████████████████████| 215kB 2.0MB/s 
Collecting importlib-metadata; python_version < "3.8" (from jsonschema<4,>=2.5.1->docker-compose)
  Downloading https://files.pythonhosted.org/packages/a0/a1/b153a0a4caf7a7e3f15c2cd56c7702e2cf3d89b1b359d1f1c5e59d68f4ce/importlib_metadata-4.8.3-py3-none-any.whl
Requirement already satisfied: setuptools in /usr/lib/python3/dist-packages (from jsonschema<4,>=2.5.1->docker-compose)
Collecting attrs>=17.4.0 (from jsonschema<4,>=2.5.1->docker-compose)
  Downloading https://files.pythonhosted.org/packages/f2/bc/d817287d1aa01878af07c19505fafd1165cd6a119e9d0821ca1d1c20312d/attrs-22.1.0-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 3.7MB/s 
Collecting pyrsistent>=0.14.0 (from jsonschema<4,>=2.5.1->docker-compose)
  Downloading https://files.pythonhosted.org/packages/f4/d7/0fa558c4fb00f15aabc6d42d365fcca7a15fcc1091cd0f5784a14f390b7f/pyrsistent-0.18.0.tar.gz (104kB)
    100% |████████████████████████████████| 112kB 3.6MB/s 
Collecting charset-normalizer~=2.0.0; python_version >= "3" (from requests<3,>=2.20.0->docker-compose)
  Downloading https://files.pythonhosted.org/packages/06/b3/24afc8868eba069a7f03650ac750a778862dc34941a4bebeb58706715726/charset_normalizer-2.0.12-py3-none-any.whl
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/lib/python3/dist-packages (from requests<3,>=2.20.0->docker-compose)
Requirement already satisfied: idna<4,>=2.5; python_version >= "3" in /usr/lib/python3/dist-packages (from requests<3,>=2.20.0->docker-compose)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests<3,>=2.20.0->docker-compose)
Requirement already satisfied: pynacl>=1.0.1 in /usr/lib/python3/dist-packages (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
Collecting bcrypt>=3.1.3 (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Downloading https://files.pythonhosted.org/packages/8c/ae/3af7d006aacf513975fd1948a6b4d6f8b4a307f8a244e1a3d3774b297aad/bcrypt-4.0.1.tar.gz
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-build-jm377z2e/bcrypt/setup.py", line 11, in <module>
        from setuptools_rust import RustExtension
    ModuleNotFoundError: No module named 'setuptools_rust'
    
            =============================DEBUG ASSISTANCE==========================
            If you are seeing an error here please try the following to
            successfully install bcrypt:
    
            Upgrade to the latest pip and try again. This will fix errors for most
            users. See: https://pip.pypa.io/en/stable/installing/#upgrading-pip
            =============================DEBUG ASSISTANCE==========================
    
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-jm377z2e/bcrypt/
```



```bash
sudo pip3 install setuptools_rust
```


```bash
maki@maki-jetson2:~/Documents/001_morter$ sudo pip3 install setuptools_rust
The directory '/home/maki/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/maki/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting setuptools_rust
  Downloading https://files.pythonhosted.org/packages/66/ca/66bdf8f326977098eff28c314c8f825bc28d6986944c590e40ad0f74c5f0/setuptools_rust-1.1.2-py3-none-any.whl
Collecting setuptools>=46.1 (from setuptools_rust)
  Downloading https://files.pythonhosted.org/packages/b0/3a/88b210db68e56854d0bcf4b38e165e03be377e13907746f825790f3df5bf/setuptools-59.6.0-py3-none-any.whl (952kB)
    100% |████████████████████████████████| 962kB 516kB/s 
Collecting typing-extensions>=3.7.4.3 (from setuptools_rust)
  Downloading https://files.pythonhosted.org/packages/45/6b/44f7f8f1e110027cf88956b59f2fad776cca7e1704396d043f89effd3a0e/typing_extensions-4.1.1-py3-none-any.whl
Collecting semantic-version<3,>=2.8.2 (from setuptools_rust)
  Downloading https://files.pythonhosted.org/packages/6a/23/8146aad7d88f4fcb3a6218f41a60f6c2d4e3a72de72da1825dc7c8f7877c/semantic_version-2.10.0-py2.py3-none-any.whl
Installing collected packages: setuptools, typing-extensions, semantic-version, setuptools-rust
  Found existing installation: setuptools 39.0.1
    Not uninstalling setuptools at /usr/lib/python3/dist-packages, outside environment /usr
Successfully installed semantic-version-2.10.0 setuptools-59.6.0 setuptools-rust-1.1.2 typing-extensions-4.1.1
```


```bash
sudo pip3 install docker-compose
```


```bash
maki@maki-jetson2:~/Documents/001_morter$ sudo pip3 install docker-compose
The directory '/home/maki/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/maki/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting docker-compose
  Downloading https://files.pythonhosted.org/packages/f3/3e/ca05e486d44e38eb495ca60b8ca526b192071717387346ed1031ecf78966/docker_compose-1.29.2-py2.py3-none-any.whl (114kB)
    100% |████████████████████████████████| 122kB 2.9MB/s 
Collecting jsonschema<4,>=2.5.1 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/c5/8f/51e89ce52a085483359217bc72cdbf6e75ee595d5b1d4b5ade40c7e018b8/jsonschema-3.2.0-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 3.7MB/s 
Collecting texttable<2,>=0.9.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/ba/a7/2c12b543f853dae886286b824200eb9d7cd2466e3d14eff1799fbe8223b9/texttable-1.6.7-py2.py3-none-any.whl
Collecting cached-property<2,>=1.2.0; python_version < "3.8" (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/48/19/f2090f7dad41e225c7f2326e4cfe6fff49e57dedb5b53636c9551f86b069/cached_property-1.5.2-py2.py3-none-any.whl
Collecting distro<2,>=1.5.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/f4/2c/c90a3adaf0ddb70afe193f5ebfb539612af57cffe677c3126be533df3098/distro-1.8.0-py3-none-any.whl
Collecting websocket-client<1,>=0.32.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/f7/0c/d52a2a63512a613817846d430d16a8fbe5ea56dd889e89c68facf6b91cb6/websocket_client-0.59.0-py2.py3-none-any.whl (67kB)
    100% |████████████████████████████████| 71kB 3.8MB/s 
Collecting requests<3,>=2.20.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/2d/61/08076519c80041bc0ffa1a8af0cbd3bf3e2b62af10435d269a9d0f40564d/requests-2.27.1-py2.py3-none-any.whl (63kB)
    100% |████████████████████████████████| 71kB 3.9MB/s 
Collecting docker[ssh]>=5 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/54/f3/7af47ead249fbb798d64a0438bad5c26f17ef6ac5cd324d802038eb10d90/docker-5.0.3-py2.py3-none-any.whl (146kB)
    100% |████████████████████████████████| 153kB 2.7MB/s 
Collecting dockerpty<1,>=0.4.1 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/8d/ee/e9ecce4c32204a6738e0a5d5883d3413794d7498fe8b06f44becc028d3ba/dockerpty-0.4.1.tar.gz
Requirement already satisfied: PyYAML<6,>=3.10 in /usr/lib/python3/dist-packages (from docker-compose)
Collecting python-dotenv<1,>=0.13.0 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/30/5f/2e5c564bd86349fe6b82ca840f46acf6f4bb76d79ba9057fce3d3e008864/python_dotenv-0.20.0-py3-none-any.whl
Collecting docopt<1,>=0.6.1 (from docker-compose)
  Downloading https://files.pythonhosted.org/packages/a2/55/8f8cab2afd404cf578136ef2cc5dfb50baa1761b68c9da1fb1e4eed343c9/docopt-0.6.2.tar.gz
Collecting pyrsistent>=0.14.0 (from jsonschema<4,>=2.5.1->docker-compose)
  Downloading https://files.pythonhosted.org/packages/f4/d7/0fa558c4fb00f15aabc6d42d365fcca7a15fcc1091cd0f5784a14f390b7f/pyrsistent-0.18.0.tar.gz (104kB)
    100% |████████████████████████████████| 112kB 3.4MB/s 
Collecting attrs>=17.4.0 (from jsonschema<4,>=2.5.1->docker-compose)
  Downloading https://files.pythonhosted.org/packages/f2/bc/d817287d1aa01878af07c19505fafd1165cd6a119e9d0821ca1d1c20312d/attrs-22.1.0-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 3.6MB/s 
Requirement already satisfied: setuptools in /usr/local/lib/python3.6/dist-packages (from jsonschema<4,>=2.5.1->docker-compose)
Requirement already satisfied: six>=1.11.0 in /usr/lib/python3/dist-packages (from jsonschema<4,>=2.5.1->docker-compose)
Collecting importlib-metadata; python_version < "3.8" (from jsonschema<4,>=2.5.1->docker-compose)
  Downloading https://files.pythonhosted.org/packages/a0/a1/b153a0a4caf7a7e3f15c2cd56c7702e2cf3d89b1b359d1f1c5e59d68f4ce/importlib_metadata-4.8.3-py3-none-any.whl
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/lib/python3/dist-packages (from requests<3,>=2.20.0->docker-compose)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests<3,>=2.20.0->docker-compose)
Requirement already satisfied: idna<4,>=2.5; python_version >= "3" in /usr/lib/python3/dist-packages (from requests<3,>=2.20.0->docker-compose)
Collecting charset-normalizer~=2.0.0; python_version >= "3" (from requests<3,>=2.20.0->docker-compose)
  Downloading https://files.pythonhosted.org/packages/06/b3/24afc8868eba069a7f03650ac750a778862dc34941a4bebeb58706715726/charset_normalizer-2.0.12-py3-none-any.whl
Collecting paramiko>=2.4.2; extra == "ssh" (from docker[ssh]>=5->docker-compose)
  Downloading https://files.pythonhosted.org/packages/71/6d/95777fd66507106d2f8f81d005255c237187951644f85a5bd0baeec8a88f/paramiko-2.12.0-py2.py3-none-any.whl (213kB)
    100% |████████████████████████████████| 215kB 946kB/s 
Requirement already satisfied: typing-extensions>=3.6.4; python_version < "3.8" in /usr/local/lib/python3.6/dist-packages (from importlib-metadata; python_version < "3.8"->jsonschema<4,>=2.5.1->docker-compose)
Collecting zipp>=0.5 (from importlib-metadata; python_version < "3.8"->jsonschema<4,>=2.5.1->docker-compose)
  Downloading https://files.pythonhosted.org/packages/bd/df/d4a4974a3e3957fd1c1fa3082366d7fff6e428ddb55f074bf64876f8e8ad/zipp-3.6.0-py3-none-any.whl
Collecting bcrypt>=3.1.3 (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Downloading https://files.pythonhosted.org/packages/8c/ae/3af7d006aacf513975fd1948a6b4d6f8b4a307f8a244e1a3d3774b297aad/bcrypt-4.0.1.tar.gz
Collecting cryptography>=2.5 (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Downloading https://files.pythonhosted.org/packages/e3/3f/41186b1f2fd86a542d399175f6b8e43f82cd4dfa51235a0b030a042b811a/cryptography-38.0.4.tar.gz (599kB)
    100% |████████████████████████████████| 604kB 774kB/s 
Requirement already satisfied: pynacl>=1.0.1 in /usr/lib/python3/dist-packages (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
Collecting cffi>=1.12 (from cryptography>=2.5->paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Downloading https://files.pythonhosted.org/packages/2b/a8/050ab4f0c3d4c1b8aaa805f70e26e84d0e27004907c5b8ecc1d31815f92a/cffi-1.15.1.tar.gz (508kB)
    100% |████████████████████████████████| 512kB 907kB/s 
Collecting pycparser (from cffi>=1.12->cryptography>=2.5->paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Downloading https://files.pythonhosted.org/packages/62/d5/5f610ebe421e85889f2e55e33b7f9a6795bd982198517d912eb1c76e1a53/pycparser-2.21-py2.py3-none-any.whl (118kB)
    100% |████████████████████████████████| 122kB 3.1MB/s 
Installing collected packages: pyrsistent, attrs, zipp, importlib-metadata, jsonschema, texttable, cached-property, distro, websocket-client, charset-normalizer, requests, bcrypt, pycparser, cffi, cryptography, paramiko, docker, dockerpty, python-dotenv, docopt, docker-compose
  Running setup.py install for pyrsistent ... done
  Found existing installation: requests 2.18.4
    Not uninstalling requests at /usr/lib/python3/dist-packages, outside environment /usr
  Running setup.py install for bcrypt ... error
    Complete output from command /usr/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-avgevi50/bcrypt/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-s841z_l0-record/install-record.txt --single-version-externally-managed --compile:
    running install
    /usr/local/lib/python3.6/dist-packages/setuptools/command/install.py:37: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
      setuptools.SetuptoolsDeprecationWarning,
    running build
    running build_py
    creating build
    creating build/lib.linux-aarch64-3.6
    creating build/lib.linux-aarch64-3.6/bcrypt
    copying src/bcrypt/__init__.py -> build/lib.linux-aarch64-3.6/bcrypt
    copying src/bcrypt/__about__.py -> build/lib.linux-aarch64-3.6/bcrypt
    running egg_info
    writing src/bcrypt.egg-info/PKG-INFO
    writing dependency_links to src/bcrypt.egg-info/dependency_links.txt
    writing requirements to src/bcrypt.egg-info/requires.txt
    writing top-level names to src/bcrypt.egg-info/top_level.txt
    reading manifest file 'src/bcrypt.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no previously-included files found matching 'requirements.txt'
    warning: no previously-included files found matching 'release.py'
    warning: no previously-included files found matching 'mypy.ini'
    warning: no previously-included files matching '*' found under directory '.github'
    warning: no previously-included files matching '*' found under directory '.circleci'
    warning: no previously-included files found matching 'src/_bcrypt/target'
    warning: no previously-included files matching '*' found under directory 'src/_bcrypt/target'
    adding license file 'LICENSE'
    writing manifest file 'src/bcrypt.egg-info/SOURCES.txt'
    copying src/bcrypt/_bcrypt.pyi -> build/lib.linux-aarch64-3.6/bcrypt
    copying src/bcrypt/py.typed -> build/lib.linux-aarch64-3.6/bcrypt
    running build_ext
    running build_rust
    
        =============================DEBUG ASSISTANCE=============================
        If you are seeing a compilation error please try the following steps to
        successfully install bcrypt:
        1) Upgrade to the latest pip and try again. This will fix errors for most
           users. See: https://pip.pypa.io/en/stable/installing/#upgrading-pip
        2) Ensure you have a recent Rust toolchain installed. bcrypt requires
           rustc >= 1.56.0.
    
        Python: 3.6.9
        platform: Linux-4.9.201-tegra-aarch64-with-Ubuntu-18.04-bionic
        pip: 9.0.1
        setuptools: 59.6.0
        setuptools_rust: 1.1.2
        rustc: n/a
        =============================DEBUG ASSISTANCE=============================
    
    error: can't find Rust compiler
    
    If you are using an outdated pip version, it is possible a prebuilt wheel is available for this package but pip is not able to install from it. Installing from the wheel would avoid the need for a Rust compiler.
    
    To update pip, run:
    
        pip install --upgrade pip
    
    and then retry package installation.
    
    If you did intend to build this package from source, try installing a Rust compiler from your system package manager and ensure it is on the PATH during installation. Alternatively, rustup (available at https://rustup.rs) is the recommended way to download and update the Rust compiler toolchain.
    
    This package requires Rust >=1.56.0.
    
    ----------------------------------------
Command "/usr/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-avgevi50/bcrypt/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /tmp/pip-s841z_l0-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-build-avgevi50/bcrypt/
```


```bash
pip install --upgrade pip
```

```bash
maki@maki-jetson2:~/Documents/001_morter$ pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/27/79/8a850fe3496446ff0d584327ae44e7500daf6764ca1a382d2d02789accf7/pip-20.3.4-py2.py3-none-any.whl (1.5MB)
    100% |████████████████████████████████| 1.5MB 294kB/s 
Installing collected packages: pip
Successfully installed pip-20.3.4
```


```bash
pip install --upgrade pip
```



```bash
maki@maki-jetson2:~/Documents/001_morter$ sudo apt-get install build-essential libssl-dev libffi-dev \
>     python3-dev cargo
[sudo] password for maki: 
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
build-essential はすでに最新バージョン (12.4ubuntu1) です。
libffi-dev はすでに最新バージョン (3.2.1-8) です。
libssl-dev はすでに最新バージョン (1.1.1-1ubuntu2.1~18.04.20) です。
python3-dev はすでに最新バージョン (3.6.7-1~18.04) です。
以下の追加パッケージがインストールされます:
  libstd-rust-1.61 libstd-rust-dev rustc
提案パッケージ:
  cargo-doc llvm-14 lld-14 clang-14
以下のパッケージが新たにインストールされます:
  cargo libstd-rust-1.61 libstd-rust-dev rustc
アップグレード: 0 個、新規インストール: 4 個、削除: 0 個、保留: 154 個。
74.6 MB のアーカイブを取得する必要があります。
この操作後に追加で 348 MB のディスク容量が消費されます。
続行しますか? [Y/n] Y
取得:1 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 libstd-rust-1.61 arm64 1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1 [33.9 MB]
取得:2 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 libstd-rust-dev arm64 1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1 [34.7 MB]                                                                                                                                       
取得:3 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 rustc arm64 1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1 [2,923 kB]                                                                                                                                                
取得:4 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 cargo arm64 0.62.0ubuntu0libgit2-0ubuntu0.18.04.1 [3,094 kB]                                                                                                                                                  
74.6 MB を 14秒 で取得しました (5,521 kB/s)                                                                                                                                                                                                                                             
debconf: delaying package configuration, since apt-utils is not installed
以前に未選択のパッケージ libstd-rust-1.61:arm64 を選択しています。
(データベースを読み込んでいます ... 現在 179091 個のファイルとディレクトリがインストールされています。)
.../libstd-rust-1.61_1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
libstd-rust-1.61:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を展開しています...
以前に未選択のパッケージ libstd-rust-dev:arm64 を選択しています。
.../libstd-rust-dev_1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
libstd-rust-dev:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を展開しています...
以前に未選択のパッケージ rustc を選択しています。
.../rustc_1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
rustc (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を展開しています...
以前に未選択のパッケージ cargo を選択しています。
.../cargo_0.62.0ubuntu0libgit2-0ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
cargo (0.62.0ubuntu0libgit2-0ubuntu0.18.04.1) を展開しています...
libstd-rust-1.61:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を設定しています ...
libstd-rust-dev:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を設定しています ...
rustc (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を設定しています ...
cargo (0.62.0ubuntu0libgit2-0ubuntu0.18.04.1) を設定しています ...
libc-bin (2.27-3ubuntu1.6) のトリガを処理しています ...
man-db (2.8.3-2ubuntu0.1) のトリガを処理しています ...
maki@maki-jetson2:~/Documents/001_morter$
```


```bash
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev cargo
```



```bash
maki@maki-jetson2:~/Documents/001_morter$ sudo apt-get install build-essential libssl-dev libffi-dev \
>     python3-dev cargo
[sudo] password for maki: 
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
build-essential はすでに最新バージョン (12.4ubuntu1) です。
libffi-dev はすでに最新バージョン (3.2.1-8) です。
libssl-dev はすでに最新バージョン (1.1.1-1ubuntu2.1~18.04.20) です。
python3-dev はすでに最新バージョン (3.6.7-1~18.04) です。
以下の追加パッケージがインストールされます:
  libstd-rust-1.61 libstd-rust-dev rustc
提案パッケージ:
  cargo-doc llvm-14 lld-14 clang-14
以下のパッケージが新たにインストールされます:
  cargo libstd-rust-1.61 libstd-rust-dev rustc
アップグレード: 0 個、新規インストール: 4 個、削除: 0 個、保留: 154 個。
74.6 MB のアーカイブを取得する必要があります。
この操作後に追加で 348 MB のディスク容量が消費されます。
続行しますか? [Y/n] Y
取得:1 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 libstd-rust-1.61 arm64 1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1 [33.9 MB]
取得:2 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 libstd-rust-dev arm64 1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1 [34.7 MB]                                                                                                                                       
取得:3 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 rustc arm64 1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1 [2,923 kB]                                                                                                                                                
取得:4 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe arm64 cargo arm64 0.62.0ubuntu0libgit2-0ubuntu0.18.04.1 [3,094 kB]                                                                                                                                                  
74.6 MB を 14秒 で取得しました (5,521 kB/s)                                                                                                                                                                                                                                             
debconf: delaying package configuration, since apt-utils is not installed
以前に未選択のパッケージ libstd-rust-1.61:arm64 を選択しています。
(データベースを読み込んでいます ... 現在 179091 個のファイルとディレクトリがインストールされています。)
.../libstd-rust-1.61_1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
libstd-rust-1.61:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を展開しています...
以前に未選択のパッケージ libstd-rust-dev:arm64 を選択しています。
.../libstd-rust-dev_1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
libstd-rust-dev:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を展開しています...
以前に未選択のパッケージ rustc を選択しています。
.../rustc_1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
rustc (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を展開しています...
以前に未選択のパッケージ cargo を選択しています。
.../cargo_0.62.0ubuntu0libgit2-0ubuntu0.18.04.1_arm64.deb を展開する準備をしています ...
cargo (0.62.0ubuntu0libgit2-0ubuntu0.18.04.1) を展開しています...
libstd-rust-1.61:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を設定しています ...
libstd-rust-dev:arm64 (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を設定しています ...
rustc (1.61.0+dfsg1~llvm-1~exp1ubuntu0.18.04.1) を設定しています ...
cargo (0.62.0ubuntu0libgit2-0ubuntu0.18.04.1) を設定しています ...
libc-bin (2.27-3ubuntu1.6) のトリガを処理しています ...
man-db (2.8.3-2ubuntu0.1) のトリガを処理しています ...
maki@maki-jetson2:~/Documents/001_morter$ 
```


```bash
pip3 install setuptools_rust docker-compose
```



```bash
maki@maki-jetson2:~/Documents/001_morter$ pip3 install setuptools_rust docker-compose
Collecting setuptools_rust
  Using cached https://files.pythonhosted.org/packages/66/ca/66bdf8f326977098eff28c314c8f825bc28d6986944c590e40ad0f74c5f0/setuptools_rust-1.1.2-py3-none-any.whl
Collecting docker-compose
  Using cached https://files.pythonhosted.org/packages/f3/3e/ca05e486d44e38eb495ca60b8ca526b192071717387346ed1031ecf78966/docker_compose-1.29.2-py2.py3-none-any.whl
Collecting setuptools>=46.1 (from setuptools_rust)
  Using cached https://files.pythonhosted.org/packages/b0/3a/88b210db68e56854d0bcf4b38e165e03be377e13907746f825790f3df5bf/setuptools-59.6.0-py3-none-any.whl
Collecting semantic-version<3,>=2.8.2 (from setuptools_rust)
  Using cached https://files.pythonhosted.org/packages/6a/23/8146aad7d88f4fcb3a6218f41a60f6c2d4e3a72de72da1825dc7c8f7877c/semantic_version-2.10.0-py2.py3-none-any.whl
Collecting typing-extensions>=3.7.4.3 (from setuptools_rust)
  Using cached https://files.pythonhosted.org/packages/45/6b/44f7f8f1e110027cf88956b59f2fad776cca7e1704396d043f89effd3a0e/typing_extensions-4.1.1-py3-none-any.whl
Collecting python-dotenv<1,>=0.13.0 (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/30/5f/2e5c564bd86349fe6b82ca840f46acf6f4bb76d79ba9057fce3d3e008864/python_dotenv-0.20.0-py3-none-any.whl
Collecting websocket-client<1,>=0.32.0 (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/f7/0c/d52a2a63512a613817846d430d16a8fbe5ea56dd889e89c68facf6b91cb6/websocket_client-0.59.0-py2.py3-none-any.whl
Collecting PyYAML<6,>=3.10 (from docker-compose)
Collecting docker[ssh]>=5 (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/54/f3/7af47ead249fbb798d64a0438bad5c26f17ef6ac5cd324d802038eb10d90/docker-5.0.3-py2.py3-none-any.whl
Collecting docopt<1,>=0.6.1 (from docker-compose)
Collecting distro<2,>=1.5.0 (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/f4/2c/c90a3adaf0ddb70afe193f5ebfb539612af57cffe677c3126be533df3098/distro-1.8.0-py3-none-any.whl
Collecting requests<3,>=2.20.0 (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/2d/61/08076519c80041bc0ffa1a8af0cbd3bf3e2b62af10435d269a9d0f40564d/requests-2.27.1-py2.py3-none-any.whl
Collecting texttable<2,>=0.9.0 (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/ba/a7/2c12b543f853dae886286b824200eb9d7cd2466e3d14eff1799fbe8223b9/texttable-1.6.7-py2.py3-none-any.whl
Collecting cached-property<2,>=1.2.0; python_version < "3.8" (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/48/19/f2090f7dad41e225c7f2326e4cfe6fff49e57dedb5b53636c9551f86b069/cached_property-1.5.2-py2.py3-none-any.whl
Collecting dockerpty<1,>=0.4.1 (from docker-compose)
Collecting jsonschema<4,>=2.5.1 (from docker-compose)
  Using cached https://files.pythonhosted.org/packages/c5/8f/51e89ce52a085483359217bc72cdbf6e75ee595d5b1d4b5ade40c7e018b8/jsonschema-3.2.0-py2.py3-none-any.whl
Collecting six (from websocket-client<1,>=0.32.0->docker-compose)
  Using cached https://files.pythonhosted.org/packages/d9/5a/e7c31adbe875f2abbb91bd84cf2dc52d792b5a01506781dbcf25c91daf11/six-1.16.0-py2.py3-none-any.whl
Collecting paramiko>=2.4.2; extra == "ssh" (from docker[ssh]>=5->docker-compose)
  Using cached https://files.pythonhosted.org/packages/71/6d/95777fd66507106d2f8f81d005255c237187951644f85a5bd0baeec8a88f/paramiko-2.12.0-py2.py3-none-any.whl
Collecting urllib3<1.27,>=1.21.1 (from requests<3,>=2.20.0->docker-compose)
  Using cached https://files.pythonhosted.org/packages/65/0c/cc6644eaa594585e5875f46f3c83ee8762b647b51fc5b0fb253a242df2dc/urllib3-1.26.13-py2.py3-none-any.whl
Collecting certifi>=2017.4.17 (from requests<3,>=2.20.0->docker-compose)
  Using cached https://files.pythonhosted.org/packages/71/4c/3db2b8021bd6f2f0ceb0e088d6b2d49147671f25832fb17970e9b583d742/certifi-2022.12.7-py3-none-any.whl
Collecting idna<4,>=2.5; python_version >= "3" (from requests<3,>=2.20.0->docker-compose)
  Using cached https://files.pythonhosted.org/packages/fc/34/3030de6f1370931b9dbb4dad48f6ab1015ab1d32447850b9fc94e60097be/idna-3.4-py3-none-any.whl
Collecting charset-normalizer~=2.0.0; python_version >= "3" (from requests<3,>=2.20.0->docker-compose)
  Using cached https://files.pythonhosted.org/packages/06/b3/24afc8868eba069a7f03650ac750a778862dc34941a4bebeb58706715726/charset_normalizer-2.0.12-py3-none-any.whl
Collecting importlib-metadata; python_version < "3.8" (from jsonschema<4,>=2.5.1->docker-compose)
  Using cached https://files.pythonhosted.org/packages/a0/a1/b153a0a4caf7a7e3f15c2cd56c7702e2cf3d89b1b359d1f1c5e59d68f4ce/importlib_metadata-4.8.3-py3-none-any.whl
Collecting attrs>=17.4.0 (from jsonschema<4,>=2.5.1->docker-compose)
  Using cached https://files.pythonhosted.org/packages/f2/bc/d817287d1aa01878af07c19505fafd1165cd6a119e9d0821ca1d1c20312d/attrs-22.1.0-py2.py3-none-any.whl
Collecting pyrsistent>=0.14.0 (from jsonschema<4,>=2.5.1->docker-compose)
Collecting cryptography>=2.5 (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Using cached https://files.pythonhosted.org/packages/e3/3f/41186b1f2fd86a542d399175f6b8e43f82cd4dfa51235a0b030a042b811a/cryptography-38.0.4.tar.gz
Collecting pynacl>=1.0.1 (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
Collecting bcrypt>=3.1.3 (from paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Using cached https://files.pythonhosted.org/packages/8c/ae/3af7d006aacf513975fd1948a6b4d6f8b4a307f8a244e1a3d3774b297aad/bcrypt-4.0.1.tar.gz
Collecting zipp>=0.5 (from importlib-metadata; python_version < "3.8"->jsonschema<4,>=2.5.1->docker-compose)
  Using cached https://files.pythonhosted.org/packages/bd/df/d4a4974a3e3957fd1c1fa3082366d7fff6e428ddb55f074bf64876f8e8ad/zipp-3.6.0-py3-none-any.whl
Collecting cffi>=1.12 (from cryptography>=2.5->paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
Collecting pycparser (from cffi>=1.12->cryptography>=2.5->paramiko>=2.4.2; extra == "ssh"->docker[ssh]>=5->docker-compose)
  Using cached https://files.pythonhosted.org/packages/62/d5/5f610ebe421e85889f2e55e33b7f9a6795bd982198517d912eb1c76e1a53/pycparser-2.21-py2.py3-none-any.whl
Building wheels for collected packages: cryptography, bcrypt
  Running setup.py bdist_wheel for cryptography ... done
  Stored in directory: /home/maki/.cache/pip/wheels/9d/92/b2/d359109d80f70fc04aff9a90be3f74f6521e3f052d239381bb
  Running setup.py bdist_wheel for bcrypt ... done
  Stored in directory: /home/maki/.cache/pip/wheels/b6/eb/44/28e787e0128ff2c6713a954c6f7254a565d620113a4de807ba
Successfully built cryptography bcrypt
Installing collected packages: setuptools, semantic-version, typing-extensions, setuptools-rust, python-dotenv, six, websocket-client, PyYAML, urllib3, certifi, idna, charset-normalizer, requests, pycparser, cffi, cryptography, pynacl, bcrypt, paramiko, docker, docopt, distro, texttable, cached-property, dockerpty, zipp, importlib-metadata, attrs, pyrsistent, jsonschema, docker-compose
Successfully installed PyYAML-5.4.1 attrs-22.1.0 bcrypt-4.0.1 cached-property-1.5.2 certifi-2022.12.7 cffi-1.15.1 charset-normalizer-2.0.12 cryptography-38.0.4 distro-1.8.0 docker-5.0.3 docker-compose-1.29.2 dockerpty-0.4.1 docopt-0.6.2 idna-3.4 importlib-metadata-4.8.3 jsonschema-3.2.0 paramiko-2.12.0 pycparser-2.21 pynacl-1.5.0 pyrsistent-0.18.0 python-dotenv-0.20.0 requests-2.27.1 semantic-version-2.10.0 setuptools-59.6.0 setuptools-rust-1.1.2 six-1.16.0 texttable-1.6.7 typing-extensions-4.1.1 urllib3-1.26.13 websocket-client-0.59.0 zipp-3.6.0
maki@maki-jetson2:~/Documents/001_morter$ 
```



```bash
maki@maki-jetson2:~/Documents/001_morter$ docker-compose ps
bash: docker-compose: command not found
```

```bash
pip3 show --files docker-compose
```

```bash
maki@maki-jetson2:~/Documents/001_morter$ pip3 show --files docker-compose
Name: docker-compose
Version: 1.29.2
Summary: Multi-container orchestration for Docker
Home-page: https://www.docker.com/
Author: Docker, Inc.
Author-email: None
License: Apache License 2.0
Location: /home/maki/.local/lib/python3.6/site-packages
Requires: distro, jsonschema, docker, PyYAML, cached-property, websocket-client, docopt, requests, python-dotenv, texttable, dockerpty
Files:
  ../../../bin/docker-compose
  compose/__init__.py
  compose/__main__.py
  compose/__pycache__/__init__.cpython-36.pyc
  compose/__pycache__/__main__.cpython-36.pyc
  compose/__pycache__/const.cpython-36.pyc
  compose/__pycache__/container.cpython-36.pyc
  compose/__pycache__/errors.cpython-36.pyc
  compose/__pycache__/network.cpython-36.pyc
  compose/__pycache__/parallel.cpython-36.pyc
  compose/__pycache__/progress_stream.cpython-36.pyc
  compose/__pycache__/project.cpython-36.pyc
  compose/__pycache__/service.cpython-36.pyc
  compose/__pycache__/timeparse.cpython-36.pyc
  compose/__pycache__/utils.cpython-36.pyc
  compose/__pycache__/version.cpython-36.pyc
  compose/__pycache__/volume.cpython-36.pyc
  compose/cli/__init__.py
  compose/cli/__pycache__/__init__.cpython-36.pyc
  compose/cli/__pycache__/colors.cpython-36.pyc
  compose/cli/__pycache__/command.cpython-36.pyc
  compose/cli/__pycache__/docker_client.cpython-36.pyc
  compose/cli/__pycache__/docopt_command.cpython-36.pyc
  compose/cli/__pycache__/errors.cpython-36.pyc
  compose/cli/__pycache__/formatter.cpython-36.pyc
  compose/cli/__pycache__/log_printer.cpython-36.pyc
  compose/cli/__pycache__/main.cpython-36.pyc
  compose/cli/__pycache__/signals.cpython-36.pyc
  compose/cli/__pycache__/utils.cpython-36.pyc
  compose/cli/__pycache__/verbose_proxy.cpython-36.pyc
  compose/cli/colors.py
  compose/cli/command.py
  compose/cli/docker_client.py
  compose/cli/docopt_command.py
  compose/cli/errors.py
  compose/cli/formatter.py
  compose/cli/log_printer.py
  compose/cli/main.py
  compose/cli/signals.py
  compose/cli/utils.py
  compose/cli/verbose_proxy.py
  compose/config/__init__.py
  compose/config/__pycache__/__init__.cpython-36.pyc
  compose/config/__pycache__/config.cpython-36.pyc
  compose/config/__pycache__/environment.cpython-36.pyc
  compose/config/__pycache__/errors.cpython-36.pyc
  compose/config/__pycache__/interpolation.cpython-36.pyc
  compose/config/__pycache__/serialize.cpython-36.pyc
  compose/config/__pycache__/sort_services.cpython-36.pyc
  compose/config/__pycache__/types.cpython-36.pyc
  compose/config/__pycache__/validation.cpython-36.pyc
  compose/config/compose_spec.json
  compose/config/config.py
  compose/config/config_schema_v1.json
  compose/config/environment.py
  compose/config/errors.py
  compose/config/interpolation.py
  compose/config/serialize.py
  compose/config/sort_services.py
  compose/config/types.py
  compose/config/validation.py
  compose/const.py
  compose/container.py
  compose/errors.py
  compose/metrics/__init__.py
  compose/metrics/__pycache__/__init__.cpython-36.pyc
  compose/metrics/__pycache__/client.cpython-36.pyc
  compose/metrics/__pycache__/decorator.cpython-36.pyc
  compose/metrics/client.py
  compose/metrics/decorator.py
  compose/network.py
  compose/parallel.py
  compose/progress_stream.py
  compose/project.py
  compose/service.py
  compose/timeparse.py
  compose/utils.py
  compose/version.py
  compose/volume.py
  docker_compose-1.29.2.dist-info/INSTALLER
  docker_compose-1.29.2.dist-info/LICENSE
  docker_compose-1.29.2.dist-info/METADATA
  docker_compose-1.29.2.dist-info/RECORD
  docker_compose-1.29.2.dist-info/WHEEL
  docker_compose-1.29.2.dist-info/entry_points.txt
  docker_compose-1.29.2.dist-info/top_level.txt
```



```bash
/home/maki/.local/bin/docker-compose 
```

```bash
maki@maki-jetson2:/$ /home/maki/.local/bin/docker-compose -v
/home/maki/.local/lib/python3.6/site-packages/paramiko/transport.py:33: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography and will be removed in a future release.
  from cryptography.hazmat.backends import default_backend
docker-compose version 1.29.2, build unknown
```

```bash
sudo ln -s /home/maki/.local/bin/docker-compose /usr/bin/docker-compose
```

```bash
 docker-compose -v
```

```bash
maki@maki-jetson2:/$ docker-compose -v
/home/maki/.local/lib/python3.6/site-packages/paramiko/transport.py:33: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography and will be removed in a future release.
  from cryptography.hazmat.backends import default_backend
docker-compose version 1.29.2, build unknown
```

```bash
++++++++++++++++++++++++++++
```

```bash
++++++++++++++++++++++++++++
```



https://qiita.com/ntrlmt/items/c001f0f98da426715cbd

https://k-kuro.hatenadiary.jp/entry/20211215/1639547966

https://github.com/docker/compose/issues/9834

https://github.com/docker/compose/issues/8105

https://github.com/pyca/cryptography/blob/main/docs/installation.rst

https://stackoverflow.com/questions/38775954/sudo-docker-compose-command-not-found

https://qiita.com/mtsiga/items/f90a3b8edd3ab58de376



sudo apt install python3-pip
pip install --upgrade pip
sudo apt install build-essential libssl-dev libffi-dev python3-dev  cargo
pip3 install setuptools_rust docker-compose


sudo ln -s /home/maki/.local/bin/docker-compose /usr/bin/docker-compose

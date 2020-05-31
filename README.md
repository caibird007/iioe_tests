## 简介
IIOE的接口case，使用httprunner框架编写

### 环境依赖  

- python3  
- pip3  
- 可以访问外网  

### 安装python依赖

```
pip3 install -r requirements.txt
```

### 检查是否安装成功

```
hrun -v
```

### 目录说明
```
├── api //这里对应了fiddler从页面抓取的api
│   ├── admin
│   ├── h5
│   └── web
├── debugtalk.py
├── logs //日志目录
│   └── testcases
├── README.md
├── reports
│   ├── 20200531T132749.718908.html
├── requirements.txt 
├── testcases //测试case
│   ├── admin
│   ├── h5
│   └── web
└── testsuites //测试suites
    └── iioe_testsuite.yml

```

### 运行方式
```
hrun testsuites/iioe_testsuite.yml
```

### 查看报告
report下面
例子：http://139.198.11.74:8000/20200531T132749.718908.html



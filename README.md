# crowdin-desktop

## 开发

首先按照 [pdm](https://pdm-project.org/latest/)

一般情况下直接使用pip或者pipx安装即可：

```bash
pip install pdm
```

接着下载仓库，拉取依赖。

```bash
pdm install
pdm dev # 开发时执行
pdm pack # 使用 Pyinstaller 打包
pdm build # 构建项目
```

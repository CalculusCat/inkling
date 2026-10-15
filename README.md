# Inkling

轻量的 Windows 笔记 / 日记软件（Neutralino + WebView2，压缩包约 1.2MB）。
PIN 锁、标签、日记模式（自动日期与天气）、深色模式、自动备份。

## 下载
到本仓库 **Releases** 页面下载 `Inkling-win_x64.zip`，解压后双击 `Inkling.exe`。
`Inkling.exe` 与 `resources.neu` 必须在同一文件夹。需要 Windows 10/11（WebView2，Win11 自带）。

## 自己构建
推送标签即可由 GitHub Actions 自动构建并发布：
```
git tag v1.0.0 && git push origin v1.0.0
```
本地构建：`npm i -g @neutralinojs/neu && neu update && neu build`，再用 `node tools/patch-exe.js` 写入图标。

## 说明
- 数据：`%APPDATA%\Inkling\db.json`；备份：`文档\Inkling-Backup`
- PIN 仅用于进入软件，笔记内容未加密
- 未签名，首次运行 SmartScreen 点「更多信息 → 仍要运行」

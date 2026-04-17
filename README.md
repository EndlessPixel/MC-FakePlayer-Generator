# MC-FakePlayer-Generator
Minecraft 假人批量生成脚本

## 介绍
用于 [minecraft-fakeplayer](https://github.com/tanyaofei/minecraft-fakeplayer) 插件的批量指令生成工具，
可快速生成大量 `/fp spawn` 指令，用于服务器压测。

## 功能
- 批量生成随机名称假人指令
- 名称长度随机（3-15位）
- 支持字母、数字、下划线组合
- 生成**可直接粘贴到服务器控制台**的完整命令
- 自动保存到带时间戳的文件

## ⚠️ 重要使用说明（必须看）
本工具生成的命令**仅适用于 Minecraft 服务器控制台**，**不适用于客户端**！

- 客户端无法批量粘贴多行命令
- 请**全选文本内容 → 一次性粘贴到服务器后台控制台**执行
- 粘贴后会自动批量创建假人

## 使用方法
1. 运行脚本：
```bash
python main.py
```
2. 输入数量 → 生成命令文件 → 全选复制 → 粘贴到服务器控制台。

## 适用场景
 - Minecraft 服务器压力测试
 - 批量生成假人
 - 配合 minecraft-fakeplayer 插件使用

## 依赖项目
- 原插件仓库：[https://github.com/tanyaofei/minecraft-fakeplayer](https://github.com/tanyaofei/minecraft-fakeplayer)


---
title: 'Python 3.10.0rc2 发布，下月推出正式版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3552'
author: 开源中国
comments: false
date: Fri, 10 Sep 2021 07:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3552'
---

<div>   
<div class="content">
                                                                                            <p>Python 3.10.0rc2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpythoninsider.blogspot.com%2F2021%2F09%2Fpython-3100rc2-is-available.html" target="_blank">已发布</a>。发布公告显示，这是 Python 3.10.0 最终版本于 2021 年 10 月 4 日发布之前的最后一个 RC 版。RC 版本和最终版本之间的区别是针对明确错误的修复，所以从现在开始，不会再出现 ABI 方面的变更，目标是尽可能少地更改代码。</p> 
<p>另外，虽然此版本已接近正式版，但毕竟还是处于预览阶段，因此不建议在生产环境使用它。</p> 
<p>获取新版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3100rc2%2F" target="_blank">https://www.python.org/downloads/release/python-3100rc2/</a></p> 
<div> 
 <p style="box-sizing: inherit; margin: 0px 0px 20px; line-height: inherit; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>与 3.9 相比，3.10 系列的主要新功能</strong></p> 
 <ul style="box-sizing: inherit; margin: 0px 0px 20px; list-style-type: disc; color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-top: 0px;">PEP 623 – 弃用并准备删除 PyUnicodeObject 中的 wstr 成员</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 604 – 允许将联合类型写为 X | Y</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 612 – 参数规范变量</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 626 – 用于调试和其他工具的精确行号</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 618 – zip 添加可选的长度检查</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">bpo-12782：现在正式允许带括号的上下文管理器</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 632 - 弃用 distutils 模块</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 613 – 显式类型别名</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 634 – 结构模式匹配：规范</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 635 – 结构模式匹配：动机和基本原理</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 636 – 结构模式匹配：教程</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 644 – 需要 OpenSSL 1.1.1 或更新版本</li> 
  <li style="box-sizing: inherit; line-height: 1.875em;">PEP 624 - 删除 Py_UNICODE 编码器 API</li> 
  <li style="box-sizing: inherit; line-height: 1.875em; margin-bottom: 0px;">PEP 597 – 添加可选的 EncodingWarning</li> 
 </ul> 
 <div>
  <span style="color: rgb(51, 51, 51); font-family: -apple-system, BlinkMacSystemFont, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;">此外，bpo-38605：from __future__ import annotations (PEP 563) 曾经在之前的预发布版本中出现，但由于某些兼容性问题，它已被推迟到 Python 3.11，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmail.python.org%2Farchives%2Flist%2Fpython-dev%40python.org%2Fthread%2FCLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ%2F" target="_blank">详情访问此链接</a>。</span>
 </div> 
</div>
                                        </div>
                                      
</div>
            
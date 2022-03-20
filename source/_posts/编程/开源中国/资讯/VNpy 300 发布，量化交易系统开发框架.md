
---
title: 'VN.py 3.0.0 发布，量化交易系统开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5077'
author: 开源中国
comments: false
date: Sun, 20 Mar 2022 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5077'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#24292f">VN.py 是一套基于 Python 的开源量化交易系统开发框架，</span><span style="color:#333333">起源于国内私募的自主量化交易系统，目前已经成长为一套全功能的交易程序开发框架，</span><span style="color:#24292f">支持 </span>CTA 策略、算法交易、期权策略、行情录制等多种量化策略应用。</p> 
<p><strong>主要变更：</strong></p> 
<ol> 
 <li>官方支持版本升级到 3.10（保持 3.7、3.8、3.9 兼容性）</li> 
 <li>图形开发库升级替换为 PySide6（由于 API 兼容性问题，放弃 PyQt6）</li> 
 <li>移除 api、gateway、app 子模块的目录</li> 
 <li>移除 requirements.txt 对于插件的默认依赖</li> 
 <li>简化重构 rpc 子模块，定位于可靠环境下跨进程通讯（本机、局域网）</li> 
 <li>移除 rpc 子模块对于鉴权的支持</li> 
 <li>调整 rpc 子模块中的心跳机制的实现方式</li> 
 <li>移除基于 QScintilla 开发的代码编辑器，改用 VSCode 打开代码</li> 
 <li>优化 MainWindow 主窗口中，对于 QAction 按钮图标的加载逻辑</li> 
</ol> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvnpy%2Fvnpy%2Freleases%2Ftag%2F3.0.0" target="_blank">https://github.com/vnpy/vnpy/releases/tag/3.0.0</a></p>
                                        </div>
                                      
</div>
            
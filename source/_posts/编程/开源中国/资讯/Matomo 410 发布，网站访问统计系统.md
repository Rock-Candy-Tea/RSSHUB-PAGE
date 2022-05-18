
---
title: 'Matomo 4.10 发布，网站访问统计系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9784'
author: 开源中国
comments: false
date: Wed, 18 May 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9784'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Matomo 是一套基于 PHP + MySQL 技术构建的开源网站访问统计系统，能够提供详细的统计信息，比如网页浏览人数、访问最多的页面、搜索引擎关键词等等流量分析功能。</p> 
<p>Matomo 4.10 正式发布，这是一个维护版本，改善了 Matomo 的可靠性和稳定性，修复了几个 bug 并改进了用户界面。具体更新内容如下：</p> 
<h3>平台变化</h3> 
<p>在 4.10 版本中，有一个重要变化，以前的静态 json 文件不再被认为是安全的服务，现在生成的 htaccess 文件将排除它们。</p> 
<h3>其他</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F18884" target="_blank">#18884</a> Data protection: 如果配置文件被禁用，则在访问日志中隐藏访客 ID</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fpull%2F19157" target="_blank">#19157</a> 让 Widgetize 页面可以翻译</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F18947" target="_blank">#18947</a> 修复控制台命令，以禁用用户的 2FA</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F19125" target="_blank">#19125</a> 修复使用嵌入仪表盘的表格的小部件的 z-index 显示问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F18128" target="_blank">#18128</a> 使 JSON 配置/包的静态文件无法通过 GET 请求到达</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F18967" target="_blank">#18967</a> 系统检查 —— 禁用时不请求私有目录</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fpull%2F19118" target="_blank">#19118</a> 修复从命令行设置许可证密钥时的错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F19124" target="_blank">#19124</a> 修复在网站/可测量的目标不存在时添加新目标的错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F19127" target="_blank">#19127</a> 修复了引用插件中 PHP8.1 的兼容性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fpull%2F19088" target="_blank">#19088</a> 在编写报告时，如果缺少 assets 文件夹，则创建该文件夹</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fpull%2F19113" target="_blank">#19113</a> 为 PiwikGlobal 类型添加 languageName 属性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fpull%2F19156" target="_blank">#19156</a> 重命名 MenuDropdown 组件以避免任何情况下的不匹配</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmatomo.org%2Fchangelog%2Fmatomo-4-10-0%2F" target="_blank">https://matomo.org/changelog/matomo-4-10-0/</a></p>
                                        </div>
                                      
</div>
            
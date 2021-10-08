
---
title: 'Matomo 4.5.0 发布，完全兼容 IE11 的最后一个版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6879'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6879'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Matomo 4.5.0 发布了。Matomo 是一套基于 PHP + MySQL 技术构建的开源网站访问统计系统，能够提供详细的统计信息，比如网页浏览人数、访问最多的页面、搜索引擎关键词等等流量分析功能。</p> 
<p>该版本也是 Matomo 与 Internet Explorer 11 完全兼容的最后一个版本。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17870" target="_blank">#17870</a> 通过不写入已经存在的占位符文件来提高 I/O 性能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17732" target="_blank">#17732</a> 当有许多通知等待处理时，用户可以注销</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17872" target="_blank">#17872</a> 如果配置中没有启用周期，在 cron 归档中会显示 "不支持周期" 信息</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17926" target="_blank">#17926</a> 当调用 <code>rememberCookieConsentGiven</code> 时，产生控制台错误 “There was an error setting cookie <code>mtm_cookie_consent</code>. Please check domain and path”</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17965" target="_blank">#17965</a> 在 "获取" > "概览" 报告中，缺少 "行" 选择器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17091" target="_blank">#17091</a> SMTP连接失败可能导致密码恢复中的信息泄露</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17773" target="_blank">#17773</a> Matomo 应设置内容安全策略以防止一些 XSS</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fpull%2F18030" target="_blank">#18030</a> 移除对 mt_rand 的回退，并始终使用 random_int 来保证安全随机性</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F2672" target="_blank">#2672</a> 新增自定义图像的 INI 配置设置以替换默认的 1×1 GIF 图像</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F16576" target="_blank">#16576</a> 新的控制台命令 <code>config:delete</code> 来删除键</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F16859" target="_blank">#16859</a> 增加 JS 跟踪方法 <code>setPagePerformanceTiming</code> 和 <code>getCustomPagePerformanceTiming</code> 来设置性能指标的特定值</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17738" target="_blank">#17738</a> 使用不支持的浏览器时不记录错误</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F14719" target="_blank">#14719</a> 在单独的 SQL 查询中对每个表运行 OPTIMIZE TABLE，以便在复制时更好地运行</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F15322" target="_blank">#15322</a> 删除了 segment dimensions 工具提示中的误导性帮助文本</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F16529" target="_blank">#16529</a> 日志表中没有 idvisit 列的旧数据没有被清除</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F15036" target="_blank">#15036</a> 当 <code>enable_create_realtime_segments = 0</code> 时，将 <code>AND segmented reports are pre-processed (speed, requires cron)</code> 从 UI 中隐藏</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F17577" target="_blank">#17577</a> 将私有目录系统检查分成 "必需" 和 "推荐" 两部分</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F16834" target="_blank">#16834</a> 创建表时默认使用 row_format=dynamic</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fissues%2F18012" target="_blank">#18012</a> 在 Matomo 用户界面中添加关于放弃支持 IE11 的警告</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmatomo-org%2Fmatomo%2Fpull%2F17905" target="_blank">#17905</a> 更新缓存组件</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmatomo.org%2Fchangelog%2Fmatomo-4-5-0%2F" target="_blank">https://matomo.org/changelog/matomo-4-5-0/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            
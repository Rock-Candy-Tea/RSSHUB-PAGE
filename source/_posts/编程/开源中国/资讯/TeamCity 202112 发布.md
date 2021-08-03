
---
title: 'TeamCity 2021.1.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=470'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 06:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=470'
---

<div>   
<div class="content">
                                                                                            <p>TeamCity 2021.1.2 现已发布。该版本解决了 70 多个问题，显著修复了实验性 UI。其中大部分都集中在构建日志预览上，以及其他各种增强功能。官方强烈建议升级，因为该版本还包含多项安全修复和性能优化。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>新功能 
  <ul> 
   <li>性能监视器现在可以显示每个选定时间段的日志条目。如要限制时间段，可以将选择拖放到图表上</li> 
   <li>如果运行属于构建链一部分的个人构建，则其所有依赖构建也将作为个人构建运行。但是，如果在依赖项设置中启用重用合适的构建，TeamCity 将尽可能尝试优化链。如果运行个人依赖构建不会带来优势，TeamCity 将使用已完成的非个人构建。</li> 
   <li>Build Results 的 Parameters 选项卡有一个新过滤器：仅显示修改后的参数。如果启用，此选项卡将仅显示其值在当前构建中自定义的参数</li> 
   <li>为构建日志搜索中的下一步按钮提供一些快捷方式</li> 
   <li>在构建代理下载中包含自述文件</li> 
   <li>在构建运行时报告 PerfMon</li> 
   <li>性能监视器应发布已取消构建的数据</li> 
   <li>在每次获取时获取远程中所有可用分支的实验能力，而不是获取当前状态</li> 
   <li>将自动自动检测 python 测试视为 “pytest” 命令，而不是 “文件”</li> 
  </ul> </li> 
 <li>可用性问题 
  <ul> 
   <li>实验性 UI：单击构建日志中的一行不会更新 url 中的 focusLine</li> 
   <li>如果没有套件/包，但有几个子元素，可以在分组测试视图中显示“无名称”</li> 
   <li>删除重复的两个搜索按钮</li> 
   <li>部署部分：运行构建后运行部署按钮向下移动</li> 
   <li>验性 UI 中未加载非活动（在新选项卡中打开）选项卡中的信息</li> 
   <li>在新 UI 中滚动长构建日志会在浏览器中生成数十个历史条目</li> 
   <li>重命名 “构建日志” 选项卡上的 “移至顶部” 按钮</li> 
   <li>为上传个人补丁提供拖放支持</li> 
   <li>为上传的统一差异补丁生成更具体的个人补丁更改描述</li> 
   <li>依赖链：无法在实验性 UI 中查看一些构建的详细信息</li> 
   <li>检查 (ReSharper)：添加附加参数应以换行符分隔到 UI 的信息</li> 
  </ul> </li> 
 <li>bug 修复 
  <ul> 
   <li>更改分支后，选项卡计数器中显示错误数量的待处理更改</li> 
   <li>修复构建日志中的重叠文本</li> 
   <li>“代理日志”选项卡不会在代理连接/断开连接时刷新，直到页面重新加载</li> 
   <li>在某些情况下，Perforce 检出可能会因客户端映射而失败（出现“必须创建客户端 'tw-28076' 以访问本地文件” 错误）</li> 
   <li>某些客户端映射可能会发生“无法构建补丁：java.lang.NullPointerException”</li> 
   <li>启用/禁用代理对话框：选择选项弹出窗口呈现在后面</li> 
   <li>默认关联池未显示在授权代理对话框中</li> 
   <li>构建日志搜索：下一个结果按钮不会跳转到一行中的每个事件</li> 
   <li>重置 buildsMetadata 缓存会导致无法在内置提要中找到 NuGet 包</li> 
  </ul> </li> 
 <li>性能优化 
  <ul> 
   <li>尝试从多个线程将相同构建加载到缓存中的高争用</li> 
   <li>在某些情况下 StringPoolInstance 中的内存使用过多（例如长测试的并发执行）</li> 
   <li>即使触发规则匹配提交的所有文件，也会缓慢处理带有触发规则的 VCS 触发器</li> 
   <li>修复与电子邮件通知相关的 NoClassDefFound 异常</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jetbrains.com%2Fteamcity%2F2021%2F08%2Fteamcity-2021-1-2-is-here%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            
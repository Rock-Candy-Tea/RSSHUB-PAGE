
---
title: 'Visual Studio 2013 _ 2015 完全卸载 - C语言零基础入门教程'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3bf80ba09d44e8d9dac4cf544de1b11~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 17:44:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3bf80ba09d44e8d9dac4cf544de1b11~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>目录</p>
<ul>
<li><a href="https://juejin.cn/post/6990529306321485838#%E4%B8%80%E6%9F%A5%E6%89%BE_vs_communityexe_%E6%96%87%E4%BB%B6" title="#%E4%B8%80%E6%9F%A5%E6%89%BE_vs_communityexe_%E6%96%87%E4%BB%B6" target="_blank">一.查找 vs_community.exe 文件</a></li>
<li><a href="https://juejin.cn/post/6990529306321485838#%E4%BA%8C%E4%BB%A5%E7%AE%A1%E7%90%86%E8%BA%AB%E4%BB%BD%E6%89%93%E5%BC%80_cmd_%E7%AA%97%E5%8F%A3" title="#%E4%BA%8C%E4%BB%A5%E7%AE%A1%E7%90%86%E8%BA%AB%E4%BB%BD%E6%89%93%E5%BC%80_cmd_%E7%AA%97%E5%8F%A3" target="_blank">二.以管理身份打开 cmd 窗口</a></li>
<li><a href="https://juejin.cn/post/6990529306321485838#%E4%B8%89%E4%BD%BF%E7%94%A8%E5%BE%AE%E8%BD%AF%E5%AE%98%E6%96%B9%E7%9A%84%E5%8D%B8%E8%BD%BD%E5%B7%A5%E5%85%B7%E6%9D%A5%E6%B8%85%E7%90%86%E6%AE%8B%E4%BD%99%E6%95%B0%E6%8D%AE" title="#%E4%B8%89%E4%BD%BF%E7%94%A8%E5%BE%AE%E8%BD%AF%E5%AE%98%E6%96%B9%E7%9A%84%E5%8D%B8%E8%BD%BD%E5%B7%A5%E5%85%B7%E6%9D%A5%E6%B8%85%E7%90%86%E6%AE%8B%E4%BD%99%E6%95%B0%E6%8D%AE" target="_blank">三.使用微软官方的卸载工具来清理残余数据</a>
<ul>
<li><a href="https://juejin.cn/post/6990529306321485838#1%E4%B8%8B%E8%BD%BD%E6%B8%85%E7%90%86%E5%B7%A5%E5%85%B7" title="#1%E4%B8%8B%E8%BD%BD%E6%B8%85%E7%90%86%E5%B7%A5%E5%85%B7" target="_blank">1.下载清理工具</a></li>
<li><a href="https://juejin.cn/post/6990529306321485838#2%E4%BB%A5%E7%AE%A1%E7%90%86%E5%91%98%E8%BA%AB%E4%BB%BD%E6%89%A7%E8%A1%8C_setupforceduninstallexe%EF%BC%9B" title="#2%E4%BB%A5%E7%AE%A1%E7%90%86%E5%91%98%E8%BA%AB%E4%BB%BD%E6%89%A7%E8%A1%8C_setupforceduninstallexe%EF%BC%9B" target="_blank">2.以管理员身份执行 setup.forceduninstall.exe；</a></li>
<li><a href="https://juejin.cn/post/6990529306321485838#3%E6%8C%89Y%E8%BF%9B%E8%A1%8C%E5%8D%B8%E8%BD%BD%EF%BC%9B" title="#3%E6%8C%89Y%E8%BF%9B%E8%A1%8C%E5%8D%B8%E8%BD%BD%EF%BC%9B" target="_blank">3.按 Y 进行卸载；</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6990529306321485838#%E5%9B%9B%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" title="#%E5%9B%9B%E7%8C%9C%E4%BD%A0%E5%96%9C%E6%AC%A2" target="_blank">四猜你喜欢</a></li>
</ul>
<blockquote>
<p>零基础 C/C++ 学习路线推荐 : <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc-c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c-c" ref="nofollow noopener noreferrer">C/C++ 学习目录</a> >> <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Fc%25e8%25af%25ad%25e8%25a8%2580%25e5%259f%25ba%25e7%25a1%2580" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/c%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80" ref="nofollow noopener noreferrer">C 语言基础入门</a></p>
</blockquote>
<p>在前一篇讲解了关于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7288.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7288.html" ref="nofollow noopener noreferrer"><strong>Visual Studio 2008 卸载</strong></a>，如果安装的是 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7292.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7292.html" ref="nofollow noopener noreferrer">Visual Studio2013 或者 Visual Studio2015</a></strong> 呢？</p>
<h2 data-id="heading-0">一.查找 vs_community.exe 文件</h2>
<p><strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7250.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7250.html" ref="nofollow noopener noreferrer">Visual Studio</a> 一共有三个版本</strong>：</p>
<ul>
<li><strong>如果是企业版：vs_enterprise.exe</strong></li>
<li><strong>如果是社区版：vs_community.exe</strong></li>
<li><strong>如果是专业版：vs_professional.exe</strong></li>
</ul>
<p>在 C 盘的搜索框内输入 vs_community.exe （我的是社区版）或者直接使用 Everything 搜索，输入后进行搜索，搜索的结果如下：</p>
<p>右击该程序，点击“打开文件的所在位置”，记住并复制该路径，比如我的路径为：</p>
<pre><code class="copyable">C:\ProgramData\Package Cache\&#123;47e285fc-2ff5-479e-9c14-4258d9954215&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二.以管理身份打开 cmd 窗口</h2>
<p>cd 到刚才复制的路径，然后输入命令行：vs_community.exe /uninstall /force(会跳出 vs 窗口，等它运行结束就行了，时间有点长。。。)</p>
<ul>
<li>如果是企业版：vs_enterprise.exe /uninstall /force</li>
<li>如果是社区版：vs_community.exe /uninstall /force</li>
<li>如果是专业版：vs_professional.exe /uninstall /force</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3bf80ba09d44e8d9dac4cf544de1b11~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>1.必须是管理员身份运行 cmd 窗口;</strong></li>
<li><strong>2.如果是自己手动输入，那么一定要是在英文输入法下输入，还有 vs_community.exe / uninstall / force 这行代码中间有两个空格，一定要加上;</strong></li>
</ul>
<h2 data-id="heading-2">三.使用微软官方的卸载工具来清理残余数据</h2>
<h3 data-id="heading-3">1.下载清理工具</h3>
<p>在卸载完成后必须要清理掉残留数据，以防止再次安装或更换别的版本无法安装，此时需要使用微软官方的卸载工具来清理，其最新版本下载地址为： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FMicrosoft%2FVisualStudioUninstaller%2Freleases" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Microsoft/VisualStudioUninstaller/releases" ref="nofollow noopener noreferrer">github.com/Microsoft/V…</a></p>
<h3 data-id="heading-4">2.以管理员身份执行 setup.forceduninstall.exe；</h3>
<h3 data-id="heading-5">3.按 Y 进行卸载；</h3>
<h2 data-id="heading-6">四<strong>猜你喜欢</strong></h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7250.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7250.html" ref="nofollow noopener noreferrer">1.安装 Visual Studio</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7280.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7280.html" ref="nofollow noopener noreferrer">2.安装 Visual Studio 插件 Visual Assist</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7288.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7288.html" ref="nofollow noopener noreferrer">3.Visual Studio 2008 卸载</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2Farchives%2F7292.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/archives/7292.html" ref="nofollow noopener noreferrer">4.Visual Studio 2003/2015 卸载</a></li>
</ul>
<blockquote>
<p>本文由博客 - 猿说编程 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.codersrc.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.codersrc.com/" ref="nofollow noopener noreferrer">猿说编程</a> 发布！</p>
</blockquote></div>  
</div>
            
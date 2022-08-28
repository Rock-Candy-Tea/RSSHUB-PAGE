
---
title: 'jQuery 3.6.1 发布，优化 jQuery.trim 性能、修复焦点相关错误'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3090'
author: 开源中国
comments: false
date: Sun, 28 Aug 2022 08:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3090'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/news/131827/jquery-3-6-0-released">jQuery 3.6.0</a> 发布一年多之后推出了维护更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jquery.com%2F2022%2F08%2F26%2Fjquery-3-6-1-maintenance-release%2F" target="_blank">3.6.1</a>。</p> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li><strong>改进基础设施</strong></li> 
</ul> 
<p>团队表示，他们在这个版本中做了很多工作来更新一些测试和构建基础设施，包括将 CI 从 Travis CI 迁移到 GitHub Actions，在 Node 16 而不是 Node 15 上进行测试，通过 https 加载测试监听器，以及为自定义构建添加更多精度测试 (accurate testing)。</p> 
<p>此外，他们还从仓库某些文件的注释中删除了一些旧链接。因为这些链接指向了已被泄露的 URL。虽然这些文件从未在某个版本中分发，但它们毕竟存在于 GitHub 源代码中。</p> 
<ul> 
 <li><strong>修复丢失焦点的错误</strong></li> 
</ul> 
<p>此版本中还有一个与焦点相关的修复。具体情况是，<span style="background-color:#ffffff; color:#182026">即使在移除了 jQuery 焦点处理程序之后，对焦点的特殊事件处理仍然保持连接，这破坏了任何后续的手动焦点触发器。例如：</span></p> 
<pre><code class="language-javascript">$elem.on("focus", function() &#123;&#125;).off("focus").trigger("focus");</code></pre> 
<p>不会触发获取获取焦点。</p> 
<ul> 
 <li><strong>优化 jQuery.trim 性能</strong></li> 
</ul> 
<p>虽然<code>jQuery.trim</code>在主分支上已被删除，以便在下一个主要版本原生支持<code>String#trim</code>，但对于分支支持的某些浏览器（例如 Android 4.0）在 3.x 分支上仍然需要它。由于正则表达式的结构存在问题，某些极端情况非常慢。不过现在这种情况已经发生了变化，并且速度提升非常<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery%2Fpull%2F5068%23issuecomment-1189112865" target="_blank">显着</a>。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jquery.com%2F2022%2F08%2F26%2Fjquery-3-6-1-maintenance-release%2F" target="_blank">详情查看发布公告</a>。</p> 
<blockquote> 
 <p>jQuery 是一个快速、小型且功能丰富的 JavaScript 库。通过易于使用的 API（可在多种浏览器中使用），使 HTML 文档的遍历和操作、事件处理、动画和 Ajax 等操作变得更加简单。结合了多功能性和可扩展性，jQuery 改变了数百万人编写 JavaScript 的方式。</p> 
</blockquote>
                                        </div>
                                      
</div>
            
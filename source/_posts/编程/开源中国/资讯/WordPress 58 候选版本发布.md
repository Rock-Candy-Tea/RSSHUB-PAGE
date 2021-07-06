
---
title: 'WordPress 5.8 候选版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8540'
author: 开源中国
comments: false
date: Tue, 06 Jul 2021 06:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8540'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmake.wordpress.org%2Fcore%2F5-8%2F" target="_blank">WordPress 5.8</a>的第一个候选版本现已发布！ </p> 
<p>“候选版本”意味着新版本已经准备好发布，但由于有成千上万的插件和主题，以及数百万人使用 WordPress 的方式的差异，可能会有一些内容被遗漏。WordPress 5.8 定于<strong>2021年7月20日</strong>发布，但需要您的帮助才能达到此目标–如果您还没有尝试过 5.8，<strong>现在是时候了</strong>！</p> 
<p>您可以通过三种方式测试WordPress 5.8候选版本：</p> 
<ul> 
 <li>安装并启用<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.wordpress.org%2Fplugins%2Fwordpress-beta-tester%2F" target="_blank">WordPress Beta Tester插件</a>（选择<code>Bleeding edge</code>通道，然后选择<code>Beta/RC Only</code>更新流）</li> 
 <li>直接下载候选版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.wordpress.org%2Fwordpress-5.8-rc-zh_CN.zip" target="_blank">（zip）</a></li> 
 <li>使用WP-CLI测试。<code>wp core update --version=5.8-RC1</code></li> 
</ul> 
<p>感谢所有测试 Beta 版本并提供反馈的贡献者。测试错误是完善每个版本的关键步骤，也是为 WordPress 做出贡献的一种简单方式。</p> 
<h2>WordPress 5.8更新了什么？</h2> 
<p>2021 年的第二个版本继续在区块编辑器方面取得进展，朝着承诺的未来目标（全站编辑）前进，并进行了如下更新：</p> 
<ul> 
 <li>用区块管理小工具</li> 
 <li>用新的区块和区块模式显示文章</li> 
 <li>编辑文章模板</li> 
 <li>页面结构概览</li> 
 <li>推荐区块模式</li> 
 <li>图片的风格样式和颜色</li> 
 <li><code>theme。 json</code></li> 
 <li>放弃对 IE11 的支持</li> 
 <li>添加对 WebP 的支持</li> 
 <li>添加额外的区块支持</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmake.wordpress.org%2Fcore%2F2021%2F05%2F27%2Fwhats-new-in-gutenberg-10-7-26-may%2F" target="_blank">Gutenberg 插件的 10.7 版本</a></li> 
</ul> 
<p>WordPress 5.8 也进行了很多改进以提升开发者体验。要了解更多信息，请订阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmake.wordpress.org%2Fcore%2F" target="_blank">Make WordPress Core 博客</a>，并时常关注 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmake.wordpress.org%2Fcore%2Ftag%2F5-8%2Bdev-notes%2F" target="_blank">developer notes 标签</a>以获取可能影响您产品的这些和其他更改的更新。</p> 
<h2>插件和主题开发者</h2> 
<p>请针对 WordPress 5.8 测试您的插件和主题，并将<code>readme</code>文件中的 Tested up to 版本更新为 5.8。如果您发现兼容性问题，请务必在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwordpress.org%2Fsupport%2Fforum%2Falphabeta%2F" target="_blank">支持论坛</a>发帖，以便在最终版本发布之前解决这些问题。</p> 
<p>即将发布的 WordPress 5.8 详解指南将让您更深入地了解主要更改。</p> 
<h2>提供帮助</h2> 
<p>您会说英语以外的语言吗？<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftranslate.wordpress.org%2Fprojects%2Fwp%2Fdev" target="_blank">帮助我们将 WordPress 翻译成 100 多种语言！</a>此版本也标志着 5.8 版本发布计划中的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmake.wordpress.org%2Fpolyglots%2Fhandbook%2Fglossary%2F%23hard-freeze" target="_blank">硬字符串冻结</a>点。</p> 
<p><strong>如果您发现了 bug</strong>，可在支持论坛的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwordpress.org%2Fsupport%2Fforum%2Falphabeta" target="_blank">Alpha/Beta 区域</a>发帖。我们很乐意听到您的意见！ 如果您愿意写一份可重现的错误报告，请在 WordPress Trac 上<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcore.trac.wordpress.org%2Fnewticket" target="_blank">提交一份报告</a>，在那里您还可以找到<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcore.trac.wordpress.org%2Ftickets%2Fmajor" target="_blank">已知 bug 的列表</a>。</p> 
<p>来源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcn.wordpress.org%2F2021%2F06%2F30%2Fwordpress-5-8-release-candidate%2F" target="_blank">WordPress China</a></p>
                                        </div>
                                      
</div>
            
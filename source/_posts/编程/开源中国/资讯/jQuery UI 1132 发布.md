
---
title: 'jQuery UI 1.13.2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8577'
author: 开源中国
comments: false
date: Sat, 16 Jul 2022 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8577'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="color:#000000">jQuery UI 1.13.2 现已</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.jqueryui.com%2F2022%2F07%2Fjquery-ui-1-13-2-released%2F" target="_blank">发布</a><span style="color:#000000">，这是 jQuery 1.13 系列的第二个补丁版本。它包括 Checkboxradio 小部件的安全修复、Datepicker 的一些本地化更新以及一些社区提交的问题的修复。内置的 jQuery UI 文件现在包含在 npm 包中，这对于一些依赖它作为真实来源的 CDN 来说很重要。</span></p> 
<p><span style="color:#000000">官方提醒称，“请记住 jQuery UI 处于维护状态：我们将确保该库与新的 jQuery 版本兼容，并且安全问题已得到修复，但没有计划新的重要功能工作。我们还将尝试修复来自 jQuery UI 1.12.1 的重要回归；较旧的长期存在的错误可能无法修复。请注意，这不会影响仍在积极维护的 jQuery Core。”</span></p> 
<p><span style="color:#000000">新版本具体更新内容如下：</span></p> 
<h4><span style="color:#000000"><strong>Widgets</strong></span></h4> 
<p><span style="color:#000000"><strong>Checkboxradio</strong></span></p> 
<ul> 
 <li><span style="color:#000000">Fixed：不要将文本标签重新评估为 HTML （</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fissues%2F2101" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2F8cc5bae1caa1fcf96bf5862c5646c787020ba3f9" target="_blank">2101，8cc5bae1c</a><span style="color:#000000">）</span></li> 
</ul> 
<p><span style="color:#000000"><strong>Datepicker</strong></span></p> 
<ul> 
 <li><span style="color:#000000">Fixed：大写一些印尼语单词（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2F9d1fc97b4ea5c364b8f1c7d9ab2a3c28f8c594e7" target="_blank">9d1fc97b4</a><span style="color:#000000">）</span></li> 
 <li><span style="color:#000000">Fixed：为 prevText 和 nextText 添加缺失的本地化（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fissues%2F2048" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2F395aa7d05601aa1f2ebeae272f81f0014c0cae90" target="_blank">2048，395aa7d05</a><span style="color:#000000">）</span></li> 
 <li><span style="color:#000000">Fixed：移除本地化中的符号（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fissues%2F2048" target="_blank"># </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2F218c6af95a5d72134c1b32220995b161c56a1453" target="_blank">2048、218c6af95、3126e1286</a><span style="color:#000000">）</span></li> 
</ul> 
<p><span style="color:#000000"><strong>Selectmenu</strong></span></p> 
<ul> 
 <li><span style="color:#000000">Fixed：移除对已弃用的 .focus() 方法的调用 ( </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2F1f467baaacf0f9927cb73482a9f3ac0253739c4a" target="_blank">1f467baaa</a> <span style="color:#000000">)</span></li> 
</ul> 
<p><span style="color:#000000"><strong>All</strong></span></p> 
<ul> 
 <li><span style="color:#000000">Fixed：移除 demos/tests 中已弃用的 .click() 用法（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2Fb53e7beb6884a8de7710146112bc48aecd8737b4" target="_blank">b53e7beb6</a><span style="color:#000000">）</span></li> 
</ul> 
<h4><span style="color:#000000"><strong>Build</strong></span></h4> 
<ul> 
 <li><span style="color:#000000">Changed：添加 dependabot.yml 配置（GitHub Actions）（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2Fd66fdd5c9a1afac13138c7f48b068c36236b9358" target="_blank">d66fdd5c9</a><span style="color:#000000">）</span></li> 
 <li><span style="color:#000000">Changed：在 npm/Bower 包中包含所有发布到 CDN 的文件（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fissues%2F2011" target="_blank">#2011</a>，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery-ui%2Fcommit%2Fe21a2543b55680f23aaa7efa38f3288b8e767e7d" target="_blank">e21a2543b</a><span style="color:#000000">）</span></li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjqueryui.com%2Fchangelog%2F1.13.2%2F" target="_blank">https://jqueryui.com/changelog/1.13.2/</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            
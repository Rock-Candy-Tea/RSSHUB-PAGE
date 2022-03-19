
---
title: 'Pale Moon 30.0.0 发布，改用 Firefox GUID'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9449'
author: 开源中国
comments: false
date: Sat, 19 Mar 2022 07:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9449'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Pale Moon 30.0.0 现已发布，</span><span style="color:#000000">这是一个新的里程碑版本。</span>Pale Moon 正在放弃自己的 GUID（globally-unique identifier）并改用 Firefox 的 GUID，以提供与旧的和未维护的Firefox扩展的最大兼容性，以及那些在 add-ons site 上维护的扩展。</p> 
<blockquote> 
 <p>请理解，这为人们使用可能不兼容和旧/不安全的浏览器扩展提供了更多的自由，但也意味着从这一点开始我们将采取更加“hands-off”的方法，这意味着你将不得不自己解决更多的问题，并采取更加谨慎的态度，特别是在使用外部/旧的扩展。</p> 
 <p>请注意，我们当前的 add-ons site 将在一段时间内同时提供旧版本的 Pale Moon 和较新的版本，并且你在访问 add-ons site 时<span><span style="color:#000000"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#f9f9f9"><span><span><span>不要欺骗你的用户代理</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>，否则你可能会得到错误的 add-ons 或 add-ons 更新类型，或者根本没有收到它们。</p> 
</blockquote> 
<p>此外，在过去几个月中，平台代码已更改为更精简的版本；并且在此里程碑中 UXP 已发布给社区进行维护和协调，以便在需要的地方继续构建。“相反，我们现在正在构建 Goanna Runtime Environment（或简称 GRE），更加专注于 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.moonchildproductions.info%2Fgoanna.shtml" target="_blank">Goanna 渲染引擎</a>并削减对不可维护组件和目标平台的支持。”</p> 
<p>由于源代码树中的大量内部更改，这些发行说明仅关注浏览器中有关实现、扩展和安全/错误修复的相关更改，并且绝不是详尽无遗的。</p> 
<p>更新内容如下：</p> 
<p><strong>Most notable user-facing/implementation changes</strong></p> 
<ul> 
 <li><span style="color:#000000">实现了 Global Privacy Control，取代无法执行的“DNT”（Do Not Track）信号。注意：DNT preference 可能无法正确迁移到 GPC。如果需要，请仔细检查并手动启用。</span></li> 
 <li>首选项中的"Default browser"控制已移至"General"。</li> 
 <li>更新了对 Twemoji 13.1 的表情符号支持。</li> 
 <li>实现了 Selection.setBaseAndExtent()，以实现 web 兼容性。</li> 
 <li>实现了 queueMicroTask() 以 web 网络兼容。</li> 
</ul> 
<p><strong>For add-on developers</strong></p> 
<p> </p> 
<ul> 
 <li>Pale Moon 现在在内部使用 Firefox GUID 进行识别。这并不影响它在网络上的识别方式。</li> 
 <li>已恢复对旧版 Firefox 扩展的直接支持。需要更新 Pale Moon 独有的扩展，以在其安装清单中以及在适用的情况下，在其 JavaScript 组件和覆盖中以 Firefox GUID 为目标。</li> 
 <li>浏览器不再存在于“browser”分发子目录中。如果你是硬编码路径，则可能会受到影响。</li> 
 <li><code>appinfo.platformVersion</code>为向后兼容而 frozen。如果需要检测平台版本，则应<code>appinfo.greVersion</code> 改为使用。</li> 
 <li>Themes：<code>scrollbar-width</code>现在映射到 scrollbar controls（bars、resizers 和 corner controls）上的属性，以便更好地支持 thin scrollbars 的主题。</li> 
 <li>Language packs：整个国际化结构发生了变化；因为这需要重新验证翻译，所以目前某些语言包中可能还有一些未翻译的字符串。</li> 
</ul> 
<p><span style="color:#000000"><strong>错误修复、稳定性和安全性：</strong></span></p> 
<ul> 
 <li>更新了各种树内库：cubeb、sqlite、cairo、...</li> 
 <li>修复了 Linux 桌面快捷方式文件的问题，以解决常见发行版上潜在的 DE 集成问题。</li> 
 <li>修复了作为属性而不是 CSS 传递时页面和 iframe 内容边距未正确应用的问题。</li> 
 <li>确保 JavaScript 和 JSON 文件始终被识别为已知的 MIME 类型，因此可以从 local sources 适当地打开它们。</li> 
 <li>修复了快速加载和卸载 js 模块导致浏览器崩溃的问题。</li> 
 <li>修复了如果包含过长的可展开字符系列，工具提示在最后被切断的问题。</li> 
 <li>修复了几个应用程序崩溃场景。</li> 
 <li>修复了大量线程锁定/互斥锁问题。</li> 
 <li>修复了由于错误报告不一致而导致的内容类型泄漏。(CVE-2022-22760)</li> 
 <li>修复了 iframe 沙盒未正确应用的问题。(CVE-2022-22759)</li> 
 <li>如果导出的书签文件包含恶意书签，则修复了潜在的书签泄漏。</li> 
 <li>修复了拖放问题。(CVE-2022-22756)</li> 
 <li>修复了由于截断 WAV 文件而导致的潜在崩溃。</li> 
 <li>修复了 XSLT 的内存安全问题。(CVE-2022-26485)</li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.palemoon.org%2Freleasenotes.shtml" target="_blank">https://www.palemoon.org/releasenotes.shtml</a></p>
                                        </div>
                                      
</div>
            
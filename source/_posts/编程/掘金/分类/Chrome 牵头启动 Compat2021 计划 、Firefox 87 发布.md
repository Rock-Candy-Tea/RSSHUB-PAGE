
---
title: 'Chrome 牵头启动 Compat2021 计划 、Firefox 87 发布'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ee8eb8a5fb14c72b8e513817863a3cc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 01:12:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ee8eb8a5fb14c72b8e513817863a3cc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ee8eb8a5fb14c72b8e513817863a3cc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></h2>
<h2 data-id="heading-1">前端快爆</h2>
<ul>
<li>
<p>Firefox 87 <a href="https://hacks.mozilla.org/2021/03/in-march-we-see-firefox-87/" target="_blank" rel="nofollow noopener noreferrer">发布</a></p>
<ul>
<li>功能 & 特性
<ul>
<li>新增 SmartBlock 功能。SmartBlock 为被 Firefox 阻止的脚本提供了替代程序，防止网站在隐私浏览和严格增强跟踪保护下显示不正确，确保网站正常显示。</li>
<li>默认剪裁 HTTP Referrer 以保护用户隐私。默认将 <code>Referrer-Policy</code> 修改为 <code>strict-origin-when-cross-origin</code> ，以减少在跨域请求中泄露敏感信息的风险，这意味着默认在 HTTP Referrers 中不再包含路径和查询字符串信息。</li>
<li>使用页面查找时使用“高亮全部”会沿滚动条显示匹配位置。</li>
<li>默认开启 <code>beforeinput</code> 事件和 <code>getTargetRanges()</code> 方法，允许 Web 应用程序在浏览器修改 DOM 树之前覆盖文本编辑行为，从而提供对文本输入的更多控制以提高性能。</li>
</ul>
</li>
<li>开发者工具
<ul>
<li>Inspector 面板中增加了模拟亮色或暗色主题按钮，用来匹配 <code>prefers-color-scheme</code> 媒体查询，开发者无需再从系统设置中更改。</li>
<li>Inspector 面板中增加伪类 <code>:target</code> ，用来匹配页面唯一元素(id)激活时的样式。</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Chrome 牵头启动了一项叫 <a href="https://web.dev/compat2021/" target="_blank" rel="nofollow noopener noreferrer">Compat2021</a> 的计划，旨在消除 Web 开发五大兼容性痛点，以下从调研、测试、使用等角度解释为什么选中这五大痛点：</p>
<ul>
<li>CSS Flexbox
<ul>
<li>调研：这是 MDN 浏览器兼容性报告中的首要问题，在 CSS 中最为人熟知和使用。</li>
<li>测试：在所有浏览器获得 85％ 的通过率。</li>
<li>使用：75％ 的页面在使用，在 HTTP Archive 中增长强劲。</li>
</ul>
</li>
<li>CSS Grid
<ul>
<li>调研：MDN 浏览器兼容性报告亚军，这个属性众所周知，但在 CSS 中较少使用。</li>
<li>测试：在所有浏览器获得 75％ 的通过率。</li>
<li>使用：8％ 的页面在使用，并正在快速增长。</li>
</ul>
</li>
<li>CSS position: sticky
<ul>
<li>调研：在 MDN 浏览器兼容性报告中被多次提到，在 CSS 中为人熟知且经常使用。</li>
<li>测试：在所有浏览器获得 66％ 的通过率。</li>
<li>使用：8％ 的页面在使用。</li>
</ul>
</li>
<li>CSS aspect-ratio property
<ul>
<li>调研：已被熟知，但并未广泛使用。</li>
<li>测试：在所有浏览器获得 27％ 的通过率。</li>
<li>使用：3％ 的页面在使用。</li>
</ul>
</li>
<li>CSS transforms
<ul>
<li>调研：为人熟知且经常使用。</li>
<li>测试：在所有浏览器获得 55％ 的通过率。</li>
<li>使用：80％ 的页面在使用。</li>
</ul>
</li>
</ul>
</li>
<li>
<p>TypeScript 团队<a href="https://devblogs.microsoft.com/typescript/announcing-the-new-typescript-handbook/" target="_blank" rel="nofollow noopener noreferrer">宣布</a>已重写 <a href="https://www.typescriptlang.org/docs/handbook/intro.html" target="_blank" rel="nofollow noopener noreferrer">TypeScript 手册</a></p>
<ul>
<li>删除了指导 JavaScript 的部分（因为网上和通过书籍学习 JavaScript 的资源非常丰富）。</li>
<li>渐进式教学。</li>
<li>发布新的 TypeScript 版本时，提供最新的代码示例。</li>
<li>编写日常用例。</li>
</ul>
</li>
<li>
<p><a href="https://blog.chromium.org/2021/03/a-safer-default-for-navigation-https.html" target="_blank" rel="nofollow noopener noreferrer">从 Chrome 90 开始，在地址栏不指定协议的情况下，将默认协议改为 HTTPS</a>，以改善隐私和访问支持 HTTPS 的网站的速度。对于还不支持 HTTPS 的网站，当尝试 HTTPS 失败（包括证书错误，如名称不匹配或不受信任的自签名证书，或连接错误，如 DNS 解析失败）时，Chrome 将退回到 HTTP。</p>
</li>
</ul>
<h2 data-id="heading-2">百宝箱</h2>
<ul>
<li><a href="https://github.com/luruke/aladino" target="_blank" rel="nofollow noopener noreferrer">Aladino</a> 是一个基于 WebGL 的网站特效工具，它可以使用「着色器效果」增强您的网站。这是一个很小的文件库（压缩后约为5KB），并且没有依赖项。</li>
</ul>
<p><img alt="1.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ac247fbae6c4547bb63c96f85265693~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt="2.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8fff2dcdac7456c9ad005e9306c7557~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"><img alt="3.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23b270d9445943cab75589954a82e5d6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p><a href="https://github.com/piscinajs/piscina" target="_blank" rel="nofollow noopener noreferrer">piscina</a> 是一个快速、高效的 Node.js 工作线程池实现。</p>
</li>
<li>
<p><a href="https://github.com/WebReflection/linkedom" target="_blank" rel="nofollow noopener noreferrer">LinkDOM</a> 是 JSDOM 的一个替代品，使用 JavaScript 解析 HTML 字符串，返回一个 DOM 对象，在上面实现了 DOM 接口。它比 JSDOM 体积更小、速度更快、内存占用更少。</p>
</li>
</ul>
<hr>
<p>本期编辑：@墨尘；审阅：@一丝。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
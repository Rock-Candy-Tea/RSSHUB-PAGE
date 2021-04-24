
---
title: '技术周刊：Node.js 16发布；中国首个 JavaScript 语言提案在 ECMA 进入 Stage 3'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03e3453ab68d41d7a5583579dc22a1ff~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 21:42:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03e3453ab68d41d7a5583579dc22a1ff~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03e3453ab68d41d7a5583579dc22a1ff~tplv-k3u1fbpfcp-zoom-1.image" alt="2020-04-21.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前端快爆</h2>
<ul>
<li><a href="https://hacks.mozilla.org/2021/04/never-too-late-for-firefox-88/" target="_blank" rel="nofollow noopener noreferrer">Firefox 88 正式发布</a>，主要包含以下特性：
<ul>
<li>正式禁用 FTP 协议，计划在 Firefox 90 版本中完全删除 FTP 支持。此前，<a href="https://developer.apple.com/documentation/safari-release-notes/safari-14-beta-release-notes" target="_blank" rel="nofollow noopener noreferrer">Safari 14</a>、<a href="https://www.chromestatus.com/feature/6246151319715840" target="_blank" rel="nofollow noopener noreferrer">Chrome 87</a> 已禁用 FTP 协议。</li>
<li>新增伪类 <code>:user-valid</code> 和 <code>:user-invalid</code>，用于匹配一个包含有效或无效数据的表单输入。与 <code>:valid</code> 和 <code>:invalid</code> 的区别是 <code>:user-valid</code> 和 <code>:user-invalid</code> 只有在用户不再关注元素时才开始匹配（例如，通过 tab 键进入下一个输入），Firefox 是第一个实现此特性的浏览器。</li>
<li>新增支持正则表达式的匹配索引（<a href="https://github.com/tc39/proposal-regexp-match-indices" target="_blank" rel="nofollow noopener noreferrer">match indices</a>）特性，该属性包含数组 <code>indices</code>，存储每个匹配的捕获组的开始和结束位置，此特性已进入 Stage 4，将进入 ECMAScript 2022，并将在 Chrome 91 中得到支持。</li>
</ul>
</li>
</ul>
<blockquote>
<p>点评：至此，三大主流浏览器均已禁用 FTP</p>
</blockquote>
<ul>
<li>
<p><a href="https://github.com/nodejs/node/blob/master/doc/changelogs/CHANGELOG_V16.md#16.0.0" target="_blank" rel="nofollow noopener noreferrer">Node.js 16.0.0 发布</a>，将于今年 10 月 26 日进入 LTS，该版本主要包含以下特性：</p>
<ul>
<li>V8 JavaScript 引擎已更新至 9.0，优化了性能表现。</li>
<li>稳定的 Timers Promises API。Timers Promises API 提供了一组返回 <code>Promise</code> 对象的替代计时器函数，从而无需使用 <code>util.promisify()</code>。该 API 是在 Node.js 15 中添加的，此版本将从实验状态升级到稳定状态。</li>
<li>新的编译器，此版本将是为 Apple M1 发布的第一个预构建的二进制版本。虽然为 Intel (darwin-x64) 和 ARM (darwin-arm64) 架构提供了单独的 tarballs，但 macOS 安装程序（.pkg）将作为一个“fat”（多架构）二进制文件发布。</li>
</ul>
</li>
<li>
<p><a href="https://github.com/w3ctag/design-reviews/blob/main/reviews/first_party_sets_feedback.md" target="_blank" rel="nofollow noopener noreferrer">W3C 技术架构组拒绝了 Google 将多个不同域名视为同源的提议</a>。</p>
<ul>
<li>该提案建议，如果多个域名由同一实体拥有，例如 google.com、google.co.uk 和 youtube.com，可以依据 “允许相关域名声明自己是相同的第一方” 来允许浏览器将这一组域作为一个域来对待。</li>
<li>基于隐私和安全的考虑，W3C 拒绝了这一提案，认为这一提议没有考虑全部后果，将会削弱同源的意义，也意味着浏览器开发商将会提供和维护自己的列表，或将导致开发者更多开发面向特定浏览器的应用</li>
<li>此前，Firefox 86 起禁用了跨域站点的存储接口读写；Safari 13.1 起禁用了所有第三方站点的 Cookie 使用。</li>
</ul>
</li>
<li>
<p>中国首个 JavaScript 语言提案在 ECMA 进入 Stage 3。</p>
<ul>
<li>该提案是阿里巴巴前端标准化小组与淘系技术部门近期在 TC39 技术委员会上提出的<a href="https://github.com/tc39/proposal-error-cause" target="_blank" rel="nofollow noopener noreferrer">《Error Cause》</a>，将开始在 JavaScript 引擎中开始实现，并在浏览器、Node.js 实验性实施。</li>
<li>该提案为 Error Constructor 新增了一个可选的参数 options，其中可以设置 cause 并且接受任意 JavaScript 值（JavaScript 可以 throw 任意值，如 undefined 或者字符串），将这个值赋值到新创建的 error.cause 上。</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6579aeda972a4cf0b1f101684aa6ec17~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">百宝箱</h2>
<ul>
<li><a href="https://trekhleb.dev/js-image-carver/" target="_blank" rel="nofollow noopener noreferrer">JS IMAGE CARVER</a> 是一个基于接缝裁剪（Seam Carving）算法的内容感知图像缩放器，可以任意改变图片的高度和宽度，而不会扭曲图像。它的原理是找出图片中对象的边缘，只改变对象之间的像素，尽量保持对象本身的高宽比例。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48d6128126f045178a8008bbfbf72bd3~tplv-k3u1fbpfcp-zoom-1.image" alt="demo-01.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://react-hook-form.com/" target="_blank" rel="nofollow noopener noreferrer">React Hook Form</a> 是一个用于 React 表单的 Hook，具有高性能、灵活、可扩展的表单、验证易用等特点。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4480819e816e465faddb5b3d4258e37e~tplv-k3u1fbpfcp-zoom-1.image" alt="v7_example.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<hr>
<p>本期编辑：@墨尘，审阅：@承虎</p></div>  
</div>
            
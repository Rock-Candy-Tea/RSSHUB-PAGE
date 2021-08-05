
---
title: '生成Github JS 仓库的测试覆盖率徽标'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c04644be6c534feca262245878df6dd3~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 06:58:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c04644be6c534feca262245878df6dd3~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>今天给我的开源项目<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnihaojob%2Fpopular-message" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nihaojob/popular-message" ref="nofollow noopener noreferrer">popular-message</a>增加了一下测试覆盖率的图标，覆盖率提高到了88%，不过这个覆盖率的图标还真不是直接放个图片链接这么简单。</p>
<p>不过也难不到哪里去，除了jest单元测试框架的语法，主要是借助<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftravis-ci.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://travis-ci.com/" ref="nofollow noopener noreferrer">travis-ci</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoveralls.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coveralls.io/" ref="nofollow noopener noreferrer">coveralls.io</a>这2工具实现测试报告自动上报。</p>
<p>快速的写下笔记备忘，如果你在搞单元测试，恰巧也要增加测试覆盖率图表，希望能够帮到你，大神跳过。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c04644be6c534feca262245878df6dd3~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>涉及工具：</p>
<ol>
<li>Jest：Js测试框架</li>
<li>Travis-CI：CI 持续集成服务平台</li>
<li>Coveralls.io：测试报告展示</li>
</ol>
<h3 data-id="heading-0">流程</h3>
<p>首先选择一个单元测试框架，我用的Jest，编写完单元测试代码以后，我们要确保<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftravis-ci.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://travis-ci.com/" ref="nofollow noopener noreferrer">travis-ci</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoveralls.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coveralls.io/" ref="nofollow noopener noreferrer">coveralls.io</a>这2个网站<strong>使用GitHub账号授权登录，并有响应的读写权限</strong>，然后再按照流程配置就轻车熟路了。</p>
<ol>
<li>GitHub账号授权登录<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftravis-ci.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://travis-ci.com/" ref="nofollow noopener noreferrer">travis-ci</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoveralls.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coveralls.io/" ref="nofollow noopener noreferrer">coveralls.io</a></li>
<li>安装Jest，编写单元测试代码</li>
<li>安装 Coveralls， 增加测试报告上报脚本</li>
<li>配置Travis 文件，提交代码后自动执行上报</li>
<li>提交代码触发CI，查看覆盖率</li>
</ol>
<h3 data-id="heading-1">1. GitHub账号授权登录<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftravis-ci.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://travis-ci.com/" ref="nofollow noopener noreferrer">travis-ci</a>、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoveralls.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coveralls.io/" ref="nofollow noopener noreferrer">coveralls.io</a></h3>
<p>这一步很简单，只需要授权登录就好，但是必须的，否则不能根据仓库自动执行。</p>
<p>授权后会有项目列表：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cb12f51fd3140d7b78934b12296206b~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9e642816b9d49a2be91296ac15703af~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">2. 安装Jest，编写单元测试代码</h3>
<p>安装依赖，编写单测代码，增加Script选项，然后直接运行即可。</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add jest -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnihaojob%2Fpopular-message%2Fblob%2Fmain%2Ftest%2Findex.test.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nihaojob/popular-message/blob/main/test/index.test.js" ref="nofollow noopener noreferrer">测试代码</a>不再贴进来，可在Github查看。</p>
<p>package.json增加测试脚本</p>
<pre><code class="hljs language-json copyable" lang="json">
&#123;
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"jest"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d80f723a707e4fd5860a734d643879ab~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="2021-08-04 19.02.48.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">3. 安装 Coveralls， 增加测试报告上报脚本</h3>
<p>本地执行 jest --coverage 时会生成测试报告HTML文件， Coveralls工具会把测试报告上传到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoveralls.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coveralls.io/" ref="nofollow noopener noreferrer">coveralls.io</a>网站，可以展示测试报告并生成徽章。</p>
<p>安装coveralls：</p>
<pre><code class="hljs language-bash copyable" lang="bash">$ yarn add coveralls -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>package.json增加上报脚本：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"popular-message"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"test"</span>: <span class="hljs-string">"jest"</span>,
    <span class="hljs-attr">"coveralls"</span>: <span class="hljs-string">"jest --coverage --coverageReporters=text-lcov | coveralls"</span>, <span class="hljs-comment">// 上报脚本</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>本地执行生成覆盖率的效果，这一步仅演示覆盖率生成，与上报无关。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75404c00583141efb62b50b2e792812a~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">4. 配置Travis 文件，提交代码后自动执行上报</h3>
<p>授权Github账号授权Travis后，在每次提交会按照项目中的<code>.travis.yml</code>配置文件自动执行脚本，只配置自动上报测试报告脚本。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">language: node_js
<span class="hljs-attr">node_js</span>:
  - <span class="hljs-number">14</span> # use nodejs v10 LTS
<span class="hljs-attr">cache</span>: npm
<span class="hljs-attr">script</span>:
  - yarn coveralls # generate <span class="hljs-keyword">static</span> files
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">5. 提交代码触发CI，查看覆盖率</h3>
<p>提交代码后，就可以在Travis-CI后台看到执行过程了，执行成功后等几分钟去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoveralls.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://coveralls.io/" ref="nofollow noopener noreferrer">coveralls.io</a>查看报告，这是我项目的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcoveralls.io%2Fgithub%2Fnihaojob%2Fpopular-message" target="_blank" rel="nofollow noopener noreferrer" title="https://coveralls.io/github/nihaojob/popular-message" ref="nofollow noopener noreferrer">测试报告</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a5e2dd5d3b7493c9d6a23d5a7e6ea8c~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b50e6c759484b6295df557e4d720bd3~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></h3>
<p>点击EMBED按钮获得带分辨率的徽章，拷贝到自己的项目ReadMe文件里就可以了。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92185563e95844558bb817d248497a25~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">结尾</h2>
<p>自己最近的一篇笔记是<a href="https://juejin.cn/post/6978831511164289055" target="_blank" title="https://juejin.cn/post/6978831511164289055">《Vue业务系统落地单元测试》</a>，对单元测试的空白算是补上了一点，趁着热乎劲把自己的小插件也加了一下单元测试，如果你也在学习单元测试，大家一起Star、相互鼓励学习吧。</p>
<p>看到自己的开源小插件<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fnihaojob%2Fpopular-message" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/nihaojob/popular-message" ref="nofollow noopener noreferrer">popular-message</a>从0到200多Star，真的是满心欢喜，感谢阮一峰老师博客的介绍，感谢公众号的推送，感谢素未谋面的朋友提来PR和Issue。</p></div>  
</div>
            
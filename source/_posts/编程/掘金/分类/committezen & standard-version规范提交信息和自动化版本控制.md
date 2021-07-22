
---
title: 'committezen & standard-version规范提交信息和自动化版本控制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4f6b7f3922434fa473f9fa0db150bd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 00:25:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4f6b7f3922434fa473f9fa0db150bd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<ul>
<li>git作为一个开发人员必不可少的工具，代码提交也是日常一个非常频繁的操作，规范提交信息肯定是有必要的。</li>
<li>如果手动按照规范提交代码，不免觉着有点麻烦。怎么办呢？最好是可以使用一个工具。</li>
<li>commitizen就是一个比较合适的git提交规范信息的工具，commitizen可以帮助团队规范化commit提交格式信息，有利于追溯代码。</li>
<li>使用commitizen 进行规范提交提交后，我们就可以使用 standard-version自动化版本控制，例如更新 CHANGELOG.md。</li>
</ul>
<h2 data-id="heading-1">一. Committezen规范提交信息</h2>
<p>当你使用Committezen提交时，系统会提示您在提交时填写所有必需的提交字段， 不需要再深入研究commit提交信息首选格式；命令行上获取有关提交消息格式的即时反馈，并提示输入必填字段即可。</p>
<h5 data-id="heading-2">规范提交信息</h5>
<ol>
<li>规范提交信息的好处如下：</li>
</ol>
<ul>
<li>清晰的历史记录，让开发人员高效地追溯代码</li>
<li>自动化生成CHANGELOG.MD</li>
<li>基于提交的类型，自动决定语义化的版本变更</li>
<li>基于提交类型，触发构建和部署自动化流程</li>
</ul>
<pre><code class="copyable"><type>[optional scope]: <subject>
//空一行
[optional body]
//空一行
[optional footer(s)]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>type 提交的类别，必须是以下类型中的一个:</p>
<pre><code class="copyable">feat：增加一个新功能
fix：修复bug
docs：只修改了文档
style：做了不影响代码含义的修改，空格、格式化、缺少分号等等
refactor：代码重构，既不是修复bug，也不是新功能的修改
perf：改进性能的代码
test：增加测试或更新已有的测试
chore：构建或辅助工具或依赖库的更新
<span class="copy-code-btn">复制代码</span></code></pre>
<p>话不多说，开始实际操作。</p>
<h5 data-id="heading-3">Installing</h5>
<p>First，安装Committeen cli工具</p>
<pre><code class="copyable">npm install commitizen -D
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Next，命令行执行以下命令初始化项目：</p>
<pre><code class="copyable">commitizen init cz-conventional-changelog --save-dev --save-exact
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Or 使用Yarn:</p>
<pre><code class="copyable">commitizen init cz-conventional-changelog --yarn --dev --exact
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Then，将config.commitizen添加到<code>package.json</code>的根目录中，如下所示：</p>
<pre><code class="copyable">"config": &#123;
    "commitizen": &#123;
      "path": "cz-conventional-changelog"
    &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code> package.json</code>中增加如下脚本：</p>
<pre><code class="copyable">"scripts": &#123;
  "commit" : "git-cz"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">现在可以npm run commit，操作如下：</h5>
<ul>
<li>git add . 文件</li>
<li>npm run commit，此时 commitizen 会通过 CLI 对我们进行询问：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa4f6b7f3922434fa473f9fa0db150bd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>选择提交类型后，根据实际情况填写详细信息：</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e6e8d59c17c41ca97f6de2f6831b088~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30b8f43993fc47e199970b0177d07ec5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上就实现半自动化规范提交信息了。</p>
<h2 data-id="heading-5">二. standard-version自动化版本控制</h2>
<h5 data-id="heading-6">Installing</h5>
<pre><code class="copyable">npm i -D standard-version
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">在<code>package.json</code>的scripts中添加：</h5>
<pre><code class="copyable">"scripts": &#123;
  "commit" : "git-cz",
  "release": "standard-version" 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">现在你可以使用 npm run release，操作如下：</h5>
<ul>
<li>git add . 文件</li>
<li>npm run commit</li>
<li>npm run release</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a471a246fa76487bab88c7d87544990f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述操作即可完成CHANGELOG.md自动化版本控制。</p>
<h5 data-id="heading-9">自定义CHANGELOG.md生成</h5>
<p>默认情况下standard-version 只会在 CHANGELOG.md 中记录 feat 和 fix 类型的提交，可以自定义，操作如下：</p>
<ul>
<li>根目录下创建文件： .versionrc, .versionrc.json or .versionrc.js</li>
<li>以创建.versionrc为例，参考配置信息如下：</li>
</ul>
<pre><code class="copyable">&#123;
    "types": [
        &#123;"type": "feat", "section": "Features"&#125;,
        &#123;"type": "fix", "section": "Bug Fixes"&#125;,
        &#123;"type": "chore", "hidden": true&#125;,
        &#123;"type": "docs", "hidden": true&#125;,
        &#123;"type": "style", "hidden": true&#125;,
        &#123;"type": "refactor", "hidden": true&#125;,
        &#123;"type": "perf", "hidden": true&#125;,
        &#123;"type": "test", "hidden": true&#125;
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>type用于匹配 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.conventionalcommits.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.conventionalcommits.org/" ref="nofollow noopener noreferrer">Conventional Commits</a> 使用的的字符串。</li>
<li>section匹配的提交类型将在CHANGELOG.md中显示的部分。</li>
<li>hidden设置为true可在CHANGELOG.md中隐藏匹配的提交类型。</li>
</ul>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fconventional-changelog%2Fconventional-changelog-config-spec%2Ftree%2Fmaster%2Fversions%2F2.1.0" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/conventional-changelog/conventional-changelog-config-spec/tree/master/versions/2.1.0" ref="nofollow noopener noreferrer">CHANGELOG.md-参考配置信息</a></p>
<h5 data-id="heading-10">参考文档：</h5>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjelly.jd.com%2Farticle%2F5f51aa34da524a0147e9529d" target="_blank" rel="nofollow noopener noreferrer" title="https://jelly.jd.com/article/5f51aa34da524a0147e9529d" ref="nofollow noopener noreferrer">规范GIT代码提交信息&自动化版本管理</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.conventionalcommits.org%2Fzh-hans%2Fv1.0.0-beta.4%2F%23%25e7%25ba%25a6%25e5%25ae%259a%25e5%25bc%258f%25e6%258f%2590%25e4%25ba%25a4%25e8%25a7%2584%25e8%258c%2583" target="_blank" rel="nofollow noopener noreferrer" title="https://www.conventionalcommits.org/zh-hans/v1.0.0-beta.4/#%e7%ba%a6%e5%ae%9a%e5%bc%8f%e6%8f%90%e4%ba%a4%e8%a7%84%e8%8c%83" ref="nofollow noopener noreferrer">约定式提交规范</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1ny4y1z77c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1ny4y1z77c" ref="nofollow noopener noreferrer">commitizen不要在瞎提交git信息啦！</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcommitizen%2Fcz-cli" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/commitizen/cz-cli" ref="nofollow noopener noreferrer">commitizen - github</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fcommitizen" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/commitizen" ref="nofollow noopener noreferrer">commitizen - npm</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fstandard-version" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/standard-version" ref="nofollow noopener noreferrer">standard-version - npm</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fconventional-changelog%2Fstandard-version" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/conventional-changelog/standard-version" ref="nofollow noopener noreferrer">standard-version - github</a></p></div>  
</div>
            
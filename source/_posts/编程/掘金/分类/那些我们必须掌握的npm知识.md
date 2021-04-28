
---
title: '那些我们必须掌握的npm知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3458'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 18:10:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=3458'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">简介</h3>
<p><code>npm</code> 是 <code>Node</code> 的模块管理器，功能极其强大。主要分为三个部分：<br></p>
<ol>
<li>
<p><a href="https://www.npmjs.com/" target="_blank" rel="nofollow noopener noreferrer">网站</a><br>
开发者可以在该网站查找各种各样的包，以供使用。</p>
</li>
<li>
<p>注册表（registry）<br>
注册表是一个巨大的数据库，保存了每个包（package）的信息。<br>
例如我们要查询 <code>react</code> 包的信息，可以访问<code>https://registry.npmjs.org/react</code>，就会看到    <code>react</code> 模块所有版本的信息。<br>
模块名后面，还可以跟上版本号或者标签，用来查询某个具体版本的信息，例如：<code>https://registry.npmjs.org/react/16.8.1</code> 查看 <code>react</code> 16.8.1版本的信息 <br>
具体用法就是，<code>https://registry.npmjs.org/</code> 后面跟上模块名，就会得到一个JSON对象，    包含模块所有版本的信息。</p>
</li>
<li>
<p>命令行工具 (CLI)<br>
开发者可以使用该命令行工具和 <code>npm</code> 进行交互，包括包的安装，发布等。</p>
</li>
</ol>
<h3 data-id="heading-1">安装机制</h3>
<p><code>node</code> 模块的首次安装过程可以简单分为四步：</p>
<ol>
<li>执行 <code>npm install <package></code> 命令</li>
<li><code>npm</code> 向 <code>registry</code> 注册表查询模块压缩包的网址</li>
<li>下载压缩包，存放在缓存目录，默认就是 <code>~/.npm</code></li>
<li>解压压缩包到当前项目的 <code>node_modules</code> 目录</li>
</ol>
<p><strong>那么什么是压缩包的网址呢？</strong><br>
我们通过注册表查询模块的信息时，返回的 JSON 对象里面，有一个 <code>dist.tarball</code> 属性，就是模块该版本压缩包的网址。</p>
<h3 data-id="heading-2">安装包的几种方式</h3>
<ul>
<li>
<p>包名安装<br>
<code>npm i react</code> : 默认安装 <code>react</code>模块 <code>latest</code> 标签上的最新版本</p>
</li>
<li>
<p>包名加版本<br>
<code>npm i react@16.8.1</code> : 安装 <code>react</code>模块16.8.1的版本</p>
</li>
<li>
<p>包名加 <code>tag</code><br>
<code>npm i react@next</code> : 安装 <code>react</code>模块 <code>next</code> 标签上的最新版本</p>
</li>
<li>
<p><code>tarball url</code> <br>
<code>npm i https://registry.npmjs.org/react/-/react-16.8.1.tgz</code> : 安装 <code>react</code>模块16.8.1的版本</p>
</li>
<li>
<p><code>tarball file</code> <br>
<code>npm i file: xxxx.xxx.tgz</code> tarball file 可以通过 <code>npm pack</code> 命令得到</p>
</li>
<li>
<p><code>git url</code><br>
<code>npm i git+https://github.com/facebook/react.git</code></p>
</li>
<li>
<p><code>username/project</code> <br>
<code>npm i github:facebook/react</code></p>
</li>
</ul>
<h3 data-id="heading-3">版本号</h3>
<p><code>npm</code> 采用了 <code>semver</code> 规范作为依赖版本管理方案，版本格式一般为：主版本号.次版本号.修订号。</p>
<ul>
<li>主版本号（<code>major</code>）：一般改动很大，不兼容低版本。</li>
<li>次版本号（<code>minor</code>）：兼容同一个大版本的API和用法。</li>
<li>修订号（<code>patch</code>）：一般用来修复bug。</li>
<li>有的时候在修订号后面可能还会有先行版本号，例如 <code>1.0.0-alpha.1</code> ， <code>1.0.0-beta.4</code> ，  <code>2.0.0-rc.1</code> 等。常用的先行版本一般为 <code>alpha</code> ，<code>beta</code> ，<code>rc</code> ，<code>stable</code> ，<code>csp</code> 等。</li>
</ul>
<h3 data-id="heading-4">发布</h3>
<ul>
<li><strong>修改版本号</strong><br>
<code>npm version major</code> : 主版本号加 1，其余版本号归 0。<br>
<code>npm version minor</code> : 次版本号加 1，修订号归 0。<br>
<code>npm version patch</code> : 修订号加 1。<br>
<code>npm version 版本号</code> : 设置版本号为指定的版本号<br>
<code>npm version prerelease</code> : 先行版本号增加1<br>
<code>npm version prerelease --preid=<prerelease-id></code> : 指定先行版本的名字
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 假定现在的版本号是1.1.1</span>
npm version major  <span class="hljs-comment">// 2.0.0</span>
npm version minor  <span class="hljs-comment">// 1.2.0</span>
npm version patch  <span class="hljs-comment">// 1.1.2</span>
npm version prerelease <span class="hljs-comment">// 1.1.2-0</span>
npm version prerelease --preid=alpha <span class="hljs-comment">// 1.1.2-alpha.0</span>
npm version <span class="hljs-number">4.1</span><span class="hljs-number">.2</span>  <span class="hljs-comment">// 4.1.2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
执行 <code>npm version</code> 修改完版本号之后，还会默认执行 <code>git add</code> -> <code>git commit</code> -> <code>git tag</code> 操作，<code>commit</code> 的信息和为 <code>tag</code> 均为版本号。</li>
<li><strong>修改 <code>commit</code> 信息</strong><br>
假如我们需要修改提交信息的话，只需在 <code>npm version</code> 命令后加上 <code>-m</code> 选项即可，<code>%s</code> 会被替换成为版本号。<code>npm version prerelease -m "update %s"</code></li>
<li><strong>禁用版本提交和标记tag</strong><br>
<code>npm version prerelease --no-git-tag-version</code></li>
<li><strong>发布</strong><br>
<code>npm publish</code> : 发布npm包</li>
</ul>
<h3 data-id="heading-5">tag</h3>
<p><code>npm</code> 中的 <code>tag</code> 类似于 <code>git</code> 中的 <code>branch</code> ，发布者可以在指定的 <code>tag</code> 上进行发版，使用者可以选择指定 <code>tag</code> 来安装，默认的<code>tag</code>是 <code>latest</code>。这对于我们日常开发非常有用，很多时候我们想要发布版本来进行验证功能，但是又不想影响正在使用的人，我们就可以利用tag和先行版本来进行发包。<br></p>
<pre><code class="hljs language-js copyable" lang="js">npm publish --tag alpha  <span class="hljs-comment">// 发版到名为alpha的tag上</span>
npm i <package>@<tag>    <span class="hljs-comment">// 从指定tag上安装包</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">link</h3>
<p>我们在日常的开发中经常会有这样的情况：有两个项目分别为A和B，A项目我们封装了一些基本的逻辑，供其他项目进行使用；B项目为我们的业务项目，依赖了A项目。然后现在来了一个新的需求，需要对AB两个项目进行改动，此时我们写完了A项目，想要在B项目中进行验证A项目的逻辑是否正确。<br>
当然我们可以通过A项目发版，然后B项目进行版本升级来进行验证，但是这导致的问题就是可能需要频繁发版；另外一种解决方案就是 <code>link</code>。<br></p>
<p>具体做法如下：</p>
<ol>
<li>在A项目中执行 <code>npm link</code> 命令。</li>
<li>在B项目中执行 <code>npm link A的包名</code> 命令。</li>
</ol>
<p>执行完上述两步之后，此时B项目中 <code>node_modules</code> 里A的依赖就会指向我们的A项目。这样就可以不用发版进行验证，非常方便。当然 <code>link</code> 的本质原理其实就是软连接。</p>
<h3 data-id="heading-7"><code>npx</code></h3>
<p><code>npx</code> 执行 Node 软件包的工具。原理很简单，就是运行的时候，会到 <code>node_modules/.bin</code> 路径和环境变量 <code>$PATH</code> 里面，检查命令是否存在；如果存在，则执行；不存在，则进行临时安装，然后执行，执行完毕将包删除。</p>
<h3 data-id="heading-8">配置</h3>
<p><code>npm config</code> 命令用来管理 npm 的配置</p>
<ul>
<li><code>npm config set <key> <value></code> : 设置一些配置</li>
<li><code>npm config get <key></code> : 获取指定的配置</li>
<li><code>npm config delete <key></code> : 删除指定的配置</li>
<li><code>npm config list</code> : 配置列表</li>
<li><code>npm config edit</code> : 用编辑器打开配置文件<br></li>
</ul>
<p>例如我们经常会对 <code>npm</code> 的 <code>registry</code> 进行设置<br>
<code>npm config set registry https://registry.npm.taobao.org/</code></p>
<h3 data-id="heading-9"><code>npm ci</code></h3>
<ul>
<li>该命令只能一次安装整个项目，不能添加单独的依赖项</li>
<li>项目必须有 <code>package-lock.json</code> 文件</li>
<li>每次开始安装之前，都会清除 <code>node_modules</code></li>
<li>不会改写 <code>package.json</code> 和 <code>package-lock.json</code> 文件</li>
<li>安装速度更快，更严格</li>
</ul>
<p>很多时候，我们新克隆一个项目，进行 <code>npm i</code> 安装的时候，经常会出现改动 <code>package.json</code> 和 <code>package-lock.json</code> 文件的情况，这有的时候会带来一些风险，而此时使用 <code>npm ci</code> 就是一个好的选择。</p>
<h3 data-id="heading-10">查询包信息</h3>
<ul>
<li><code>npm view 包名</code> : 显示包的详细信息</li>
<li><code>npm view 包名 versions</code> : 显示包的所有历史版本</li>
<li><code>npm repo 包名</code> : 打开包的源码仓库页面</li>
<li><code>npm docs 包名</code> : 打开包的文档地址</li>
</ul>
<h3 data-id="heading-11">其他</h3>
<ul>
<li><code>npm login</code> : 登陆 npm</li>
<li><code>npm whoami</code> : 显示 npm 用户名</li>
<li><code>npm bin</code> : 显示 npm 的 bin 文件夹的路径</li>
<li><code>npm root</code> : 显示 npm 根目录</li>
</ul>
<h3 data-id="heading-12">参考文章</h3>
<ul>
<li><a href="https://www.npmjs.cn/" target="_blank" rel="nofollow noopener noreferrer">npm 中文文档</a></li>
<li><a href="http://www.ruanyifeng.com/blog/2019/02/npx.html" target="_blank" rel="nofollow noopener noreferrer">npx 使用教程</a></li>
<li><a href="http://www.ruanyifeng.com/blog/2016/01/npm-install.html" target="_blank" rel="nofollow noopener noreferrer">npm 模块安装机制简介</a></li>
<li><a href="https://tian-cai.github.io/my-blog/" target="_blank" rel="nofollow noopener noreferrer">阿呆的博客</a></li>
</ul></div>  
</div>
            
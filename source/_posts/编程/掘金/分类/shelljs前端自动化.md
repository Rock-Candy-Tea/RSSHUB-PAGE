
---
title: 'shelljs前端自动化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a204995f879468ca9ffb1f87a8775b4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 01:20:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a204995f879468ca9ffb1f87a8775b4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">场景</h2>
<p>在开发过程中，常会遇到如下命令：</p>
<pre><code class="copyable">git add .
git commit -m '*****'
git push 
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">Shelljs</h2>
<p>这个库能够让我们在js文件中执行shell命令。shelljs做的事就是自动化，从耗时的重复性常规动作里解放出来，提升开发效率和工作心情。</p>
<h5 data-id="heading-2">1.Installing</h5>
<pre><code class="copyable">$ npm install  shelljs -D
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">2. 在根目录下新建文件shell.js，内容如下：</h5>
<pre><code class="copyable">let shell = require('shelljs')
let name = process.argv[2] || 'Auto-commit';
let exec = shell.exec

if (exec('git add .').code !== 0) &#123;
    echo('Error: Git add failed')
    exit(1)
&#125;
if (exec(`git commit -am "$&#123;name&#125;"`).code !== 0) &#123;
    echo('Error: Git commit failed')
    exit(1)
&#125;
if (exec('git push').code !== 0) &#123;
    echo('Error: Git commit failed')
    exit(1)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">3.只用一条命令执行以上所有任务，在package.json中加入,方法如下:</h5>
<pre><code class="copyable">"script":&#123;
    "push":"node ./shell.js"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">$ npm run push 测试shelljs提交代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a204995f879468ca9ffb1f87a8775b4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上述操作就可以通过执行shelljs脚本提交代码啦。</p>
<h2 data-id="heading-5">Examples</h2>
<p>1.运行命令环境时，配置文件config根据开发和生产环境进行区分, 所以这里根据命令环境，将文件复制到目标文件，以vue.config.js为例，区分开发和生产环境：</p>
<pre><code class="copyable">// 运行命令环境 用于config区分开发和生成环境
const shell = require('shelljs')
const apiEnv = process.env.API_ENV
shell.cp(`./src/config/$&#123;apiEnv&#125;.js`, './src/config/index.js')
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0b451bc7133466db95e36835ac263d9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53770f9776774d4db5c17b3bb4b3395e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">基本语法</h2>
<ul>
<li>shell.which(command)</li>
</ul>
<p>在环境变量PATH中寻找指定命令的地址，判断该命令是否可执行，返回该命令的绝对地址</p>
<ul>
<li>echo</li>
</ul>
<p>在控制台输出指定内容</p>
<ul>
<li>exit(code)</li>
</ul>
<p>以退出码为code退出当前进程</p>
<pre><code class="copyable">//引入shelljs
var shell = require('shelljs')
 
//检查控制台是否以运行`git `开头的命令
if (!shell.which('git')) &#123;
  //在控制台输出内容
  shell.echo('Sorry, this script requires git');
  shell.exit(1);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>rm（[options，] file [，file ...]）</li>
</ul>
<p>删除一个目录中一个或多个文件或目录，一旦删除，无法恢复。
常用参数：
-f:强制删除文件;
-i:删除之前先询问用户;
-r:递归处理目录;
-v:显示处理过程;</p>
<pre><code class="copyable">shell.rm('-rf','out/Release')  //强制递归删除`out/Release目录` 
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>cp([options,] source_array, dest)</li>
</ul>
<p>用来将一个或多个源文件或目录复制到指定的文件或目录</p>
<pre><code class="copyable">shell.cp('-R','stuff/','out/Release')  //将`stuff/`中所有内容拷贝至`out/Release`目录
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>cd</li>
</ul>
<p>切换工作目录至指定的相对路径或绝对路径。cd..为返回上一级，cd-回到前一目录</p>
<pre><code class="copyable">shell.cd('lib')  //进入`lib`目录
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ls</li>
</ul>
<p>用来显示目标列表</p>
<pre><code class="copyable">ls(path.join('bundle', 'css/')).forEach(cssName => &#123;
  ***
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>sed([options,] search_regex, replacement, file_array)</li>
</ul>
<p>将file_array中符合search_regex的内容替换为replacement，支持正则的捕获组自引用。一次处理一行内容，处理完成后把缓冲区内容送往屏幕，然后处理下一行，循环直至结束。</p>
<pre><code class="copyable">/* -i表示直接作用源文件 */
/* 将build_version字段替换为'v0.1.2' */
  shell.sed('-i', 'BUILD_VERSION', 'v0.1.2', file);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>cat([options,] file [, file ...])</li>
</ul>
<p>将一个或多个文件内容读入，指定一个文件时读入该文件，指定多个文件时将内容连接在一起读入。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fshelljs" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/shelljs" ref="nofollow noopener noreferrer">shelljs-npm</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocumentup.com%2Fshelljs%2Fshelljs" target="_blank" rel="nofollow noopener noreferrer" title="https://documentup.com/shelljs/shelljs" ref="nofollow noopener noreferrer">shelljs官方文档</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshelljs%2Fshelljs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shelljs/shelljs" ref="nofollow noopener noreferrer">shelljs-github</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.kancloud.cn%2Foutsider%2Fclitool%2F313191" target="_blank" rel="nofollow noopener noreferrer" title="https://www.kancloud.cn/outsider/clitool/313191" ref="nofollow noopener noreferrer">shelljs中文文档介绍</a></p></div>  
</div>
            
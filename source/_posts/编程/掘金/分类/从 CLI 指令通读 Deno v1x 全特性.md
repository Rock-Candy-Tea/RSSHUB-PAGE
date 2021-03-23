
---
title: '从 CLI 指令通读 Deno v1.x 全特性'
categories: 
 - 编程
 - 掘金
 - — 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2691d6aa39e44e4ad694e85307563fd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 22 Mar 2021 19:53:31 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2691d6aa39e44e4ad694e85307563fd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2691d6aa39e44e4ad694e85307563fd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>随着掘金开启了第一期技术专题之“<a href="https://juejin.im/post/6854573219266887694" target="_blank" rel="nofollow noopener noreferrer">聊聊 Deno 的一些事儿</a>”的征稿活动，赶在截稿日的最后一天（08/04），一篇新的 Deno 文章呼之欲出。拜读了下其他伙伴的 Deno 征文，有 Deno TCP Echo Server、在 Deno 上进行 TDD 实践、Deno 程序如何调用 Rust、Deno 命令行开发方案、Deno 造一个简单的 Router、Deno 的简单应用以及 Deno 从入门到跑路、Deno 从零到架构开发等等文章，每篇都很生动精彩。那么...如果你是这两天看到的这篇文章，觉得有所帮助，<strong>欢(gan)迎(jin)来我的掘金文章里点点赞</strong>，可以让我获得一个不错的掘金周边礼物~如果是未来某天看到的，<a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer"><strong>戳这里</strong></a>。</p>
<ul>
<li><strong>掘金文章点赞传送门</strong>：<a href="https://juejin.im/user/3702810890732904/posts" target="_blank" rel="nofollow noopener noreferrer">juejin.im/user/370281…</a></li>
</ul>
<p>本篇的主题是“通读 Deno 架构”，切入的方向是“命令行指令通读”的角度。关于“通读 Deno 架构”主题，感觉可以挖坑出一个系列文章来，比如从 CLI、标准库、内核以及工具库角度来深入到源码之中。</p>
<p>从命令行指令可以看出，Deno 官方内置了很多工具用来测试、打包、格式化、Linter、安装依赖库等；而在 Node 中，我们可能需要寻找并选型大量的第三方库来填补每一个功能。一起来看看都有哪些工具吧！<strong>本文写作时间 14h+</strong>，大量重构后沉淀出的目录结构：</p>
<ul>
<li><strong>通读命令行基本信息</strong>：从 deno --help 来通读通用指令、内置工具包和环境变量；</li>
<li><strong>通读 Deno 通用指令</strong>：逐个通读通用指令；</li>
<li><strong>通读 Deno 内置工具包</strong>：逐个通读 14 个 Deno 内置工具关键功能；</li>
<li><strong>通读 Deno 环境变量</strong>：将环境变量分离出来进行解析；</li>
</ul>
<blockquote>
<p>《Deno 钻研之术》系列于 Deno v1 发布之日全新推出，不定期更新在 Github 中（<a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer">github.com/hylerrix/de…</a> ✨），官网（<a href="http://deno-tutorial.js.org/" target="_blank" rel="nofollow noopener noreferrer">deno-tutorial.js.org</a>）。让我们一起循序渐进学 Deno，先易后难补 Node，面向未来开发属于自己的 Deno Web App。欢迎订阅，欢迎交流。</p>
</blockquote>
<h2 data-id="heading-0">通读命令行基本信息</h2>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8eea007d4f704173883e0b7fbc9e39d9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">deno --help, help</h3>
<p>了解一个命令的最快速实用的方法就是直接阅读其帮助文档，每行帮助信息都是简短且关键的介绍，不难理解和翻译。终端输入如下命令（help 或 --help 用来打印全局帮助信息或给定子命令的帮助信息）：</p>
<pre><code class="copyable">$ deno --help
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从而获得 Deno 的基本帮助信息：</p>
<ul>
<li>deno 1.2.2（2020-08-01 发布）</li>
<li>一个安全的 JavaScript 和 TypeScript 运行时</li>
<li>文档：<a href="https://deno.land/manual" target="_blank" rel="nofollow noopener noreferrer">deno.land/manual</a></li>
<li>模块：<a href="https://deno.land/std/" target="_blank" rel="nofollow noopener noreferrer">deno.land/std/</a> <a href="https://deno.land/x/" target="_blank" rel="nofollow noopener noreferrer">deno.land/x/</a></li>
<li>Bugs：<a href="https://github.com/denoland/deno/issues" target="_blank" rel="nofollow noopener noreferrer">github.com/denoland/de…</a></li>
<li>使用方式：deno [选项] [子命令]</li>
</ul>
<pre><code class="copyable"># 以 REPL 模式启动：
$ deno
# 执行一个脚本：
$ deno run https://deno.land/std/examples/welcome.ts
# 在 Shell 中执行一段代码：
$ deno eval "console.log(30933 + 404)"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">汇总 26 个通用指令</h3>
<p>结合 deno --help 中出现的选项以及通常也会在 14 个内置工具包的帮助信息中看到的选项，将通用指令整理在这里做一个通览（只要某指令被使用两次及以上便视为通用指令，几乎涵盖了所有）：</p>
<ul>
<li>P.S：在纠结到底称为“参数”还是“选项”还是“指令”的时候，差点选了“参数”，最后选择了“指令”。</li>
</ul>
<blockquote>
<p>注：以下表格整理了好几小时，如果能帮到你，别忘记多多点赞哟。挖个坑：以后可以绘制出一个思维导图来。同时，如果哪里有差错，欢迎在评论区 Github 仓库 issues 里留言哈。</p>
</blockquote>







































































































































































<table><thead><tr><th>序号</th><th>选项</th><th>哪些工具可以使用？</th><th>用途</th></tr></thead><tbody><tr><td>01</td><td>-h, --help</td><td>全部</td><td>打印帮助信息</td></tr><tr><td>02</td><td>-L, --log-level </td><td>全部</td><td>设置日志级别 [可能的值: debug, info]</td></tr><tr><td>03</td><td>-q, --quiet</td><td>全部</td><td>禁止诊断输出；默认情况下，子命令会将可读性友好的诊断消息打印到 stderr；如果设置了这个标志，则将这些消息限制为 errors</td></tr><tr><td>04</td><td>-A, --allow-all</td><td>run, install, test</td><td>允许所有权限，这将禁用所有安全限制</td></tr><tr><td>05</td><td>--allow-env</td><td>run, install, test</td><td>允许环境访问，例如读取和设置环境变量</td></tr><tr><td>06</td><td>--allow-hrtime</td><td>run, install, test</td><td>允许高精度时间测量，高精度时间能够在计时攻击和特征识别中使用</td></tr><tr><td>07</td><td>--allow-net=</td><td>run, install, test</td><td>允许网络访问。可以指定一系列用逗号分隔的域名，来提供域名白名单</td></tr><tr><td>08</td><td>--allow-plugin</td><td>run, install, test</td><td>允许加载插件。请注意：这目前是一个不稳定功能</td></tr><tr><td>09</td><td>--allow-read=</td><td>run, install, test</td><td>允许读取文件系统。可以指定一系列用逗号分隔的目录或文件，来提供文件系统白名单。</td></tr><tr><td>10</td><td>--allow-run</td><td>run, install, test</td><td>允许运行子进程。请注意，子进程不在沙箱中运行，因此没有与 deno 进程相同的安全限制，请谨慎使用</td></tr><tr><td>11</td><td>--allow-write=</td><td>run, install, test</td><td>允许写入文件系统。您可以指定一系列用逗号分隔的目录或文件，来提供文件系统白名单</td></tr><tr><td>12</td><td>--cert </td><td>run, install, bundle, chche, eval, info, test, upgrade, repl</td><td>从 PEM 编码的文件中加载证书颁发机构</td></tr><tr><td>13</td><td>-c, --config </td><td>run, install, budle, cache, test</td><td>读取 tsconfig.json 配置文件</td></tr><tr><td>14</td><td>--unstable</td><td>run, install, bundle, cache, doc, eval, fmt, info, lint, test, types, repl</td><td>开启不稳定的 APIs 支持</td></tr><tr><td>15</td><td>--inspect=<a href="https://juejin.cn/post/undefined">HOST:PORT</a></td><td>run, eval, test, repl</td><td>激活监听器 主机:端口 (默认: 127.0.0.1:9229)</td></tr><tr><td>16</td><td>--inspect-brk=<a href="https://juejin.cn/post/undefined">HOST:PORT</a></td><td>run, eval, test, repl</td><td>在 主机:端口 上激活监听器，并在用户脚本启动时中断</td></tr><tr><td>17</td><td>--v8-flags=</td><td>run, eval, test, repl</td><td>设置 V8 命令行选项。帮助： --v8-flags=--help</td></tr><tr><td>18</td><td>--cached-only</td><td>run, test</td><td>要求远程依赖项已经被缓存</td></tr><tr><td>19</td><td>-r, --reload=<CACHE_BLOCKLIST></td><td>run, cache, doc, test</td><td>重新加载源代码缓存（重新编译TypeScript）。重新加载全部/仅标准模块/特定模块</td></tr><tr><td>20</td><td>--lock </td><td>run, bundle, cache, test</td><td>检查指定的锁文件</td></tr><tr><td>21</td><td>--lock-write</td><td>run, bundle, cache, test</td><td>写入锁文件，和 --lock 一起使用</td></tr><tr><td>22</td><td>--no-check</td><td>run, cache, info, test</td><td>禁用 TypeScript 的类型检查，这会大大减少程序的启动时间</td></tr><tr><td>23</td><td>--no-remote</td><td>run, cache, test</td><td>不解析远程模块</td></tr><tr><td>24</td><td>--seed </td><td>run, test</td><td>Math.random() 种子</td></tr><tr><td>25</td><td>--importmap </td><td>run, install, bundle, test</td><td>不稳定：读取 import map 文件</td></tr><tr><td>26</td><td>--json</td><td>doc, info</td><td>以 JSON 格式输出文档</td></tr></tbody></table>
<p>具体通用指令会在“通读 Deno 通用指令”章节进行深入了解。</p>
<h3 data-id="heading-3">汇总 14 个内置工具包</h3>
<p>帮助信息中初步介绍了这 14 个内置工具（为了强调每个工具的独立性，这些工具暂时都翻译为“xx 器”）：</p>































































































<table><thead><tr><th>序号</th><th>名称</th><th>命令</th><th>功能</th></tr></thead><tbody><tr><td>01</td><td>运行器</td><td>deno run</td><td>运行指定文件名或 URL 程序。 使用“-”作为文件名从标准输入中读取</td></tr><tr><td>02</td><td>脚本安装器</td><td>deno install</td><td>将脚本安装为可执行文件</td></tr><tr><td>03</td><td>打包器</td><td>deno bundle</td><td>将模块和依赖项打包到单个文件中</td></tr><tr><td>04</td><td>缓存器</td><td>deno cache</td><td>缓存依赖</td></tr><tr><td>05</td><td>文档生成器</td><td>deno doc</td><td>显示某模块的文档</td></tr><tr><td>06</td><td>执行器</td><td>deno eval</td><td>执行一段脚本</td></tr><tr><td>07</td><td>格式化器</td><td>deno fmt</td><td>格式化源文件</td></tr><tr><td>08</td><td>依赖检查器</td><td>deno info</td><td>显示有关缓存的信息或与源文件相关的信息</td></tr><tr><td>09</td><td>规范器</td><td>deno lint</td><td>规范化源文件</td></tr><tr><td>10</td><td>测试器</td><td>deno test</td><td>执行测试</td></tr><tr><td>11</td><td>类型器</td><td>deno types</td><td>打印运行时 TypeScript 声明</td></tr><tr><td>12</td><td>补全器</td><td>deno completions</td><td>生成 Shell 补全信息</td></tr><tr><td>13</td><td>升级器</td><td>deno upgrade</td><td>将 Deno 可执行文件升级到给定版本</td></tr><tr><td>14</td><td>REPL 器</td><td>deo repl</td><td>读取/执行/打印/循环</td></tr></tbody></table>
<p>具体工具会在“通读 Deno 内置工具包”章节进行深入了解。</p>
<h3 data-id="heading-4">汇总 6 个基本环境变量</h3>
<p>帮助信息里初步介绍了这 6 个环境变量：</p>















































<table><thead><tr><th>序号</th><th>变量名</th><th>用途</th><th>备注</th></tr></thead><tbody><tr><td>01</td><td>DENO_DIR</td><td>设置缓存目录</td><td></td></tr><tr><td>02</td><td>DENO_INSTALL_ROOT</td><td>设置 Deno 安装的软件包输入目录</td><td>默认为 $HOME/.deno/bin</td></tr><tr><td>03</td><td>NO_COLOR</td><td>设置禁止使用颜色</td><td></td></tr><tr><td>04</td><td>DENO_CERT</td><td>从 PEM 编码的文件加载证书颁发机构</td><td></td></tr><tr><td>05</td><td>HTTP_PROXY</td><td>HTTP 请求的代理地址</td><td>模块 downloads 和 fetch</td></tr><tr><td>06</td><td>HTTPS_PROXY</td><td>HTTPS 请求的代理地址</td><td>模块 downloads 和 fetch</td></tr></tbody></table>
<p>具体基本环境变量会在“通读 Deno 环境变量”章节进行深入了解。</p>
<h2 data-id="heading-5">通读 Deno 通用指令</h2>
<blockquote>
<p>相关实战代码都收录在<a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer">《Deno 钻研之术》仓库</a>中的 demos/ningowood/v1-cli-example 下。</p>
</blockquote>
<p>本章目录按照 14 个内置工具使用到的数量进行由大到小的排序。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/841e0c2c38684bd68dcb928a70a48093~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">(01) --log-level/--quiet</h3>
<p>这两个指令所有内置工具都可以使用。</p>
<p>在 --log-level 中，可以加入 debug 或 info 参数 来设置日志等级。其中设置为 debug 时会出现如下信息。此时是非常详细的信息，一个简单的启动和网络访问都会打印出很多行的日志来。</p>
<pre><code class="copyable">$ deno run --allow-net --log-level debug main.ts
Deno isolate init with snapshots.
rust:shared_queue:reset
DEBUG JS - cwd /Users/&#123;$HOME&#125;/WorkSpace/Hylerrix/deno-tutorial/demos/ningowood/v1-cli-example
DEBUG JS - args []
...
⚠️️  Granted network access to "0.0.0.0:8000"
New listener 3 0.0.0.0:8000
Welcome to Deno 🦕
http://localhost:8000/
DEBUG JS - sendAsync op_accept
<span class="copy-code-btn">复制代码</span></code></pre>
<p>--quiet 指令于 2019-10-20 日的 issues 被提出<a href="https://github.com/denoland/deno/issues/3162" target="_blank" rel="nofollow noopener noreferrer">新功能建议（#3162）</a>，2020-03-10 日成功添加。目的之一是解决多次运行同一程序但获得到不同的输出的情况。官方文档上该指令介绍是：将本来可读性友好的诊断消息限制为通用错误类型。</p>
<h3 data-id="heading-7">(02) --unstable/--cert/--config</h3>
<p>这三个指令是除了所有指令都能用到的 --log-level 和 --quiet 外，被使用量最大的前三名。</p>
<p>--unstable 允许程序执行时使用不稳定的 API 列表。什么样的 API 是不稳定的？官网文档这么解答：</p>
<blockquote>
<p>纵使 Deno v1 开始 Deno 命名空间的 API 稳定起来，但并非 Deno 的所有功能都可以投入生产。由于尚未准备就绪的功能仍处于草稿阶段，因此将其锁定在 --unstable 命令行标志后面。</p>
</blockquote>
<p>不稳定的 API 大多没有经过安全性检查，将来可能会发生重大的 API 更改，并且尚未准备好投入生产环境。</p>
<p>同时，Deno 的标准模块（<a href="https://deno.land/std/%EF%BC%89%E4%B9%9F%E5%B0%9A%E4%B8%8D%E7%A8%B3%E5%AE%9A%E3%80%82%E5%BD%93%E5%89%8D" target="_blank" rel="nofollow noopener noreferrer">deno.land/std/）也尚不稳定。…</a> Deno 对标准模块的版本与 CLI 不同，以强调不稳定这一特点。 请注意，与 Deno 命名空间不同，使用标准模块不需要 --unstable 标志（除非标准模块本身使用了不稳定的 Deno 功能）。测试方式：</p>
<pre><code class="copyable">$ deno install --unstable --allow-read --allow-write --allow-net https://deno.land/x/pagic/mod.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<p>--cert 用来从 PEM 编码的文件中加载证书颁发机构。那么问题来了：</p>
<ul>
<li><strong>什么是 PEM</strong>？PEM 这是一种容器格式，可以只包含公共证书，或者可以包括完整的证书链，包括公共密钥，私钥和根证书；名称来源于网络安全领域一款增强安全的私人邮件类型 Privacy Enhanced Mail。</li>
<li><strong>PEM 格式</strong>？以"-----BEGIN..."开头, "-----END..."结尾，内容是 ASCII（Base64）编码。</li>
<li><strong>查看 PEM 格式证书的信息</strong>？openssl x509 -in certificate.pem -text -noout。</li>
</ul>
<p>--config 用来读取 tsconfig.json 文件，当然也可以读取其它名称的文件来当作 tsconfig.json。</p>
<pre><code class="copyable">deno run --allow-net main.ts --config tsconfig.json
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">(03) --inspect*/--v8-flags</h3>
<p>这几个指令均只能在 run、eval、test 或 repl 四个工具包中使用。</p>
<p>Deno 支持 V8 Inspector Protocol，使用 --inspect 或 --inspect-brk 指令可以在 Chrome Devtools 或其他支持该协议的客户端（比如 VSCode）上调试 Deno 程序。</p>
<p>--inspect 允许在任何时间点连接调试器，而 --inspect-brk 选项会等待调试器连接，在第一行代码处暂停执行。输入以下代码，打开 chrome://inspect，点击 target 旁边的 Inspect 进行调试测试：</p>
<pre><code class="copyable">$ deno run --inspect-brk --allow-read --allow-net https://deno.land/std/http/file_server.ts
Debugger listening on ws://127.0.0.1:9229/ws/4947ac73-b9fc-4fd2-9336-c6071f4f3e9e
Debugger session started.
Debugger session ended: WebSocket protocol error: Connection reset without closing handshake.
HTTP server listening on http://0.0.0.0:4507/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>--v8-flags 前身是 --v8-options，于 <a href="https://github.com/denoland/deno/pull/3389" target="_blank" rel="nofollow noopener noreferrer">2019-11-21 日（#3389）</a>更替为 --v8-flags，负责设置 v8 的命令行选项。可以这样了解具体参数：</p>
<pre><code class="copyable">$ deno run --v8-flags=--help main.ts
SSE3=1 SSSE3=1 SSE4_1=1 SSE4_2=1 SAHF=1 AVX=1 FMA3=1 BMI1=1 BMI2=1 LZCNT=1 POPCNT=1 ATOM=0
Synopsis:
  shell [options] [--shell] [<file>...]
  d8 [options] [-e <string>] [--shell] [[--module] <file>...]
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">(04) --allow-*</h3>
<p>--allow-* 作为一个整体，只被 run、install 和 test 三个工具分别使用，其中包括：</p>
<ul>
<li>-A, --allow-all：允许所有权限，这将禁用所有安全限制。</li>
<li>--allow-env：允许环境访问，例如读取和设置环境变量</li>
<li>--allow-hrtime：允许高精度时间测量，高精度时间能够在计时攻击和特征识别中使用</li>
<li>--allow-net：允许网络访问。可以指定一系列用逗号分隔的域名，来提供域名白名单</li>
<li>--allow-plugin：允许加载插件。请注意：这目前是一个不稳定功能</li>
<li>--allow-read：允许读取文件系统。可以指定一系列用逗号分隔的目录或文件，来提供文件系统白名单。</li>
<li>--allow-run：允许运行子进程。请注意，子进程不在沙箱中运行，因此没有与 deno 进程相同的安全限制，请谨慎使用</li>
<li>--allow-write：允许写入文件系统。您可以指定一系列用逗号分隔的目录或文件，来提供文件系统白名单</li>
</ul>
<p>在 Denon （监听 Deno 应用程序中的所有更改并自动重新启动，还可以配置更多功能）中，可以这样简单的设置在 denon.config.ts 中：</p>
<pre><code class="copyable">import &#123; DenonConfig &#125; from "https://deno.land/x/denon/mod.ts"
import &#123; config as env &#125; from "https://deno.land/x/dotenv/mod.ts"

const config: DenonConfig = &#123;
  scripts: &#123;
    start: &#123;
      allow: [ "env", "net", "read", "write", "plugin" ],
      ...
&#125;

export default config
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 denon start 这将默认替换为：</p>
<pre><code class="copyable">$ deno run --allow-net --allow-env --allow-write --allow-read --allow-plugin --unstable main.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">(05) --cached-only/--seed</h3>
<p>这两个指令只被 run 和 test 工具使用。</p>
<p>--cached-only 要求远程依赖已经被缓存，当我们使用这个指令从远程找一个没有缓存过其软件包的 Deno 程序执行的时候，会报错无法从缓存中找到这个软件包：</p>
<pre><code class="copyable">$ deno run --allow-net --cached-only not-cache.ts
error: Cannot find module "https://deno.land/x/alosaur@v0.21.1/mod.ts"
from "file:///Users/&#123;$HOME&#125;/WorkSpace/Hylerrix/deno-tutorial/
...demos/ningowood/v1-cli-example/not-cache.ts" in cache, --cached-only is specified
<span class="copy-code-btn">复制代码</span></code></pre>
<p>--seed 为程序提供种子随机值。程序怎么获取这个随机值？留下来以后思考。</p>
<pre><code class="copyable">$ deno run --allow-net --seed 1 main.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">(06) --reload/--lock*/.--no-*</h3>
<p>这五个指令是剩余的最后指令，分别被以下工具使用：</p>
<ul>
<li>--reload：run, cache, doc, test</li>
<li>--lock：run, bundle, cache, test</li>
<li>--lock-write：run, bundle, cache, test</li>
<li>--no-check：run, cache, info, test</li>
<li>--no-remote：run, cache, test</li>
</ul>
<p>--reload 将重新缓存源码，并重新编译 TypeScript，其中又包括：</p>
<ul>
<li>--reload：重新加载所有源码</li>
<li>--reload=<a href="https://deno.land/std%EF%BC%9A%E9%87%8D%E6%96%B0%E7%BC%93%E5%AD%98%E6%A0%87%E5%87%86%E5%BA%93%E6%BA%90%E7%A0%81" target="_blank" rel="nofollow noopener noreferrer">deno.land/std：重新缓存标准库…</a></li>
<li>--reload=<a href="https://deno.land/std/fs/utils.ts,https://deno.land/std/fmt/colors.ts%EF%BC%9A%E9%87%8D%E6%96%B0%E7%BC%93%E5%AD%98%E6%8C%87%E5%AE%9A%E7%9A%84%E5%A4%9A%E4%B8%AA%E6%BA%90%E7%A0%81%E5%88%97%E8%A1%A8" target="_blank" rel="nofollow noopener noreferrer">deno.land/std/fs/util…</a></li>
</ul>
<p>--lock 和 --lock-write 用来检查锁文件，因为在眼花缭乱的各大库的多版本中，管理、锁定文件版本也是很重要的；--no-check 禁用 TypeScript 的类型检查，从而大大减少程序的启动时间；--no-remote 来不解析远程模块。</p>
<pre><code class="copyable">$ deno run --allow-net --reload main.ts
$ deno run --allow-net --lock lock.json main.ts
Subresource integrity check failed --lock=lock.json
https://deno.land/std@0.63.0/textproto/mod.tsa
$ deno run --allow-net --no-check main.ts
$ deno run --allow-net --no-remote main.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">通读 Deno 内置工具包</h2>
<blockquote>
<p>相关实战代码都收录在<a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer">《Deno 钻研之术》仓库</a>中的 demos/ningowood/v1-cli-example 下。</p>
</blockquote>
<p>由于本文在“通读 Deno 通用指令章节”将 Deno 内置工具包可复用的指令都已经一一介绍了一遍。本章重点以目录的形式强调 14 个内置工具包的独立性（中文名以 xx 器来命名），并进行除了通用指令外的一些独特介绍。</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b206d2c987949df9f04b5e6625e56aa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">(01) 运行器：deno run</h3>
<p>run 工具支持近乎 100% 的通用指令列表（--json 指令除外），且上一个章节的通用指令示例都以 run 工具来举例，这里无需多讲。</p>
<ul>
<li>deno-run：执行一个模块程序，可以是一个文件名或 URL 地址。</li>
<li>使用方式：deno run [选项] <脚本参数>...</li>
<li>常用示例：</li>
</ul>
<pre><code class="copyable"># 默认情况下所有的程序都会运行在安全沙盒中，无法访问硬盘、网络或生成子进程。
$ deno run https://deno.land/std/examples/welcome.ts
# 给予所有权限
$ deno run -A https://deno.land/std/http/file_server.ts
# 给予读取权限和网络监听权限：
$ deno run --allow-read --allow-net https://deno.land/std/http/file_server.ts
# 给予允许读取权限的硬盘目录白名单：
$ deno run --allow-read=/etc https://deno.land/std/http/file_server.ts
# Deno 允许指定文件名 “-” 以从 stdin 中读取文件。
$ curl https://deno.land/std/examples/welcome.ts | target/debug/deno run -
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">(02) 脚本安装器：deno install</h3>
<ul>
<li>
<p>deno-install：将脚本作为可执行文件安装在安装路径的根目录的 bin 目录中。</p>
</li>
<li>
<p>使用方式：deno install [选项] <命令>...</p>
</li>
<li>
<p>独特指令：</p>
</li>
<li>
<ul>
<li>-f, --force：强制覆盖现有安装</li>
<li>-n, --name ：可执行文件名</li>
<li>--root ：安装路径</li>
</ul>
</li>
<li>
<p>常用示例：</p>
</li>
</ul>
<pre><code class="copyable">$ deno install --allow-net --allow-read https://deno.land/std/http/file_server.ts
$ deno install https://deno.land/std/examples/colors.ts
# 要更改可执行文件的名称，请使用 -n/-name：
$ deno install --allow-net --allow-read -n serve https://deno.land/std/http/file_server.ts
# 可执行文件名称默认情况下被推断：
#   - 尝试获取 URL 路径文件结构。正如上方上面的例子
#     become 'file_server'.
#   - 如果文件结构是通用名称（例如“main”、“mod”、“index”或“ cli”），并且该路径没有父级，则采用父级路径的文件名。否则，使用通用名称解决。
# 要更改安装根目录，请使用 --root：
$ deno install --allow-net --allow-read --root /usr/local https://deno.land/std/http/file_server.ts
# 按优先级确定安装路径的根目录：
#   - --root option
#   - DENO_INSTALL_ROOT 环境变量
#   - $HOME/.deno
# 如果需要，必须将它们手动添加到路径中。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">(03) 打包器：deno bundle</h3>
<ul>
<li>deno-bundle：打包。</li>
<li>使用方式：deno bundle [OPTIONS] <source_file> [out_file]</li>
<li>常用示例：</li>
</ul>
<pre><code class="copyable"># 输入一个单独的 JavaScript 文件，其拥有所有相关依赖：
$ deno bundle https://deno.land/std/examples/colors.ts colors.bundle.js
# 如果没有指定输入文件，输入将会写入到标准输出流中：
$ deno bundle https://deno.land/std/examples/colors.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">(04) 缓存器：deno cache</h3>
<ul>
<li>deno-cache：递归地缓存并编译远程依赖</li>
<li>使用方式：deno cache [OPTIONS] ...</li>
<li>常用示例：</li>
</ul>
<pre><code class="copyable"># 下载并编译包括所有静态依赖项的模块并保存在
# 本地缓存中，无需运行任何代码：
$ deno cache https://deno.land/std/http/file_server.ts
# 除非以后运行此模块，否则不会触发下载或编译
# --reload 已指定。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">(05) 文档生成器：deno doc</h3>
<ul>
<li>
<p>deno-doc：显示某模块的文档</p>
</li>
<li>
<p>使用方式：deno doc [OPTIONS] [ARGS]</p>
</li>
<li>
<p>独特指令：</p>
</li>
<li>
<ul>
<li>--private：输出私有文档</li>
</ul>
</li>
<li>
<p>常用示例：</p>
</li>
</ul>
<pre><code class="copyable"># 输出文档到标准输入流中：
$ deno doc ./path/to/module.ts
# 输出私有文档到标准输出流中：
$ deno doc --private ./path/to/module.ts
# 以 JSON 格式输出文档：
$ deno doc --json ./path/to/module.ts
# 定位特定的符号：
$ deno doc ./path/to/module.ts MyClass.someField
# 显示运行时内置文档：
$ deno doc
$ deno doc --builtin Deno.Listener
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-18">(06) 执行器：deno eval</h3>
<ul>
<li>
<p>deno-eval：执行代码。</p>
</li>
<li>
<p>使用方式：deno eval [OPTIOS]<code><CODE></code></p>
</li>
<li>
<p>独特指令：</p>
</li>
<li>
<ul>
<li>-p, --print：打印结果到标准输出流中</li>
<li>-T, --ts：将输入视为 TypeScript</li>
</ul>
</li>
<li>
<p>常用示例：</p>
</li>
</ul>
<pre><code class="copyable"># 从命令行中执行 JavaScript。
$ deno eval "console.log('hello world')"
# 以 TypeScript 方式执行：
$ deno eval -T "const v: string = 'hello'; console.log(v)"
# 此命令具有对所有权限的隐式访问权限（--allow-all）。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">(07) 格式化器：deno fmt</h3>
<ul>
<li>
<p>deno-fmt：自动格式化 JavaScript/TypeScript 源代码。</p>
</li>
<li>
<p>使用方式：deno fmt [选项] [文件]...</p>
</li>
<li>
<p>独特指令：</p>
</li>
<li>
<ul>
<li>--check：检查源文件是否已被格式化</li>
<li>--ignore=：忽略格式化特定的源文件。 与 --unstable 一起使用。</li>
</ul>
</li>
<li>
<p>常用示例：</p>
</li>
</ul>
<pre><code class="copyable">$ deno fmt --help
$ deno fmt
$ deno fmt myfile1.ts myfile2.ts
$ deno fmt --check
# 格式化标准输入流并输出到标准输出流：
$ cat file.ts | deno fmt -
# 通过在其前面加上忽略注释来忽略此行代码格式化：
#   // deno-fmt-ignore
# 通过在文件顶部添加忽略注释来忽略此文件格式化：
#   // deno-fmt-ignore-file
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">(08) 依赖检查器：deno info</h3>
<ul>
<li>deno-info：有关模块或缓存目录的信息。</li>
<li>使用方式：deno info [OPTIONS] [FILE]</li>
<li>常用示例：</li>
</ul>
<pre><code class="copyable"># 获取有关模块的信息：
$ deno info https://deno.land/std/http/file_server.ts
# 将显示以下信息：
# local: 文件的本地路径
# type: JavaScript、TypeScript 或者 JSON。
# compiled: 编译源代码的本地路径。（仅 TypeScript）
# map: 源映射的本地路径。 （仅 TypeScript）
# deps: 源文件的依赖关系树。
# 没有任何其他参数，“deno info” 将显示：
# DENO_DIR: 包含 Deno 管理文件的目录。
# Remote modules cache: 包含下载的远程模块的子目录。
# TypeScript compiler cache: 包含 TS 编译器输出的子目录。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">(09) 规范器：deno lint</h3>
<ul>
<li>
<p>deno-lint：规范 JavaScript/TypeScript 源码。</p>
</li>
<li>
<p>独特指令：</p>
</li>
<li>
<ul>
<li>--rules：列出可用规则</li>
</ul>
</li>
<li>
<p>使用方式：deno lint [OPTIONS] [FILE]...</p>
</li>
<li>
<p>常用示例：</p>
</li>
</ul>
<pre><code class="copyable">$ deno lint --unstable
$ deno lint --unstable myfile1.ts myfile2.js
# 列出可用规则：
$ deno lint --unstable --rules
# 通过在其前面加上忽略注释来忽略下一行的诊断，规则名称:
#   // deno-lint-ignore no-explicit-any
#   // deno-lint-ignore require-await no-empty
# 必须在忽略注释之后指定要忽略的规则的名称。
# 还支持 ESLint 忽略注释：
#   // eslint-ignore-next-line @typescrit-eslint/no-explicit-any no-empty
# 通过在文件顶部添加忽略注释来忽略整个文件：
#   // deno-lint-ignore-file
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">(10) 测试器：deno test</h3>
<ul>
<li>
<p>deno-test：使用 Deno 的内置测试运行程序运行测试。</p>
</li>
<li>
<p>使用方式：deno test [选项] [文件名]...</p>
</li>
<li>
<p>独特指令：</p>
</li>
<li>
<ul>
<li>--allow-none：如果未找到测试文件，则不返回错误代码</li>
<li>--failfast：在第一个错误发生时停止</li>
<li>--filter ：使用测试名称中的此字符串或模式运行测试</li>
</ul>
</li>
<li>
<p>常用示例：</p>
</li>
</ul>
<pre><code class="copyable"># 执行给定的模块，运行'Deno.test（）'声明的所有测试，然后将结果输出到到标准输出溜中：
$ deno test src/fetch_test.ts src/signal_test.ts
# 目录参数扩展为与 glob 匹配的所有包含文件
# &#123;*_,*.,&#125;test.&#123;js,mjs,ts,jsx,tsx&#125;：
$ deno test src/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">(11) 类型器：deno types</h3>
<ul>
<li>deno-types：打印运行时的 TypeScript 声明。</li>
<li>使用方式：deno types [OPTIONS]</li>
<li>常用示例：</li>
</ul>
<pre><code class="copyable">$ deno types --help
$ deno types > lib.deno.d.ts
# 声明文件可以保存并用于录入新内容。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">(12) 补全器：deno completions</h3>
<ul>
<li>deno-completions：输入 shell 补全信息到标准输出流中。</li>
<li>使用方式：deno completions [OPTIONS] </li>
<li>常用示例：</li>
</ul>
<pre><code class="copyable">$ deno completions bash > /usr/local/etc/bash_completion.d/deno.bash
$ source /usr/local/etc/bash_completion.d/deno.bash
# [shell 可能的值： zsh, bash, fish, powershell, elvish]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-25">(13) 升级器：deno upgrade</h3>
<ul>
<li>
<p>deno-upgrade：将 deno 可执行文件升级到给定的版本。</p>
</li>
<li>
<p>使用方式：deno upgrade [OPTIONS]</p>
</li>
<li>
<p>独特指令：</p>
</li>
<li>
<ul>
<li>--dry-run：执行所有检查，而不替换旧的 exe</li>
<li>-f, --force：即使不是过期也要替换当前的 exe</li>
<li>--output ：将更新版本输出到的路径</li>
<li>--version ：想要升级到的版本号</li>
</ul>
</li>
<li>
<p>常用示例：</p>
</li>
</ul>
<pre><code class="copyable">$ deno upgrade --help
# 默认将更新到最新版。
# 该版本是从这里下载：
# https://github.com/denoland/deno/releases
# 并且用于替换当前的可执行文件。
# 如果您不想替换当前的 Deno 可执行文件，而是下载一个新版本到其他位置，请使用 --output 标志
$ deno upgrade --output $HOME/my_deno
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">(14) REPL 器：deno repl</h3>
<ul>
<li>deno-repl：读取 执行 打印 循环</li>
<li>使用方式：deno repl [OPTIONS]</li>
<li>常用示例：</li>
</ul>
<pre><code class="copyable">$ deno repl # deno
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">通读 Deno 环境变量</h2>
<blockquote>
<p>相关实战代码都收录在<a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer">《Deno 钻研之术》仓库</a>中的 demos/ningowood/v1-cli-example 下。</p>
</blockquote>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97aefb73a05046d980de1465822a7a69~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-28">(01) DENO_DIR</h3>
<p>DENO_DIR 默认为 $HOME/.cache/deno，但可以设置为任何路径。这是 Deno 存放生成的代码和缓存的源码的路径。</p>
<p>输入 deno info，可以看到自己的缓存位置，其中为远程模块、TypeScript 编译位置提供了专门的目录。</p>
<pre><code class="copyable">$ deno info
# DENO_DIR 位置: "/Users/&#123;$HOME&#125;/Library/Caches/deno"
# 远程模块缓存位置: "/Users/&#123;$HOME&#125;/Library/Caches/deno/deps"
# TypeScript 编译缓存位置: "/Users/&#123;$HOME&#125;/Library/Caches/deno/gen"
$ tree -L 2 /Users/&#123;$HOME&#125;/Library/Caches/deno
.
├── deno_history.txt
├── deps
│   ├── http
│   └── https
├── gen
│   ├── xxx.js
│   ├── xxx.js.map
│   ├── file
│   └── https
├── lib.deno.d.ts
├── lib.deno_runtime.d.ts
└── lib.webworker.d.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">(02) DENO_INSTALL_ROOT</h3>
<p>默认为 $HOME/.deno/bin。输入如下命令，可以看到我目前安装在全局的几个 Deno 程序：</p>
<pre><code class="copyable">$ tree /Users/&#123;$HOME&#125;/.deno
.
└── bin
    ├── Trex
    ├── Trex_Cache_Map
    ├── deno
    ├── denon
    ├── pagic
    └── vr
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">(02) NO_COLOR</h3>
<p>如果 NO_COLOR 被设置，Deno 将会关闭彩色输出 (<a href="https://no-color.org/" target="_blank" rel="nofollow noopener noreferrer">no-color.org</a>)。用户代码可以通过布尔常量 Deno.noColor 测试 NO_COLOR 是否被设置，这不需要环境权限 (--allow-env)。</p>
<pre><code class="copyable">$ deno run var.ts 
Check file:///Users/didi/WorkSpace/Hylerrix/deno-tutorial/demos/ningowood/v1-cli-example/no-color.ts
false
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">(03) DENO_CERT & HTTP*_PROXY</h3>
<p>留个空白猜猜怎么用。</p>
<h2 data-id="heading-32">总结 & 订阅</h2>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc800e9605ae47178162cfd9413e987d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>至此，《从 CLI 指令通读 Deno v1.x 全特性》文章大功告成。在写作的这 14h+ 过程中，产生了很多灵感，也对更多内容感兴趣觉得可以深挖。奈何一篇文章能承载的内容十分有限，所以可以从本文引发思考的一些有趣的主题也就先推迟再看了。同时，未来很可能会有更多的指令作为新功能推出，或许也有些指令由于不在文档帮助信息中而没办法收录。</p>
<p>总之可以继续学习的地方还有很多！可以入手学习 Deno 的角度也非常之多。期待一起进行更多的编程实战后，对 Deno CLI 特性会有更为全面的认识。</p>
<p>订阅？你懂得：</p>
<ul>
<li>仓库：<a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer">github.com/hylerrix/de…</a></li>
<li>官网：<a href="http://deno-tutorial.js.org/" target="_blank" rel="nofollow noopener noreferrer">deno-tutorial.js.org</a></li>
<li>Me：<a href="https://github.com/hylerrix/deno-tutorial" target="_blank" rel="nofollow noopener noreferrer">github.com/hylerrix</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            
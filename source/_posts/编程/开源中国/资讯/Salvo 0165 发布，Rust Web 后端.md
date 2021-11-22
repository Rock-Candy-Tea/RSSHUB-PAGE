
---
title: 'Salvo 0.16.5 发布，Rust Web 后端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://github.com/salvo-rs/salvo/workflows/ci-linux/badge.svg?branch=master&event=push'
author: 开源中国
comments: false
date: Mon, 22 Nov 2021 07:32:00 GMT
thumbnail: 'https://github.com/salvo-rs/salvo/workflows/ci-linux/badge.svg?branch=master&event=push'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Salvo 是一个极其简单易用却又功能强大的 Rust Web 后端框架. 仅仅需要基本的 Rust 基础即可写成功能强大的后端服务器, 我们的目标是: 编码最简单, 功能不缺失, 性能有保障.</p> 
<p><strong>主要更新功能:</strong></p> 
<p>1. BasicAuthValidator 中的 validate 改成了异步.</p> 
<p>2. Rustls 和 Native Tls 的支持, 已经证书的热加载.</p> 
<p>3. 改进插件系统.</p> 
<p>4. 改进 Server 对应的功能.</p> 
<h2><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Factions" target="_blank"><img alt="build status" src="https://github.com/salvo-rs/salvo/workflows/ci-linux/badge.svg?branch=master&event=push" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Factions" target="_blank"><img alt="build status" src="https://github.com/salvo-rs/salvo//workflows/ci-macos/badge.svg?branch=master&event=push" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Factions" target="_blank"><img alt="build status" src="https://github.com/salvo-rs/salvo/workflows/ci-windows/badge.svg?branch=master&event=push" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrates.io%2Fcrates%2Fsalvo" target="_blank"><img alt="crates.io" src="https://camo.githubusercontent.com/65ca9335a4e133a59d15f37e11b61af1e66b82ba76ea3d7b040f1c4f3d876efa/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f762f73616c766f" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.rs%2Fsalvo" target="_blank"><img alt="Documentation" src="https://camo.githubusercontent.com/2308c502901552660a86928a98c99b28bb3102e4eda155e457766559f310d0b4/68747470733a2f2f646f63732e72732f73616c766f2f62616467652e737667" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Frust-secure-code%2Fsafety-dance%2F" target="_blank"><img alt="unsafe forbidden" src="https://camo.githubusercontent.com/a3785b859e346cc8ef5a9deb5359d841cc68fb3c66f9cada6326037a89af902d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f756e736166652d666f7262696464656e2d737563636573732e737667" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrates.io%2Fcrates%2Fsalvo" target="_blank"><img alt="Download" src="https://camo.githubusercontent.com/634b0bbbf5621e25795ac3f5fd0668f1642a6d1cd365fdac52ce9712a43fc6d2/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f642f73616c766f2e737667" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.rust-lang.org%2F2021%2F10%2F21%2FRust-1.56.0.html" target="_blank"><img alt="Rust Version" src="https://camo.githubusercontent.com/7059cd9106c6e3e15e5bc3123fd22fa6db53d7cc87ebacef1748587ff8274815/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f727573742d312e35362532422d626c7565" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodecov.io%2Fgh%2Fsalvo-rs%2Fsalvo" target="_blank"><img alt="codecov" src="https://camo.githubusercontent.com/2b7e97123e9a18ea958c398c95f6fd7f1a918bbd9b54b0faea48cf607e07da11/68747470733a2f2f636f6465636f762e696f2f67682f73616c766f2d72732f73616c766f2f6272616e63682f6d61737465722f67726170682f62616467652e737667" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsalvo.rs" target="_blank"><img alt="Website" src="https://camo.githubusercontent.com/9bfffc95e9753f948b427a82cc3813f2c2c019c58e9094f971509d252c7a3331/68747470733a2f2f696d672e736869656c64732e696f2f776562736974653f646f776e5f636f6c6f723d6c696768746772657926646f776e5f6d6573736167653d6f66666c696e652675705f636f6c6f723d626c75652675705f6d6573736167653d6f6e6c696e652675726c3d687474707325334125324625324673616c766f2e7273" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2F093fc33ad6230c9fc08a4ca2392f4cf7fbe51e746be4d1a09456d8b1e1101a40%2F68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f6c2f73616c766f2e737667" target="_blank"><img alt="License" src="https://camo.githubusercontent.com/093fc33ad6230c9fc08a4ca2392f4cf7fbe51e746be4d1a09456d8b1e1101a40/68747470733a2f2f696d672e736869656c64732e696f2f6372617465732f6c2f73616c766f2e737667" referrerpolicy="no-referrer"></a></h2> 
<p> </p> 
<h2>🎯 功能特色</h2> 
<ul> 
 <li>基于hyper, tokio 的异步 Web 后端框架;</li> 
 <li>支持 Websocket;</li> 
 <li>统一的中间件和句柄接口, 中间件系统支持在句柄之前或者之后运行;</li> 
 <li>简单易用的路由系统, 支持路由嵌套, 在任何嵌套层都可以添加中间件;</li> 
 <li>集成 multipart 表单处理, 处理上传文件变得非常简单;</li> 
 <li>支持从多个本地目录映射成一个虚拟目录提供服务.</li> 
</ul> 
<h2>⚡️ 快速开始</h2> 
<p>你可以查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Ftree%2Fmaster%2Fexamples" target="_blank">实例代码</a>, 或者访问<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsalvo.rs" target="_blank">官网</a>.</p> 
<p>创建一个全新的项目:</p> 
<pre>cargo new hello_salvo --bin</pre> 
<p>添加依赖项到 <code>Cargo.toml</code></p> 
<pre>[<span>dependencies</span>]
<span>salvo</span> = &#123; <span>version</span> = <span><span>"</span>0.16<span>"</span></span>, <span>features</span> = [<span><span>"</span>full<span>"</span></span>] &#125;
<span>tokio</span> = &#123; <span>version</span> = <span><span>"</span>1<span>"</span></span>, <span>features</span> = [<span><span>"</span>full<span>"</span></span>] &#125;</pre> 
<p>在 <code>main.rs</code> 中创建一个简单的函数句柄, 命名为<code>hello_world</code>, 这个函数只是简单地打印文本 <code>"Hello World"</code>.</p> 
<pre><span>use</span> salvo<span>::</span>prelude<span>::</span><span>*</span>;

#[fn_handler]
<span>async</span> <span>fn</span> <span>hello_world</span>(_req: <span>&</span><span>mut</span> Request, _depot: <span>&</span><span>mut</span> Depot, res: <span>&</span><span>mut</span> Response) &#123;
    res.<span>render_plain_text</span>(<span>"Hello World"</span>);
&#125;</pre> 
<h3>中间件</h3> 
<p>Salvo 中的中间件其实就是 Handler, 没有其他任何特别之处. <strong>所以书写中间件并不需要像其他某些框架需要掌握泛型关联类型等知识. 只要你会写函数就会写中间件, 就是这么简单!!!</strong></p> 
<h3>树状路由系统</h3> 
<p>正常情况下我们是这样写路由的：</p> 
<pre>Router<span>::</span><span>with_path</span>(<span>"articles"</span>).<span>get</span>(list_articles).<span>post</span>(create_article);
Router<span>::</span><span>with_path</span>(<span>"articles/"</span>)
    .<span>get</span>(show_article)
    .<span>patch</span>(edit_article)
    .<span>delete</span>(delete_article);</pre> 
<p>往往查看文章和文章列表是不需要用户登录的, 但是创建, 编辑, 删除文章等需要用户登录认证权限才可以. Salvo 中支持嵌套的路由系统可以很好地满足这种需求. 我们可以把不需要用户登录的路由写到一起：</p> 
<pre>Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
    .<span>get</span>(list_articles)
    .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>""</span>).<span>get</span>(show_article));</pre> 
<p>然后把需要用户登录的路由写到一起， 并且使用相应的中间件验证用户是否登录：</p> 
<pre>Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
    .<span>hoop</span>(auth_check)
    .<span>post</span>(list_articles)
    .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>""</span>).<span>patch</span>(edit_article).<span>delete</span>(delete_article));</pre> 
<p>虽然这两个路由都有这同样的 <code>path("articles")</code>, 然而它们依然可以被同时添加到同一个父路由, 所以最后的路由长成了这个样子:</p> 
<pre>Router<span>::</span><span>new</span>()
    .<span>push</span>(
        Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
            .<span>get</span>(list_articles)
            .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>""</span>).<span>get</span>(show_article)),
    )
    .<span>push</span>(
        Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
            .<span>hoop</span>(auth_check)
            .<span>post</span>(list_articles)
            .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>""</span>).<span>patch</span>(edit_article).<span>delete</span>(delete_article)),
    );</pre> 
<p>匹配了路径中的一个片段, 正常情况下文章的 <code>id</code> 只是一个数字, 这是我们可以使用正则表达式限制 <code>id</code> 的匹配规则, <code>r"<a href="id:/%5C%5Cd+/">id:/\\d+/</a>"</code>.</p> 
<p>还可以通过 <code><*></code> 或者 <code><**></code> 匹配所有剩余的路径片段. 为了代码易读性性强些, 也可以添加适合的名字, 让路径语义更清晰, 比如: <code><**file_path></code>.</p> 
<h3> </h3> 
<h3>文件上传</h3> 
<p>可以通过 Request 中的 get_file 异步获取上传的文件:</p> 
<pre>#[fn_handler]
<span>async</span> <span>fn</span> <span>upload</span>(req: <span>&</span><span>mut</span> Request, res: <span>&</span><span>mut</span> Response) &#123;
    <span>let</span> file <span>=</span> req.<span>get_file</span>(<span>"file"</span>).<span>await</span>;
    <span>if</span> <span>let</span> <span>Some</span>(file) <span>=</span> file &#123;
        <span>let</span> dest <span>=</span> <span>format!</span>(<span>"temp/&#123;&#125;"</span>, file.<span>filename</span>().<span>unwrap_or_else</span>(<span>||</span> <span>"file"</span>.<span>into</span>()));
        <span>if</span> <span>let</span> <span>Err</span>(e) <span>=</span> std<span>::</span>fs<span>::</span><span>copy</span>(<span>&</span>file.path, <span>Path</span><span>::</span><span>new</span>(<span>&</span>dest)) &#123;
            res.<span>set_status_code</span>(StatusCode<span>::</span>INTERNAL_SERVER_ERROR);
        &#125; <span>else</span> &#123;
            res.<span>render_plain_text</span>(<span>"Ok"</span>);
        &#125;
    &#125; <span>else</span> &#123;
        res.<span>set_status_code</span>(StatusCode<span>::</span>BAD_REQUEST);
    &#125;
&#125;</pre> 
<h3> </h3> 
<h3>更多示例</h3> 
<p>您可以从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Fblob%2Fmaster%2Fexamples" target="_blank">examples</a> 文件夹下查看更多示例代码, 您可以通过以下命令运行这些示例：</p> 
<pre><code>cargo run --example basic_auth
</code></pre> 
<p>您可以使用任何你想运行的示例名称替代这里的 <code>basic_auth</code>.</p> 
<p>这里有一个真实的项目使用了 Salvo：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdriftluo%2Fmyblog" target="_blank">https://github.com/driftluo/myblog</a>.</p> 
<h2>🚀 性能</h2> 
<p>Benchmark 测试结果可以从这里查看:</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fweb-frameworks-benchmark.netlify.app%2Fresult%3Fl%3Drust" target="_blank">https://web-frameworks-benchmark.netlify.app/result?l=rust</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3D1922b097-2d7f-413c-be21-9571c8302734%26hw%3Dph%26test%3Dquery%26l%3Dzik0zj-e6%26a%3D2" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=1922b097-2d7f-413c-be21-9571c8302734&hw=ph&test=query&l=zik0zj-e6&a=2</a></p>
                                        </div>
                                      
</div>
            

---
title: 'Salvo 0.23.3 发布, Rust 编写的简单且强大的后端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6380'
author: 开源中国
comments: false
date: Tue, 17 May 2022 12:41:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6380'
---

<div>   
<div class="content">
                                                                    
                                                        <p>更新内容:</p> 
<p>1. 改进中间件执行流程.</p> 
<p>2. 改进依赖包结构</p> 
<p>github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo" target="_blank">https://github.com/salvo-rs/salvo</a></p> 
<p>Salvo 是一个极其简单且功能强大的 Rust Web 后端框架. 仅仅需要基础 Rust 知识即可开发后端服务.</p> 
<h2>🎯 功能特色</h2> 
<ul> 
 <li>基于 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrates.io%2Fcrates%2Fhyper" target="_blank">Hyper</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcrates.io%2Fcrates%2Ftokio" target="_blank">Tokio</a> 开发;</li> 
 <li>统一的中间件和句柄接口;</li> 
 <li>路由支持多层次嵌套, 在任何层都可以添加中间件;</li> 
 <li>集成 Multipart 表单处理;</li> 
 <li>支持 Websocket;</li> 
 <li>支持 Acme, 自动从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fletsencrypt.org%2F" target="_blank">let's encrypt</a> 获取 TLS 证书;</li> 
 <li>支持从多个本地目录映射成一个虚拟目录提供服务.</li> 
</ul> 
<h2>⚡️ 快速开始</h2> 
<p>你可以查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Ftree%2Fmain%2Fexamples" target="_blank">实例代码</a>, 或者访问<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsalvo.rs%2Fbook%2Fquick-start%2Fhello_world%2F" target="_blank">官网</a>.</p> 
<p>创建一个全新的项目:</p> 
<div> 
 <pre>cargo new hello_salvo --bin</pre> 
</div> 
<p>添加依赖项到 <code>Cargo.toml</code></p> 
<div> 
 <pre>[<span>dependencies</span>]
<span>salvo</span> = <span><span>"</span>0.23<span>"</span></span>
<span>tokio</span> = <span><span>"</span>1<span>"</span></span></pre> 
</div> 
<p>在 <code>main.rs</code> 中创建一个简单的函数句柄, 命名为<code>hello_world</code>, 这个函数只是简单地打印文本 <code>"Hello World"</code>.</p> 
<div> 
 <pre><span>use</span> salvo<span>::</span>prelude<span>::</span><span>*</span>;

#[fn_handler]
<span>async</span> <span>fn</span> <span>hello_world</span>(_req: <span>&</span><span>mut</span> Request, _depot: <span>&</span><span>mut</span> Depot, res: <span>&</span><span>mut</span> Response) &#123;
    res.<span>render</span>(Text<span>::</span><span>Plain</span>(<span>"Hello World"</span>));
&#125;
</pre> 
</div> 
<h3>中间件</h3> 
<p>Salvo 中的中间件其实就是 Handler, 没有其他任何特别之处. <strong>所以书写中间件并不需要像其他某些框架需要掌握泛型关联类型等知识. 只要你会写函数就会写中间件, 就是这么简单!!!</strong></p> 
<div> 
 <pre><span>use</span> salvo<span>::</span>http<span>::</span>header<span>::</span>&#123;<span>self</span>, HeaderValue&#125;;
<span>use</span> salvo<span>::</span>prelude<span>::</span><span>*</span>;

#[fn_handler]
<span>async</span> <span>fn</span> <span>add_header</span>(res: <span>&</span><span>mut</span> Response) &#123;
    res.<span>headers_mut</span>()
        .<span>insert</span>(header<span>::</span>SERVER, HeaderValue<span>::</span><span>from_static</span>(<span>"Salvo"</span>));
&#125;</pre> 
</div> 
<p>然后将它添加到路由中:</p> 
<div> 
 <pre>Router<span>::</span><span>new</span>().<span>hoop</span>(add_header).<span>get</span>(hello_world)</pre> 
</div> 
<p>这就是一个简单的中间件, 它向 <code>Response</code> 的头部添加了 <code>Header</code>, 查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Fblob%2Fmain%2Fexamples%2Fmiddleware-add-header%2Fsrc%2Fmain.rs" target="_blank">完整源码</a>.</p> 
<h3>可链式书写的树状路由系统</h3> 
<p>正常情况下我们是这样写路由的：</p> 
<div> 
 <pre>Router<span>::</span><span>with_path</span>(<span>"articles"</span>).<span>get</span>(list_articles).<span>post</span>(create_article);
Router<span>::</span><span>with_path</span>(<span>"articles/<id>"</span>)
    .<span>get</span>(show_article)
    .<span>patch</span>(edit_article)
    .<span>delete</span>(delete_article);</pre> 
</div> 
<p>往往查看文章和文章列表是不需要用户登录的, 但是创建, 编辑, 删除文章等需要用户登录认证权限才可以. Salvo 中支持嵌套的路由系统可以很好地满足这种需求. 我们可以把不需要用户登录的路由写到一起：</p> 
<div> 
 <pre>Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
    .<span>get</span>(list_articles)
    .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>"<id>"</span>).<span>get</span>(show_article));</pre> 
</div> 
<p>然后把需要用户登录的路由写到一起， 并且使用相应的中间件验证用户是否登录：</p> 
<div> 
 <pre>Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
    .<span>hoop</span>(auth_check)
    .<span>post</span>(list_articles)
    .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>"<id>"</span>).<span>patch</span>(edit_article).<span>delete</span>(delete_article));</pre> 
</div> 
<p>虽然这两个路由都有这同样的 <code>path("articles")</code>, 然而它们依然可以被同时添加到同一个父路由, 所以最后的路由长成了这个样子:</p> 
<div> 
 <pre>Router<span>::</span><span>new</span>()
    .<span>push</span>(
        Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
            .<span>get</span>(list_articles)
            .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>"<id>"</span>).<span>get</span>(show_article)),
    )
    .<span>push</span>(
        Router<span>::</span><span>with_path</span>(<span>"articles"</span>)
            .<span>hoop</span>(auth_check)
            .<span>post</span>(list_articles)
            .<span>push</span>(Router<span>::</span><span>with_path</span>(<span>"<id>"</span>).<span>patch</span>(edit_article).<span>delete</span>(delete_article)),
    );</pre> 
</div> 
<p><code><id></code>匹配了路径中的一个片段, 正常情况下文章的 <code>id</code> 只是一个数字, 这是我们可以使用正则表达式限制 <code>id</code> 的匹配规则, <code>r"<id:/\d+/>"</code>.</p> 
<p>还可以通过 <code><*></code> 或者 <code><**></code> 匹配所有剩余的路径片段. 为了代码易读性性强些, 也可以添加适合的名字, 让路径语义更清晰, 比如: <code><**file_path></code>.</p> 
<p>有些用于匹配路径的正则表达式需要经常被使用, 可以将它事先注册, 比如 GUID:</p> 
<div> 
 <pre>PathFilter<span>::</span><span>register_part_regex</span>(
    <span>"guid"</span>,
    Regex<span>::</span><span>new</span>(<span>"[0-9a-fA-F]&#123;8&#125;-([0-9a-fA-F]&#123;4&#125;-)&#123;3&#125;[0-9a-fA-F]&#123;12&#125;"</span>).<span>unwrap</span>(),
);</pre> 
</div> 
<p>这样在需要路径匹配时就变得更简洁:</p> 
<div> 
 <pre>Router<span>::</span><span>with_path</span>(<span>"<id:guid>"</span>).<span>get</span>(index)</pre> 
</div> 
<p>查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Fblob%2Fmain%2Fexamples%2Frouting-guid%2Fsrc%2Fmain.rs" target="_blank">完整源码</a></p> 
<h3>文件上传</h3> 
<p>可以通过 <code>Request</code> 中的 <code>file</code> 异步获取上传的文件:</p> 
<div> 
 <pre>#[fn_handler]
<span>async</span> <span>fn</span> <span>upload</span>(req: <span>&</span><span>mut</span> Request, res: <span>&</span><span>mut</span> Response) &#123;
    <span>let</span> file <span>=</span> req.<span>file</span>(<span>"file"</span>).<span>await</span>;
    <span>if</span> <span>let</span> <span>Some</span>(file) <span>=</span> file &#123;
        <span>let</span> dest <span>=</span> <span>format!</span>(<span>"temp/&#123;&#125;"</span>, file.<span>name</span>().<span>unwrap_or_else</span>(<span>||</span> <span>"file"</span>.<span>into</span>()));
        <span>if</span> <span>let</span> <span>Err</span>(e) <span>=</span> std<span>::</span>fs<span>::</span><span>copy</span>(<span>&</span>file.path, <span>Path</span><span>::</span><span>new</span>(<span>&</span>dest)) &#123;
            res.<span>set_status_code</span>(StatusCode<span>::</span>INTERNAL_SERVER_ERROR);
        &#125; <span>else</span> &#123;
            res.<span>render</span>(<span>"Ok"</span>);
        &#125;
    &#125; <span>else</span> &#123;
        res.<span>set_status_code</span>(StatusCode<span>::</span>BAD_REQUEST);
    &#125;
&#125;
</pre> 
</div> 
<h3>更多示例</h3> 
<p>您可以从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Fblob%2Fmain%2Fexamples" target="_blank">examples</a> 文件夹下查看更多示例代码, 您可以通过以下命令运行这些示例：</p> 
<div> 
 <pre><code>cargo run --bin --example-basic_auth
</code></pre> 
</div> 
<p>您可以使用任何你想运行的示例名称替代这里的 <code>basic_auth</code>.</p> 
<p>这里有一个真实的项目使用了 Salvo：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdriftluo%2Fmyblog" target="_blank">https://github.com/driftluo/myblog</a>.</p> 
<h2>🚀 性能</h2> 
<p>Benchmark 测试结果可以从这里查看:</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fweb-frameworks-benchmark.netlify.app%2Fresult%3Fl%3Drust" target="_blank">https://web-frameworks-benchmark.netlify.app/result?l=rust</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.techempower.com%2Fbenchmarks%2F%23section%3Dtest%26runid%3D785f3715-0f93-443c-8de0-10dca9424049" target="_blank">https://www.techempower.com/benchmarks/#section=test&runid=785f3715-0f93-443c-8de0-10dca9424049</a></p> 
<div>
  
</div> 
<p>github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo" target="_blank">https://github.com/salvo-rs/salvo</a></p>
                                        </div>
                                      
</div>
            

---
title: 'Salvo 0.24.2 发布, 简单强大的 Rust Web 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2469'
author: 开源中国
comments: false
date: Tue, 24 May 2022 00:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2469'
---

<div>   
<div class="content">
                                                                    
                                                        <p>更新内容:</p> 
<ul> 
 <li>添加了 test 模块, 方便单元测试, 比起之前使用 http::Request::builder 构建 Request 请求简洁很多.</li> 
 <li>添加解析 Request 请求数据到强类型的功能, 并且支持多数据源组合. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsalvo.rs%2Fzh-hans%2Fbook%2Fadvanced%2Fparse-request-data%2F" target="_blank">详细介绍</a></li> 
</ul> 
<p><strong>Salvo 是极其简单且功能强大的框架</strong></p> 
<h3>Handler</h3> 
<pre><span>use</span> salvo<span>::</span>prelude<span>::</span><span>*</span>;

#[fn_handler]
<span>async</span> <span>fn</span> <span>hello_world</span>(_req: <span>&</span><span>mut</span> Request, _depot: <span>&</span><span>mut</span> Depot, res: <span>&</span><span>mut</span> Response) &#123;
    res.<span>render</span>(Text<span>::</span><span>Plain</span>(<span>"Hello World"</span>));
&#125;</pre> 
<h3>中间件</h3> 
<pre><span>use</span> salvo<span>::</span>http<span>::</span>header<span>::</span>&#123;<span>self</span>, HeaderValue&#125;;
<span>use</span> salvo<span>::</span>prelude<span>::</span><span>*</span>;

#[fn_handler]
<span>async</span> <span>fn</span> <span>add_header</span>(res: <span>&</span><span>mut</span> Response) &#123;
    res.<span>headers_mut</span>()
        .<span>insert</span>(header<span>::</span>SERVER, HeaderValue<span>::</span><span>from_static</span>(<span>"Salvo"</span>));
&#125;</pre> 
<h3>路由</h3> 
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
<p>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo" target="_blank">https://github.com/salvo-rs/salvo</a></p>
                                        </div>
                                      
</div>
            
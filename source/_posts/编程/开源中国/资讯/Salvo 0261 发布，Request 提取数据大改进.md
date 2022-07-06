
---
title: 'Salvo 0.26.1 发布，Request 提取数据大改进'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4110'
author: 开源中国
comments: false
date: Tue, 05 Jul 2022 21:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4110'
---

<div>   
<div class="content">
                                                                                            <p>Salvo 是 Rust 语言编写的简单易用, 又不失功能强大的 Web 后端框架.</p> 
<p>此版本主要改进了 Request 数据提取的功能:</p> 
<p>可以轻松地从多个不同数据源获取数据, 并且组装为你想要的类型. 可以先定义一个自定义的类型, 比如:</p> 
<pre>#[derive(Serialize, Deserialize, Extractible, Debug)]
<span>/// 默认从 body 中获取数据字段值</span>
#[extract(default_source(from = <span>"body"</span>))]
<span>struct</span> <span>GoodMan</span><<span>'<span>a</span></span>> &#123;
    <span>/// 其中, id 号从请求路径参数中获取, 并且自动解析数据为 i64 类型.</span>
    #[extract(source(from = <span>"param"</span>))]
    id: <span>i64</span>,
    <span>/// 可以使用引用类型, 避免内存复制.</span>
    username: &<span>'<span>a</span></span> <span>str</span>,
    first_name: <span>String</span>,
    last_name: <span>String</span>,
&#125;</pre> 
<p>然后在 <code>Handler</code> 中可以这样获取数据:</p> 
<pre>#[fn_handler]
<span>async</span> <span>fn</span> <span>edit</span>(req: <span>&</span><span>mut</span> Request) -> <span>String</span> &#123;
    <span>let</span> good_man: GoodMan<span><</span><span>'<span>_</span></span><span>></span> <span>=</span> req.<span>extract</span>().<span>await</span>.<span>unwrap</span>();
&#125;</pre> 
<p>甚至于可以直接把类型作为参数传入函数, 像这样:</p> 
<pre>#[fn_handler]
<span>async</span> <span>fn</span> <span>edit</span><<span>'<span>a</span></span>>(good_man: GoodMan<<span>'<span>a</span></span>>) -> <span>String</span> &#123;
    res.<span>render</span>(<span>Json</span>(good_man));
&#125;</pre> 
<p>数据类型的定义有相当大的灵活性, 甚至可以根据需要解析为嵌套的结构:</p> 
<pre>#[derive(Serialize, Deserialize, Extractible, Debug)]
#[extract(default_source(from = <span>"body"</span>, format = <span>"json"</span>))]
<span>struct</span> <span>GoodMan</span><<span>'<span>a</span></span>> &#123;
    #[extract(source(from = <span>"param"</span>))]
    id: <span>i64</span>,
    #[extract(source(from = <span>"query"</span>))]
    username: &<span>'<span>a</span></span> <span>str</span>,
    first_name: <span>String</span>,
    last_name: <span>String</span>,
    lovers: <span>Vec</span><span><</span><span>String</span><span>></span>,
    <span>/// 这个 nested 字段完全是从 Request 重新解析.</span>
    #[extract(source(from = <span>"request"</span>))]
    nested: Nested<span><</span><span>'<span>a</span></span><span>></span>,
&#125;

#[derive(Serialize, Deserialize, Extractible, Debug)]
#[extract(default_source(from = <span>"body"</span>, format = <span>"json"</span>))]
<span>struct</span> <span>Nested</span><<span>'<span>a</span></span>> &#123;
    #[extract(source(from = <span>"param"</span>))]
    id: <span>i64</span>,
    #[extract(source(from = <span>"query"</span>))]
    username: &<span>'<span>a</span></span> <span>str</span>,
    first_name: <span>String</span>,
    last_name: <span>String</span>,
    #[extract(rename = <span>"lovers"</span>)]
    #[serde(default)]
    pets: <span>Vec</span><span><</span><span>String</span><span>></span>,
&#125;</pre> 
<p>查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo%2Fblob%2Fmain%2Fexamples%2Fextract-nested%2Fsrc%2Fmain.rs" target="_blank">完整源码</a></p> 
<p>Github: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsalvo-rs%2Fsalvo" target="_blank">https://github.com/salvo-rs/salvo</a></p>
                                        </div>
                                      
</div>
            
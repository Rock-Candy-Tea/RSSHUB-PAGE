
---
title: 'Diesel 2.0.0 RC1 发布，Rust 的 ORM 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5447'
author: 开源中国
comments: false
date: Mon, 25 Jul 2022 11:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5447'
---

<div>   
<div class="content">
                                                                                            <p>Rust 的 ORM 框架 Diesel 发布 2.0 的第一个 RC 版本，该版本包含一些 bug 修复以及改进，值得关注的有：</p> 
<ul> 
 <li>修复连接重用的 bug</li> 
 <li>支持来自<span> </span><code>ipnet</code><span> 的类型</span></li> 
 <li>支持通过 libpg 的按行模式的值加载</li> 
 <li>改进错误信息生成</li> 
</ul> 
<p style="color:#24292f; text-align:start">这个版本很有可能是 2.0 稳定版之前的最后一个版本，稳定版很快将发布。</p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><span style="color:#db2828">Diesel</span><span> </span>是一个安全可扩展的<span> </span><a href="http://www.oschina.net/p/rust" target="_blank">Rust</a><span> </span>编程语言的 ORM 框架和查询构建工具。<span style="color:#db2828">Diesel</span><span> </span>可避免运行时错误，提供最好的性能。</p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">示例代码：</p> 
<pre style="text-align:start">extern crate <span style="color:#db2828">diesel</span>_demo;
extern crate <span style="color:#db2828">diesel</span>;

use self::<span style="color:#db2828">diesel</span>_demo::*;
use self::<span style="color:#db2828">diesel</span>_demo::models::*;
use self::<span style="color:#db2828">diesel</span>::prelude::*;

fn main() &#123;
    use <span style="color:#db2828">diesel</span>_demo::schema::posts::dsl::*;

    let connection = establish_connection();
    let results = posts.filter(published.eq(true))
        .limit(5)
        .load::<Post>(&connection)
        .expect("Error loading posts");

    println!("Displaying &#123;&#125; posts", results.len());
    for post in results &#123;
        println!("&#123;&#125;", post.title);
        println!("----------\n");
        println!("&#123;&#125;", post.body);
    &#125;
&#125;
</pre> 
<p> </p>
                                        </div>
                                      
</div>
            

---
title: 'clop v0.0.12 发布，go 实现的纯结构体命令行解析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1133'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 10:55:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1133'
---

<div>   
<div class="content">
                                                                    
                                                        <p>clop v0.0.12 版本现已发布。地址:</p> 
<ul> 
 <li><a href="https://gitee.com/guonaihong/clop">https://gitee.com/guonaihong/clop</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop" target="_blank">https://github.com/guonaihong/clop</a></li> 
</ul> 
<p>更新内容</p> 
<p>本地新加short, long 标记，可以更快地实现命令行解析器</p> 
<pre style="text-align:start"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">NumberNonblank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-c;long" </span>
<span style="color:var(--color-prettylights-syntax-string)">                     usage:"number nonempty output lines, overrides"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowEnds</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-E;long" </span>
<span style="color:var(--color-prettylights-syntax-string)">               usage:"display $ at end of each line"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">Number</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-n;long" </span>
<span style="color:var(--color-prettylights-syntax-string)">             usage:"number all output lines"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">SqueezeBlank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-s;long" </span>
<span style="color:var(--color-prettylights-syntax-string)">                   usage:"suppress repeated empty output lines"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowTab</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-T;long" </span>
<span style="color:var(--color-prettylights-syntax-string)">              usage:"display TAB characters as ^I"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowNonprinting</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-v;long" </span>
<span style="color:var(--color-prettylights-syntax-string)">                      usage:"use ^ and M- notation, except for LFD and TAB" `</span>

<span style="color:var(--color-prettylights-syntax-constant)">Files</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"args=files"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
 c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span>&#123;&#125;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>c)

fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%#v, %s\n"</span>, c, err)
&#125;</pre>
                                        </div>
                                      
</div>
            
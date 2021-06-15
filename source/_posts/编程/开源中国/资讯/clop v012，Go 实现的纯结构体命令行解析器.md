
---
title: 'clop v0.1.2，Go 实现的纯结构体命令行解析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://github.com/guonaihong/clop/workflows/Go/badge.svg'
author: 开源中国
comments: false
date: Tue, 15 Jun 2021 13:55:00 GMT
thumbnail: 'https://github.com/guonaihong/clop/workflows/Go/badge.svg'
---

<div>   
<div class="content">
                                                                    
                                                        <h3>项目地址</h3> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop" target="_blank">https://gitee.com/guonaihong/clop</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop" target="_blank">https://github.com/guonaihong/clop</a></p> 
<h3>更新更新</h3> 
<ul> 
 <li>优化: 输入错误选项, 更易推荐到正确的选项</li> 
 <li>完整文档</li> 
</ul> 
<h1 style="text-align:start">clop</h1> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%2Factions" target="_blank"><img alt="Go" src="https://github.com/guonaihong/clop/workflows/Go/badge.svg" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodecov.io%2Fgh%2Fguonaihong%2Fclop" target="_blank"><img alt="codecov" src="https://camo.githubusercontent.com/5d7c2d573c0d202b49b364bae93913eafc02a33684408a6a14ac1c1f9ce028db/68747470733a2f2f636f6465636f762e696f2f67682f67756f6e6169686f6e672f636c6f702f6272616e63682f6d61737465722f67726170682f62616467652e737667" referrerpolicy="no-referrer"></a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoreportcard.com%2Freport%2Fgithub.com%2Fguonaihong%2Fclop" target="_blank"><img alt="Go Report Card" src="https://camo.githubusercontent.com/160da3074f3ed744c11a5b66a426429e7d03e43f09fe6980b1e5e213b0e809bf/68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f6769746875622e636f6d2f67756f6e6169686f6e672f636c6f70" referrerpolicy="no-referrer"></a></p> 
<p style="text-align:start">clop 是一款基于struct的命令行解析器，麻雀虽小，五脏俱全。(从零实现) <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fimages%2Fblob%2Fmaster%2Fclop.png%3Fraw%3Dtrue" target="_blank"><img alt="clop.png" src="https://github.com/guonaihong/images/raw/master/clop.png?raw=true" referrerpolicy="no-referrer"></a></p> 
<h2 style="text-align:start">feature</h2> 
<ul> 
 <li>支持环境变量绑定 <code>env DEBUG=xx ./proc</code></li> 
 <li>支持参数搜集 <code>cat a.txt b.txt</code>，可以把<code>a.txt, b.txt</code>散装成员归归类，收集到你指定的结构体成员里</li> 
 <li>支持短选项<code>proc -d</code> 或者长选项<code>proc --debug</code>不在话下</li> 
 <li>posix风格命令行支持，支持命令组合<code>ls -ltr</code>是<code>ls -l -t -r</code>简写形式，方便实现普通posix 标准命令</li> 
 <li>子命令支持，方便实现git风格子命令<code>git add </code>，简洁的子命令注册方式，只要会写结构体就行，3,4,5到无穷尽子命令也支持，只要你喜欢，用上clop就可以实现</li> 
 <li>默认值支持<code>default:"1"</code>，支持多种数据类型，让你省去类型转换的烦恼</li> 
 <li>贴心的重复命令报错</li> 
 <li>严格的短选项，长选项报错。避免二义性选项诞生</li> 
 <li>效验模式支持，不需要写一堆的<code>if x!= "" </code>or <code>if y!=0</code>浪费青春的代码</li> 
 <li>可以获取命令优先级别，方便设置命令别名</li> 
 <li>解析flag包代码生成clop代码</li> 
</ul> 
<h2 style="text-align:start">内容</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Installation" target="_blank">Installation</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23quick-start" target="_blank">Quick start</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23example" target="_blank">example</a> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23base-type" target="_blank">base type</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23int" target="_blank">int</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23float64" target="_blank">float64</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23duration" target="_blank">time.Duration</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23string" target="_blank">string</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23array" target="_blank">array</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23similar-to-curl-command" target="_blank">similar to curl command</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23similar-to-join-command" target="_blank">similar to join command</a></li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23required-flag" target="_blank">1. How to use required tags</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23support-environment-variables" target="_blank">2. Support environment variables</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23set-default-value" target="_blank">3. Set default value</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23subcommand" target="_blank">4. How to implement git style commands</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23get-command-priority" target="_blank">5. Get command priority</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23can-only-be-set-once" target="_blank">6. Can only be set once</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23quick-write" target="_blank">7. Quick write</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Advanced-features" target="_blank">Advanced features</a> 
    <ul> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Parsing-flag-code-to-generate-clop-code" target="_blank">Parsing flag code to generate clop code</a></li> 
    </ul> </li> 
  </ul> </li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Implementing-linux-command-options" target="_blank">Implementing linux command options</a> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23cat" target="_blank">cat</a></li> 
  </ul> </li> 
</ul> 
<h2 style="text-align:start">Installation</h2> 
<div style="text-align:start"> 
 <pre><code>go get github.com/guonaihong/clop
</code></pre> 
</div> 
<h2 style="text-align:start">Quick start</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Hello</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">File</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-f; --file" usage:"file"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

h <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Hello</span>&#123;&#125;
clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>h)
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%#v\n"</span>, h)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// ./one -f test</span>
<span style="color:var(--color-prettylights-syntax-comment)">// main.Hello&#123;File:"test"&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">// ./one --file test</span>
<span style="color:var(--color-prettylights-syntax-comment)">// main.Hello&#123;File:"test"&#125;</span></pre> 
</div> 
<h2 style="text-align:start">example</h2> 
<h3 style="text-align:start">base type</h3> 
<h4 style="text-align:start">int</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
        <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>

        <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">IntDemo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Int</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"short;long" usage:"int"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
        id <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">IntDemo</span>&#123;&#125;
        clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(id)
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"id = %v\n"</span>, id)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">//  ./int -i 3</span>
<span style="color:var(--color-prettylights-syntax-comment)">// id = &&#123;3&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">// ./int --int 3</span>
<span style="color:var(--color-prettylights-syntax-comment)">// id = &&#123;3&#125;</span></pre> 
</div> 
<h4 style="text-align:start">float64</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
        <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>

        <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Float64Demo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Float64</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">float64</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"short;long" usage:"float64"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
        fd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Float64Demo</span>&#123;&#125;
        clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(fd)
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"fd = %v\n"</span>, fd)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// ./float64 -f 3.14</span>
<span style="color:var(--color-prettylights-syntax-comment)">// fd = &&#123;3.14&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">// ./float64 --float64 3.14</span>
<span style="color:var(--color-prettylights-syntax-comment)">// fd = &&#123;3.14&#125;</span></pre> 
</div> 
<h4 style="text-align:start">duration</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
        <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
        <span style="color:var(--color-prettylights-syntax-string)">"time"</span>

        <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">DurationDemo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Duration</span> time.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Duration</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"short;long" usage:"duration"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
        dd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">DurationDemo</span>&#123;&#125;
        clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(dd)
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"dd = %v\n"</span>, dd)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// ./duration -d 1h</span>
<span style="color:var(--color-prettylights-syntax-comment)">// dd = &&#123;1h0m0s&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">// ./duration --duration 1h</span>
<span style="color:var(--color-prettylights-syntax-comment)">// dd = &&#123;1h0m0s&#125;</span></pre> 
</div> 
<h4 style="text-align:start">string</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
        <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>

        <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">StringDemo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">String</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"short;long" usage:"string"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
        s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">StringDemo</span>&#123;&#125;
        clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(s)
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"s = %v\n"</span>, s)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// ./string --string hello</span>
<span style="color:var(--color-prettylights-syntax-comment)">// s = &&#123;hello&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">// ./string -s hello</span>
<span style="color:var(--color-prettylights-syntax-comment)">// s = &&#123;hello&#125;</span></pre> 
</div> 
<h2 style="text-align:start">array</h2> 
<h4 style="text-align:start">similar to curl command</h4> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
        <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>

        <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">ArrayDemo</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Header</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-H;long" usage:"header"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
        h <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">ArrayDemo</span>&#123;&#125;
        clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(h)
        fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"h = %v\n"</span>, h)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// ./array -H session:sid --header token:my</span>
<span style="color:var(--color-prettylights-syntax-comment)">// h = &&#123;[session:sid token:my]&#125;</span></pre> 
</div> 
<h2 style="text-align:start">similar to join command</h2> 
<p style="text-align:start">加上greedy属性，就支持数组贪婪写法。类似join命令。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>

    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">test</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">A</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-a;greedy" usage:"test array"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">B</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>   <span style="color:var(--color-prettylights-syntax-string)">`clop:"-b" usage:"test int"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    a <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">test</span>&#123;&#125;
    clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(a)
    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%#v\n"</span>, a)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">运行</span>
<span style="color:var(--color-prettylights-syntax-comment)">./use_array -a 12 34 56 78 -b 100</span>
<span style="color:var(--color-prettylights-syntax-comment)">输出</span>
<span style="color:var(--color-prettylights-syntax-comment)">&main.test&#123;A:[]int&#123;12, 34, 56, 78&#125;, B:100&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h3 style="text-align:start">required flag</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">curl</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Url</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-u; --url" usage:"url" valid:"required"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">curl</span>&#123;&#125;
clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>c)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// ./required </span>
<span style="color:var(--color-prettylights-syntax-comment)">// error: -u; --url must have a value!</span>
<span style="color:var(--color-prettylights-syntax-comment)">// For more information try --help</span></pre> 
</div> 
<h4 style="text-align:start">set default value</h4> 
<p style="text-align:start">可以使用default tag设置默认值，普通类型直接写，复合类型用json表示</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">defaultExample</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Int</span>          <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>       <span style="color:var(--color-prettylights-syntax-string)">`default:"1"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Float64</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">float64</span>   <span style="color:var(--color-prettylights-syntax-string)">`default:"3.64"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">Float32</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">float32</span>   <span style="color:var(--color-prettylights-syntax-string)">`default:"3.32"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">SliceString</span>  []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>  <span style="color:var(--color-prettylights-syntax-string)">`default:"[\"one\", \"two\"]"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">SliceInt</span>     []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>     <span style="color:var(--color-prettylights-syntax-string)">`default:"[1,2,3,4,5]"`</span>
    <span style="color:var(--color-prettylights-syntax-constant)">SliceFloat64</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">float64</span> <span style="color:var(--color-prettylights-syntax-string)">`default:"[1.1,2.2,3.3,4.4,5.5]"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    de <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">defaultExample</span>&#123;&#125;
    clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>de)
    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%v\n"</span>, de) 
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// run</span>
<span style="color:var(--color-prettylights-syntax-comment)">//         ./use_def</span>
<span style="color:var(--color-prettylights-syntax-comment)">// output:</span>
<span style="color:var(--color-prettylights-syntax-comment)">//         &#123;1 3.64 3.32 [one two] [1 2 3 4 5] [1.1 2.2 3.3 4.4 5.5]&#125;</span></pre> 
</div> 
<h3 style="text-align:start">Support environment variables</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-comment)">// file name use_env.go</span>
<span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">env</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">OmpNumThread</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"env=omp_num_thread" usage:"omp num thread"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Path</span>         <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"env=XPATH" usage:"xpath"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Max</span>          <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`clop:"env=MAX" usage:"max thread"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
e <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">env</span>&#123;&#125;
clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>e)
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%#v\n"</span>, e)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// run</span>
<span style="color:var(--color-prettylights-syntax-comment)">// env XPATH=`pwd` omp_num_thread=3 MAX=4 ./use_env </span>
<span style="color:var(--color-prettylights-syntax-comment)">// output</span>
<span style="color:var(--color-prettylights-syntax-comment)">// main.env&#123;OmpNumThread:"3", Path:"/home/guo", Max:4&#125;</span></pre> 
</div> 
<h3 style="text-align:start">subcommand</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">add</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">All</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span>     <span style="color:var(--color-prettylights-syntax-string)">`clop:"-A; --all" usage:"add changes from all tracked and untracked files"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Force</span>    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span>     <span style="color:var(--color-prettylights-syntax-string)">`clop:"-f; --force" usage:"allow adding otherwise ignored files"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Pathspec</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"args=pathspec"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">mv</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Force</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-f; --force" usage:"allow adding otherwise ignored files"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">git</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Add</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">add</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"subcommand=add" usage:"Add file contents to the index"`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Mv</span>  <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">mv</span>  <span style="color:var(--color-prettylights-syntax-string)">`clop:"subcommand=mv" usage:"Move or rename a file, a directory, or a symlink"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
g <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">git</span>&#123;&#125;
clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>g)
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"git:%#v\n"</span>, g)
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"git:set mv(%t) or set add(%t)\n"</span>, clop.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)">"mv"</span>), clop.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)">"add"</span>))

<span style="color:var(--color-prettylights-syntax-keyword)">switch</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">case</span> clop.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)">"mv"</span>):
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"subcommand mv\n"</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">case</span> clop.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)">"add"</span>):
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"subcommand add\n"</span>)
&#125;
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// run:</span>
<span style="color:var(--color-prettylights-syntax-comment)">// ./git add -f</span>

<span style="color:var(--color-prettylights-syntax-comment)">// output:</span>
<span style="color:var(--color-prettylights-syntax-comment)">// git:main.git&#123;Add:main.add&#123;All:false, Force:true, Pathspec:[]string(nil)&#125;, Mv:main.mv&#123;Force:false&#125;&#125;</span>
<span style="color:var(--color-prettylights-syntax-comment)">// git:set mv(false) or set add(true)</span>
<span style="color:var(--color-prettylights-syntax-comment)">// subcommand add</span></pre> 
</div> 
<h2 style="text-align:start">Get command priority</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">NumberNonblank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-b;--number-nonblank"</span>
<span style="color:var(--color-prettylights-syntax-string)">                             usage:"number nonempty output lines, overrides"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowEnds</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-E;--show-ends"</span>
<span style="color:var(--color-prettylights-syntax-string)">                       usage:"display $ at end of each line"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span>&#123;&#125;
clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>c)

<span style="color:var(--color-prettylights-syntax-keyword)">if</span> clop.<span style="color:var(--color-prettylights-syntax-entity)">GetIndex</span>(<span style="color:var(--color-prettylights-syntax-string)">"number-nonblank"</span>) <span style="color:var(--color-prettylights-syntax-constant)"><</span> clop.<span style="color:var(--color-prettylights-syntax-entity)">GetIndex</span>(<span style="color:var(--color-prettylights-syntax-string)">"show-ends"</span>) &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"cat -b -E\n"</span>)
&#125; <span style="color:var(--color-prettylights-syntax-keyword)">else</span> &#123;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"cat -E -b \n"</span>)
&#125;
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">// cat -be </span>
<span style="color:var(--color-prettylights-syntax-comment)">// 输出 cat -b -E</span>
<span style="color:var(--color-prettylights-syntax-comment)">// cat -Eb</span>
<span style="color:var(--color-prettylights-syntax-comment)">// 输出 cat -E -b</span></pre> 
</div> 
<h2 style="text-align:start">Can only be set once</h2> 
<p style="text-align:start">指定选项只能被设置一次，如果命令行选项，使用两次则会报错。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Once</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Debug</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-d; --debug; once" usage:"debug mode"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    o <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Once</span>&#123;&#125;
    clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>o)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">./once -debug -debug</span>
<span style="color:var(--color-prettylights-syntax-comment)">error: The argument '-d' was provided more than once, but cannot be used multiple times</span>
<span style="color:var(--color-prettylights-syntax-comment)">For more information try --help</span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div> 
<h2 style="text-align:start">quick write</h2> 
<p style="text-align:start">快速写法，通过使用固定的short, long tag生成短，长选项。可以和 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23cat" target="_blank">cat</a> 例子直观比较下。命令行选项越多，越能节约时间，提升效率。</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

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
<h2 style="text-align:start">Advanced features</h2> 
<p style="text-align:start">高级功能里面有一些clop包比较有特色的功能</p> 
<h3 style="text-align:start">Parsing flag code to generate clop code</h3> 
<p style="text-align:start">让你爽翻天, 如果你的command想迁移至clop, 但是面对众多的flag代码, 又不想花费太多时间在无谓的人肉code转换上, 这时候你就需要clop命令, 一行命令解决你的痛点.</p> 
<h4 style="text-align:start">1.安装clop命令</h4> 
<div style="text-align:start"> 
 <pre>go get github.com/guonaihong/clop/cmd/clop</pre> 
</div> 
<h4 style="text-align:start">2.使用clop解析包含flag包的代码</h4> 
<p style="text-align:start">就可以把main.go里面的flag库转成clop包的调用方式</p> 
<div style="text-align:start"> 
 <pre>clop -f main.go</pre> 
</div> 
<p style="text-align:start"><code>main.go</code>代码如下</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> <span style="color:var(--color-prettylights-syntax-string)">"flag"</span>

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">"string"</span>, <span style="color:var(--color-prettylights-syntax-string)">""</span>, <span style="color:var(--color-prettylights-syntax-string)">"string usage"</span>)
i <span style="color:var(--color-prettylights-syntax-constant)">:=</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Int</span>(<span style="color:var(--color-prettylights-syntax-string)">"int"</span>, <span style="color:var(--color-prettylights-syntax-string)">""</span>, <span style="color:var(--color-prettylights-syntax-string)">"int usage"</span>)
flag.<span style="color:var(--color-prettylights-syntax-entity)">Parse</span>()
&#125;</pre> 
</div> 
<p style="text-align:start">输出代码如下</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">flagAutoGen</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Flag</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"--string" usage:"string usage" `</span>
<span style="color:var(--color-prettylights-syntax-constant)">Flag</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`clop:"--int" usage:"int usage" `</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">var</span> flagVar <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">flagAutoGen</span>
clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>flagVar)
&#125;</pre> 
</div> 
<h2 style="text-align:start">Implementing linux command options</h2> 
<h3 style="text-align:start">cat</h3> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/guonaihong/clop"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">NumberNonblank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-c;--number-nonblank" </span>
<span style="color:var(--color-prettylights-syntax-string)">                     usage:"number nonempty output lines, overrides"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowEnds</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-E;--show-ends" </span>
<span style="color:var(--color-prettylights-syntax-string)">               usage:"display $ at end of each line"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">Number</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-n;--number" </span>
<span style="color:var(--color-prettylights-syntax-string)">             usage:"number all output lines"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">SqueezeBlank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-s;--squeeze-blank" </span>
<span style="color:var(--color-prettylights-syntax-string)">                   usage:"suppress repeated empty output lines"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowTab</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-T;--show-tabs" </span>
<span style="color:var(--color-prettylights-syntax-string)">              usage:"display TAB characters as ^I"`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowNonprinting</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"-v;--show-nonprinting" </span>
<span style="color:var(--color-prettylights-syntax-string)">                      usage:"use ^ and M- notation, except for LFD and TAB" `</span>

<span style="color:var(--color-prettylights-syntax-constant)">Files</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:"args=files"`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

c <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span>&#123;&#125;
err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> clop.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>c)

fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%#v, %s\n"</span>, c, err)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">/*</span>
<span style="color:var(--color-prettylights-syntax-comment)">Usage:</span>
<span style="color:var(--color-prettylights-syntax-comment)">    ./cat [Flags] <files> </span>

<span style="color:var(--color-prettylights-syntax-comment)">Flags:</span>
<span style="color:var(--color-prettylights-syntax-comment)">    -E,--show-ends           display $ at end of each line </span>
<span style="color:var(--color-prettylights-syntax-comment)">    -T,--show-tabs           display TAB characters as ^I </span>
<span style="color:var(--color-prettylights-syntax-comment)">    -c,--number-nonblank     number nonempty output lines, overrides </span>
<span style="color:var(--color-prettylights-syntax-comment)">    -n,--number              number all output lines </span>
<span style="color:var(--color-prettylights-syntax-comment)">    -s,--squeeze-blank       suppress repeated empty output lines </span>
<span style="color:var(--color-prettylights-syntax-comment)">    -v,--show-nonprinting    use ^ and M- notation, except for LFD and TAB </span>

<span style="color:var(--color-prettylights-syntax-comment)">Args:</span>
<span style="color:var(--color-prettylights-syntax-comment)">    <files></span>
<span style="color:var(--color-prettylights-syntax-comment)">*/</span></pre> 
</div>
                                        </div>
                                      
</div>
            
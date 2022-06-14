
---
title: 'clop v0.2.6，Go 纯结构体（struct）命令行解析器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://github.com/guonaihong/clop/workflows/Go/badge.svg'
author: 开源中国
comments: false
date: Tue, 14 Jun 2022 15:45:00 GMT
thumbnail: 'https://github.com/guonaihong/clop/workflows/Go/badge.svg'
---

<div>   
<div class="content">
                                                                                            <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li><span> </span>项目地址 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>https://gitee.com/guonaihong/clop</li> 
   <li>https://github.com/guonaihong/clop</li> 
  </ul> </li> 
 <li>本次更新内容 
  <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
   <li>优化：子命令的用法</li> 
  </ul> </li> 
</ul> 
<hr> 
<div style="text-align:start"> 
 <div style="margin-left:0px; margin-right:0px"> 
  <h1 style="margin-left:0; margin-right:0">clop</h1> 
  <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%2Factions" target="_blank"><img alt="Go" src="https://github.com/guonaihong/clop/workflows/Go/badge.svg" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodecov.io%2Fgh%2Fguonaihong%2Fclop" target="_blank"><img alt="codecov" src="https://camo.githubusercontent.com/5d7c2d573c0d202b49b364bae93913eafc02a33684408a6a14ac1c1f9ce028db/68747470733a2f2f636f6465636f762e696f2f67682f67756f6e6169686f6e672f636c6f702f6272616e63682f6d61737465722f67726170682f62616467652e737667" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoreportcard.com%2Freport%2Fgithub.com%2Fguonaihong%2Fclop" target="_blank"><img alt="Go Report Card" src="https://camo.githubusercontent.com/160da3074f3ed744c11a5b66a426429e7d03e43f09fe6980b1e5e213b0e809bf/68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f6769746875622e636f6d2f67756f6e6169686f6e672f636c6f70" referrerpolicy="no-referrer"></a></p> 
  <p style="margin-left:0; margin-right:0">clop (Command Line Option Parse) 是一款基于 struct 的命令行解析器，麻雀虽小，五脏俱全 (从零实现)。</p> 
  <p style="margin-left:0; margin-right:0"><img alt height="388" src="https://oscimg.oschina.net/oscnet/up-fe03ae23574fa2c9c0852dcb1647afe06e2.png" width="649" referrerpolicy="no-referrer"></p> 
  <h2 style="margin-left:0; margin-right:0">feature</h2> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li>支持环境变量绑定<span> </span><code>env DEBUG=xx ./proc</code></li> 
   <li>支持参数搜集<span> </span><code>cat a.txt b.txt</code>，可以把<span> </span><code>a.txt, b.txt</code><span> </span>散装成员归归类，收集到你指定的结构体成员里</li> 
   <li>支持短选项<span> </span><code>proc -d</code><span> </span>或者长选项<span> </span><code>proc --debug</code><span> </span>不在话下</li> 
   <li>posix 风格命令行支持，支持命令组合<span> </span><code>ls -ltr</code><span> </span>是<span> </span><code>ls -l -t -r</code><span> </span>简写形式，方便实现普通 posix 标准命令</li> 
   <li>子命令 (<code>subcommand</code>) 支持，方便实现 git 风格子命令<span> </span><code>git add<span> </span></code>，简洁的子命令注册方式，只要会写结构体就行，3,4,5 到无穷尽子命令也支持，只要你喜欢，用上 clop 就可以实现</li> 
   <li>默认值支持<span> </span><code>default:"1"</code>，支持多种数据类型，让你省去类型转换的烦恼</li> 
   <li>贴心的重复命令报错</li> 
   <li>严格的短选项，长选项报错。避免二义性选项诞生</li> 
   <li>效验模式支持，不需要写一堆的<span> </span><code>if x!= ""<span> </span></code>or<span> </span><code>if y!=0</code><span> </span>浪费青春的代码</li> 
   <li>可以获取命令优先级别，方便设置命令别名</li> 
   <li>解析 flag 包代码生成 clop 代码</li> 
  </ul> 
  <p style="margin-left:0; margin-right:0"><img alt height="711" src="https://oscimg.oschina.net/oscnet/up-62e3edd442f3f9613e879cefbb614d67b10.png" width="899" referrerpolicy="no-referrer"></p> 
  <h2 style="margin-left:0; margin-right:0">内容</h2> 
  <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Installation" target="_blank">Installation</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23quick-start" target="_blank">Quick start</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23example" target="_blank">example</a> 
    <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23base-type" target="_blank">base type</a> 
      <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23int" target="_blank">int</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23float64" target="_blank">float64</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23duration" target="_blank">time.Duration</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23string" target="_blank">string</a></li> 
      </ul> </li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23array" target="_blank">array</a> 
      <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23similar-to-curl-command" target="_blank">similar to curl command</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23similar-to-join-command" target="_blank">similar to join command</a></li> 
      </ul> </li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23required-flag" target="_blank">1. How to use required tags</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23support-environment-variables" target="_blank">2. Support environment variables</a> 
      <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23custom-environment-variable-name" target="_blank">2.1 Custom environment variable name</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23quick-writing-of-environment-variables" target="_blank">2.2 Quick writing of environment variables</a></li> 
      </ul> </li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23set-default-value" target="_blank">3. Set default value</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23subcommand" target="_blank">4. How to implement git style commands</a> 
      <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23sub-command-implementation-method-1" target="_blank">4.1 Sub command implementation method 1</a></li> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23sub-command-implementation-method-2" target="_blank">4.2 Sub command implementation method 2</a></li> 
      </ul> </li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23get-command-priority" target="_blank">5. Get command priority</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23can-only-be-set-once" target="_blank">6. Can only be set once</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23quick-write" target="_blank">7. Quick write</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23multi-structure-series" target="_blank">8. Multi structure series</a></li> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Advanced-features" target="_blank">Advanced features</a> 
      <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
       <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Parsing-flag-code-to-generate-clop-code" target="_blank">Parsing flag code to generate clop code</a></li> 
      </ul> </li> 
    </ul> </li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23Implementing-linux-command-options" target="_blank">Implementing linux command options</a> 
    <ul style="list-style-type:circle; margin-left:0; margin-right:0"> 
     <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23cat" target="_blank">cat</a></li> 
    </ul> </li> 
  </ul> 
  <h2 style="margin-left:0; margin-right:0">Installation</h2> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><code><span style="color:#6f42c1">go</span> <span style="color:#032f62">get github.com/guonaihong/clop</span>
</code></pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">Quick start</h2> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Hello</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">File</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-f; --file" usage:"file"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;

<span>h</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Hello</span>&#123;&#125;
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">SetVersion</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"v0.2.0"</span></span>)
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">SetAbout</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"这是一个简单的示例demo"</span></span>)
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>h</span>)
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"%#v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>h</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./one -f test</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// main.Hello&#123;File:"test"&#125;</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./one --file test</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// main.Hello&#123;File:"test"&#125;</span></span></pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">example</h2> 
  <h3 style="margin-left:0; margin-right:0">base type</h3> 
  <h4 style="margin-left:0; margin-right:0">int</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>

        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">IntDemo</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Int</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">int</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"short;long" usage:"int"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
        <span>id</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">IntDemo</span>&#123;&#125;
        <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span>id</span>)
        <span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"id = %v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>id</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">//  ./int -i 3</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// id = &&#123;3&#125;</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./int --int 3</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// id = &&#123;3&#125;</span></span></pre> 
  </div> 
  <h4 style="margin-left:0; margin-right:0">float64</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>

        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Float64Demo</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Float64</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">float64</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"short;long" usage:"float64"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
        <span>fd</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Float64Demo</span>&#123;&#125;
        <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span>fd</span>)
        <span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fd = %v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>fd</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./float64 -f 3.14</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// fd = &&#123;3.14&#125;</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./float64 --float64 3.14</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// fd = &&#123;3.14&#125;</span></span></pre> 
  </div> 
  <h4 style="margin-left:0; margin-right:0">duration</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"time"</span></span>

        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">DurationDemo</span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> </span>&#123;
        <span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">Duration</span></span> time.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">Duration</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"short;long"</span> usage:<span style="color:#032f62">"duration"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
        <span>dd</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">DurationDemo</span></span>&#123;&#125;
        <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">Bind</span></span>(<span>dd</span>)
        <span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">Printf</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"dd = %v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>dd</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./duration -d 1h</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// dd = &&#123;1h0m0s&#125;</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./duration --duration 1h</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// dd = &&#123;1h0m0s&#125;</span></span></pre> 
  </div> 
  <h4 style="margin-left:0; margin-right:0">string</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>

        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">StringDemo</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">String</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"short;long" usage:"string"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
        <span>s</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">StringDemo</span>&#123;&#125;
        <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span>s</span>)
        <span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"s = %v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>s</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./string --string hello</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// s = &&#123;hello&#125;</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./string -s hello</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// s = &&#123;hello&#125;</span></span></pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">array</h2> 
  <h4 style="margin-left:0; margin-right:0">similar to curl command</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>

        <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">ArrayDemo</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Header</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-H;long" usage:"header"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
        <span>h</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">ArrayDemo</span>&#123;&#125;
        <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span>h</span>)
        <span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"h = %v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>h</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./array -H session:sid --header token:my</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// h = &&#123;[session:sid token:my]&#125;</span></span></pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">similar to join command</h2> 
  <p style="margin-left:0; margin-right:0">加上 greedy 属性，就支持数组贪婪写法。类似 join 命令。</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>

    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">test</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">A</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">int</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-a;greedy" usage:"test array"`</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">B</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">int</span></span>   <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-b" usage:"test int"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
    <span>a</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">test</span>&#123;&#125;
    <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span>a</span>)
    <span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"%#v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>a</span>)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">/*</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">运行</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">./use_array -a 12 34 56 78 -b 100</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">输出</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">&main.test&#123;A:[]int&#123;12, 34, 56, 78&#125;, B:100&#125;</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">*/</span></span></pre> 
  </div> 
  <h3 style="margin-left:0; margin-right:0">required flag</h3> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">curl</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> </span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">Url</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-u; --url"</span> usage:<span style="color:#032f62">"url"</span> valid:<span style="color:#032f62">"required"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;

<span><span>c</span></span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">curl</span>&#123;&#125;
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">Bind</span></span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span><span>c</span></span>)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./required </span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// error: -u; --url must have a value!</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// For more information try --help</span></span></pre> 
  </div> 
  <h4 style="margin-left:0; margin-right:0">set default value</h4> 
  <p style="margin-left:0; margin-right:0">可以使用 default tag 设置默认值，普通类型直接写，复合类型用 json 表示</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">defaultExample</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Int</span>          <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">int</span></span>       <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`default:"1"`</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">Float64</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">float64</span></span>   <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`default:"3.64"`</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">Float32</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">float32</span></span>   <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`default:"3.32"`</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">SliceString</span>  []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span>  <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`default:"[\"one\", \"two\"]"`</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">SliceInt</span>     []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">int</span></span>     <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`default:"[1,2,3,4,5]"`</span></span>
    <span style="color:var(--color-prettylights-syntax-constant)">SliceFloat64</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">float64</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`default:"[1.1,2.2,3.3,4.4,5.5]"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
    <span>de</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">defaultExample</span>&#123;&#125;
    <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>de</span>)
    <span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"%v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>de</span>) 
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// run</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">//         ./use_def</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// output:</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">//         &#123;1 3.64 3.32 [one two] [1 2 3 4 5] [1.1 2.2 3.3 4.4 5.5]&#125;</span></span></pre> 
  </div> 
  <h3 style="margin-left:0; margin-right:0">Support environment variables</h3> 
  <h4 style="margin-left:0; margin-right:0">custom environment variable name</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// file name use_env.go</span></span>
<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">env</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">OmpNumThread</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"env=omp_num_thread" usage:"omp num thread"`</span></span>
<span style="color:var(--color-prettylights-syntax-constant)">Path</span>         <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"env=XPATH" usage:"xpath"`</span></span>
<span style="color:var(--color-prettylights-syntax-constant)">Max</span>          <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">int</span></span>    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"env=MAX" usage:"max thread"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
<span>e</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">env</span>&#123;&#125;
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>e</span>)
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"%#v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>e</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// run</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// env XPATH=`pwd` omp_num_thread=3 MAX=4 ./use_env </span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// output</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// main.env&#123;OmpNumThread:"3", Path:"/home/guo", Max:4&#125;</span></span></pre> 
  </div> 
  <h4 style="margin-left:0; margin-right:0">Quick writing of environment variables</h4> 
  <p style="margin-left:0; margin-right:0">使用 env tag 会根据结构体名，生成一个环境变量名，规则就是驼峰命令名，改成大写下划线</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// file name use_env.go</span></span>
<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">env</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">OmpNumThread</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"env" usage:"omp num thread"`</span></span>
<span style="color:var(--color-prettylights-syntax-constant)">Xpath</span>         <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"env" usage:"xpath"`</span></span>
<span style="color:var(--color-prettylights-syntax-constant)">Max</span>          <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">int</span></span>    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"env" usage:"max thread"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
<span>e</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">env</span>&#123;&#125;
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>e</span>)
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"%#v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>e</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// run</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// env XPATH=`pwd` OMP_NUM_THREAD=3 MAX=4 ./use_env </span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// output</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// main.env&#123;OmpNumThread:"3", Xpath:"/home/guo", Max:4&#125;</span></span></pre> 
  </div> 
  <h3 style="margin-left:0; margin-right:0">subcommand</h3> 
  <h4 style="margin-left:0; margin-right:0">Sub command implementation method 1</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">type</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span style="color:#6f42c1">add</span></span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> &#123;</span>
<span style="color:var(--color-prettylights-syntax-constant)">All</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span>     <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-A; --all"</span> usage:<span style="color:#032f62">"add changes from all tracked and untracked files"</span>`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Force</span>    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span>     <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-f; --force"</span> usage:<span style="color:#032f62">"allow adding otherwise ignored files"</span>`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Pathspec</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"args=pathspec"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">type</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span style="color:#6f42c1">mv</span></span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> &#123;</span>
<span style="color:var(--color-prettylights-syntax-constant)">Force</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-f; --force"</span> usage:<span style="color:#032f62">"allow adding otherwise ignored files"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">type</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span style="color:#6f42c1">git</span></span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> &#123;</span>
<span style="color:var(--color-prettylights-syntax-constant)">Add</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">add</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"subcommand=add"</span> usage:<span style="color:#032f62">"Add file contents to the index"</span>`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Mv</span>  <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">mv</span>  <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"subcommand=mv"</span> usage:<span style="color:#032f62">"Move or rename a file, a directory, or a symlink"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
<span>g</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">git</span>&#123;&#125;
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>g</span>)
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"git:%#v</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>g</span>)
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"git:set mv(%t) or set add(%t)</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"mv"</span></span>), <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"add"</span></span>))

<span style="color:var(--color-prettylights-syntax-keyword)">switch</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">case</span> <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"mv"</span></span>):
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"subcommand mv</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>)
<span style="color:var(--color-prettylights-syntax-keyword)">case</span> <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">IsSetSubcommand</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"add"</span></span>):
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"subcommand add</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>)
&#125;
&#125;

<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// run:</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./git add -f</span></span>

<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// output:</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// git:main.git&#123;Add:main.add&#123;All:false, Force:true, Pathspec:[]string(nil)&#125;, Mv:main.mv&#123;Force:false&#125;&#125;</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// git:set mv(false) or set add(true)</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// subcommand add</span></span></pre> 
  </div> 
  <h4 style="margin-left:0; margin-right:0">Sub command implementation method 2</h4> 
  <p style="margin-left:0; margin-right:0">使用 clop 实现子命令的第 2 种做法，子命令结构体只要实现<span> </span><code>SubMain</code><span> </span>方法，该方法 clop 库会帮你自动调用。省去在 main 里面写一堆 if else 判断 (相对方法 1 来说), 特别是子命令特别多的情况，推荐用这种方法.</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">add</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">All</span>      <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">bool</span></span>     <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-A; --all" usage:"add changes from all tracked and untracked files"`</span></span>
<span style="color:var(--color-prettylights-syntax-constant)">Force</span>    <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">bool</span></span>     <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-f; --force" usage:"allow adding otherwise ignored files"`</span></span>
<span style="color:var(--color-prettylights-syntax-constant)">Pathspec</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">string</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"args=pathspec"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> <span>(</span></span><span><span><span>a</span></span></span><span><span> </span></span><span style="color:var(--color-prettylights-syntax-constant)"><span><span>*</span></span></span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span>add</span></span></span><span><span>)</span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">SubMain</span></span></span><span><span>()</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// 当add子命令被设置时</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// clop会自动调用这个函数</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">mv</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Force</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">bool</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-f; --force" usage:"allow adding otherwise ignored files"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> <span>(</span></span><span><span><span>m</span></span></span><span><span> </span></span><span style="color:var(--color-prettylights-syntax-constant)"><span><span>*</span></span></span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span>mv</span></span></span><span><span>)</span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">SubMain</span></span></span><span><span>()</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// 当mv 子命令被设置时</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// clop会自动调用这个函数</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">git</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Add</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">add</span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"subcommand=add" usage:"Add file contents to the index"`</span></span>
<span style="color:var(--color-prettylights-syntax-constant)">Mv</span>  <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">mv</span>  <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"subcommand=mv" usage:"Move or rename a file, a directory, or a symlink"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
<span>g</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">git</span>&#123;&#125;
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>g</span>)
&#125;</pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">Get command priority</h2> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> </span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">NumberNonblank</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-b;--number-nonblank"</span></span>
<span style="color:var(--color-prettylights-syntax-string)">                             usage:<span style="color:#032f62">"number nonempty output lines, overrides"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">ShowEnds</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-E;--show-ends"</span></span>
<span style="color:var(--color-prettylights-syntax-string)">                       usage:<span style="color:#032f62">"display $ at end of each line"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;

<span><span>c</span></span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span>&#123;&#125;
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">Bind</span></span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span><span>c</span></span>)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">if</span></span> <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">GetIndex</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"number-nonblank"</span></span>) <span style="color:var(--color-prettylights-syntax-constant)"><</span> <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">GetIndex</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"show-ends"</span></span>) &#123;
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">Printf</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"cat -b -E</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>)
&#125; <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">else</span></span> &#123;
<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">Printf</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"cat -E -b </span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>)
&#125;
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// cat -be </span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// 输出 cat -b -E</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// cat -Eb</span></span>
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// 输出 cat -E -b</span></span></pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">Can only be set once</h2> 
  <p style="margin-left:0; margin-right:0">指定选项只能被设置一次，如果命令行选项，使用两次则会报错。</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">type</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Once</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">struct</span></span> &#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Debug</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span style="color:#d73a49">bool</span></span> <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">`clop:"-d; --debug; once" usage:"debug mode"`</span></span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
    <span>o</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Once</span>&#123;&#125;
    <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>o</span>)
&#125;
<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">/*</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">./once -debug -debug</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">error: The argument '-d' was provided more than once, but cannot be used multiple times</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">For more information try --help</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">*/</span></span></pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">quick write</h2> 
  <p style="margin-left:0; margin-right:0">快速写法，通过使用固定的 short, long tag 生成短，长选项。可以和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fguonaihong%2Fclop%23cat" target="_blank">cat</a><span> </span>例子直观比较下。命令行选项越多，越能节约时间，提升效率。</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
    <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">type</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span style="color:#6f42c1">cat</span></span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> &#123;</span>
<span style="color:var(--color-prettylights-syntax-constant)">NumberNonblank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-c;long"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">                     usage:<span style="color:#032f62">"number nonempty output lines, overrides"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowEnds</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-E;long"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">               usage:<span style="color:#032f62">"display $ at end of each line"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">Number</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-n;long"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">             usage:<span style="color:#032f62">"number all output lines"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">SqueezeBlank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-s;long"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">                   usage:<span style="color:#032f62">"suppress repeated empty output lines"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowTab</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-T;long"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">              usage:<span style="color:#032f62">"display TAB characters as ^I"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowNonprinting</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-v;long"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">                      usage:<span style="color:#032f62">"use ^ and M- notation, except for LFD and TAB"</span> `</span>

<span style="color:var(--color-prettylights-syntax-constant)">Files</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"args=files"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
 <span>c</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span>&#123;&#125;
<span>err</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>c</span>)

<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"%#v, %s</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>c</span>, <span>err</span>)
&#125;</pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">Multi structure series</h2> 
  <p style="margin-left:0; margin-right:0">多结构体串联功能。多结构体统一组成一个命令行视图</p> 
  <p style="margin-left:0; margin-right:0">如果命令行解析是要怼到多个 (>=2) 结构体里面，可以使用结构体串联功能，前面几个结构体使用<span> </span><code>clop.Register()</code><span> </span>接口，最后一个结构体使用<span> </span><code>clop.Bind()</code><span> </span>函数.</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">/*</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">┌────────────────┐</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│  ServerAddress │                        ┌─────────────────────┐</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">├────────────────┤                        │                     │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │   ──────────────────►  │                     │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │                        │  clop.MustRegitser()│</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│     Rate       │                        │                     │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │                        └─────────────────────┘</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">└────────────────┘</span></span><span style="color:#6a737d">



</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">┌────────────────┐</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│   ThreadNum    │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │                        ┌─────────────────────┐</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │                        │                     │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">├────────────────┤   ──────────────────►  │                     │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │                        │ clop.Bind()         │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│   OpenVad      │                        │                     │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">│                │                        │                     │</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">└────────────────┘                        └─────────────────────┘</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d"> */</span></span>

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">type</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span style="color:#6f42c1">Server</span></span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> &#123;</span>
<span style="color:var(--color-prettylights-syntax-constant)">ServerAddress</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"long"</span> usage:<span style="color:#032f62">"Server address"</span>`</span>
<span style="color:var(--color-prettylights-syntax-constant)">Rate</span> time.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Duration</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"long"</span> usage:<span style="color:#032f62">"The speed at which audio is sent"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">type</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span style="color:#6f42c1">Asr</span></span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span>&#123;</span>
<span style="color:var(--color-prettylights-syntax-constant)">ThreadNum</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"long"</span> usage:<span style="color:#032f62">"thread number"</span>`</span>
<span style="color:var(--color-prettylights-syntax-constant)">OpenVad</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"long"</span> usage:<span style="color:#032f62">"open vad"</span>`</span>
&#125;

 <span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
 <span>asr</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Asr</span>&#123;&#125;
 <span>ser</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Server</span>&#123;&#125;
 <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">MustRegister</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>asr</span>)
 <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>ser</span>)
 &#125;

 <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// 可以使用如下命令行参数测试下效果</span></span>
 <span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">// ./example --server-address", ":8080", "--rate", "1s", "--thread-num", "20", "--open-vad"</span></span></pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">Advanced features</h2> 
  <p style="margin-left:0; margin-right:0">高级功能里面有一些 clop 包比较有特色的功能</p> 
  <h3 style="margin-left:0; margin-right:0">Parsing flag code to generate clop code</h3> 
  <p style="margin-left:0; margin-right:0">让你爽翻天，如果你的 command 想迁移至 clop, 但是面对众多的 flag 代码，又不想花费太多时间在无谓的人肉 code 转换上，这时候你就需要 clop 命令，一行命令解决你的痛点.</p> 
  <h4 style="margin-left:0; margin-right:0">1. 安装 clop 命令</h4> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1">go</span> <span style="color:#032f62">get github.com/guonaihong/clop/cmd/clop</span></pre> 
  </div> 
  <h4 style="margin-left:0; margin-right:0">2. 使用 clop 解析包含 flag 包的代码</h4> 
  <p style="margin-left:0; margin-right:0">就可以把 main.go 里面的 flag 库转成 clop 包的调用方式</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:#6f42c1">clop</span> <span style="color:#032f62">-f main.go</span></pre> 
  </div> 
  <p style="margin-left:0; margin-right:0"><code>main.go</code><span> </span>代码如下</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">package</span></span> <span style="color:#d73a49">main</span>

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> <span style="color:var(--color-prettylights-syntax-string)">"<span style="color:#d73a49">flag</span>"</span>

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">func</span></span> <span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">main</span></span>() &#123;
<span><span style="color:#005cc5">s</span></span><span style="color:#005cc5"> </span><span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span>flag</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span>String</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"string"</span></span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">""</span></span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"string usage"</span></span>)
<span>i</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span>flag</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span>Int</span></span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"int"</span></span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">""</span></span>, <span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"int usage"</span></span>)
<span>flag</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span>Parse</span></span>()
&#125;</pre> 
  </div> 
  <p style="margin-left:0; margin-right:0">输出代码如下</p> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">import</span></span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">flagAutoGen</span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> </span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">Flag</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"--string"</span> usage:<span style="color:#032f62">"string usage"</span> `</span>
<span style="color:var(--color-prettylights-syntax-constant)"><span style="color:#d73a49">Flag</span></span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">int</span>    <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"--int"</span> usage:<span style="color:#032f62">"int usage"</span> `</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">func</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-entity)"><span><span style="color:#6f42c1">main</span></span></span><span><span>()</span></span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)"><span style="color:#d73a49">var</span></span> <span>flagVar</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">flagAutoGen</span>
<span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)"><span style="color:#d73a49">Bind</span></span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>flagVar</span>)
&#125;</pre> 
  </div> 
  <h2 style="margin-left:0; margin-right:0">Implementing linux command options</h2> 
  <h3 style="margin-left:0; margin-right:0">cat</h3> 
  <div> 
   <pre style="margin-left:0; margin-right:0"><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"fmt"</span></span>
<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"github.com/guonaihong/clop"</span></span>
)

<span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">type</span></span></span><span> </span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span><span style="color:#6f42c1">cat</span></span></span> <span style="color:var(--color-prettylights-syntax-keyword)"><span><span style="color:#d73a49">struct</span></span></span><span> &#123;</span>
<span style="color:var(--color-prettylights-syntax-constant)">NumberNonblank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-c;--number-nonblank"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">                     usage:<span style="color:#032f62">"number nonempty output lines, overrides"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowEnds</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-E;--show-ends"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">               usage:<span style="color:#032f62">"display $ at end of each line"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">Number</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-n;--number"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">             usage:<span style="color:#032f62">"number all output lines"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">SqueezeBlank</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-s;--squeeze-blank"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">                   usage:<span style="color:#032f62">"suppress repeated empty output lines"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowTab</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-T;--show-tabs"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">              usage:<span style="color:#032f62">"display TAB characters as ^I"</span>`</span>

<span style="color:var(--color-prettylights-syntax-constant)">ShowNonprinting</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)"><span>bool</span></span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"-v;--show-nonprinting"</span> </span>
<span style="color:var(--color-prettylights-syntax-string)">                      usage:<span style="color:#032f62">"use ^ and M- notation, except for LFD and TAB"</span> `</span>

<span style="color:var(--color-prettylights-syntax-constant)">Files</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> <span style="color:var(--color-prettylights-syntax-string)">`clop:<span style="color:#032f62">"args=files"</span>`</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;

<span>c</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">cat</span>&#123;&#125;
<span>err</span> <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span>clop</span>.<span style="color:var(--color-prettylights-syntax-entity)">Bind</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span><span>c</span>)

<span>fmt</span>.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)"><span style="color:#032f62">"%#v, %s</span><span><span style="color:#032f62">\n</span></span><span style="color:#032f62">"</span></span>, <span>c</span>, <span>err</span>)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">/*</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">Usage:</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    ./cat [Flags] <files> </span></span><span style="color:#6a737d">

</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">Flags:</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    -E,--show-ends           display $ at end of each line </span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    -T,--show-tabs           display TAB characters as ^I </span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    -c,--number-nonblank     number nonempty output lines, overrides </span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    -n,--number              number all output lines </span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    -s,--squeeze-blank       suppress repeated empty output lines </span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    -v,--show-nonprinting    use ^ and M- notation, except for LFD and TAB </span></span><span style="color:#6a737d">

</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">Args:</span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">    <files></span></span><span style="color:#6a737d">
</span><span style="color:var(--color-prettylights-syntax-comment)"><span style="color:#6a737d">*/</span><span> </span></span></pre> 
  </div> 
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            
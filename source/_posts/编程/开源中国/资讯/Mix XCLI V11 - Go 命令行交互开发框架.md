
---
title: 'Mix XCLI V1.1 - Go 命令行交互开发框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6276'
author: 开源中国
comments: false
date: Thu, 22 Apr 2021 11:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6276'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">Mix XCLI</h2> 
<p style="text-align:start"><span style="color:#000000">命令行交互开发框架</span></p> 
<p style="text-align:start"><span style="color:#000000">CLI Interactive Commander</span></p> 
<h2 style="text-align:start">Overview</h2> 
<p style="text-align:start"><span style="color:#000000">一个命令行交互开发库，它可以让单个 CLI 程序可执行多个命令，同时它还包括命令行参数获取、全局 panic 捕获与处理、程序后台执行等命令行开发常用功能。</span></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxcli" target="_blank">https://github.com/mix-go/xcli</a></p> 
<h2 style="text-align:start">Installation</h2> 
<pre style="text-align:start"><code>go get github.com/mix-go/xcli
</code></pre> 
<h2 style="text-align:start">Quick start</h2> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/flag"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
    xcli.<span style="color:var(--color-prettylights-syntax-entity)">SetName</span>(<span style="color:var(--color-prettylights-syntax-string)">"app"</span>).<span style="color:var(--color-prettylights-syntax-entity)">SetVersion</span>(<span style="color:var(--color-prettylights-syntax-string)">"0.0.0-alpha"</span>)
    cmd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"hello"</span>,
        <span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"Echo demo"</span>,
        <span style="color:var(--color-prettylights-syntax-constant)">Run</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
            name <span style="color:var(--color-prettylights-syntax-constant)">:=</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"n"</span>, <span style="color:var(--color-prettylights-syntax-string)">"name"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">"default"</span>)
            <span style="color:var(--color-prettylights-syntax-comment)">// do something</span>
        &#125;,
    &#125;
    opt <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Option</span>&#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"n"</span>, <span style="color:var(--color-prettylights-syntax-string)">"name"</span>&#125;,
        <span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"Your name"</span>,
    &#125;
    cmd.<span style="color:var(--color-prettylights-syntax-entity)">AddOption</span>(opt)
    xcli.<span style="color:var(--color-prettylights-syntax-entity)">AddCommand</span>(cmd).<span style="color:var(--color-prettylights-syntax-entity)">Run</span>()
&#125;</pre> 
</div> 
<p style="text-align:start"><span style="color:#000000">编译后，查看整个命令行程序的帮助</span></p> 
<pre style="text-align:start"><code>$ ./go_build_main_go 
Usage: ./go_build_main_go [OPTIONS] COMMAND [opt...]

Commands:
  hello         Echo demo

Global Options:
  -h, --help    Print usage
  -v, --version Print version information

Run './go_build_main_go COMMAND --help' for more information on a command.

Developed with Mix Go framework. (openmix.org/mix-go)
</code></pre> 
<p style="text-align:start"><span style="color:#000000">查看命令行程序的版本信息</span></p> 
<pre style="text-align:start"><code>$ ./go_build_main_go -v
app 0.0.0-alpha, framework 1.0.9
</code></pre> 
<p style="text-align:start"><span style="color:#000000">查看 <code>hello</code> 命令的帮助</span></p> 
<pre style="text-align:start"><code>$ ./go_build_main_go hello --help
Usage: ./go_build_main_go hello [opt...]

Command Options:
  -n, --name    Your name

Developed with Mix Go framework. (openmix.org/mix-go)
</code></pre> 
<p style="text-align:start"><span style="color:#000000">执行 <code>hello</code> 命令</span></p> 
<pre style="text-align:start"><code>$ ./go_build_main_go hello 
</code></pre> 
<h2 style="text-align:start">Flag 参数获取</h2> 
<blockquote> 
 <p>该 flag 比 golang 自带的更加好用，不需要 Parse 操作</p> 
</blockquote> 
<p style="text-align:start"><span style="color:#000000">参数规则 (部分UNIX风格+GNU风格)</span></p> 
<pre style="text-align:start"><code>/examples/app home -d -rf --debug -v vvv --page 23 -s=test --name=john arg0
</code></pre> 
<ul> 
 <li>命令： 
  <ul> 
   <li>第一个参数，可以为空：<code>home</code></li> 
  </ul> </li> 
 <li>选项： 
  <ul> 
   <li>短选项：一个中杠，如 <code>-d</code>、<code>-rf</code></li> 
   <li>长选项：二个中杠，如：<code>--debug</code></li> 
  </ul> </li> 
 <li>选项值： 
  <ul> 
   <li>无值：<code>-d</code>、<code>-rf</code>、 <code>--debug</code></li> 
   <li>有值(空格)：<code>-v vvv</code>、<code>--page 23</code></li> 
   <li>有值(等号)：<code>-s=test</code>、<code>--name=john</code></li> 
  </ul> </li> 
 <li>参数： 
  <ul> 
   <li>没有定义 <code>-</code> 的参数：<code>arg0</code></li> 
  </ul> </li> 
</ul> 
<p style="text-align:start"><span style="color:#000000">获取选项，可以获取 <code>String</code>、<code>Bool</code>、<code>Int64</code>、<code>Float64</code> 多种类型，也可以指定默认值。</span></p> 
<pre style="text-align:start"><code>name := flag.Match("n", "name").String("Xiao Ming")
</code></pre> 
<p style="text-align:start"><span style="color:#000000">获取第一个参数</span></p> 
<pre style="text-align:start"><code>arg0 := flag.Arguments().First().String()
</code></pre> 
<p style="text-align:start"><span style="color:#000000">获取全部参数</span></p> 
<pre style="text-align:start"><code>for k, v := range flag.Arguments().Values() &#123;
    // do something
&#125;
</code></pre> 
<h2 style="text-align:start">Daemon 后台执行</h2> 
<p style="text-align:start"><span style="color:#000000">将命令行程序变为后台执行，该方法只可在 Main 协程中使用。</span></p> 
<pre style="text-align:start"><code>process.Daemon()
</code></pre> 
<p style="text-align:start"><span style="color:#000000">我们可以通过配合 <code>flag</code> 获取参数，实现通过某几个参数控制程序后台执行。</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">if</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"d"</span>, <span style="color:var(--color-prettylights-syntax-string)">"daemon"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>() &#123;
    process.<span style="color:var(--color-prettylights-syntax-entity)">Daemon</span>()
&#125;</pre> 
</div> 
<p style="text-align:start"><span style="color:#000000">上面就实现了一个当命令行参数中带有 <code>-d/--daemon</code> 参数时，程序就在后台执行。</span></p> 
<h2 style="text-align:start">Handle panic 错误处理</h2> 
<div style="text-align:start"> 
 <pre>h <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(next <span style="color:var(--color-prettylights-syntax-keyword)">func</span>()) &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)">defer</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">recover</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
            <span style="color:var(--color-prettylights-syntax-comment)">// handle panic</span>
        &#125;
    &#125;()
    <span style="color:var(--color-prettylights-syntax-entity)">next</span>()
&#125;
cmd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"hello"</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"Echo demo"</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">Run</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-comment)">// do something</span>
    &#125;,
&#125;
xcli.<span style="color:var(--color-prettylights-syntax-entity)">Use</span>(h).<span style="color:var(--color-prettylights-syntax-entity)">AddCommand</span>(cmd).<span style="color:var(--color-prettylights-syntax-entity)">Run</span>()</pre> 
</div> 
<h2 style="text-align:start">Application</h2> 
<p style="text-align:start"><span style="color:#000000">我们在编写代码时，可能会要用到 App 中的一些信息。</span></p> 
<pre style="text-align:start"><code>// 获取基础路径(二进制所在目录路径)
xcli.App().BasePath

// App名称
xcli.App().Name

// App版本号
xcli.App().Version

// 是否开启debug
xcli.App().Debug
</code></pre> 
<h2 style="text-align:start">Singleton 单命令</h2> 
<p style="text-align:start"><span style="color:#000000">当我们的 CLI 只有一个命令时，只需要配置一下 <code>Singleton</code>：</span></p> 
<div style="text-align:start"> 
 <pre>cmd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"hello"</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"Echo demo"</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">Run</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-comment)">// do something</span>
    &#125;,
    <span style="color:var(--color-prettylights-syntax-constant)">Singleton</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>,
&#125;</pre> 
</div> 
<p style="text-align:start"><span style="color:#000000">命令的 Options 将会在 <code>-h/--help</code> 中打印</span></p> 
<pre style="text-align:start"><code>$ ./go_build_main_go 
Usage: ./go_build_main_go [OPTIONS] COMMAND [opt...]

Command Options:
  -n, --name    Your name

Global Options:
  -h, --help    Print usage
  -v, --version Print version information

Run './go_build_main_go --help' for more information on a command.

Developed with Mix Go framework. (openmix.org/mix-go)
</code></pre> 
<h2 style="text-align:start">Default 默认执行</h2> 
<p style="text-align:start"><span style="color:#000000">当我们的 CLI 有 CUI 时，需要实现点击后默认启动 UI 界面，只需要配置一下 <code>Default</code>：</span></p> 
<div style="text-align:start"> 
 <pre>cmd <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
    <span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"hello"</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"Echo demo"</span>,
    <span style="color:var(--color-prettylights-syntax-constant)">Run</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-comment)">// do something</span>
    &#125;,
    <span style="color:var(--color-prettylights-syntax-constant)">Default</span>: <span style="color:var(--color-prettylights-syntax-constant)">true</span>,
&#125;</pre> 
</div> 
<h2 style="text-align:start">License</h2> 
<p style="text-align:start"><span style="color:#000000">Apache License Version 2.0, </span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank"><span style="color:#000000">http://www.apache.org/licenses/</span></a></p>
                                        </div>
                                      
</div>
            
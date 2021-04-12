
---
title: 'MixGo v1.1 Go 快速开发标准工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://camo.githubusercontent.com/f5bcee97d6b49c118b671b7d752060c33165ad8ca4285eec76ecfbdd038e17a6/68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f6c6f67696e2e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267'
author: 开源中国
comments: false
date: Mon, 12 Apr 2021 17:36:00 GMT
thumbnail: 'https://camo.githubusercontent.com/f5bcee97d6b49c118b671b7d752060c33165ad8ca4285eec76ecfbdd038e17a6/68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f6c6f67696e2e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267'
---

<div>   
<div class="content">
                                                                                            <p style="text-align:start"><span style="color:#000000">Mix Go 是一个基于 Go 进行快速开发的完整系统，类似前端的 <code>Vue CLI</code>，提供：</span></p> 
<ul> 
 <li>通过 <code>mix-go/mixcli</code> 实现的交互式项目脚手架： 
  <ul> 
   <li>可以生成 <code>cli</code>, <code>api</code>, <code>web</code>, <code>grpc</code> 多种项目代码</li> 
   <li>生成的代码开箱即用</li> 
   <li>可选择是否需要 <code>.env</code> 环境配置</li> 
   <li>可选择是否需要 <code>.yml</code>, <code>.json</code>, <code>.toml</code> 等独立配置</li> 
   <li>可选择使用 <code>gorm</code>, <code>xorm</code> 的数据库</li> 
   <li>可选择使用 <code>logrus</code>, <code>zap</code> 的日志库</li> 
  </ul> </li> 
 <li>通过 <code>mix-go/xcli</code> 实现的命令行原型开发。</li> 
 <li>基于 <code>mix-go/xdi</code> 的 DI, IoC 容器。</li> 
</ul> 
<h2 style="text-align:start">快速开始</h2> 
<p style="text-align:start">安装</p> 
<pre style="text-align:start"><code>go get github.com/mix-go/mixcli
</code></pre> 
<p style="text-align:start">创建项目</p> 
<pre style="text-align:start"><code>$ mixcli new hello
Use the arrow keys to navigate: ↓ ↑ → ← 
? Select project type:
  ▸ CLI
    API
    Web (contains the websocket)
    gRPC
</code></pre> 
<h2 style="text-align:start">技术交流</h2> 
<p style="text-align:start">知乎：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zhihu.com%2Fpeople%2Fonanying" target="_blank">https://www.zhihu.com/people/onanying</a><br> 微博：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fweibo.com%2Fonanying" target="_blank">http://weibo.com/onanying</a></p> 
<h2 style="text-align:start">编写一个 CLI 程序</h2> 
<p style="text-align:start">首先我们使用 <code>mixcli</code> 命令创建一个项目骨架：</p> 
<pre style="text-align:start"><code>$ mixcli new hello
Use the arrow keys to navigate: ↓ ↑ → ← 
? Select project type:
  ▸ CLI
    API
    Web (contains the websocket)
    gRPC
</code></pre> 
<p style="text-align:start">生成骨架目录结构如下：</p> 
<pre style="text-align:start"><code>.
├── README.md
├── bin
├── commands
├── conf
├── configor
├── di
├── dotenv
├── go.mod
├── go.sum
├── logs
└── main.go
</code></pre> 
<p style="text-align:start"><code>mian.go</code> 文件：</p> 
<ul> 
 <li><code>xcli.AddCommand</code> 方法传入的 <code>commands.Commands</code> 定义了全部的命令</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/cli-skeleton/commands"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/cli-skeleton/configor"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/cli-skeleton/di"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/cli-skeleton/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
xcli.<span style="color:var(--color-prettylights-syntax-entity)">SetName</span>(<span style="color:var(--color-prettylights-syntax-string)">"app"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetVersion</span>(<span style="color:var(--color-prettylights-syntax-string)">"0.0.0-alpha"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetDebug</span>(dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"APP_DEBUG"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>(<span style="color:var(--color-prettylights-syntax-constant)">false</span>))
xcli.<span style="color:var(--color-prettylights-syntax-entity)">AddCommand</span>(commands.<span style="color:var(--color-prettylights-syntax-constant)">Commands</span><span style="color:var(--color-prettylights-syntax-constant)">...</span>).<span style="color:var(--color-prettylights-syntax-entity)">Run</span>()
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/main.go</code> 文件：</p> 
<p style="text-align:start">我们可以在这里自定义命令，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxcli" target="_blank">查看更多</a></p> 
<ul> 
 <li><code>RunI</code> 定义了 <code>hello</code> 命令执行的接口，也可以使用 <code>Run</code> 设定一个匿名函数</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">var</span> Commands <span style="color:var(--color-prettylights-syntax-constant)">=</span> []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"hello"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tEcho demo"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Options</span>: []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Option</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"n"</span>, <span style="color:var(--color-prettylights-syntax-string)">"name"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"Your name"</span>,
&#125;,
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"say"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tSay ..."</span>,
&#125;,
&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">RunI</span>: <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">HelloCommand</span>&#123;&#125;,
&#125;,
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/hello.go</code> 文件：</p> 
<p style="text-align:start">业务代码写在 <code>HelloCommand</code> 结构体的 <code>main</code> 方法中</p> 
<ul> 
 <li>代码中可以使用 <code>flag</code> 获取命令行参数，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxcli%23flag" target="_blank">查看更多</a></li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/flag"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">HelloCommand</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">HelloCommand</span>) <span style="color:var(--color-prettylights-syntax-entity)">Main</span>() &#123;
name <span style="color:var(--color-prettylights-syntax-constant)">:=</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"n"</span>, <span style="color:var(--color-prettylights-syntax-string)">"name"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">"OpenMix"</span>)
say <span style="color:var(--color-prettylights-syntax-constant)">:=</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"say"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">"Hello, World!"</span>)
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Printf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s: %s\n"</span>, name, say)
&#125;</pre> 
</div> 
<p style="text-align:start">接下来我们编译上面的程序：</p> 
<ul> 
 <li>linux & macOS</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go main.go
</code></pre> 
<ul> 
 <li>win</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go.exe main.go
</code></pre> 
<p style="text-align:start">查看全部命令的帮助信息：</p> 
<pre style="text-align:start"><code>$ cd bin
$ ./go_build_main_go 
Usage: ./go_build_main_go [OPTIONS] COMMAND [opt...]

Global Options:
  -h, --help    Print usage
  -v, --version Print version information

Commands:
  hello         Echo demo

Run './go_build_main_go COMMAND --help' for more information on a command.

Developed with Mix Go framework. (openmix.org/mix-go)
</code></pre> 
<p style="text-align:start">查看上面编写的 hello 命令的帮助信息：</p> 
<pre style="text-align:start"><code>$ ./go_build_main_go hello --help
Usage: ./go_build_main_go hello [opt...]

Command Options:
  -n, --name    Your name
  --say         Say ...

Developed with Mix Go framework. (openmix.org/mix-go)
</code></pre> 
<p style="text-align:start">执行 <code>hello</code> 命令，并传入两个参数：</p> 
<pre style="text-align:start"><code>$ ./go_build_main_go hello --name=liujian --say=hello
liujian: hello
</code></pre> 
<h3 style="text-align:start">编写一个 Worker Pool 队列消费</h3> 
<p style="text-align:start">队列消费是高并发系统中最常用的异步处理模型，通常我们是编写一个 CLI 命令行程序在后台执行 Redis、RabbitMQ 等 MQ 的队列消费，并将处理结果落地到 mysql 等数据库中，由于这类需求的标准化比较容易，因此我们开发了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxwp" target="_blank">mix-go/xwp</a> 库来处理这类需求，基本上大部分异步处理类需求都可使用。</p> 
<p style="text-align:start">新建 <code>commands/workerpool.go</code> 文件：</p> 
<ul> 
 <li><code>workerpool.NewDispatcher(jobQueue, 15, NewWorker)</code> 创建了一个调度器</li> 
 <li><code>NewWorker</code> 负责初始化执行任务的工作协程</li> 
 <li>任务数据会在 <code>worker.Do</code> 方法中触发，我们只需要将我们的业务逻辑写到该方法中即可</li> 
 <li>当程序接收到进程退出信号时，调度器能平滑控制所有的 Worker 在执行完队列里全部的任务后再退出调度，保证数据的完整性</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"context"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/cli-skeleton/di"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xwp"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"os"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"os/signal"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"strings"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"syscall"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">worker</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
    xwp.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WorkerTrait</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">worker</span>) <span style="color:var(--color-prettylights-syntax-entity)">Do</span>(data <span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;) &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)">defer</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">recover</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
            logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
            logger.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(err)
        &#125;
    &#125;()

    <span style="color:var(--color-prettylights-syntax-comment)">// 执行业务处理</span>
    <span style="color:var(--color-prettylights-syntax-comment)">// ...</span>
    
    <span style="color:var(--color-prettylights-syntax-comment)">// 将处理结果落地到数据库</span>
    <span style="color:var(--color-prettylights-syntax-comment)">// ...</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">NewWorker</span>() xwp.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Worker</span> &#123;
    <span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">worker</span>&#123;&#125;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WorkerPoolDaemonCommand</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WorkerPoolDaemonCommand</span>) <span style="color:var(--color-prettylights-syntax-entity)">Main</span>() &#123;
    redis <span style="color:var(--color-prettylights-syntax-constant)">:=</span> globals.<span style="color:var(--color-prettylights-syntax-entity)">Redis</span>()
    jobQueue <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(<span style="color:var(--color-prettylights-syntax-keyword)">chan</span> <span style="color:var(--color-prettylights-syntax-keyword)">interface</span>&#123;&#125;, <span style="color:var(--color-prettylights-syntax-constant)">50</span>)
    d <span style="color:var(--color-prettylights-syntax-constant)">:=</span> xwp.<span style="color:var(--color-prettylights-syntax-entity)">NewDispatcher</span>(jobQueue, <span style="color:var(--color-prettylights-syntax-constant)">15</span>, NewWorker)

    ch <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(<span style="color:var(--color-prettylights-syntax-keyword)">chan</span> os.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Signal</span>)
    signal.<span style="color:var(--color-prettylights-syntax-entity)">Notify</span>(ch, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGHUP</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGINT</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGTERM</span>)
    <span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-constant)"><-</span>ch
        d.<span style="color:var(--color-prettylights-syntax-entity)">Stop</span>()
    &#125;()

    <span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        <span style="color:var(--color-prettylights-syntax-keyword)">for</span> &#123;
            res, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> redis.<span style="color:var(--color-prettylights-syntax-entity)">BRPop</span>(context.<span style="color:var(--color-prettylights-syntax-entity)">Background</span>(), <span style="color:var(--color-prettylights-syntax-constant)">3</span><span style="color:var(--color-prettylights-syntax-constant)">*</span>time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>, <span style="color:var(--color-prettylights-syntax-string)">"foo"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Result</span>()
            <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
                <span style="color:var(--color-prettylights-syntax-keyword)">if</span> strings.<span style="color:var(--color-prettylights-syntax-entity)">Contains</span>(err.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(), <span style="color:var(--color-prettylights-syntax-string)">"redis: nil"</span>) &#123;
                    <span style="color:var(--color-prettylights-syntax-keyword)">continue</span>
                &#125;
                fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"Redis Error: %s"</span>, err))
                d.<span style="color:var(--color-prettylights-syntax-entity)">Stop</span>();
                <span style="color:var(--color-prettylights-syntax-keyword)">return</span>
            &#125;
            <span style="color:var(--color-prettylights-syntax-comment)">// brPop命令最后一个键才是值</span>
            jobQueue <span style="color:var(--color-prettylights-syntax-constant)"><-</span> res[<span style="color:var(--color-prettylights-syntax-constant)">1</span>]
        &#125;
    &#125;()

    d.<span style="color:var(--color-prettylights-syntax-entity)">Run</span>() <span style="color:var(--color-prettylights-syntax-comment)">// 阻塞代码，直到任务全部执行完成并且全部 Worker 停止</span>
&#125;</pre> 
</div> 
<p style="text-align:start">接下来只需要把这个命令通过 <code>xcli.AddCommand</code> 注册到 CLI 中即可。</p> 
<h2 style="text-align:start">编写一个 API 服务</h2> 
<p style="text-align:start">首先我们使用 <code>mixcli</code> 命令创建一个项目骨架：</p> 
<pre style="text-align:start"><code>$ mixcli new hello
Use the arrow keys to navigate: ↓ ↑ → ← 
? Select project type:
    CLI
  ▸ API
    Web (contains the websocket)
    gRPC
</code></pre> 
<p style="text-align:start">生成骨架目录结构如下：</p> 
<pre style="text-align:start"><code>.
├── README.md
├── bin
├── commands
├── conf
├── configor
├── controllers
├── di
├── dotenv
├── go.mod
├── go.sum
├── main.go
├── middleware
├── routes
└── runtime
</code></pre> 
<p style="text-align:start"><code>mian.go</code> 文件：</p> 
<ul> 
 <li><code>xcli.AddCommand</code> 方法传入的 <code>commands.Commands</code> 定义了全部的命令</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/commands"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/configor"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/di"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
xcli.<span style="color:var(--color-prettylights-syntax-entity)">SetName</span>(<span style="color:var(--color-prettylights-syntax-string)">"app"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetVersion</span>(<span style="color:var(--color-prettylights-syntax-string)">"0.0.0-alpha"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetDebug</span>(dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"APP_DEBUG"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>(<span style="color:var(--color-prettylights-syntax-constant)">false</span>))
xcli.<span style="color:var(--color-prettylights-syntax-entity)">AddCommand</span>(commands.<span style="color:var(--color-prettylights-syntax-constant)">Commands</span><span style="color:var(--color-prettylights-syntax-constant)">...</span>).<span style="color:var(--color-prettylights-syntax-entity)">Run</span>()
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/main.go</code> 文件：</p> 
<p style="text-align:start">我们可以在这里自定义命令，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxcli" target="_blank">查看更多</a></p> 
<ul> 
 <li><code>RunI</code> 指定了命令执行的接口，也可以使用 <code>Run</code> 设定一个匿名函数</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">var</span> Commands <span style="color:var(--color-prettylights-syntax-constant)">=</span> []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"api"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tStart the api server"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Options</span>: []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Option</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"a"</span>, <span style="color:var(--color-prettylights-syntax-string)">"addr"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tListen to the specified address"</span>,
&#125;,
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"d"</span>, <span style="color:var(--color-prettylights-syntax-string)">"daemon"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tRun in the background"</span>,
&#125;,
&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">RunI</span>: <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">APICommand</span>&#123;&#125;,
&#125;,
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/api.go</code> 文件：</p> 
<p style="text-align:start">业务代码写在 <code>APICommand</code> 结构体的 <code>main</code> 方法中，生成的代码中已经包含了：</p> 
<ul> 
 <li>监听信号停止服务</li> 
 <li>根据模式打印日志</li> 
 <li>可选的后台守护执行</li> 
</ul> 
<p style="text-align:start">基本上无需修改即可上线使用</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"context"</span>
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/gin-gonic/gin"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/di"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/routes"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/flag"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/process"</span>
<span style="color:var(--color-prettylights-syntax-string)">"os"</span>
<span style="color:var(--color-prettylights-syntax-string)">"os/signal"</span>
<span style="color:var(--color-prettylights-syntax-string)">"strings"</span>
<span style="color:var(--color-prettylights-syntax-string)">"syscall"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">APICommand</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">APICommand</span>) <span style="color:var(--color-prettylights-syntax-entity)">Main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"d"</span>, <span style="color:var(--color-prettylights-syntax-string)">"daemon"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>() &#123;
process.<span style="color:var(--color-prettylights-syntax-entity)">Daemon</span>()
&#125;

logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
server <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Server</span>()
addr <span style="color:var(--color-prettylights-syntax-constant)">:=</span> dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"GIN_ADDR"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>)
mode <span style="color:var(--color-prettylights-syntax-constant)">:=</span> dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"GIN_MODE"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(gin.<span style="color:var(--color-prettylights-syntax-constant)">ReleaseMode</span>)

<span style="color:var(--color-prettylights-syntax-comment)">// server</span>
gin.<span style="color:var(--color-prettylights-syntax-entity)">SetMode</span>(mode)
router <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gin.<span style="color:var(--color-prettylights-syntax-entity)">New</span>()
routes.<span style="color:var(--color-prettylights-syntax-entity)">SetRoutes</span>(router)
server.<span style="color:var(--color-prettylights-syntax-constant)">Addr</span> <span style="color:var(--color-prettylights-syntax-constant)">=</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"a"</span>, <span style="color:var(--color-prettylights-syntax-string)">"addr"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(addr)
server.<span style="color:var(--color-prettylights-syntax-constant)">Handler</span> <span style="color:var(--color-prettylights-syntax-constant)">=</span> router

<span style="color:var(--color-prettylights-syntax-comment)">// signal</span>
ch <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(<span style="color:var(--color-prettylights-syntax-keyword)">chan</span> os.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Signal</span>)
signal.<span style="color:var(--color-prettylights-syntax-entity)">Notify</span>(ch, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGHUP</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGINT</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGTERM</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
<span style="color:var(--color-prettylights-syntax-constant)"><-</span>ch
logger.<span style="color:var(--color-prettylights-syntax-entity)">Info</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server shutdown"</span>)
ctx, _ <span style="color:var(--color-prettylights-syntax-constant)">:=</span> context.<span style="color:var(--color-prettylights-syntax-entity)">WithTimeout</span>(context.<span style="color:var(--color-prettylights-syntax-entity)">Background</span>(), <span style="color:var(--color-prettylights-syntax-constant)">10</span><span style="color:var(--color-prettylights-syntax-constant)">*</span>time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> server.<span style="color:var(--color-prettylights-syntax-entity)">Shutdown</span>(ctx); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
logger.<span style="color:var(--color-prettylights-syntax-entity)">Errorf</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server shutdown error: %s"</span>, err)
&#125;
&#125;()

<span style="color:var(--color-prettylights-syntax-comment)">// logger</span>
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> mode <span style="color:var(--color-prettylights-syntax-constant)">!=</span> gin.<span style="color:var(--color-prettylights-syntax-constant)">ReleaseMode</span> &#123;
handlerFunc <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gin.<span style="color:var(--color-prettylights-syntax-entity)">LoggerWithConfig</span>(gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">LoggerConfig</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Formatter</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(params gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">LogFormatterParams</span>) <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s|%s|%d|%s"</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">Method</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">Path</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">StatusCode</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">ClientIP</span>,
)
&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Output</span>: logger.<span style="color:var(--color-prettylights-syntax-constant)">Out</span>,
&#125;)
router.<span style="color:var(--color-prettylights-syntax-entity)">Use</span>(handlerFunc)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// run</span>
<span style="color:var(--color-prettylights-syntax-entity)">welcome</span>()
logger.<span style="color:var(--color-prettylights-syntax-entity)">Infof</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server start at %s"</span>, server.<span style="color:var(--color-prettylights-syntax-constant)">Addr</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> server.<span style="color:var(--color-prettylights-syntax-entity)">ListenAndServe</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> <span style="color:var(--color-prettylights-syntax-constant)">&&</span> <span style="color:var(--color-prettylights-syntax-constant)">!</span>strings.<span style="color:var(--color-prettylights-syntax-entity)">Contains</span>(err.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(), <span style="color:var(--color-prettylights-syntax-string)">"http: Server closed"</span>) &#123;
<span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;
&#125;</pre> 
</div> 
<p style="text-align:start">在 <code>routes/main.go</code> 文件中配置路由：</p> 
<p style="text-align:start">已经包含一些常用实例，只需要在这里新增路由即可开始开发</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> routes

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/gin-gonic/gin"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/controllers"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/api-skeleton/middleware"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">SetRoutes</span>(router <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Engine</span>) &#123;
router.<span style="color:var(--color-prettylights-syntax-entity)">Use</span>(gin.<span style="color:var(--color-prettylights-syntax-entity)">Recovery</span>()) <span style="color:var(--color-prettylights-syntax-comment)">// error handle</span>

router.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"hello"</span>,
middleware.<span style="color:var(--color-prettylights-syntax-entity)">CorsMiddleware</span>(),
<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
hello <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">HelloController</span>&#123;&#125;
hello.<span style="color:var(--color-prettylights-syntax-entity)">Index</span>(ctx)
&#125;,
)

router.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">"users/add"</span>,
middleware.<span style="color:var(--color-prettylights-syntax-entity)">AuthMiddleware</span>(),
<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
hello <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">UserController</span>&#123;&#125;
hello.<span style="color:var(--color-prettylights-syntax-entity)">Add</span>(ctx)
&#125;,
)

router.<span style="color:var(--color-prettylights-syntax-entity)">POST</span>(<span style="color:var(--color-prettylights-syntax-string)">"auth"</span>, <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
auth <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">AuthController</span>&#123;&#125;
auth.<span style="color:var(--color-prettylights-syntax-entity)">Index</span>(ctx)
&#125;)
&#125;</pre> 
</div> 
<p style="text-align:start">接下来我们编译上面的程序：</p> 
<ul> 
 <li>linux & macOS</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go main.go
</code></pre> 
<ul> 
 <li>win</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go.exe main.go
</code></pre> 
<p style="text-align:start">启动服务器</p> 
<pre style="text-align:start"><code>$ bin/go_build_main_go api
             ___         
 ______ ___  _ /__ ___ _____ ______ 
  / __ `__ \/ /\ \/ /__  __ `/  __ \
 / / / / / / / /\ \/ _  /_/ // /_/ /
/_/ /_/ /_/_/ /_/\_\  \__, / \____/ 
                     /____/


Server      Name:      mix-api
Listen      Addr:      :8080
System      Name:      darwin
Go          Version:   1.13.4
Framework   Version:   1.0.9
time=2020-09-16 20:24:41.515 level=info msg=Server start file=api.go:58
</code></pre> 
<h2 style="text-align:start">编写一个 Web 服务</h2> 
<p style="text-align:start">首先我们使用 <code>mixcli</code> 命令创建一个项目骨架：</p> 
<pre style="text-align:start"><code>$ mixcli new hello
Use the arrow keys to navigate: ↓ ↑ → ← 
? Select project type:
    CLI
    API
  ▸ Web (contains the websocket)
    gRPC
</code></pre> 
<p style="text-align:start">生成骨架目录结构如下：</p> 
<pre style="text-align:start"><code>.
├── README.md
├── bin
├── commands
├── conf
├── configor
├── controllers
├── di
├── dotenv
├── go.mod
├── go.sum
├── main.go
├── middleware
├── public
├── routes
├── runtime
└── templates
</code></pre> 
<p style="text-align:start"><code>mian.go</code> 文件：</p> 
<ul> 
 <li><code>xcli.AddCommand</code> 方法传入的 <code>commands.Commands</code> 定义了全部的命令</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/commands"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/configor"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/di"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
xcli.<span style="color:var(--color-prettylights-syntax-entity)">SetName</span>(<span style="color:var(--color-prettylights-syntax-string)">"app"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetVersion</span>(<span style="color:var(--color-prettylights-syntax-string)">"0.0.0-alpha"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetDebug</span>(dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"APP_DEBUG"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>(<span style="color:var(--color-prettylights-syntax-constant)">false</span>))
xcli.<span style="color:var(--color-prettylights-syntax-entity)">AddCommand</span>(commands.<span style="color:var(--color-prettylights-syntax-constant)">Commands</span><span style="color:var(--color-prettylights-syntax-constant)">...</span>).<span style="color:var(--color-prettylights-syntax-entity)">Run</span>()
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/main.go</code> 文件：</p> 
<p style="text-align:start">我们可以在这里自定义命令，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxcli" target="_blank">查看更多</a></p> 
<ul> 
 <li><code>RunI</code> 指定了命令执行的接口，也可以使用 <code>Run</code> 设定一个匿名函数</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">var</span> Commands <span style="color:var(--color-prettylights-syntax-constant)">=</span> []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"web"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tStart the web server"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Options</span>: []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Option</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"a"</span>, <span style="color:var(--color-prettylights-syntax-string)">"addr"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tListen to the specified address"</span>,
&#125;,
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"d"</span>, <span style="color:var(--color-prettylights-syntax-string)">"daemon"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"\tRun in the background"</span>,
&#125;,
&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">RunI</span>: <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebCommand</span>&#123;&#125;,
&#125;,
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/web.go</code> 文件：</p> 
<p style="text-align:start">业务代码写在 <code>WebCommand</code> 结构体的 <code>main</code> 方法中，生成的代码中已经包含了：</p> 
<ul> 
 <li>监听信号停止服务</li> 
 <li>根据模式打印日志</li> 
 <li>可选的后台守护执行</li> 
</ul> 
<p style="text-align:start">基本上无需修改即可上线使用</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"context"</span>
<span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/gin-gonic/gin"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/di"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/routes"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/flag"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/process"</span>
<span style="color:var(--color-prettylights-syntax-string)">"os"</span>
<span style="color:var(--color-prettylights-syntax-string)">"os/signal"</span>
<span style="color:var(--color-prettylights-syntax-string)">"strings"</span>
<span style="color:var(--color-prettylights-syntax-string)">"syscall"</span>
<span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebCommand</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebCommand</span>) <span style="color:var(--color-prettylights-syntax-entity)">Main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"d"</span>, <span style="color:var(--color-prettylights-syntax-string)">"daemon"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>() &#123;
process.<span style="color:var(--color-prettylights-syntax-entity)">Daemon</span>()
&#125;

logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
server <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Server</span>()
addr <span style="color:var(--color-prettylights-syntax-constant)">:=</span> dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"GIN_ADDR"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>)
mode <span style="color:var(--color-prettylights-syntax-constant)">:=</span> dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"GIN_MODE"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(gin.<span style="color:var(--color-prettylights-syntax-constant)">ReleaseMode</span>)

<span style="color:var(--color-prettylights-syntax-comment)">// server</span>
gin.<span style="color:var(--color-prettylights-syntax-entity)">SetMode</span>(mode)
router <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gin.<span style="color:var(--color-prettylights-syntax-entity)">New</span>()
routes.<span style="color:var(--color-prettylights-syntax-entity)">SetRoutes</span>(router)
server.<span style="color:var(--color-prettylights-syntax-constant)">Addr</span> <span style="color:var(--color-prettylights-syntax-constant)">=</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"a"</span>, <span style="color:var(--color-prettylights-syntax-string)">"addr"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(addr)
server.<span style="color:var(--color-prettylights-syntax-constant)">Handler</span> <span style="color:var(--color-prettylights-syntax-constant)">=</span> router

<span style="color:var(--color-prettylights-syntax-comment)">// signal</span>
ch <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(<span style="color:var(--color-prettylights-syntax-keyword)">chan</span> os.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Signal</span>)
signal.<span style="color:var(--color-prettylights-syntax-entity)">Notify</span>(ch, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGHUP</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGINT</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGTERM</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
<span style="color:var(--color-prettylights-syntax-constant)"><-</span>ch
logger.<span style="color:var(--color-prettylights-syntax-entity)">Info</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server shutdown"</span>)
ctx, _ <span style="color:var(--color-prettylights-syntax-constant)">:=</span> context.<span style="color:var(--color-prettylights-syntax-entity)">WithTimeout</span>(context.<span style="color:var(--color-prettylights-syntax-entity)">Background</span>(), <span style="color:var(--color-prettylights-syntax-constant)">10</span><span style="color:var(--color-prettylights-syntax-constant)">*</span>time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> server.<span style="color:var(--color-prettylights-syntax-entity)">Shutdown</span>(ctx); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
logger.<span style="color:var(--color-prettylights-syntax-entity)">Errorf</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server shutdown error: %s"</span>, err)
&#125;
&#125;()

<span style="color:var(--color-prettylights-syntax-comment)">// logger</span>
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> mode <span style="color:var(--color-prettylights-syntax-constant)">!=</span> gin.<span style="color:var(--color-prettylights-syntax-constant)">ReleaseMode</span> &#123;
handlerFunc <span style="color:var(--color-prettylights-syntax-constant)">:=</span> gin.<span style="color:var(--color-prettylights-syntax-entity)">LoggerWithConfig</span>(gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">LoggerConfig</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Formatter</span>: <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(params gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">LogFormatterParams</span>) <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s|%s|%d|%s"</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">Method</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">Path</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">StatusCode</span>,
params.<span style="color:var(--color-prettylights-syntax-constant)">ClientIP</span>,
)
&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Output</span>: logger.<span style="color:var(--color-prettylights-syntax-constant)">Out</span>,
&#125;)
router.<span style="color:var(--color-prettylights-syntax-entity)">Use</span>(handlerFunc)
&#125;

<span style="color:var(--color-prettylights-syntax-comment)">// templates</span>
router.<span style="color:var(--color-prettylights-syntax-entity)">LoadHTMLGlob</span>(fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s/../templates/*"</span>, xcli.<span style="color:var(--color-prettylights-syntax-entity)">App</span>().<span style="color:var(--color-prettylights-syntax-constant)">BasePath</span>))

<span style="color:var(--color-prettylights-syntax-comment)">// static file</span>
router.<span style="color:var(--color-prettylights-syntax-entity)">Static</span>(<span style="color:var(--color-prettylights-syntax-string)">"/static"</span>, fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s/../public/static"</span>, xcli.<span style="color:var(--color-prettylights-syntax-entity)">App</span>().<span style="color:var(--color-prettylights-syntax-constant)">BasePath</span>))
router.<span style="color:var(--color-prettylights-syntax-entity)">StaticFile</span>(<span style="color:var(--color-prettylights-syntax-string)">"/favicon.ico"</span>, fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"%s/../public/favicon.ico"</span>, xcli.<span style="color:var(--color-prettylights-syntax-entity)">App</span>().<span style="color:var(--color-prettylights-syntax-constant)">BasePath</span>))

<span style="color:var(--color-prettylights-syntax-comment)">// run</span>
<span style="color:var(--color-prettylights-syntax-entity)">welcome</span>()
logger.<span style="color:var(--color-prettylights-syntax-entity)">Infof</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server start at %s"</span>, server.<span style="color:var(--color-prettylights-syntax-constant)">Addr</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> server.<span style="color:var(--color-prettylights-syntax-entity)">ListenAndServe</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> <span style="color:var(--color-prettylights-syntax-constant)">&&</span> <span style="color:var(--color-prettylights-syntax-constant)">!</span>strings.<span style="color:var(--color-prettylights-syntax-entity)">Contains</span>(err.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(), <span style="color:var(--color-prettylights-syntax-string)">"http: Server closed"</span>) &#123;
<span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;
&#125;</pre> 
</div> 
<p style="text-align:start">在 <code>routes/main.go</code> 文件中配置路由：</p> 
<p style="text-align:start">已经包含一些常用实例，只需要在这里新增路由即可开始开发</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> routes

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/gin-gonic/gin"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/controllers"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/middleware"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">SetRoutes</span>(router <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Engine</span>) &#123;
router.<span style="color:var(--color-prettylights-syntax-entity)">Use</span>(gin.<span style="color:var(--color-prettylights-syntax-entity)">Recovery</span>()) <span style="color:var(--color-prettylights-syntax-comment)">// error handle</span>

router.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"hello"</span>,
<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
hello <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">HelloController</span>&#123;&#125;
hello.<span style="color:var(--color-prettylights-syntax-entity)">Index</span>(ctx)
&#125;,
)

router.<span style="color:var(--color-prettylights-syntax-entity)">Any</span>(<span style="color:var(--color-prettylights-syntax-string)">"users/add"</span>,
middleware.<span style="color:var(--color-prettylights-syntax-entity)">SessionMiddleware</span>(),
<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
user <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">UserController</span>&#123;&#125;
user.<span style="color:var(--color-prettylights-syntax-entity)">Add</span>(ctx)
&#125;,
)

router.<span style="color:var(--color-prettylights-syntax-entity)">Any</span>(<span style="color:var(--color-prettylights-syntax-string)">"login"</span>, <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
login <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">LoginController</span>&#123;&#125;
login.<span style="color:var(--color-prettylights-syntax-entity)">Index</span>(ctx)
&#125;)

router.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"websocket"</span>,
<span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
ws <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketController</span>&#123;&#125;
ws.<span style="color:var(--color-prettylights-syntax-entity)">Index</span>(ctx)
&#125;,
)
&#125;</pre> 
</div> 
<p style="text-align:start">接下来我们编译上面的程序：</p> 
<ul> 
 <li>linux & macOS</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go main.go
</code></pre> 
<ul> 
 <li>win</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go.exe main.go
</code></pre> 
<p style="text-align:start">命令行启动 <code>web</code> 服务器：</p> 
<pre style="text-align:start"><code>$ bin/go_build_main_go web
             ___         
 ______ ___  _ /__ ___ _____ ______ 
  / __ `__ \/ /\ \/ /__  __ `/  __ \
 / / / / / / / /\ \/ _  /_/ // /_/ /
/_/ /_/ /_/_/ /_/\_\  \__, / \____/ 
                     /____/


Server      Name:      mix-web
Listen      Addr:      :8080
System      Name:      darwin
Go          Version:   1.13.4
Framework   Version:   1.0.9
time=2020-09-16 20:24:41.515 level=info msg=Server start file=web.go:58
</code></pre> 
<p style="text-align:start">浏览器测试:</p> 
<ul> 
 <li>首先浏览器进入 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F127.0.0.1%3A8080%2Flogin" target="_blank">http://127.0.0.1:8080/login</a> 获取 session</li> 
</ul> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2Ff5bcee97d6b49c118b671b7d752060c33165ad8ca4285eec76ecfbdd038e17a6%2F68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f6c6f67696e2e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267" target="_blank"><img alt src="https://camo.githubusercontent.com/f5bcee97d6b49c118b671b7d752060c33165ad8ca4285eec76ecfbdd038e17a6/68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f6c6f67696e2e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267" referrerpolicy="no-referrer"></a></p> 
<ul> 
 <li>提交表单后跳转到 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F127.0.0.1%3A8080%2Fusers%2Fadd" target="_blank">http://127.0.0.1:8080/users/add</a> 页面</li> 
</ul> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2Ff46afbd37b7b3bbbcbfdf7de262d645130fcce20b64121f5254716856a3b4ff0%2F68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f757365722d6164642e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267" target="_blank"><img alt src="https://camo.githubusercontent.com/f46afbd37b7b3bbbcbfdf7de262d645130fcce20b64121f5254716856a3b4ff0/68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f757365722d6164642e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267" referrerpolicy="no-referrer"></a></p> 
<h3 style="text-align:start">编写一个 WebSocket 服务</h3> 
<p style="text-align:start">WebSocket 是基于 http 协议完成握手的，因此我们编写代码时，也是和编写 Web 项目是差不多的，差别就是请求过来后，我们需要使用一个 WebSocket 的升级器，将请求升级为 WebSocket 连接，接下来就是针对连接的逻辑处理，从这个部分开始就和传统的 Socket 操作一致了。</p> 
<p style="text-align:start"><code>routes/main.go</code> 文件已经定义了一个 WebSocket 的路由：</p> 
<div style="text-align:start"> 
 <pre>router.<span style="color:var(--color-prettylights-syntax-entity)">GET</span>(<span style="color:var(--color-prettylights-syntax-string)">"websocket"</span>,
    <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(ctx <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
        ws <span style="color:var(--color-prettylights-syntax-constant)">:=</span> controllers.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketController</span>&#123;&#125;
        ws.<span style="color:var(--color-prettylights-syntax-entity)">Index</span>(ctx)
    &#125;,
)</pre> 
</div> 
<p style="text-align:start"><code>controllers/ws.go</code> 文件：</p> 
<ul> 
 <li>创建了一个 <code>upgrader</code> 的升级器，当请求过来时将会升级为 WebSocket 连接</li> 
 <li>定义了一个 <code>WebSocketSession</code> 的结构体负责管理连接的整个生命周期</li> 
 <li><code>session.Start()</code> 中启动了两个协程，分别处理消息的读和写</li> 
 <li>在消息读取的协程中，启动了 <code>WebSocketHandler</code> 结构体的 <code>Index</code> 方法来处理消息，在实际项目中我们可以根据不同的消息内容使用不同的结构体来处理，实现 Web 项目那种控制器的功能</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> controllers

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/gin-gonic/gin"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/gorilla/websocket"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/web-skeleton/di"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
<span style="color:var(--color-prettylights-syntax-string)">"net/http"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">var</span> upgrader <span style="color:var(--color-prettylights-syntax-constant)">=</span> websocket.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Upgrader</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">ReadBufferSize</span>:  <span style="color:var(--color-prettylights-syntax-constant)">1024</span>,
<span style="color:var(--color-prettylights-syntax-constant)">WriteBufferSize</span>: <span style="color:var(--color-prettylights-syntax-constant)">1024</span>,
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketController</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketController</span>) <span style="color:var(--color-prettylights-syntax-entity)">Index</span>(c <span style="color:var(--color-prettylights-syntax-constant)">*</span>gin.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>) &#123;
logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> xcli.<span style="color:var(--color-prettylights-syntax-entity)">App</span>().<span style="color:var(--color-prettylights-syntax-constant)">Debug</span> &#123;
upgrader.<span style="color:var(--color-prettylights-syntax-constant)">CheckOrigin</span> <span style="color:var(--color-prettylights-syntax-constant)">=</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>(r <span style="color:var(--color-prettylights-syntax-constant)">*</span>http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Request</span>) <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">bool</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">true</span>
&#125;
&#125;
conn, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> upgrader.<span style="color:var(--color-prettylights-syntax-entity)">Upgrade</span>(c.<span style="color:var(--color-prettylights-syntax-constant)">Writer</span>, c.<span style="color:var(--color-prettylights-syntax-constant)">Request</span>, <span style="color:var(--color-prettylights-syntax-constant)">nil</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
logger.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(err)
c.<span style="color:var(--color-prettylights-syntax-entity)">Status</span>(http.<span style="color:var(--color-prettylights-syntax-constant)">StatusInternalServerError</span>)
c.<span style="color:var(--color-prettylights-syntax-entity)">Abort</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;

session <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketSession</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Conn</span>:   conn,
<span style="color:var(--color-prettylights-syntax-constant)">Header</span>: c.<span style="color:var(--color-prettylights-syntax-constant)">Request</span>.<span style="color:var(--color-prettylights-syntax-constant)">Header</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Send</span>:   <span style="color:var(--color-prettylights-syntax-entity)">make</span>(<span style="color:var(--color-prettylights-syntax-keyword)">chan</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>, <span style="color:var(--color-prettylights-syntax-constant)">100</span>),
&#125;
session.<span style="color:var(--color-prettylights-syntax-entity)">Start</span>()

server <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Server</span>()
server.<span style="color:var(--color-prettylights-syntax-entity)">RegisterOnShutdown</span>(<span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
session.<span style="color:var(--color-prettylights-syntax-entity)">Stop</span>()
&#125;)

logger.<span style="color:var(--color-prettylights-syntax-entity)">Infof</span>(<span style="color:var(--color-prettylights-syntax-string)">"Upgrade: %s"</span>, c.<span style="color:var(--color-prettylights-syntax-constant)">Request</span>.<span style="color:var(--color-prettylights-syntax-entity)">UserAgent</span>())
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketSession</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Conn</span>   <span style="color:var(--color-prettylights-syntax-constant)">*</span>websocket.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Conn</span>
<span style="color:var(--color-prettylights-syntax-constant)">Header</span> http.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Header</span>
<span style="color:var(--color-prettylights-syntax-constant)">Send</span>   <span style="color:var(--color-prettylights-syntax-keyword)">chan</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketSession</span>) <span style="color:var(--color-prettylights-syntax-entity)">Start</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">for</span> &#123;
msgType, msg, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> t.<span style="color:var(--color-prettylights-syntax-constant)">Conn</span>.<span style="color:var(--color-prettylights-syntax-entity)">ReadMessage</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> <span style="color:var(--color-prettylights-syntax-constant)">!</span>websocket.<span style="color:var(--color-prettylights-syntax-entity)">IsCloseError</span>(err, <span style="color:var(--color-prettylights-syntax-constant)">1001</span>, <span style="color:var(--color-prettylights-syntax-constant)">1006</span>) &#123;
logger.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(err)
&#125;
t.<span style="color:var(--color-prettylights-syntax-entity)">Stop</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> msgType <span style="color:var(--color-prettylights-syntax-constant)">!=</span> websocket.<span style="color:var(--color-prettylights-syntax-constant)">TextMessage</span> &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">continue</span>
&#125;

handler <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketHandler</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Session</span>: t,
&#125;
handler.<span style="color:var(--color-prettylights-syntax-entity)">Index</span>(msg)
&#125;
&#125;()
<span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">for</span> &#123;
msg, ok <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-constant)"><-</span>t.<span style="color:var(--color-prettylights-syntax-constant)">Send</span>
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> <span style="color:var(--color-prettylights-syntax-constant)">!</span>ok &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> t.<span style="color:var(--color-prettylights-syntax-constant)">Conn</span>.<span style="color:var(--color-prettylights-syntax-entity)">WriteMessage</span>(websocket.<span style="color:var(--color-prettylights-syntax-constant)">TextMessage</span>, msg); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
logger.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(err)
t.<span style="color:var(--color-prettylights-syntax-entity)">Stop</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">return</span>
&#125;
&#125;
&#125;()
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketSession</span>) <span style="color:var(--color-prettylights-syntax-entity)">Stop</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">defer</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">recover</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
logger.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(err)
&#125;
&#125;()
<span style="color:var(--color-prettylights-syntax-entity)">close</span>(t.<span style="color:var(--color-prettylights-syntax-constant)">Send</span>)
_ <span style="color:var(--color-prettylights-syntax-constant)">=</span> t.<span style="color:var(--color-prettylights-syntax-constant)">Conn</span>.<span style="color:var(--color-prettylights-syntax-entity)">Close</span>()
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketHandler</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
<span style="color:var(--color-prettylights-syntax-constant)">Session</span> <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketSession</span>
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">WebSocketHandler</span>) <span style="color:var(--color-prettylights-syntax-entity)">Index</span>(msg []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>) &#123;
t.<span style="color:var(--color-prettylights-syntax-constant)">Session</span>.<span style="color:var(--color-prettylights-syntax-constant)">Send</span> <span style="color:var(--color-prettylights-syntax-constant)"><-</span> []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">byte</span>(<span style="color:var(--color-prettylights-syntax-string)">"hello, world!"</span>)
&#125;</pre> 
</div> 
<p style="text-align:start">接下来我们编译上面的程序：</p> 
<ul> 
 <li>linux & macOS</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go main.go
</code></pre> 
<ul> 
 <li>win</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go.exe main.go
</code></pre> 
<p style="text-align:start">在命令行启动 <code>web</code> 服务器：</p> 
<pre style="text-align:start"><code>$ bin/go_build_main_go web
             ___         
 ______ ___  _ /__ ___ _____ ______ 
  / __ `__ \/ /\ \/ /__  __ `/  __ \
 / / / / / / / /\ \/ _  /_/ // /_/ /
/_/ /_/ /_/_/ /_/\_\  \__, / \____/ 
                     /____/


Server      Name:      mix-web
Listen      Addr:      :8080
System      Name:      darwin
Go          Version:   1.13.4
Framework   Version:   1.0.9
time=2020-09-16 20:24:41.515 level=info msg=Server start file=web.go:58
</code></pre> 
<p style="text-align:start">浏览器测试:</p> 
<ul> 
 <li>我们使用现成的工具测试：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.easyswoole.com%2Fwstool.html" target="_blank">http://www.easyswoole.com/wstool.html</a></li> 
</ul> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2Fc89dc8e755ced15dc1a6e016f3a29bd0c078a618c1e20bed46291bf861e68f5b%2F68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f776562736f636b65745f746573742e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267" target="_blank"><img alt src="https://camo.githubusercontent.com/c89dc8e755ced15dc1a6e016f3a29bd0c078a618c1e20bed46291bf861e68f5b/68747470733a2f2f6769742e6b616e636c6f75642e636e2f7265706f732f6f6e616e79696e672f6d6978676f312f7261772f346633393830333835326632313535303034313732373631616539353633336634363636613365352f696d616765732f776562736f636b65745f746573742e706e673f6163636573732d746f6b656e3d65794a30655841694f694a4b563151694c434a68624763694f694a49557a49314e694a392e65794a6c654841694f6a45324d5463354f5455344e6a4573496d6c68644349364d5459784e7a6b314d6a59324d537769636d567762334e706447397965534936496d3975595735356157356e584339746158686e627a45694c434a3163325679496a7037496e567a5a584a755957316c496a6f6962323568626e6c70626d63694c434a755957316c496a6f69584855324e474934584855305a57557a584855334f444178584855334e6a6730584855305a545978584855305a544269584855305a574a68496977695a573168615777694f694a6a6232526c6369357361585641635845755932397449697769644739725a5734694f6949784f446b355a6a45774f44497a5a5759774d6d55784e7a51314d54677a4d6a6b34596a686a4e7a466b4d794973496d463164476876636d6c365a53493665794a7764577873496a7030636e566c4c434a7764584e6f496a7030636e566c4c434a685a4731706269493664484a315a58313966512e736961353333764e734c716256657476777674747973786757645262627a3076666d4e366a424e646c3267" referrerpolicy="no-referrer"></a></p> 
<h2 style="text-align:start">编写一个 gRPC 服务、客户端</h2> 
<p style="text-align:start">首先我们使用 <code>mixcli</code> 命令创建一个项目骨架：</p> 
<pre style="text-align:start"><code>$ mixcli new hello
Use the arrow keys to navigate: ↓ ↑ → ← 
? Select project type:
    CLI
    API
    Web (contains the websocket)
  ▸ gRPC
</code></pre> 
<p style="text-align:start">生成骨架目录结构如下：</p> 
<pre style="text-align:start"><code>.
├── README.md
├── bin
├── commands
├── conf
├── configor
├── di
├── dotenv
├── go.mod
├── go.sum
├── main.go
├── protos
├── runtime
└── services
</code></pre> 
<p style="text-align:start"><code>mian.go</code> 文件：</p> 
<ul> 
 <li><code>xcli.AddCommand</code> 方法传入的 <code>commands.Commands</code> 定义了全部的命令</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> main

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/commands"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/configor"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/di"</span>
_ <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> <span style="color:var(--color-prettylights-syntax-entity)">main</span>() &#123;
xcli.<span style="color:var(--color-prettylights-syntax-entity)">SetName</span>(<span style="color:var(--color-prettylights-syntax-string)">"app"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetVersion</span>(<span style="color:var(--color-prettylights-syntax-string)">"0.0.0-alpha"</span>).
<span style="color:var(--color-prettylights-syntax-entity)">SetDebug</span>(dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"APP_DEBUG"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>(<span style="color:var(--color-prettylights-syntax-constant)">false</span>))
xcli.<span style="color:var(--color-prettylights-syntax-entity)">AddCommand</span>(commands.<span style="color:var(--color-prettylights-syntax-constant)">Commands</span><span style="color:var(--color-prettylights-syntax-constant)">...</span>).<span style="color:var(--color-prettylights-syntax-entity)">Run</span>()
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/main.go</code> 文件：</p> 
<p style="text-align:start">我们可以在这里自定义命令，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxcli" target="_blank">查看更多</a></p> 
<ul> 
 <li>定义了 <code>grpc:server</code>、<code>grpc:client</code> 两个子命令</li> 
 <li><code>RunI</code> 指定了命令执行的接口，也可以使用 <code>Run</code> 设定一个匿名函数</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">var</span> Commands <span style="color:var(--color-prettylights-syntax-constant)">=</span> []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Command</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"grpc:server"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"gRPC server demo"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Options</span>: []<span style="color:var(--color-prettylights-syntax-constant)">*</span>xcli.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Option</span>&#123;
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Names</span>: []<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">string</span>&#123;<span style="color:var(--color-prettylights-syntax-string)">"d"</span>, <span style="color:var(--color-prettylights-syntax-string)">"daemon"</span>&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">Usage</span>: <span style="color:var(--color-prettylights-syntax-string)">"Run in the background"</span>,
&#125;,
&#125;,
<span style="color:var(--color-prettylights-syntax-constant)">RunI</span>: <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">GrpcServerCommand</span>&#123;&#125;,
&#125;,
&#123;
<span style="color:var(--color-prettylights-syntax-constant)">Name</span>:  <span style="color:var(--color-prettylights-syntax-string)">"grpc:client"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">Short</span>: <span style="color:var(--color-prettylights-syntax-string)">"gRPC client demo"</span>,
<span style="color:var(--color-prettylights-syntax-constant)">RunI</span>:  <span style="color:var(--color-prettylights-syntax-constant)">&</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">GrpcClientCommand</span>&#123;&#125;,
&#125;,
&#125;</pre> 
</div> 
<p style="text-align:start"><code>protos/user.proto</code> 数据结构文件：</p> 
<p style="text-align:start">客户端与服务器端代码中都需要使用 <code>.proto</code> 生成的 go 代码，因为双方需要使用该数据结构通讯</p> 
<ul> 
 <li><code>.proto</code> 是 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgrpc%2Fgrpc" target="_blank">gRPC</a> 通信的数据结构文件，采用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fprotocolbuffers%2Fprotobuf" target="_blank">protobuf</a> 协议</li> 
</ul> 
<pre style="text-align:start"><code>syntax = "proto3";

package go.micro.grpc.user;
option go_package = ".;protos";

service User &#123;
    rpc Add(AddRequest) returns (AddResponse) &#123;&#125;
&#125;

message AddRequest &#123;
    string Name = 1;
&#125;

message AddResponse &#123;
    int32 error_code = 1;
    string error_message = 2;
    int64 user_id = 3;
&#125;
</code></pre> 
<p style="text-align:start">然后我们需要安装 gRPC 相关的编译程序：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.cnblogs.com%2Foolo%2Fp%2F11840305.html%23%25E5%25AE%2589%25E8%25A3%2585-grpc" target="_blank">https://www.cnblogs.com/oolo/p/11840305.html#%E5%AE%89%E8%A3%85-grpc</a></li> 
</ul> 
<p style="text-align:start">接下来我们开始编译 <code>.proto</code> 文件：</p> 
<ul> 
 <li>编译成功后会在当前目录生成 <code>protos/user.pb.go</code> 文件</li> 
</ul> 
<pre style="text-align:start"><code>cd protos
protoc --go_out=plugins=grpc:. user.proto
</code></pre> 
<p style="text-align:start"><code>commands/server.go</code> 文件：</p> 
<p style="text-align:start">服务端代码写在 <code>GrpcServerCommand</code> 结构体的 <code>main</code> 方法中，生成的代码中已经包含了：</p> 
<ul> 
 <li>监听信号停止服务</li> 
 <li>可选的后台守护执行</li> 
 <li><code>pb.RegisterUserServer</code> 注册了一个默认服务，用户只需要扩展自己的服务即可</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/di"</span>
pb <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/protos"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/services"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/flag"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/xcli/process"</span>
<span style="color:var(--color-prettylights-syntax-string)">"google.golang.org/grpc"</span>
<span style="color:var(--color-prettylights-syntax-string)">"net"</span>
<span style="color:var(--color-prettylights-syntax-string)">"os"</span>
<span style="color:var(--color-prettylights-syntax-string)">"os/signal"</span>
<span style="color:var(--color-prettylights-syntax-string)">"strings"</span>
<span style="color:var(--color-prettylights-syntax-string)">"syscall"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">var</span> listener net.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Listener</span>

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">GrpcServerCommand</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">GrpcServerCommand</span>) <span style="color:var(--color-prettylights-syntax-entity)">Main</span>() &#123;
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> flag.<span style="color:var(--color-prettylights-syntax-entity)">Match</span>(<span style="color:var(--color-prettylights-syntax-string)">"d"</span>, <span style="color:var(--color-prettylights-syntax-string)">"daemon"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Bool</span>() &#123;
process.<span style="color:var(--color-prettylights-syntax-entity)">Daemon</span>()
&#125;

addr <span style="color:var(--color-prettylights-syntax-constant)">:=</span> dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"GIN_ADDR"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>)
logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()

<span style="color:var(--color-prettylights-syntax-comment)">// listen</span>
listener, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> net.<span style="color:var(--color-prettylights-syntax-entity)">Listen</span>(<span style="color:var(--color-prettylights-syntax-string)">"tcp"</span>, addr)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
<span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;
listener <span style="color:var(--color-prettylights-syntax-constant)">=</span> listener

<span style="color:var(--color-prettylights-syntax-comment)">// signal</span>
ch <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-entity)">make</span>(<span style="color:var(--color-prettylights-syntax-keyword)">chan</span> os.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Signal</span>)
signal.<span style="color:var(--color-prettylights-syntax-entity)">Notify</span>(ch, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGHUP</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGINT</span>, syscall.<span style="color:var(--color-prettylights-syntax-constant)">SIGTERM</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">go</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
<span style="color:var(--color-prettylights-syntax-constant)"><-</span>ch
logger.<span style="color:var(--color-prettylights-syntax-entity)">Info</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server shutdown"</span>)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> listener.<span style="color:var(--color-prettylights-syntax-entity)">Close</span>(); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
<span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;
&#125;()

<span style="color:var(--color-prettylights-syntax-comment)">// server</span>
s <span style="color:var(--color-prettylights-syntax-constant)">:=</span> grpc.<span style="color:var(--color-prettylights-syntax-entity)">NewServer</span>()
pb.<span style="color:var(--color-prettylights-syntax-entity)">RegisterUserServer</span>(s, <span style="color:var(--color-prettylights-syntax-constant)">&</span>services.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">UserService</span>&#123;&#125;)

<span style="color:var(--color-prettylights-syntax-comment)">// run</span>
<span style="color:var(--color-prettylights-syntax-entity)">welcome</span>()
logger.<span style="color:var(--color-prettylights-syntax-entity)">Infof</span>(<span style="color:var(--color-prettylights-syntax-string)">"Server run %s"</span>, addr)
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> s.<span style="color:var(--color-prettylights-syntax-entity)">Serve</span>(listener); err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> <span style="color:var(--color-prettylights-syntax-constant)">&&</span> <span style="color:var(--color-prettylights-syntax-constant)">!</span>strings.<span style="color:var(--color-prettylights-syntax-entity)">Contains</span>(err.<span style="color:var(--color-prettylights-syntax-entity)">Error</span>(), <span style="color:var(--color-prettylights-syntax-string)">"use of closed network connection"</span>) &#123;
<span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;
&#125;</pre> 
</div> 
<p style="text-align:start"><code>services/user.go</code> 文件：</p> 
<p style="text-align:start">服务端代码中注册的 <code>services.UserService&#123;&#125;</code> 服务代码如下：</p> 
<p style="text-align:start">只需要填充业务逻辑即可</p> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> services

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
<span style="color:var(--color-prettylights-syntax-string)">"context"</span>
pb <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/protos"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">UserService</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">UserService</span>) <span style="color:var(--color-prettylights-syntax-entity)">Add</span>(ctx context.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">Context</span>, in <span style="color:var(--color-prettylights-syntax-constant)">*</span>pb.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">AddRequest</span>) (<span style="color:var(--color-prettylights-syntax-constant)">*</span>pb.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">AddResponse</span>, <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">error</span>) &#123;
<span style="color:var(--color-prettylights-syntax-comment)">// 执行数据库操作</span>
<span style="color:var(--color-prettylights-syntax-comment)">// ...</span>

resp <span style="color:var(--color-prettylights-syntax-constant)">:=</span> pb.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">AddResponse</span>&#123;
<span style="color:var(--color-prettylights-syntax-constant)">ErrorCode</span>:    <span style="color:var(--color-prettylights-syntax-constant)">0</span>,
<span style="color:var(--color-prettylights-syntax-constant)">ErrorMessage</span>: <span style="color:var(--color-prettylights-syntax-string)">""</span>,
<span style="color:var(--color-prettylights-syntax-constant)">UserId</span>:       <span style="color:var(--color-prettylights-syntax-constant)">10001</span>,
&#125;
<span style="color:var(--color-prettylights-syntax-keyword)">return</span> <span style="color:var(--color-prettylights-syntax-constant)">&</span>resp, <span style="color:var(--color-prettylights-syntax-constant)">nil</span>
&#125;</pre> 
</div> 
<p style="text-align:start"><code>commands/client.go</code> 文件：</p> 
<p style="text-align:start">客户端代码写在 <code>GrpcClientCommand</code> 结构体的 <code>main</code> 方法中，生成的代码中已经包含了：</p> 
<ul> 
 <li>通过环境配置获取服务端连接地址</li> 
 <li>设定了 <code>5s</code> 的执行超时时间</li> 
</ul> 
<div style="text-align:start"> 
 <pre><span style="color:var(--color-prettylights-syntax-keyword)">package</span> commands

<span style="color:var(--color-prettylights-syntax-keyword)">import</span> (
    <span style="color:var(--color-prettylights-syntax-string)">"context"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"fmt"</span>
<span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/dotenv"</span>
pb <span style="color:var(--color-prettylights-syntax-string)">"github.com/mix-go/grpc-skeleton/protos"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"google.golang.org/grpc"</span>
    <span style="color:var(--color-prettylights-syntax-string)">"time"</span>
)

<span style="color:var(--color-prettylights-syntax-keyword)">type</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">GrpcClientCommand</span> <span style="color:var(--color-prettylights-syntax-keyword)">struct</span> &#123;
&#125;

<span style="color:var(--color-prettylights-syntax-keyword)">func</span> (t <span style="color:var(--color-prettylights-syntax-constant)">*</span><span style="color:var(--color-prettylights-syntax-storage-modifier-import)">GrpcClientCommand</span>) <span style="color:var(--color-prettylights-syntax-entity)">Main</span>() &#123;
addr <span style="color:var(--color-prettylights-syntax-constant)">:=</span> dotenv.<span style="color:var(--color-prettylights-syntax-entity)">Getenv</span>(<span style="color:var(--color-prettylights-syntax-string)">"GIN_ADDR"</span>).<span style="color:var(--color-prettylights-syntax-entity)">String</span>(<span style="color:var(--color-prettylights-syntax-string)">":8080"</span>)
    ctx, _ <span style="color:var(--color-prettylights-syntax-constant)">:=</span> context.<span style="color:var(--color-prettylights-syntax-entity)">WithTimeout</span>(context.<span style="color:var(--color-prettylights-syntax-entity)">Background</span>(), time.<span style="color:var(--color-prettylights-syntax-entity)">Duration</span>(<span style="color:var(--color-prettylights-syntax-constant)">5</span>)<span style="color:var(--color-prettylights-syntax-constant)">*</span>time.<span style="color:var(--color-prettylights-syntax-constant)">Second</span>)
    conn, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> grpc.<span style="color:var(--color-prettylights-syntax-entity)">DialContext</span>(ctx, addr, grpc.<span style="color:var(--color-prettylights-syntax-entity)">WithInsecure</span>(), grpc.<span style="color:var(--color-prettylights-syntax-entity)">WithBlock</span>())
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
    &#125;
    <span style="color:var(--color-prettylights-syntax-keyword)">defer</span> <span style="color:var(--color-prettylights-syntax-keyword)">func</span>() &#123;
        _ <span style="color:var(--color-prettylights-syntax-constant)">=</span> conn.<span style="color:var(--color-prettylights-syntax-entity)">Close</span>()
    &#125;()
    cli <span style="color:var(--color-prettylights-syntax-constant)">:=</span> pb.<span style="color:var(--color-prettylights-syntax-entity)">NewUserClient</span>(conn)
    req <span style="color:var(--color-prettylights-syntax-constant)">:=</span> pb.<span style="color:var(--color-prettylights-syntax-storage-modifier-import)">AddRequest</span>&#123;
        <span style="color:var(--color-prettylights-syntax-constant)">Name</span>: <span style="color:var(--color-prettylights-syntax-string)">"xiaoliu"</span>,
    &#125;
    resp, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> cli.<span style="color:var(--color-prettylights-syntax-entity)">Add</span>(ctx, <span style="color:var(--color-prettylights-syntax-constant)">&</span>req)
    <span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
        <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
    &#125;
    fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(fmt.<span style="color:var(--color-prettylights-syntax-entity)">Sprintf</span>(<span style="color:var(--color-prettylights-syntax-string)">"Add User: %d"</span>, resp.<span style="color:var(--color-prettylights-syntax-constant)">UserId</span>))
&#125;</pre> 
</div> 
<p style="text-align:start">接下来我们编译上面的程序：</p> 
<ul> 
 <li>linux & macOS</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go main.go
</code></pre> 
<ul> 
 <li>win</li> 
</ul> 
<pre style="text-align:start"><code>go build -o bin/go_build_main_go.exe main.go
</code></pre> 
<p style="text-align:start">首先在命令行启动 <code>grpc:server</code> 服务器：</p> 
<pre style="text-align:start"><code>$ bin/go_build_main_go grpc:server
             ___         
 ______ ___  _ /__ ___ _____ ______ 
  / __ `__ \/ /\ \/ /__  __ `/  __ \
 / / / / / / / /\ \/ _  /_/ // /_/ /
/_/ /_/ /_/_/ /_/\_\  \__, / \____/ 
                     /____/


Server      Name:      mix-grpc
Listen      Addr:      :8080
System      Name:      darwin
Go          Version:   1.13.4
Framework   Version:   1.0.20
time=2020-11-09 15:08:17.544 level=info msg=Server run :8080 file=server.go:46
</code></pre> 
<p style="text-align:start">然后开启一个新的终端，执行下面的客户端命令与上面的服务器通信</p> 
<pre style="text-align:start"><code>$ bin/go_build_main_go grpc:client
Add User: 10001
</code></pre> 
<h2 style="text-align:start">如何使用 DI 容器中的 Logger、Database、Redis 等组件</h2> 
<p style="text-align:start">项目中要使用的公共组件，都定义在 <code>di</code> 目录，框架默认生成了一些常用的组件，用户也可以定义自己的组件，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxdi" target="_blank">查看更多</a></p> 
<ul> 
 <li>可以在哪里使用</li> 
</ul> 
<p style="text-align:start">可以在代码的任意位置使用，但是为了可以使用到环境变量和自定义配置，通常我们在 <code>xcli.Command</code> 结构体定义的 <code>Run</code>、<code>RunI</code> 中使用。</p> 
<ul> 
 <li>使用日志，比如：<code>logrus</code>、<code>zap</code></li> 
</ul> 
<div style="text-align:start"> 
 <pre>logger <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Logrus</span>()
logger.<span style="color:var(--color-prettylights-syntax-entity)">Info</span>(<span style="color:var(--color-prettylights-syntax-string)">"test"</span>)</pre> 
</div> 
<ul> 
 <li>使用数据库，比如：<code>gorm</code>、<code>xorm</code></li> 
</ul> 
<div style="text-align:start"> 
 <pre>db <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">Gorm</span>()
user <span style="color:var(--color-prettylights-syntax-constant)">:=</span> <span style="color:var(--color-prettylights-syntax-storage-modifier-import)">User</span>&#123;<span style="color:var(--color-prettylights-syntax-constant)">Name</span>: <span style="color:var(--color-prettylights-syntax-string)">"Jinzhu"</span>, <span style="color:var(--color-prettylights-syntax-constant)">Age</span>: <span style="color:var(--color-prettylights-syntax-constant)">18</span>, <span style="color:var(--color-prettylights-syntax-constant)">Birthday</span>: time.<span style="color:var(--color-prettylights-syntax-entity)">Now</span>()&#125;
result <span style="color:var(--color-prettylights-syntax-constant)">:=</span> db.<span style="color:var(--color-prettylights-syntax-entity)">Create</span>(<span style="color:var(--color-prettylights-syntax-constant)">&</span>user)
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(result)</pre> 
</div> 
<ul> 
 <li>使用 Redis，比如：<code>go-redis</code></li> 
</ul> 
<div style="text-align:start"> 
 <pre>rdb <span style="color:var(--color-prettylights-syntax-constant)">:=</span> di.<span style="color:var(--color-prettylights-syntax-entity)">GoRedis</span>()
val, err <span style="color:var(--color-prettylights-syntax-constant)">:=</span> rdb.<span style="color:var(--color-prettylights-syntax-entity)">Get</span>(context.<span style="color:var(--color-prettylights-syntax-entity)">Background</span>(), <span style="color:var(--color-prettylights-syntax-string)">"key"</span>).<span style="color:var(--color-prettylights-syntax-entity)">Result</span>()
<span style="color:var(--color-prettylights-syntax-keyword)">if</span> err <span style="color:var(--color-prettylights-syntax-constant)">!=</span> <span style="color:var(--color-prettylights-syntax-constant)">nil</span> &#123;
    <span style="color:var(--color-prettylights-syntax-entity)">panic</span>(err)
&#125;
fmt.<span style="color:var(--color-prettylights-syntax-entity)">Println</span>(<span style="color:var(--color-prettylights-syntax-string)">"key"</span>, val)</pre> 
</div> 
<h2 style="text-align:start">依赖</h2> 
<p style="text-align:start">官方库</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fmixcli" target="_blank">https://github.com/mix-go/mixcli</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxcli" target="_blank">https://github.com/mix-go/xcli</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxdi" target="_blank">https://github.com/mix-go/xdi</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxwp" target="_blank">https://github.com/mix-go/xwp</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fxfmt" target="_blank">https://github.com/mix-go/xfmt</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-go%2Fdotenv" target="_blank">https://github.com/mix-go/dotenv</a></li> 
</ul> 
<p style="text-align:start">第三方库</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgin-gonic%2Fgin" target="_blank">https://github.com/gin-gonic/gin</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgorm.io%2F" target="_blank">https://gorm.io</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-redis%2Fredis" target="_blank">https://github.com/go-redis/redis</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjinzhu%2Fconfigor" target="_blank">https://github.com/jinzhu/configor</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fuber-go%2Fzap" target="_blank">https://github.com/uber-go/zap</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsirupsen%2Flogrus" target="_blank">https://github.com/sirupsen/logrus</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnatefinch%2Flumberjack" target="_blank">https://github.com/natefinch/lumberjack</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Flestrrat-go%2Ffile-rotatelogs" target="_blank">https://github.com/lestrrat-go/file-rotatelogs</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-session%2Fsession" target="_blank">https://github.com/go-session/session</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-session%2Fredis" target="_blank">https://github.com/go-session/redis</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdgrijalva%2Fjwt-go" target="_blank">https://github.com/dgrijalva/jwt-go</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgorilla%2Fwebsocket" target="_blank">https://github.com/gorilla/websocket</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fgrpc" target="_blank">https://github.com/golang/grpc</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgolang%2Fprotobuf" target="_blank">https://github.com/golang/protobuf</a></li> 
</ul> 
<h2 style="text-align:start">License</h2> 
<p style="text-align:start">Apache License Version 2.0, <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.apache.org%2Flicenses%2F" target="_blank">http://www.apache.org/licenses/</a></p>
                                        </div>
                                      
</div>
            
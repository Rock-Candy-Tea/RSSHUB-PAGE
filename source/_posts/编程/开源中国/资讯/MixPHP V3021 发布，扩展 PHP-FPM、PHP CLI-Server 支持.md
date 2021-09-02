
---
title: 'MixPHP V3.0.21 发布，扩展 PHP-FPM、PHP CLI-Server 支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3073'
author: 开源中国
comments: false
date: Thu, 02 Sep 2021 10:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3073'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <div> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenmix.org%2F" target="_blank">MixPHP</a> <code>V3.0.21</code> 发布后，由于本身支持超多的执行模式，用户可能无从下手，这里先大体介绍一下：</p> 
  <ul> 
   <li>CLI-Server: 适合本机开发，零扩展依赖，Windows/MacOS 等全平台支持</li> 
   <li>PHP-FPM: 适合共享开发环境部署，同时适合 admin 等管理后台项目</li> 
   <li>Swoole, Workerman: 适合线上部署，根据需要选择其一即可</li> 
  </ul> 
  <p style="text-align:left">Swoole 的多种模式：</p> 
  <ul> 
   <li>Swoole 多进程同步: 适合需要使用那些协程不支持的第三方库的项目，和 Workerman 一致</li> 
   <li>Swoole 多进程协程: 适合专注 mysql + redis 需要超高 io 性能的项目</li> 
   <li>Swoole 单进程协程: 单进程协程就是 <code>V2.2</code> 版本那种 golang 风格协程，适合开发 websocket</li> 
  </ul> 
  <p style="text-align:left">几乎支持 PHP 流行的全部执行模式，并且以上执行模式代码是无缝切换的，真正做到效率与性能并存。</p> 
  <h2 style="text-align:left"><strong>请帮忙 Star 一下</strong></h2> 
  <ul> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmix-php%2Fmix" target="_blank">https://github.com/mix-php/mix</a></li> 
   <li><a href="https://gitee.com/mix-php/mix">https://gitee.com/mix-php/mix</a></li> 
  </ul> 
  <h2 style="text-align:left">首先创建一个骨架</h2> 
  <p style="text-align:left">我们以开发一个 API 项目为例，打开 MixPHP 的 <a href="https://gitee.com/mix-php/mix#mix-php">开发文档</a> 里面有 <code>cli</code> <code>api</code> <code>web</code> <code>websocket</code> <code>grpc</code> 项目的开发教程，<code>V3</code> 开始仓库底下的 <code>README</code> 就是开发文档，如果有不明白的可以加我们的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fshang.qq.com%2Fwpa%2Fqunwpa%3Fidkey%3Db3a8618d3977cda4fed2363a666b081a31d89e3d31ab164497f53b72cf49968a" target="_blank">官方QQ群</a> 参与讨论。</p> 
  <ul> 
   <li>首先创建一个骨架</li> 
  </ul> 
  <p style="text-align:left">如果提示缺少 <code>redis</code> 等扩展支持，可以使用 <code>--ignore-platform-reqs</code> 暂时忽略依赖检查</p> 
  <pre style="text-align:left"><span style="color:#032f62">composer</span> <span style="color:#e36209">create-project</span> <span style="color:#e36209">--prefer-dist</span> <span style="color:#e36209">--ignore-platform-reqs</span> <span style="color:#032f62">mix</span>/<span style="color:#032f62">api-skeleton</span> <span style="color:#032f62">api</span></pre> 
  <p style="text-align:left">安装后目录结构如下：</p> 
  <ul> 
   <li><code>bin</code> 目录是全部入口文件，不同文件对应的不同驱动模式</li> 
   <li><code>routes</code> 是路由配置文件</li> 
   <li><code>public/index.php</code> 是 FPM, CLI-Server 两种模式的入口文件</li> 
   <li><code>shell/server.sh</code> 是部署是管理进程 <code>start|stop|restart</code></li> 
  </ul> 
  <pre style="text-align:left">├── README<span style="color:#005cc5">.md</span>
├── bin
│   ├── cli<span style="color:#005cc5">.php</span>
│   ├── swoole<span style="color:#005cc5">.php</span>
│   ├── swooleco<span style="color:#005cc5">.php</span>
│   └── workerman<span style="color:#005cc5">.php</span>
├── composer<span style="color:#005cc5">.json</span>
├── composer<span style="color:#005cc5">.lock</span>
├── conf
│   └── config<span style="color:#005cc5">.json</span>
├── public
│   └── index<span style="color:#005cc5">.php</span>
├── routes
│   └── index<span style="color:#005cc5">.php</span>
├── runtime
├── shell
│   └── server<span style="color:#005cc5">.sh</span>
├── <span style="color:#005cc5">src</span>
│   ├── Command
│   ├── Container
│   ├── Controller
│   ├── Error<span style="color:#005cc5">.php</span>
│   ├── Middleware
│   ├── Vega<span style="color:#005cc5">.php</span>
│   └── functions<span style="color:#005cc5">.php</span>
└── vendor</pre> 
  <h2 style="text-align:left">使用 CLI-Server 零扩展依赖模式本机开发</h2> 
  <p style="text-align:left">首先我们查看一下 <code>composer.json</code>，与其他框架不同的是我们推荐在本机开发阶段使用 <code>composer run-script</code> 启动程序，可以和 <code>PhpStorm</code> 的调试功能完美配合。</p> 
  <ul> 
   <li>这里定义了每个执行模式的命令入口文件</li> 
   <li><code>composer run-script --timeout=0 cliserver:start</code> 就可以启动命令</li> 
  </ul> 
  <pre style="text-align:left">  <span style="color:#005cc5">"scripts"</span>: &#123;
    <span style="color:#005cc5">"cliserver:start"</span>: <span style="color:#032f62">"php -S localhost:8000 public/index.php"</span>,
    <span style="color:#005cc5">"swoole:start"</span>: <span style="color:#032f62">"php bin/swoole.php"</span>,
    <span style="color:#005cc5">"swooleco:start"</span>: <span style="color:#032f62">"php bin/swooleco.php"</span>,
    <span style="color:#005cc5">"workerman:start"</span>: <span style="color:#032f62">"php bin/workerman.php start"</span>,
    <span style="color:#005cc5">"cli:clearcache"</span>: <span style="color:#032f62">"php bin/cli.php clearcache"</span>
  &#125;</pre> 
  <p style="text-align:left">由于现在是本机开发，我们使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.php.net%2Fmanual%2Fzh%2Ffeatures.commandline.webserver.php" target="_blank">CLI-Server</a> 模式启动，零扩展依赖，无需 <code>pcntl</code>, <code>event</code>, <code>swoole</code> 这些扩展，自带热更新。</p> 
  <pre style="text-align:left">% composer run-script <span style="color:#6a737d">--timeout=0 cliserver:start</span>
> php -S localhost:<span style="color:#005cc5">8000</span> <span style="color:#e36209">public</span>/<span style="color:#d73a49">index</span>.php
PHP <span style="color:#005cc5">7.3</span><span style="color:#005cc5">.24</span>-(<span style="color:#d73a49">to</span> be removed <span style="color:#d73a49">in</span> future macOS) Development <span style="color:#d73a49">Server</span> started at Tue Aug <span style="color:#005cc5">10</span> <span style="color:#005cc5">17</span>:<span style="color:#005cc5">00</span>:<span style="color:#005cc5">55</span> <span style="color:#005cc5">2021</span>
Listening <span style="color:#d73a49">on</span> http://localhost:<span style="color:#005cc5">8000</span>
Document root <span style="color:#d73a49">is</span> /Users<span style="color:#6a737d">/***/</span>mix/examples/api-skeleton
Press Ctrl-C <span style="color:#d73a49">to</span> quit.</pre> 
  <p style="text-align:left">测试一下默认的路由</p> 
  <pre style="text-align:left">% curl http:<span style="color:#032f62">//</span><span style="color:#005cc5">127.0</span>.<span style="color:#005cc5">0.1</span>:<span style="color:#005cc5">8000</span>/hello
hello, world!</pre> 
  <p style="text-align:left">接下来就可以根据文档：</p> 
  <ul> 
   <li><a href="https://gitee.com/mix-php/mix/tree/master/examples/api-skeleton#%E7%BC%96%E5%86%99%E4%B8%80%E4%B8%AA-api-%E6%8E%A5%E5%8F%A3">编写一个 API 接口</a></li> 
  </ul> 
  <h2 style="text-align:left">使用 PHP-FPM 部署共享开发环境</h2> 
  <p style="text-align:left">热更新是刚性需求，所以共享开发环境我们直接采用 PHP-FPM 部署，和 Laravel、ThinkPHP 部署方法完全一致，将 <code>public/index.php</code> 在 <code>nginx</code> 配置 <code>rewrite</code> 重写即可。</p> 
  <pre style="text-align:left"><strong>server</strong> &#123;
    <span style="color:#005cc5">server_name</span> www.domain.com;
    <span style="color:#005cc5">listen</span> <span style="color:#005cc5">80</span>;
    <span style="color:#005cc5">root</span> /data/project/public;
    <span style="color:#005cc5">index</span> index.html index.php;

    <strong>location</strong> / &#123;
        <span style="color:#005cc5">if</span> (!-e <span style="color:#005cc5">$request_filename</span>) &#123;
            <span style="color:#005cc5">rewrite</span><span style="color:#032f62"> ^/(.*)$</span> /index.php/<span style="color:#005cc5">$1</span> <span style="color:#005cc5">last</span>;
        &#125;
    &#125;

    <strong>location</strong> <span style="color:#032f62">~ ^(.+\.php)(.*)$</span> &#123;
        <span style="color:#005cc5">fastcgi_pass</span> <span style="color:#005cc5">127.0.0.1:9000</span>;
        <span style="color:#005cc5">fastcgi_split_path_info</span><span style="color:#032f62"> ^(.+\.php)(.*)$</span>;
        <span style="color:#005cc5">fastcgi_param</span> PATH_INFO <span style="color:#005cc5">$fastcgi_path_info</span>;
        <span style="color:#005cc5">fastcgi_param</span> SCRIPT_FILENAME <span style="color:#005cc5">$document_root</span><span style="color:#005cc5">$fastcgi_script_name</span>;
        <span style="color:#005cc5">include</span> fastcgi_params;
    &#125;
&#125;</pre> 
  <h2 style="text-align:left">使用 Swoole 多进程协程模式线上部署</h2> 
  <p style="text-align:left">Swoole、Workerman 你可以随意选择，这里我们采用 Swoole 举例。</p> 
  <ul> 
   <li>首先安装 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwiki.swoole.com%2F%23%2Fenvironment" target="_blank">Swoole</a> 扩展</li> 
   <li>修改 <code>shell/server.sh</code> 脚本中的绝对路径和参数</li> 
  </ul> 
  <p style="text-align:left">这里我们选择的 Swoole 多进程协程模式，因此入口文件为 <code>bin/swoole.php</code>，其他模式参考 <code>composer.json</code></p> 
  <pre style="text-align:left">php=<span style="color:#032f62">/usr/</span>local<span style="color:#032f62">/bin/</span>php
<span style="color:#d73a49">file</span>=<span style="color:#032f62">/data/</span><span style="color:#d73a49">project</span><span style="color:#032f62">/bin/</span>swoole.php
cmd=start
numprocs=<span style="color:#005cc5">1</span></pre> 
  <p style="text-align:left">启动管理</p> 
  <pre style="text-align:left">sh <span style="color:#032f62">/data/</span><span style="color:#d73a49">project</span><span style="color:#032f62">/shell/</span>server.sh start
sh <span style="color:#032f62">/data/</span><span style="color:#d73a49">project</span><span style="color:#032f62">/shell/</span>server.sh stop
sh <span style="color:#032f62">/data/</span><span style="color:#d73a49">project</span><span style="color:#032f62">/shell/</span>server.sh restart</pre> 
  <p style="text-align:left">接下来将启动命令加入 <code>crontab</code> 防止程序异常中断</p> 
  <pre style="text-align:left">*<span style="color:#032f62">/1 * * * * sh /</span>data<span style="color:#032f62">/project/</span>shell<span style="color:#032f62">/server.sh start > /</span>tmp/server.sh.log <span style="color:#005cc5">2</span>>&<span style="color:#005cc5">1</span> &</pre> 
  <p style="text-align:left">当修改代码时，使用 <code>restart</code> 让代码生效</p> 
  <pre style="text-align:left">sh <span style="color:#032f62">/data/</span><span style="color:#d73a49">project</span><span style="color:#032f62">/shell/</span>server.sh restart</pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            
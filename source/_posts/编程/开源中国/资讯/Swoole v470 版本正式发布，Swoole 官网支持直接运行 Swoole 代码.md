
---
title: 'Swoole v4.7.0 版本正式发布，Swoole 官网支持直接运行 Swoole 代码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6958'
author: 开源中国
comments: false
date: Fri, 16 Jul 2021 18:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6958'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">在 <code>Swoole</code> 官网增加了 <strong>在线运行</strong> 的按钮，可以直接运行首页提供的一些示例代码，当然也可以手动输出一些 <code>PHP</code> 代码进行测试。</p> 
<p style="text-align:left">可以访问 Swoole 官网首页进行测试使用：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fwww.swoole.com%252F" target="_blank">https://www.swoole.com/</a></p> 
<p style="text-align:left">目前还处于测试阶段，有遇到 <code>BUG</code> 可以向识沃科技客服反馈或交流群中反馈。</p> 
<h2 style="text-align:left">版本说明</h2> 
<p style="text-align:left">在未正式发布时，对于一些新特性和功能发布过文章进行说明，所以重复的在此就不再赘述，可以查看：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fwenda.swoole.com%252Fdetail%252F107787" target="_blank">Swoole v4.7 版本新特性预览之 Process\Pool::detach()</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fwenda.swoole.com%252Fdetail%252F107792" target="_blank">Swoole v4.7 版本新特性预览之 onDisconnect 事件回调</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fwenda.swoole.com%252Fdetail%252F107796" target="_blank">Swoole v4.7 版本新特性预览之 Co::cancel()</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fwenda.swoole.com%252Fdetail%252F107830" target="_blank">Swoole v4.7 版本预览之支持 c-ares</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fwenda.swoole.com%252Fdetail%252F107837" target="_blank">Swoole v4.7 版本新特性预览之支持为每个端口设置不同的心跳检测时间</a></li> 
</ul> 
<p style="text-align:left">对于其他的一些修改进行说明：</p> 
<ul> 
 <li>禁止 Hook 已经被 PHP 禁用的函数</li> 
</ul> 
<p style="text-align:left">在之前的版本中，如果使用<code>disable_functions</code>将方法进行了禁用，在 <code>HOOK</code> 之后依旧能正常调用。</p> 
<p style="text-align:left">如下代码：</p> 
<pre style="text-align:left"><code>var_dump(`ls`);

Swoole\Coroutine\run(<strong>function</strong> () &#123;
    var_dump(`ls`);
&#125;);</code></pre> 
<p style="text-align:left">保存到<code>test.php</code>中，命令行使用<code>php -d disable_functions=shell_exec test.php</code>执行</p> 
<p style="text-align:left">之前的版本输出为：</p> 
<pre style="text-align:left"><code>PHP Warning:  shell_exec() has been disabled <strong>for</strong> security reasons <strong>in</strong> /Users/lufei/Swoole/test.php on line 3
NULL
string(11) <span style="color:#dd1144">"swoole.php
"</span></code></pre> 
<p style="text-align:left">而升级 <code>v4.7.0</code> 之后，行为和 HOOK 前一致。</p> 
<pre style="text-align:left"><code>PHP Warning:  shell_exec() has been disabled <strong>for</strong> security reasons <strong>in</strong> /Users/lufei/Swoole/test.php on line 3
NULL
PHP Warning:  shell_exec() has been disabled <strong>for</strong> security reasons <strong>in</strong> /Users/lufei/Swoole/test.php on line 6
NULL</code></pre> 
<ul> 
 <li><code>Coroutine\go()</code> 方法增加了返回值</li> 
</ul> 
<p style="text-align:left">之前的版本中使用 <code>Coroutine\go()</code> 方法不会返回协程 ID，从<code>v4.7.0</code>中开始增加了返回值，返回当前协程 ID。</p> 
<pre style="text-align:left"><code><strong>use</strong> <strong>Swoole</strong>\<strong>Coroutine</strong>\<strong>System</strong>;
<strong>use</strong> <strong>function</strong> <strong>Swoole</strong>\<strong>Coroutine</strong>\<strong>run</strong>;
<strong>use</strong> <strong>function</strong> <strong>Swoole</strong>\<strong>Coroutine</strong>\<strong>go</strong>;

run(<strong>function</strong> () &#123;
    <span style="color:teal">$cid</span> = go(<strong>function</strong>() &#123;
        System::sleep(<span style="color:teal">0.001</span>);
    &#125;);
    var_dump(<span style="color:teal">$cid</span>);
&#125;);</code></pre> 
<ul> 
 <li>增加了 <code>Cygwin</code> 环境下的构建</li> 
</ul> 
<p style="text-align:left">从<code>v4.7.0</code>版本开始，可以从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.segmentfault.com%2F%3Furl%3Dhttps%253A%252F%252Fgithub.com%252Fswoole%252Fswoole-src%252Freleases%252Flatest" target="_blank">GitHub release</a> 中获取到该版本的 <code>Cygwin</code> 版本压缩包进行使用。</p> 
<h2 style="text-align:left">更新日志</h2> 
<p style="text-align:left">下面是完整的更新日志：</p> 
<h3 style="text-align:left">新增 API</h3> 
<ul> 
 <li>新增 <code>Process\Pool::detach()</code> 方法 (#4221) (@matyhtf)</li> 
 <li><code>Server</code> 支持 <code>onDisconnect</code> 回调函数 (#4230) (@matyhtf)</li> 
 <li>新增 <code>Coroutine::cancel()</code> 和 <code>Coroutine::isCanceled()</code> 方法 (#4247) (#4249) (@matyhtf)</li> 
 <li><code>Http\Client</code> 支持 <code>http_compression</code> 和 <code>body_decompression</code> 选项 (#4299) (@matyhtf)</li> 
</ul> 
<h3 style="text-align:left">增强</h3> 
<ul> 
 <li>支持协程 MySQL 客户端在 <code>prepare</code> 时字段严格类型 (#4238) (@Yurunsoft)</li> 
 <li>DNS 支持 <code>c-ares</code> 库 (#4275) (@matyhtf)</li> 
 <li><code>Server</code> 支持在多端口监听时给不同的端口配置心跳检测时间 (#4290) (@matyhtf)</li> 
 <li><code>Server</code> 的 <code>dispatch_mode</code> 支持 <code>SWOOLE_DISPATCH_CO_CONN_LB</code> 和 <code>SWOOLE_DISPATCH_CO_REQ_LB</code> 模式 (#4318) (@matyhtf)</li> 
 <li><code>ConnectionPool::get()</code> 支持 <code>timeout</code> 参数 (swoole/library#108) (@leocavalcante)</li> 
 <li>Hook Curl 支持 <code>CURLOPT_PRIVATE</code> 选项 (swoole/library#112) (@sy-records)</li> 
 <li>优化 <code>PDOStatementProxy::setFetchMode()</code> 方法的函数声明 (swoole/library#109) (@yespire)</li> 
</ul> 
<h3 style="text-align:left">修复</h3> 
<ul> 
 <li>修复使用线程上下文的时候，创建大量协程时抛出无法创建线程的异常 (8ce5041) (@matyhtf)</li> 
 <li>修复安装 Swoole 时 php_swoole.h 头文件丢失的问题 (#4239) (@sy-records)</li> 
 <li>修复 EVENT_HANDSHAKE 不向下兼容的问题 (#4248) (@sy-records)</li> 
 <li>修复 SW_LOCK_CHECK_RETURN 宏可能会调用两次函数的问题 (#4302) (@zmyWL)</li> 
 <li>修复 <code>Atomic\Long</code> 在 M1 芯片下的问题 (e6fae2e) (@matyhtf)</li> 
 <li>修复 <code>Coroutine\go()</code> 丢失返回值的问题 (swoole/library@1ed49db) (@matyhtf)</li> 
 <li>修复 <code>StringObject</code> 返回值类型问题 (swoole/library#111) (swoole/library#113) (@leocavalcante) (@sy-records)</li> 
</ul> 
<h3 style="text-align:left">内核</h3> 
<ul> 
 <li>禁止 Hook 已经被 PHP 禁用的函数 (#4283) (@twose)</li> 
</ul> 
<h3 style="text-align:left">测试</h3> 
<ul> 
 <li>新增 <code>Cygwin</code> 环境下的构建 (#4222) (@sy-records)</li> 
 <li>新增 <code>alpine 3.13</code> 和 <code>3.14</code> 的编译测试 (#4309) (@limingxinleo)</li> 
</ul>
                                        </div>
                                      
</div>
            
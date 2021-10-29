
---
title: 'Swoole v4.8.1 版本发布，支持忽略指定错误码的日志'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.swoole.com/dist/dashboard/img/home.png'
author: 开源中国
comments: false
date: Fri, 29 Oct 2021 18:16:00 GMT
thumbnail: 'https://www.swoole.com/dist/dashboard/img/home.png'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fswoole%2Fswoole-src%2Freleases%2Ftag%2Fv4.8.1" target="_blank">v4.8.1</a> 版本主要优化了 admin server 的代码，没有向下不兼容改动。</p> 
<h2>支持忽略指定的错误码日志</h2> 
<p>在此版本中增加了可以忽略指定的错误码所对应的错误日志，举个例子：</p> 
<pre><code class="language-php">const LOG_FILE = __DIR__ . '/log';
if (is_file(LOG_FILE)) &#123;
    unlink(LOG_FILE);
&#125;

const ERRNO_1 = 888888;
const ERRNO_2 = 999999;

swoole_async_set(['log_file' => LOG_FILE]);
swoole_error_log(SWOOLE_LOG_NOTICE, 'swoole_error_log msg');
swoole_error_log_ex(SWOOLE_LOG_NOTICE, ERRNO_1, 'swoole_error_log_ex msg');

// 忽略错误码为ERRNO_2的日志
swoole_ignore_error(ERRNO_2);
swoole_error_log_ex(SWOOLE_LOG_NOTICE, ERRNO_2, 'swoole_error_log_ex ERRNO_2 msg');

echo file_get_contents(LOG_FILE);
</code></pre> 
<p>忽略了错误码为<code>ERRNO_2</code>的日志，所以查看错误日志中没有<code>swoole_error_log_ex ERRNO_2 msg</code>的信息。</p> 
<pre><code class="language-log">[2021-10-28 10:34:01 @23580.0]  NOTICE  swoole_error_log msg
[2021-10-28 10:34:01 @23580.0]  NOTICE  zif_swoole_error_log_ex() (ERRNO 888888): swoole_error_log_ex msg
</code></pre> 
<p>同时也可以使用<code>swoole_error_log_ex</code>函数写入指定错误等级、错误码的日志到日志文件中。</p> 
<h2>Admin Server</h2> 
<p>此版本中优化了大量的 <code>admin_server</code> 的代码：</p> 
<ul> 
 <li>迁移 ext-swoole_plus 中的 admin api 到 ext-swoole，可以使用 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdashboard.swoole.com%2F" target="_blank">Swoole Dashboard</a> 的全部功能</li> 
</ul> 
<p><img alt src="https://www.swoole.com/dist/dashboard/img/home.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>支持了并发请求多个目标和并发请求多个 API，详情可以查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fswoole%2Fcommunity-chinese%2Fissues%2F78" target="_blank">RFC #78</a></li> 
 <li>新增 get_composer_packages 命令，可以查看项目中的 composer 依赖信息</li> 
</ul> 
<p><img alt src="https://www.swoole.com/dist/dashboard/img/composer.png" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>支持获取某个类中的方法信息</li> 
 <li>支持获取某个<code>interface</code>的信息</li> 
</ul> 
<p>可以更新 swoole 版本后，前往 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdashboard.swoole.com%2F" target="_blank">Swoole Dashboard</a> 进行体验。</p> 
<h2>更新日志</h2> 
<p>下面是完整的更新日志：</p> 
<h3>新增 API</h3> 
<ul> 
 <li>新增 <code>swoole_error_log_ex()</code> 和 <code>swoole_ignore_error()</code> 函数 (#4440) (@matyhtf)</li> 
</ul> 
<h3>增强</h3> 
<ul> 
 <li>迁移 ext-swoole_plus 中的 admin api 到 ext-swoole (#4441) (@matyhtf)</li> 
 <li>admin server 新增 get_composer_packages 命令 (swoole/library@07763f46) (swoole/library@8805dc05) (swoole/library@175f1797) (@sy-records) (@yunbaoi)</li> 
 <li>增加了写操作的 POST 方法请求限制 (swoole/library@ac16927c) (@yunbaoi)</li> 
 <li>admin server 支持获取类方法信息 (swoole/library@690a1952) (@djw1028769140) (@sy-records)</li> 
 <li>优化 admin server 代码 (swoole/library#128) (swoole/library#131) (@sy-records)</li> 
 <li>admin server 支持并发请求多个目标和并发请求多个 API (swoole/library#124) (@sy-records)</li> 
 <li>admin server 支持获取接口信息 (swoole/library#130) (@sy-records)</li> 
 <li>SWOOLE_HOOK_CURL 支持 CURLOPT_HTTPPROXYTUNNEL (swoole/library#126) (@sy-records)</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>join 方法禁止并发调用同一个协程 (#4442) (@matyhtf)</li> 
 <li>修复 Table 原子锁意外释放的问题 (#4446) (@Txhua) (@matyhtf)</li> 
 <li>修复丢失的 helper options (swoole/library#123) (@sy-records)</li> 
 <li>修复 get_static_property_value 命令参数错误 (swoole/library#129) (@sy-records)</li> 
</ul>
                                        </div>
                                      
</div>
            
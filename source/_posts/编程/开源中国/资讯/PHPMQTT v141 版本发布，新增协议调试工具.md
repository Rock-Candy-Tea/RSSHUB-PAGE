
---
title: 'PHPMQTT v1.4.1 版本发布，新增协议调试工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6741'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 11:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6741'
---

<div>   
<div class="content">
                                                                                            <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsimps%2Fmqtt%2F" target="_blank">PHPMQTT</a> v1.4.1 版本发布，在此版本中主要是新增了一个协议调试工具。 提供了 5 种方法来调试二进制数据，实际上就是一个二进制数据查看工具。</p> 
<p>主要是将二进制数据转为 ASCII、十六进制的格式进行查看，可以用来调试 TCP、WebSocket、UDP 等。</p> 
<pre><code class="language-php">public function hexDump(): string // 以16进制显示
public function hexDumpAscii(): string // 以16进制和相应的ASCII字符显示
public function printableText(): string // 可打印字符
public function hexStream(): string // 16进制流
public function ascii(): string // 以ASCII字符显示
</code></pre> 
<h2>使用</h2> 
<p>可以通过实例化<code>Simps\\MQTT\\Tools\\Debug</code>或者<code>Simps\\MQTT\\Tools\\Common</code>/<code>Simps\\MQTT\\Tools\\UnPackTool</code>静态调用：</p> 
<ul> 
 <li>实例化</li> 
</ul> 
<pre><code class="language-php">use Simps\\MQTT\\Tools\\Debug;
$debug = new Debug('0:simps-mqtt/user001/update&#123;
  "msg": "hello, mqtt"
&#125;');
//$debug = (new Debug())->setEncode('0:simps-mqtt/user001/update&#123;
//  "msg": "hello, mqtt"
//&#125;');
echo $debug->hexDump(), PHP_EOL;
echo $debug->hexDumpAscii(), PHP_EOL;
echo $debug->printableText(), PHP_EOL;
echo $debug->hexStream(), PHP_EOL;
echo $debug->ascii();
</code></pre> 
<ul> 
 <li>静态调用</li> 
</ul> 
<pre><code class="language-php">use Simps\\MQTT\\Tools\\UnPackTool;
echo UnPackTool::hexDumpAscii('0:simps-mqtt/user001/update&#123;
  "msg": "hello, mqtt"
&#125;');
</code></pre> 
<pre><code class="language-text">00000000    30 3a 73 69 6d 70 73 2d 6d 71 74 74 2f 75 73 65    0:simps-mqtt/use
00000010    72 30 30 31 2f 75 70 64 61 74 65 7b 0a 20 20 22    r001/update&#123;.  "
00000020    6d 73 67 22 3a 20 22 68 65 6c 6c 6f 2c 20 6d 71    msg": "hello, mq
00000030    74 74 22 0a 7d                                     tt".&#125;
</code></pre> 
<h3>在 Client 中使用</h3> 
<p>调用配置对象的<code>setVerbose</code>方法，设置需要的调试级别即可。</p> 
<h2>更新日志</h2> 
<ul> 
 <li>添加调试工具 (#56)</li> 
 <li>添加 mqtt 相关常量 (#58)</li> 
 <li>优化 CI (#60) (#61) (#64)</li> 
 <li>为 Client 添加调试工具 (#65)</li> 
</ul>
                                        </div>
                                      
</div>
            
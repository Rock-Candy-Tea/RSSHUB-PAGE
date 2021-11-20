
---
title: 'HTTP、TCP 以及数据库可用性检测服务：CyberTect 1.0.0版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://github.com/vicanso/cyber-tect/workflows/Test/badge.svg'
author: 开源中国
comments: false
date: Sat, 20 Nov 2021 09:27:00 GMT
thumbnail: 'https://github.com/vicanso/cyber-tect/workflows/Test/badge.svg'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:start"><span style="color:#333333">Cyber Tect</span></h1> 
<p style="color:#c9d1d9; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvicanso%2Fcyber-tect%2Factions" target="_blank"><span style="color:#333333"><img alt="Build Status" src="https://github.com/vicanso/cyber-tect/workflows/Test/badge.svg" referrerpolicy="no-referrer"></span></a><span style="color:#333333">提供常用的HTTP接口、TCP端口、DNS域名解析、Ping以及各常用数据库的定时检测告警。</span></p> 
<h2 style="text-align:start"><span style="color:#333333">启动程序</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">建议直接使用已打包好的docker镜像启动项目，启动脚本如下：</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:#333333">docker run -d --restart=always \
  -p 7001:7001 \
  -e GO_ENV=production \
  -e DATABASE_URI=postgres://vicanso:A123456@127.0.0.1:5432/cybertect \
  -e MAIL_URI=smtp://tree.xie@outlook.com:pass@smtp.office365.com:587 \
  -e DETECTOR_INTERVAL=1m \
  -e DETECTOR_EXPIRED=30d \
  --name=cybertect \
  vicanso/cybertect</span></pre> 
</div> 
<ul> 
 <li><span style="color:#333333"><code>GO_ENV</code> 设置为正式环境</span></li> 
 <li><span style="color:#333333"><code>DATABASE_URI</code> 数据库连接地址</span></li> 
 <li><span style="color:#333333"><code>MAIL_URI</code> 用于发送告警邮件的SMTP设置</span></li> 
 <li><span style="color:#333333"><code>DETECTOR_INTERVAL</code> 检测间隔，默认为1m（1分钟一次)</span></li> 
 <li><span style="color:#333333"><code>DETECTOR_EXPIRED</code> 检测结果过期时间，默认为30天(30d)，过期后的数据会自动清除。若不希望清除检测结果，则设置为负数则可，如：-1d</span></li> 
</ul> 
<h2 style="text-align:start"><span style="color:#333333">数据存储</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">检测配置等数据暂仅支持存储至postgres与mysql，仅需要启动时通过环境变量(DATABASE_URI)指定数据库连接串时指定则可，连接串格式如下：</span></p> 
<ul> 
 <li><span style="color:#333333"><code>postgres</code>: postgres://root:pass@127.0.0.1:5432/cybertect?maxIdleConns=5&maxIdleTime=30m&maxOpenConns=100</span></li> 
 <li><span style="color:#333333"><code>mysql</code>: mysql://root:pass@tcp(127.0.0.1:3306)/cybertect?timeout=30s&parseTime=true&maxIdleConns=5&maxIdleTime=30m&maxOpenConns=100</span></li> 
</ul> 
<h3 style="text-align:start"><span style="color:#333333">postgres</span></h3> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">用户信息及检测配置、结果等数据保存在postgres中，若无现成的postgres可使用以下脚本启动实例：</span></p> 
<div style="text-align:start"> 
 <pre><code>docker pull postgres:14-alpine

docker run -d --restart=always \
  -v $PWD/data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=A123456 \
  -p 5432:5432 \
  --name=postgres \
  postgres:14-alpine

docker exec -it postgres sh

psql -c "CREATE DATABASE cybertect;" -U postgres
psql -c "CREATE USER vicanso WITH PASSWORD 'A123456';" -U postgres
psql -c "GRANT ALL PRIVILEGES ON DATABASE cybertect to vicanso;" -U postgres
</code></pre> 
</div> 
<h2 style="text-align:start"><span style="color:#333333">项目启动</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">项目连接数据库使用ent框架，相关代码动态生成，因此使用前需要先执行：</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:#333333">make install && make generate</span></pre> 
</div> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">启动程序：</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:#333333">go run main.go </span></pre> 
</div> 
<h2 style="text-align:start"><span style="color:#333333">HTTP检测</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">HTTP检测通过指定检测URL，定时调用判断返回的HTTP状态码是否>=200且<400，如果是则认为成功，否则失败（对于https还检测期证书是否差不多过期，如果要过期则认为检测失败），失败时通过email发送告警邮箱。配置如下：</span></p> 
<ul> 
 <li><span style="color:#333333"><code>名称</code> 检测配置名称</span></li> 
 <li><span style="color:#333333"><code>状态</code> 是否启用状态</span></li> 
 <li><span style="color:#333333"><code>超时</code> 设置超时时长，单位为秒</span></li> 
 <li><span style="color:#333333"><code>用户列表</code> 可以编辑该配置的用户</span></li> 
 <li><span style="color:#333333"><code>告警接收</code> 选择接收告警邮件的用户</span></li> 
 <li><span style="color:#333333"><code>IP列表</code> 指定URL中域名对应的解析，如果域名解析的IP为多个，可以配置多个IP地址，以<code>,</code>分隔。如果不需要指定（配置的检测地址为IP形式或直接通过DNS解析），则配置为<code>0.0.0.0</code></span></li> 
 <li><span style="color:#333333"><code>检测地址</code> 配置检测的http(s)访问地址则可</span></li> 
 <li><span style="color:#333333"><code>检测脚本</code> 可配置基于响应数据的检测脚本（javascript)，如果响应类型的json，则resp为Object，否则为String</span></li> 
 <li><span style="color:#333333"><code>配置描述</code> 检测配置描述</span></li> 
</ul> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">检测脚本示例（响应数据为json)：</span></p> 
<div style="text-align:start"> 
 <pre><span style="color:#333333">if (!resp || resp.code != "123") &#123;
  throw new Error("信息异常");
&#125;</span></pre> 
</div> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">完成配置之后，系统会定时执行检测配置，相关检测结果可在列表中查询并可查询每次检测的详情，包括HTTP(s)请求完整链路的时间（tcp连接、tls连接等）。</span></p> 
<h2 style="text-align:start"><span style="color:#333333">DNS检测</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">DNS检测域名在指定DNS服务器的解析记录是否与期望的IP列表一致，主要用于检测是否有DNS劫持，支持IPV4与IPV6的DNS解析。配置如下：</span></p> 
<ul> 
 <li><span style="color:#333333"><code>名称</code> 检测配置名称</span></li> 
 <li><span style="color:#333333"><code>状态</code> 是否启用状态</span></li> 
 <li><span style="color:#333333"><code>超时</code> 设置超时时长，单位为秒</span></li> 
 <li><span style="color:#333333"><code>用户列表</code> 可以编辑该配置的用户</span></li> 
 <li><span style="color:#333333"><code>告警接收</code> 选择接收告警邮件的用户</span></li> 
 <li><span style="color:#333333"><code>域名</code> 检测域名</span></li> 
 <li><span style="color:#333333"><code>IP列表</code> 域名对应的IP地址列表，如果DNS解析的IP不在此列表中，则失败</span></li> 
 <li><span style="color:#333333"><code>DNS</code> DNS服务器列表</span></li> 
 <li><span style="color:#333333"><code>配置描述</code> 检测配置描述</span></li> 
</ul> 
<h2 style="text-align:start"><span style="color:#333333">TCP检测</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">TCP检测指定的多个地址的端口监听状态(相关服务)，如redis集群等，主要用于简单的服务是否可用的检测。配置如下：</span></p> 
<ul> 
 <li><span style="color:#333333"><code>名称</code> 检测配置名称</span></li> 
 <li><span style="color:#333333"><code>状态</code> 是否启用状态</span></li> 
 <li><span style="color:#333333"><code>超时</code> 设置超时时长，单位为秒</span></li> 
 <li><span style="color:#333333"><code>用户列表</code> 可以编辑该配置的用户</span></li> 
 <li><span style="color:#333333"><code>告警接收</code> 选择接收告警邮件的用户</span></li> 
 <li><span style="color:#333333"><code>地址列表</code> 检测的地址列表</span></li> 
 <li><span style="color:#333333"><code>超时</code> 设置超时时长，单位为秒</span></li> 
 <li><span style="color:#333333"><code>配置描述</code> 检测配置描述</span></li> 
</ul> 
<h2 style="text-align:start"><span style="color:#333333">Ping检测</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">Ping检测用于检测网络的连通性，主要用于测试简单的网络连通、机器是否在线等最基本的检测。配置如下：</span></p> 
<ul> 
 <li><span style="color:#333333"><code>名称</code> 检测配置名称</span></li> 
 <li><span style="color:#333333"><code>状态</code> 是否启用状态</span></li> 
 <li><span style="color:#333333"><code>超时</code> 设置超时时长，单位为秒</span></li> 
 <li><span style="color:#333333"><code>用户列表</code> 可以编辑该配置的用户</span></li> 
 <li><span style="color:#333333"><code>告警接收</code> 选择接收告警邮件的用户</span></li> 
 <li><span style="color:#333333"><code>IP列表</code> 检测的IP列表</span></li> 
 <li><span style="color:#333333"><code>配置描述</code> 检测配置描述</span></li> 
</ul> 
<h2 style="text-align:start"><span style="color:#333333">Database检测</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">Database检测用于测试数据库连通性，主要用于简单的测试数据库是否可正常连接，现支持以下数据库：<code>redis</code>，<code>postgres</code>，<code>mysql</code>以及<code>mongodb</code></span></p> 
<h3 style="text-align:start"><span style="color:#333333">Redis</span></h3> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">Redis数据库支持三种模式，数据库驱动使用</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-redis%2Fredis" target="_blank"><span style="color:#333333">go-redis</span></a><span style="color:#333333">，数据库连接串格式如下：</span></p> 
<ul> 
 <li><span style="color:#333333"><code>单实例</code>: <code>redis://[:pass@]host:port/</code>，密码选项根据数据库是否有设置密码而添加。</span></li> 
 <li><span style="color:#333333"><code>Sentinel</code>: <code>redis://[:pass@]host1,port1,host2:port2/?master=master[&sentinelPassword=sentinelPassword]</code>，密码选项根据数据库是否有设置密码而添加，sentinel必须指定master，若不指定master则会判断为cluster模式。</span></li> 
 <li><span style="color:#333333"><code>Cluster</code>: <code>redis://[:pass@]host1,port1,host2:port2,host3:port3/</code>，密码选项根据数据库是否有设置密码而添加。</span></li> 
</ul> 
<h3 style="text-align:start"><span style="color:#333333">Postgres</span></h3> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">postgres连接串格式如下：<code>postgres://[jack:secret@]foo.example.com:5432[,...bar.example.com:5432]/mydb</code>，数据库驱动使用</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjackc%2Fpgx" target="_blank"><span style="color:#333333">pgx</span></a><span style="color:#333333">模块。</span></p> 
<h3 style="text-align:start"><span style="color:#333333">Mysql</span></h3> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">mysql连接串格式如下：<code>mysql://[username[:password]@][protocol[(address)]]/dbname[?param1=value1&...&paramN=valueN]</code>，数据库驱动使用</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgo-sql-driver%2Fmysql" target="_blank"><span style="color:#333333">mysql</span></a><span style="color:#333333">模块。</span></p> 
<h3 style="text-align:start"><span style="color:#333333">Mongodb</span></h3> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">mongodb连接串格式如下：<code>mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]</code>，数据库驱动使用</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmongodb%2Fmongo-go-driver" target="_blank"><span style="color:#333333">mongodb</span></a><span style="color:#333333">模块。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvicanso%2Fcyber-tect%2Fblob%2Fmaster%2Fimages%2Fdatabase-detect-result-detail.jpg" target="_blank"><span style="color:#333333"><img alt src="https://github.com/vicanso/cyber-tect/raw/master/images/database-detect-result-detail.jpg" referrerpolicy="no-referrer"></span></a></p> 
<h2 style="text-align:start"><span style="color:#333333">个人信息设置</span></h2> 
<p style="color:#c9d1d9; text-align:start"><span style="color:#333333">告警信息使用Email发送，因此需要设置个人邮箱后才可接收到告警信息。</span></p>
                                        </div>
                                      
</div>
            

---
title: '学习Nginx这一篇就够了'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/0a41bf1eeab851494f7179590561975e.png'
author: Dockone
comments: false
date: 2021-07-14 13:16:40
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/0a41bf1eeab851494f7179590561975e.png'
---

<div>   
<br><h3>第一章：Nginx概述</h3><h4>1.1、Nginx概述</h4>Nginx（“engine x”）是一个高性能的HTTP和反向代理服务器，特点是占有内存少，并发能力强，事实上Nginx的并发能力确实在同类型的网页服务器中表现较好，中国大陆使用Nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。<br>
<h4>1.2、Nginx官网</h4>官网地址：<a href="http://nginx.org/" rel="nofollow" target="_blank">http://nginx.org/</a><br>
<h4>1.3、Nginx用处</h4>Nginx可以作为静态页面的Web服务器，同时还支持CGI协议的动态语言，比如Perl、PHP等。但是不支持Java。Java程序只能通过与Tomcat配合完成。Nginx专为性能优化而开发，性能是其最重要的考量，实现上非常注重效率，能经受高负载的考验，有报告表明能支持高达50000个并发连接数。<br>
<h3>第二章：Nginx单实例安装</h3><h4>2.1、环境说明</h4><ul><li>模拟工具：VMware-workstation-full-15.5.6-16341506.exe</li><li>操作系统：CentOS-6.10-x86_64-bin-DVD1.iso、纯净安装、桌面版</li><li>内存大小：2GB</li><li>连接工具：SecureCRT</li></ul><br>
<br><h4>2.2、安装依赖</h4><pre class="prettyprint">[root@caochenlei ~]# yum install -y gcc gcc-c++ make libtool wget pcre pcre-devel zlib zlib-devel openssl openssl-devel<br>
</pre><br>
<h4>2.3、Nginx下载</h4><pre class="prettyprint">[root@caochenlei ~]# wget http://nginx.org/download/nginx-1.18.0.tar.gz<br>
</pre><br>
<h4>2.4、Nginx解压</h4><pre class="prettyprint">[root@caochenlei ~]# tar -zxvf nginx-1.18.0.tar.gz<br>
</pre><br>
<h4>2.5、Nginx安装</h4><pre class="prettyprint">[root@caochenlei ~]# cd nginx-1.18.0<br>
[root@caochenlei nginx-1.18.0]# ./configure<br>
[root@caochenlei nginx-1.18.0]# make && make install<br>
</pre><br>
注意：安装完成后的路径为：/usr/local/nginx<br>
<h4>2.6、Nginx命令</h4><ul><li>普通启动服务：/usr/local/nginx/sbin/nginx</li><li>配置文件启动：/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf</li><li>暴力停止服务：/usr/local/nginx/sbin/nginx -s stop</li><li>优雅停止服务：/usr/local/nginx/sbin/nginx -s quit</li><li>检查配置文件：/usr/local/nginx/sbin/nginx -t</li><li>重新加载配置：/usr/local/nginx/sbin/nginx -s reload</li><li>查看相关进程：ps -ef | grep nginx</li></ul><br>
<br><h4>2.7、开放防火墙</h4><pre class="prettyprint">[root@caochenlei ~]# /sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT<br>
[root@caochenlei ~]# /etc/rc.d/init.d/iptables save<br>
iptables：将防火墙规则保存到 /etc/sysconfig/iptables：[确定]<br>
</pre><br>
<h4>2.8、启动后效果</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/0a41bf1eeab851494f7179590561975e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/0a41bf1eeab851494f7179590561975e.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>第三章：Nginx反向代理</h3><h4>3.1、概述</h4>Nginx不仅可以做反向代理，还能用作正向代理来进行上网等功能，正向代理：如果把局域网外的Internet想象成一个巨大的资源库，则局域网中的客户端要访问Internet，则需要通过代理服务器来访问，这种代理服务就称为正向代理。对于反向代理，客户端对代理是无感知的，因为客户端不需要任何配置就可以访问，我们只需要将请求发送到反向代理服务器，由反向代理服务器去选择目标服务器获取数据后，在返回给客户端，此时反向代理服务器和目标服务器对外就是一个服务器，暴露的是代理服务器地址，隐藏了真实服务器IP地址。<br>
<h4>3.2、配置反向代理实例1</h4><strong>3.2.1、实现效果</strong><br>
<br>打开浏览器，在浏览器地址栏输入地址：<a href="http://www.123.com/" rel="nofollow" target="_blank">http://www.123.com</a>，跳转到Liunx系统Tomcat主页面中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/128e92ab68f9094463a200ca885ca5f5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/128e92ab68f9094463a200ca885ca5f5.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3.2.2、实现思路</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/cd12c2e13cbf58ccf311f3183d16030a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/cd12c2e13cbf58ccf311f3183d16030a.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3.2.3、实现步骤</strong><br>
<br>步骤一：修改Windows中的hosts域名映射<br>
<br>复制“C:\Windows\System32\drivers\etc\hosts”到桌面，右键记事本打开，在里边加上以下代码保存，然后再复制回去，不要直接修改，会不让保存！<br>
<pre class="prettyprint">#虚拟机域名       映射的网址<br>
192.168.206.128 www.123.com<br>
</pre><br>
步骤二：修改Nginx中的配置文件并启动<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /usr/local/nginx/conf/nginx.conf<br>
</pre><br>
<pre class="prettyprint">server &#123;<br>
    listen       80;<br>
    server_name  192.168.206.128;<br>
<br>
    #charset koi8-r;<br>
<br>
    #access_log  logs/host.access.log  main;<br>
<br>
    location / &#123;<br>
        proxy_pass http:127.0.0.1:8080;<br>
        root   html;<br>
        index  index.html index.htm;<br>
    &#125; <br>
</pre><br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx<br>
</pre><br>
步骤三：下载Tomcat、解压Tomcat、安装Tomcat、启动Tomcat<br>
<br>注意：Tomcat启动需要JDK，在这里我没有安装，使用系统自带的OpenJDK Runtime Environment (rhel-2.6.14.10.el6-x86_64 u181-b00)<br>
<br>下载：<br>
<pre class="prettyprint">[root@caochenlei ~]# wget https://mirror.bit.edu.cn/apache/tomcat/tomcat-7/v7.0.105/bin/apache-tomcat-7.0.105.tar.gz<br>
</pre><br>
解压：<br>
<pre class="prettyprint">[root@caochenlei ~]# tar -zxvf apache-tomcat-7.0.105.tar.gz<br>
</pre><br>
安装：<br>
<pre class="prettyprint">[root@caochenlei ~]# mv apache-tomcat-7.0.105 /usr/local/tomcat<br>
</pre><br>
启动：<br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/tomcat/bin/startup.sh    <br>
</pre><br>
添加到防火墙：<br>
<pre class="prettyprint">[root@caochenlei ~]# /sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT<br>
[root@caochenlei ~]# /etc/rc.d/init.d/iptables save<br>
</pre><br>
如果关闭请用：<br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/tomcat/bin/shutdown.sh<br>
</pre><br>
<strong>3.2.4、关闭服务</strong><br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx -s quit<br>
[root@caochenlei ~]# /usr/local/tomcat/bin/shutdown.sh<br>
</pre><br>
<h4>3.3、配置反向代理实例2</h4><strong>3.3.1、实现效果</strong><br>
<br>使用Nginx反向代理，根据访问的路径跳转到不同端口的服务中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/535bd14d206cea3fdc264ef61b98458a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/535bd14d206cea3fdc264ef61b98458a.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3.3.2、实现思路</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/a1b0864fc644cb67aaf7d0a11a357ae3.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/a1b0864fc644cb67aaf7d0a11a357ae3.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3.3.3、实现步骤</strong><br>
<br>步骤一：修改Nginx的配置文件，然后启动<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /usr/local/nginx/conf/nginx.conf<br>
</pre><br>
<pre class="prettyprint">server &#123;<br>
    listen       80;<br>
    server_name  192.168.206.128;<br>
<br>
    #charset koi8-r;<br>
<br>
    #access_log  logs/host.access.log  main;<br>
<br>
    location ~ /edu/ &#123;<br>
        proxy_pass http://127.0.0.1:8080;<br>
    &#125;<br>
<br>
    location ~ /vod/ &#123;<br>
        proxy_pass http://127.0.0.1:8081;<br>
    &#125; <br>
</pre><br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx<br>
</pre><br>
步骤二：拷贝两个Tomcat，将其中一个的端口信息修改为8081，开启防火墙，然后分别启动这两台Tomcat<br>
<br>解压：<br>
<pre class="prettyprint">[root@caochenlei ~]# tar -zxvf apache-tomcat-7.0.105.tar.gz<br>
[root@caochenlei ~]# mv apache-tomcat-7.0.105 /usr/local/tomcat1<br>
<br>
[root@caochenlei ~]# tar -zxvf apache-tomcat-7.0.105.tar.gz<br>
[root@caochenlei ~]# mv apache-tomcat-7.0.105 /usr/local/tomcat2<br>
</pre><br>
删除：<br>
<pre class="prettyprint">[root@caochenlei ~]# rm -f /usr/local/tomcat2/conf/server.xml<br>
</pre><br>
添加：<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /usr/local/tomcat2/conf/server.xml<br>
</pre><br>
<pre class="prettyprint"><?xml version='1.0' encoding='utf-8'?><br>
<!--<br>
Licensed to the Apache Software Foundation (ASF) under one or more<br>
contributor license agreements.  See the NOTICE file distributed with<br>
this work for additional information regarding copyright ownership.<br>
The ASF licenses this file to You under the Apache License, Version 2.0<br>
(the "License"); you may not use this file except in compliance with<br>
the License.  You may obtain a copy of the License at<br>
  http://www.apache.org/licenses/LICENSE-2.0<br>
Unless required by applicable law or agreed to in writing, software<br>
distributed under the License is distributed on an "AS IS" BASIS,<br>
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.<br>
See the License for the specific language governing permissions and<br>
limitations under the License.<br>
--><br>
<!-- Note:  A "Server" is not itself a "Container", so you may not<br>
 define subcomponents such as "Valves" at this level.<br>
 Documentation at /docs/config/server.html<br>
--><br>
<Server port="8006" shutdown="SHUTDOWN"><br>
<Listener className="org.apache.catalina.startup.VersionLoggerListener" /><br>
<!-- Security listener. Documentation at /docs/config/listeners.html<br>
<Listener className="org.apache.catalina.security.SecurityListener" /><br>
--><br>
<!--APR library loader. Documentation at /docs/apr.html --><br>
<Listener className="org.apache.catalina.core.AprLifecycleListener" SSLEngine="on" /><br>
<!--Initialize Jasper prior to webapps are loaded. Documentation at /docs/jasper-howto.html --><br>
<Listener className="org.apache.catalina.core.JasperListener" /><br>
<!-- Prevent memory leaks due to use of particular java/javax APIs--><br>
<Listener className="org.apache.catalina.core.JreMemoryLeakPreventionListener" /><br>
<Listener className="org.apache.catalina.mbeans.GlobalResourcesLifecycleListener" /><br>
<Listener className="org.apache.catalina.core.ThreadLocalLeakPreventionListener" /><br>
<!-- Global JNDI resources<br>
   Documentation at /docs/jndi-resources-howto.html<br>
--><br>
<GlobalNamingResources><br>
<!-- Editable user database that can also be used by<br>
     UserDatabaseRealm to authenticate users<br>
--><br>
<Resource name="UserDatabase" auth="Container"<br>
          type="org.apache.catalina.UserDatabase"<br>
          description="User database that can be updated and saved"<br>
          factory="org.apache.catalina.users.MemoryUserDatabaseFactory"<br>
          pathname="conf/tomcat-users.xml" /><br>
</GlobalNamingResources><br>
<!-- A "Service" is a collection of one or more "Connectors" that share<br>
   a single "Container" Note:  A "Service" is not itself a "Container",<br>
   so you may not define subcomponents such as "Valves" at this level.<br>
   Documentation at /docs/config/service.html<br>
--><br>
<Service name="Catalina"><br>
<!--The connectors can use a shared executor, you can define one or more named thread pools--><br>
<!--<br>
<Executor name="tomcatThreadPool" namePrefix="catalina-exec-"<br>
    maxThreads="150" minSpareThreads="4"/><br>
--><br>
<!-- A "Connector" represents an endpoint by which requests are received<br>
     and responses are returned. Documentation at :<br>
     Java HTTP Connector: /docs/config/http.html (blocking & non-blocking)<br>
     Java AJP  Connector: /docs/config/ajp.html<br>
     APR (HTTP/AJP) Connector: /docs/apr.html<br>
     Define a non-SSL HTTP/1.1 Connector on port 8080<br>
--><br>
<Connector port="8081" protocol="HTTP/1.1"<br>
           connectionTimeout="20000"<br>
           redirectPort="8444" /><br>
<!-- A "Connector" using the shared thread pool--><br>
<!--<br>
<Connector executor="tomcatThreadPool"<br>
           port="8081" protocol="HTTP/1.1"<br>
           connectionTimeout="20000"<br>
           redirectPort="8444" /><br>
--><br>
<!-- Define an SSL HTTP/1.1 Connector on port 8443<br>
     This connector uses the BIO implementation that requires the JSSE<br>
     style configuration. When using the APR/native implementation, the<br>
     OpenSSL style configuration is required as described in the APR/native<br>
     documentation --><br>
<!--<br>
<Connector port="8444" protocol="org.apache.coyote.http11.Http11Protocol"<br>
           maxThreads="150" SSLEnabled="true" scheme="https" secure="true"<br>
           clientAuth="false" sslProtocol="TLS" /><br>
--><br>
<!-- Define an AJP 1.3 Connector on port 8009 --><br>
<!--<br>
<Connector protocol="AJP/1.3"<br>
           address="::1"<br>
           port="8010"<br>
           redirectPort="8444" /><br>
--><br>
<!-- An Engine represents the entry point (within Catalina) that processes<br>
     every request.  The Engine implementation for Tomcat stand alone<br>
     analyzes the HTTP headers included with the request, and passes them<br>
     on to the appropriate Host (virtual host).<br>
     Documentation at /docs/config/engine.html --><br>
<!-- You should set jvmRoute to support load-balancing via AJP ie :<br>
<Engine name="Catalina" defaultHost="localhost" jvmRoute="jvm1"><br>
--><br>
<Engine name="Catalina" defaultHost="localhost"><br>
  <!--For clustering, please take a look at documentation at:<br>
      /docs/cluster-howto.html  (simple how to)<br>
      /docs/config/cluster.html (reference documentation) --><br>
  <!--<br>
  <Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"/><br>
  --><br>
  <!-- Use the LockOutRealm to prevent attempts to guess user passwords<br>
       via a brute-force attack --><br>
  <Realm className="org.apache.catalina.realm.LockOutRealm"><br>
    <!-- This Realm uses the UserDatabase configured in the global JNDI<br>
         resources under the key "UserDatabase".  Any edits<br>
         that are performed against this UserDatabase are immediately<br>
         available for use by the Realm.  --><br>
    <Realm className="org.apache.catalina.realm.UserDatabaseRealm"<br>
           resourceName="UserDatabase"/><br>
  </Realm><br>
  <Host name="localhost"  appBase="webapps"<br>
        unpackWARs="true" autoDeploy="true"><br>
    <!-- SingleSignOn valve, share authentication between web applications<br>
         Documentation at: /docs/config/valve.html --><br>
    <!--<br>
    <Valve className="org.apache.catalina.authenticator.SingleSignOn" /><br>
    --><br>
    <!-- Access log processes all example.<br>
         Documentation at: /docs/config/valve.html<br>
         Note: The pattern used is equivalent to using pattern="common" --><br>
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"<br>
           prefix="localhost_access_log." suffix=".txt"<br>
           pattern="%h %l %u %t &quot;%r&quot; %s %b" /><br>
  </Host><br>
</Engine><br>
</Service><br>
</Server> <br>
</pre><br>
开启Tomcat2的防火墙：<br>
<pre class="prettyprint">[root@caochenlei ~]# /sbin/iptables -I INPUT -p tcp --dport 8081 -j ACCEPT<br>
[root@caochenlei ~]# /etc/rc.d/init.d/iptables save<br>
</pre><br>
在每一个Tomcat的WebApps中创建一个文件夹和一个a.html文件：<br>
<pre class="prettyprint">[root@caochenlei ~]# mkdir -p /usr/local/tomcat1/webapps/edu<br>
[root@caochenlei ~]# echo "<h1>This is 8080 Port</h1>" > /usr/local/tomcat1/webapps/edu/a.html<br>
<br>
[root@caochenlei ~]# mkdir -p /usr/local/tomcat2/webapps/vod<br>
[root@caochenlei ~]# echo "<h1>This is 8081 Port</h1>" > /usr/local/tomcat2/webapps/vod/a.html<br>
</pre><br>
启动：<br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/tomcat1/bin/startup.sh<br>
[root@caochenlei ~]# /usr/local/tomcat2/bin/startup.sh<br>
</pre><br>
步骤三：打开本机浏览器进行测试<br>
<br>在浏览器输入：<a href="http://192.168.206.128/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.128/edu/a.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/3e365f09a43571ed461aac7de8526236.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/3e365f09a43571ed461aac7de8526236.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在浏览器输入：<a href="http://192.168.206.128/vod/a.html" rel="nofollow" target="_blank">http://192.168.206.128/vod/a.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/4c29a6e37ce9b9fe712f31f0620b217c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/4c29a6e37ce9b9fe712f31f0620b217c.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>3.3.4、关闭服务</strong><br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx -s quit<br>
[root@caochenlei ~]# /usr/local/tomcat1/bin/shutdown.sh<br>
[root@caochenlei ~]# /usr/local/tomcat2/bin/shutdown.sh<br>
</pre><br>
<h4>3.4、location指令说明</h4>描述：该指令用于匹配URL。<br>
<br>语法：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/95202c82f34cb7d6e7ecf657f8d5b9c2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/95202c82f34cb7d6e7ecf657f8d5b9c2.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通配符：<br>
<ul><li>=：用于不含正则表达式的uri前，要求请求字符串与uri严格匹配，如果匹配成功，就停止继续向下搜索并立即处理该请求。</li><li>~：用于表示uri包含正则表达式，并且区分大小写。</li><li>~*：用于表示uri包含正则表达式，并且不区分大小写。</li><li>^~：用于不含正则表达式的uri前，要求Nginx服务器找到标识uri和请求字符串匹配度最高的location后，立即使用此location处理请求，而不再使用location块中的正则uri和请求字符串做匹配。</li></ul><br>
<br>注意：如果uri包含正则表达式，则必须要有~ 或者~*标识。<br>
<h3>第四章：Nginx负载均衡</h3><h4>4.1、概述</h4>客户端发送多个请求到服务器，服务器处理请求，有一些可能要与数据库进行交互，服务器处理完毕后，再将结果返回给客户端。<br>
<br>这种架构模式对于早期的系统相对单一，并发请求相对较少的情况下是比较适合的，成本也低。但是随着信息数量的不断增长，访问量和数据量的飞速增长，以及系统业务的复杂度增加，这种架构会造成服务器相应客户端的请求日益缓慢，并发量特别大的时候，还容易造成服务器直接崩溃。很明显这是由于服务器性能的瓶颈造成的问题，那么如何解决这种情况呢？<br>
<br>我们首先想到的可能是升级服务器的配置，比如提高CPU执行频率，加大内存等提高机器的物理性能来解决此问题，但是我们知道摩尔定律的日益失效，硬件的性能提升已经不能满足日益提升的需求了。最明显的一个例子，天猫双十一当天，某个热销商品的瞬时访问量是极其庞大的，那么类似上面的系统架构，将机器都增加到现有的顶级物理配置，都是不能够满足需求的。那么怎么办呢？<br>
<br>上面的分析我们去掉了增加服务器物理配置来解决问题的办法，也就是说纵向解决问题的办法行不通了，那么横向增加服务器的数量呢？这时候集群的概念产生了，单个服务器解决不了，我们增加服务器的数量，然后将请求分发到各个服务器上，将原先请求集中到单个服务器上的情况改为将请求分发到多个服务器上，将负载分发到不同的服务器，也就是我们所说的负载均衡。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/82148b81fc8120c78462c04c9a3d9136.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/82148b81fc8120c78462c04c9a3d9136.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>4.2、实现效果</h4>浏览器地址栏输入地址：<a href="http://192.168.206.128/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.128/edu/a.html</a>，负载均衡效果，将请求平均到8080和8081端口中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/e169385c45d56cabded1fe97b4ec3e0c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/e169385c45d56cabded1fe97b4ec3e0c.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>4.3、实现思路</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/e8b064df63ef010bf5b9613a159b73a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/e8b064df63ef010bf5b9613a159b73a4.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>4.4、实现步骤</h4>第一步：修改Nginx的配置文件<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /usr/local/nginx/conf/nginx.conf<br>
</pre><br>
<pre class="prettyprint">upstream myserver &#123;<br>
    server 192.168.206.128:8080;<br>
    server 192.168.206.128:8081;<br>
&#125;<br>
<br>
server &#123;<br>
    listen       80;<br>
    server_name  192.168.206.128;<br>
<br>
    #charset koi8-r;<br>
<br>
    #access_log  logs/host.access.log  main;<br>
<br>
    location / &#123;<br>
        proxy_pass http://myserver;<br>
    &#125; <br>
</pre><br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx<br>
</pre><br>
第二步：在Tomcat2的webapps文件夹中，创建一个edu文件夹，在里边创建a.html<br>
<br>创建：<br>
<pre class="prettyprint">[root@caochenlei ~]# mkdir -p /usr/local/tomcat2/webapps/edu<br>
[root@caochenlei ~]# echo "<h1>This is 8081 Port</h1>" > /usr/local/tomcat2/webapps/edu/a.html<br>
</pre><br>
启动：<br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/tomcat1/bin/startup.sh<br>
[root@caochenlei ~]# /usr/local/tomcat2/bin/startup.sh<br>
</pre><br>
第三步：测试效果<br>
<br>打开IE浏览器输入：<a href="http://192.168.206.128/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.128/edu/a.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/30350fe356851cd4f460e935c7db873b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/30350fe356851cd4f460e935c7db873b.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
打开IE浏览器输入：<a href="http://192.168.206.128/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.128/edu/a.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/ab5decfde43f2f7d18759a1488fb9059.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/ab5decfde43f2f7d18759a1488fb9059.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>4.5、关闭服务</h4><pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx -s quit<br>
[root@caochenlei ~]# /usr/local/tomcat1/bin/shutdown.sh<br>
[root@caochenlei ~]# /usr/local/tomcat2/bin/shutdown.sh<br>
</pre><br>
<h4>4.6、分配策略</h4>轮询（默认）：每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务器down掉，能自动剔除。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/d89cf8a27da8c9ce9d1893d836281218.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/d89cf8a27da8c9ce9d1893d836281218.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
weight：weight代表权重，默认为1，权重越高被分配的客户端越多，weight和访问比率成正比，用于后端服务器性能不均的情况。 例如：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/0d438a76894dae25bb5cb5998ce15e8a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/0d438a76894dae25bb5cb5998ce15e8a.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
ip_hash：每个请求按访问IP的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。 例如：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/62a477f4ba33e390f9e278c388ce2f27.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/62a477f4ba33e390f9e278c388ce2f27.png" class="img-polaroid" title="16.png" alt="16.png" referrerpolicy="no-referrer"></a>
</div>
<br>
fair（第三方）：按后端服务器的响应时间来分配请求，响应时间短的优先分配。例如：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/03c8144bffb6af50b0a7e4b938436e0f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/03c8144bffb6af50b0a7e4b938436e0f.png" class="img-polaroid" title="17.png" alt="17.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>第五章：Nginx动静分离</h3><h4>5.1、概述</h4>Nginx动静分离简单来说就是把动态跟静态请求分开，不能理解成只是单纯的把动态页面和静态页面物理分离。严格意义上说应该是动态请求跟静态请求分开，可以理解成使用Nginx处理静态页面，Tomcat处理动态页面。动静分离从目前实现角度来讲大致分为两种，一种是纯粹把静态文件独立成单独的域名，放在独立的服务器上，也是目前主流推崇的方案；另外一种方法就是动态跟静态文件混合在一起发布，通过Nginx来分开。<br>
<h4>5.2、实现效果</h4>如果不设置动静分离，默认会通过Nginx的反向代理去找Tomcat对应的资源，现在我们在根目录下创建一个/data/www/文件夹，里边放上静态资源，比如一个html页面，在8080的那台Tomcat的WebApps下也创建一个www目录，同样是放一个静态资源，当输入这个静态资源的请求时，访问到的是/data/www中的数据。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/6b50c9c8903b6c2bccbf43c57dcd532a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/6b50c9c8903b6c2bccbf43c57dcd532a.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>5.3、实现思路</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/6e391d09dcf99ddf6f6427a6a4c30c15.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/6e391d09dcf99ddf6f6427a6a4c30c15.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>5.4、实现步骤</h4>第一步：创建静态资源文件，为了对比，Tomcat中也放一个<br>
<pre class="prettyprint">[root@caochenlei ~]# mkdir -p /data/www/<br>
[root@caochenlei ~]# mkdir -p /usr/local/tomcat/webapps/ROOT/www<br>
[root@caochenlei ~]# echo "<h1>/data/www/a.html</h1>" > /data/www/a.html<br>
[root@caochenlei ~]# echo "<h1>/usr/local/tomcat/webapps/ROOT/www/a.html</h1>" > /usr/local/tomcat/webapps/ROOT/www/a.html<br>
</pre><br>
第二步：修改Nginx的配置文件<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /usr/local/nginx/conf/nginx.conf<br>
</pre><br>
<pre class="prettyprint">server &#123;<br>
    listen       80;<br>
    server_name  192.168.206.128;<br>
<br>
    #charset koi8-r;<br>
<br>
    #access_log  logs/host.access.log  main;<br>
<br>
    location /www/ &#123;<br>
        root /data/;<br>
        index index.html index.htm;<br>
    &#125; <br>
</pre><br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx<br>
</pre><br>
第三步：启动Tomcat<br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/tomcat/bin/startup.sh<br>
</pre><br>
第四步：启动浏览器进行测试<br>
<br>打开浏览器输入：<a href="http://192.168.206.128/www/a.html" rel="nofollow" target="_blank">http://192.168.206.128/www/a.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/04373d617568709aad198562aa8bfa6c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/04373d617568709aad198562aa8bfa6c.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>5.5、关闭服务</h4><pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx -s quit<br>
[root@caochenlei ~]# /usr/local/tomcat/bin/shutdown.sh<br>
</pre><br>
<h3>第六章：Nginx高可用集群</h3><h4>6.1、概述</h4>前边我们学习了反向代理、负载均衡、动静分离，但试想一下，如果Nginx挂掉了，那么服务肯定就没有了，有没有一种解决方案，可以保证Nginx挂掉了，服务也可以照常使用，答案肯定是有的，这就是我们接下来要学习的高可用集群，采用的是一主一备的模式，当主节点Nginx挂掉，备份服务器Nginx立刻跟上，这样就保证了服务的高可用性。<br>
<h4>6.2、实现效果</h4>当主节点Nginx挂掉以后，服务依然可以正常使用。<br>
<h4>6.3、实现思路</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/33fce94598f8d07fd7e1fad18053610f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/33fce94598f8d07fd7e1fad18053610f.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>6.4、实现步骤</h4>第一步：修改主节点上的Nginx的配置文件<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /usr/local/nginx/conf/nginx.conf<br>
</pre><br>
<pre class="prettyprint">upstream myserver &#123;<br>
    server 192.168.206.128:8080;<br>
    server 192.168.206.128:8081;<br>
&#125;<br>
<br>
server &#123;<br>
    listen       80;<br>
    server_name  192.168.206.128;<br>
<br>
    #charset koi8-r;<br>
<br>
    #access_log  logs/host.access.log  main;<br>
<br>
    location / &#123;<br>
        proxy_pass http://myserver;<br>
    &#125; <br>
</pre><br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx<br>
</pre><br>
第二步：启动主节点上的两台Tomcat<br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/tomcat1/bin/startup.sh<br>
[root@caochenlei ~]# /usr/local/tomcat2/bin/startup.sh<br>
</pre><br>
第三步：安装主节点上的keepalived<br>
<br>安装keepalived：<br>
<pre class="prettyprint">[root@caochenlei ~]# yum install -y keepalived<br>
</pre><br>
删除keepalived的配置文件：<br>
<pre class="prettyprint">[root@caochenlei ~]# rm -f /etc/keepalived/keepalived.conf<br>
</pre><br>
新增keepalived的配置文件：<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /etc/keepalived/keepalived.conf<br>
</pre><br>
注意：一定要注意router_id、state、interface的值，我就在这里踩坑了。<br>
<pre class="prettyprint">! Configuration File for keepalived<br>
<br>
global_defs &#123;<br>
notification_email &#123;<br>
 acassen@firewall.loc<br>
 failover@firewall.loc<br>
 sysadmin@firewall.loc<br>
&#125;<br>
notification_email_from Alexandre.Cassen@firewall.loc<br>
#邮件服务器通知地址（暂不配置，默认即可）<br>
smtp_server 192.168.200.1<br>
#邮件服务器超时时间（暂不配置，默认即可）<br>
smtp_connect_timeout 30<br>
#当前虚拟机的IP地址<br>
router_id 192.168.206.128<br>
&#125;<br>
<br>
vrrp_script Monitor_Nginx &#123;<br>
script "/etc/keepalived/nginx_check.sh"    #检测脚本执行的路径<br>
interval 2                                 #检测脚本执行的间隔<br>
weight 2                                   #检测脚本执行的权重<br>
&#125;<br>
<br>
vrrp_instance VI_1 &#123;<br>
state MASTER         #标识这个机器是MASTER还是BACKUP<br>
interface eth0       #当前机器的网卡名称  <br>
virtual_router_id 51 #虚拟路由的编号，主备必须一致<br>
priority 100         #主、备机取不同的优先级，主机值较大，备份机值较小<br>
advert_int 1         #（VRRP Multicast广播周期秒数）<br>
authentication &#123;<br>
    auth_type PASS   #（VRRP认证方式）<br>
    auth_pass 1111   #（密码）<br>
&#125;<br>
track_script &#123;<br>
    Monitor_Nginx #（调用Nginx进程检测脚本）<br>
&#125;<br>
virtual_ipaddress &#123;<br>
    192.168.206.50  #虚拟IP地址<br>
&#125;<br>
&#125; <br>
</pre><br>
新增keepalived的检测脚本：<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /etc/keepalived/nginx_check.sh<br>
</pre><br>
<pre class="prettyprint">#!/bin/bash<br>
if [ "$(ps -ef | grep "nginx: master process" | grep -v grep )" == "" ]<br>
then<br>
killall keepalived<br>
fi<br>
</pre><br>
启动keepalived服务：<br>
<pre class="prettyprint">[root@caochenlei ~]# service keepalived start<br>
</pre><br>
第四步：准备一台全新的虚拟机，安装Nginx和keepalived<br>
<br>启动虚拟机：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/7a84d94e56c576528ce0f628debff4fb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/7a84d94e56c576528ce0f628debff4fb.png" class="img-polaroid" title="22.png" alt="22.png" referrerpolicy="no-referrer"></a>
</div>
<br>
安装Nginx依赖：<br>
<pre class="prettyprint">[root@caochenlei ~]# yum install -y gcc gcc-c++ make libtool wget pcre pcre-devel zlib zlib-devel openssl openssl-devel<br>
</pre><br>
下载Nginx文件：<br>
<pre class="prettyprint">[root@caochenlei ~]# wget http://nginx.org/download/nginx-1.18.0.tar.gz<br>
</pre><br>
安装Nginx程序：<br>
<pre class="prettyprint">[root@caochenlei ~]# tar -zxvf nginx-1.18.0.tar.gz<br>
[root@caochenlei ~]# cd nginx-1.18.0<br>
[root@caochenlei nginx-1.18.0]# ./configure<br>
[root@caochenlei nginx-1.18.0]# make && make install<br>
[root@caochenlei nginx-1.18.0]# cd ~<br>
</pre><br>
开放Nginx防火墙：<br>
<pre class="prettyprint">[root@caochenlei ~]# /sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT<br>
[root@caochenlei ~]# /etc/rc.d/init.d/iptables save<br>
iptables：将防火墙规则保存到 /etc/sysconfig/iptables：     [确定]<br>
</pre><br>
修改Nginx的配置：<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /usr/local/nginx/conf/nginx.conf<br>
</pre><br>
<pre class="prettyprint">upstream myserver &#123;<br>
    server 192.168.206.128:8080;<br>
    server 192.168.206.128:8081;<br>
&#125;<br>
<br>
server &#123;<br>
    listen       80;<br>
    server_name  192.168.206.128;<br>
<br>
    #charset koi8-r;<br>
<br>
    #access_log  logs/host.access.log  main;<br>
<br>
    location / &#123;<br>
        proxy_pass http://myserver;<br>
    &#125; <br>
</pre><br>
启动Nginx的服务：<br>
<pre class="prettyprint">[root@caochenlei ~]# /usr/local/nginx/sbin/nginx<br>
</pre><br>
安装keepalived：<br>
<pre class="prettyprint">[root@caochenlei ~]# yum install -y keepalived<br>
</pre><br>
删除keepalived的配置文件：<br>
<pre class="prettyprint">[root@caochenlei ~]# rm -f /etc/keepalived/keepalived.conf<br>
</pre><br>
新增keepalived的配置文件：<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /etc/keepalived/keepalived.conf<br>
</pre><br>
注意：一定要注意router_id、state、interface的值，我就在这里踩坑了。<br>
<pre class="prettyprint">! Configuration File for keepalived<br>
<br>
global_defs &#123;<br>
notification_email &#123;<br>
 acassen@firewall.loc<br>
 failover@firewall.loc<br>
 sysadmin@firewall.loc<br>
&#125;<br>
notification_email_from Alexandre.Cassen@firewall.loc<br>
#邮件服务器通知地址（暂不配置，默认即可）<br>
smtp_server 192.168.200.1<br>
#邮件服务器超时时间（暂不配置，默认即可）<br>
smtp_connect_timeout 30<br>
#当前虚拟机的IP地址<br>
router_id 192.168.206.129<br>
&#125;<br>
<br>
vrrp_script Monitor_Nginx &#123;<br>
script "/etc/keepalived/nginx_check.sh"    #检测脚本执行的路径<br>
interval 2                                 #检测脚本执行的间隔<br>
weight 2                                   #检测脚本执行的权重<br>
&#125;<br>
<br>
vrrp_instance VI_1 &#123;<br>
state BACKUP         #标识这个机器是MASTER还是BACKUP<br>
interface eth1       #当前机器的网卡名称  <br>
virtual_router_id 51 #虚拟路由的编号，主备必须一致<br>
priority 10          #主、备机取不同的优先级，主机值较大，备份机值较小<br>
advert_int 1         #（VRRP Multicast广播周期秒数）<br>
authentication &#123;<br>
    auth_type PASS   #（VRRP认证方式）<br>
    auth_pass 1111   #（密码）<br>
&#125;<br>
track_script &#123;<br>
    Monitor_Nginx    #（调用Nginx进程检测脚本）<br>
&#125;<br>
virtual_ipaddress &#123;<br>
    192.168.206.50   #虚拟IP地址<br>
&#125;<br>
&#125; <br>
</pre><br>
新增keepalived的检测脚本：<br>
<pre class="prettyprint">[root@caochenlei ~]# vi /etc/keepalived/nginx_check.sh<br>
</pre><br>
<pre class="prettyprint">#!/bin/bash<br>
if [ "$(ps -ef | grep "nginx: master process" | grep -v grep )" == "" ]<br>
then<br>
killall keepalived<br>
fi<br>
</pre><br>
启动keepalived服务：<br>
<pre class="prettyprint">[root@caochenlei ~]# service keepalived start<br>
</pre><br>
第五步：测试两个Nginx是否能正确的将请求分发到不同的Tomcat（负载均衡）<br>
<br>打开IE浏览器输入：<a href="http://192.168.206.128/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.128/edu/a.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/dac7c292884953e470790853f034cdaf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/dac7c292884953e470790853f034cdaf.png" class="img-polaroid" title="23.png" alt="23.png" referrerpolicy="no-referrer"></a>
</div>
<br>
按住F5多刷新两遍，看看会不会，将请求转发到Tomcat2中去。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/f890011ddd2f14dd6edeb62e1cc13b06.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/f890011ddd2f14dd6edeb62e1cc13b06.png" class="img-polaroid" title="24.png" alt="24.png" referrerpolicy="no-referrer"></a>
</div>
<br>
打开IE浏览器输入：<a href="http://192.168.206.129/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.129/edu/a.html</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/7d7a1f23764b4cbe7ac17eca1e60173f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/7d7a1f23764b4cbe7ac17eca1e60173f.png" class="img-polaroid" title="25.png" alt="25.png" referrerpolicy="no-referrer"></a>
</div>
<br>
按住F5多刷新两遍，看看会不会，将请求转发到Tomcat2中去。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/08b1e222be50c132601b9b109b29ce11.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/08b1e222be50c132601b9b109b29ce11.png" class="img-polaroid" title="26.png" alt="26.png" referrerpolicy="no-referrer"></a>
</div>
<br>
打开IE浏览器输入：<a href="http://192.168.206.50/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.50/edu/a.html</a>，测试虚拟IP能不能实现负载均衡。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/813863b5e5fc0f776b2066c1ab1c967f.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/813863b5e5fc0f776b2066c1ab1c967f.png" class="img-polaroid" title="27.png" alt="27.png" referrerpolicy="no-referrer"></a>
</div>
<br>
按住F5多刷新两遍，看看会不会，将请求转发到Tomcat2中去。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/1f35faad8a5273a4fbb260c83844ab6b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/1f35faad8a5273a4fbb260c83844ab6b.png" class="img-polaroid" title="28.png" alt="28.png" referrerpolicy="no-referrer"></a>
</div>
<br>
经过测试，我们发现一主一从、虚拟IP都能正常的进行负载均衡，接下来我们测试主节点挂掉，从节点会不会自动顶上，打开主节点机器，查看相关进程，杀死Nginx，然后打开浏览器，输入配置的虚拟IP地址：<a href="http://192.168.206.50/edu/a.html" rel="nofollow" target="_blank">http://192.168.206.50/edu/a.html</a>，发现负载均衡的效果还在，说明配置成功了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/9a74315cddfeb948fb4db351aa8a725c.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/9a74315cddfeb948fb4db351aa8a725c.png" class="img-polaroid" title="29.png" alt="29.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/d85302312c659b9ade2799e0d95329dc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/d85302312c659b9ade2799e0d95329dc.png" class="img-polaroid" title="30.png" alt="30.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>6.5、关闭服务</h4>主机节点：<br>
<pre class="prettyprint">[root@caochenlei ~]# service keepalived stop<br>
[root@caochenlei ~]# /usr/local/nginx/sbin/nginx -s quit<br>
[root@caochenlei ~]# /usr/local/tomcat1/bin/shutdown.sh<br>
[root@caochenlei ~]# /usr/local/tomcat2/bin/shutdown.sh<br>
</pre><br>
备份节点：<br>
<pre class="prettyprint">[root@caochenlei ~]# service keepalived stop<br>
[root@caochenlei ~]# /usr/local/nginx/sbin/nginx -s quit<br>
</pre><br>
<h3>第七章：Nginx配置详解</h3>Nginx是通过配置文件来做到各个功能的实现的。Nginx的配置文件的格式非常合乎逻辑，学习这种格式以及如何使用这种每个部分是基础，这将帮助我们有可能手工创建一个配置文件。<br>
<h4>7.1、整体结构图</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/9a4062500902e98b29fa15fd50e7a4ff.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/9a4062500902e98b29fa15fd50e7a4ff.png" class="img-polaroid" title="31.png" alt="31.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>7.2、配置演示图</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/9f9ae210b7ba08005ac72824df72fd31.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/9f9ae210b7ba08005ac72824df72fd31.png" class="img-polaroid" title="32.png" alt="32.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>7.3、全局块</h4>配置影响Nginx全局的指令。主要包括：<br>
<ul><li>配置运行Nginx服务器用户（组）</li><li>worker process数</li><li>Nginx进程</li><li>PID存放路径错误日志的存放路径</li><li>一个nginx进程打开的最多文件描述符数目</li></ul><br>
<br>例如：<br>
<pre class="prettyprint">#配置worker进程运行用户（和用户组），nobody也是一个Linux用户，一般用于启动程序，没有密码<br>
user nobody;<br>
<h1>user www www;</h1><h1>配置工作进程数目，根据硬件调整，通常等于CPU数量或者2倍于CPU数量</h1>worker_processes 1;<br>
<h1>配置全局错误日志及类型，[debug | info | notice | warn | error | crit]，默认是error</h1>error_log logs/error.log;<br>
<h1>error_log logs/error.log notice;</h1><h1>error_log logs/error.log info;</h1><h1>配置进程pid文件</h1>pid logs/nginx.pid;<br>
<h1>一个nginx进程打开的最多文件描述符数目，理论值应该是最多打开文件数（系统的值ulimit -n）与Nginx进程数相除，但是Nginx分配请求并不均匀，所以建议与ulimit -n的值保持一致。</h1>worker_rlimit_nofile 65535;<br>
</pre><br>
<h4>7.4、events块</h4>配置影响Nginx服务器或与用户的网络连接。主要包括：<br>
<ul><li>事件驱动模型的选择</li><li>最大连接数的配置</li></ul><br>
<br>例如：<br>
<pre class="prettyprint">#参考事件模型，use [ kqueue | rtsig | epoll | /dev/poll | select | poll ]; <br>
<h1>epoll模型是Linux 2.6以上版本内核中的高性能网络I/O模型，如果跑在FreeBSD上面，就用kqueue模型。</h1>use epoll;<br>
<h1>单个进程最大连接数（最大连接数=连接数*进程数）</h1>worker_connections 65535;<br>
</pre><br>
<h4>7.5、http块</h4>可以嵌套多个server，配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置。主要包括：<br>
<ul><li>定义MIMI-Type</li><li>自定义服务日志</li><li>允许sendfile方式传输文件</li><li>连接超时时间</li><li>单连接请求数上限</li></ul><br>
<br>例如：<br>
<pre class="prettyprint">#常见的一些基础配置<br>
include mime.types; #文件扩展名与文件类型映射表<br>
default_type application/octet-stream; #默认文件类型<br>
charset utf-8; #默认编码<br>
server_names_hash_bucket_size 128; #服务器名字的hash表大小<br>
client_header_buffer_size 32k; #上传文件大小限制<br>
large_client_header_buffers 4 64k; #设定请求缓冲<br>
client_max_body_size 8m; #设定请求缓冲<br>
sendfile on; #开启高效文件传输模式，对于普通应用设为on，如果用来进行下载等应用磁盘IO重负载应用，可设置为off，以平衡磁盘与网络I/O处理速度，降低系统的负载。注意：如果图片显示不正常把这个改成off。<br>
autoindex on; #开启目录列表访问，合适下载服务器，默认关闭。<br>
tcp_nopush on; #防止网络阻塞<br>
tcp_nodelay on; #防止网络阻塞<br>
keepalive_timeout 120; #长连接超时时间，单位是秒<br>
<h1>FastCGI相关参数是为了改善网站的性能：减少资源占用，提高访问速度。</h1>fastcgi_connect_timeout 300;<br>
fastcgi_send_timeout 300;<br>
fastcgi_read_timeout 300;<br>
fastcgi_buffer_size 64k;<br>
fastcgi_buffers 4 64k;<br>
fastcgi_busy_buffers_size 128k;<br>
fastcgi_temp_file_write_size 128k;<br>
<h1>gzip模块设置</h1>gzip on; #开启gzip压缩输出<br>
gzip_min_length 1k; #最小压缩文件大小<br>
gzip_buffers 4 16k; #压缩缓冲区<br>
gzip_http_version 1.0; #压缩版本（默认1.1，前端如果是squid2.5请使用1.0）<br>
gzip_comp_level 2; #压缩等级<br>
gzip_types text/plain application/x-javascript text/css application/xml; #压缩类型<br>
gzip_vary on; #增加响应头'Vary: Accept-Encoding'<br>
limit_zone crawler $binary_remote_addr 10m; #开启限制IP连接数的时候需要使用<br>
</pre><br>
<h4>7.6、server块</h4>配置虚拟主机的相关参数，一个http中可以有多个server。主要包括：<br>
<ul><li>配置网络监听</li><li>配置https服务</li><li>基于名称的虚拟主机配置</li><li>基于IP的虚拟主机配置</li></ul><br>
<br>例如：<br>
<pre class="prettyprint">#虚拟主机的常见配置<br>
server &#123;<br>
listen       80; #配置监听端口<br>
server_name  localhost; #配置服务名<br>
charset utf-8; #配置字符集<br>
access_log  logs/host.access.log  main; #配置本虚拟主机的访问日志<br>
<br>
location / &#123;<br>
    root html; #root是配置服务器的默认网站根目录位置，默认为Nginx安装主目录下的html目录<br>
    index index.html index.htm; #配置首页文件的名称<br>
&#125;<br>
<br>
error_page 404             /404.html; #配置404错误页面<br>
error_page 500 502 503 504 /50x.html; #配置50x错误页面<br>
&#125;<br>
<h1>配置https服务，安全的网络传输协议，加密传输，端口443</h1>server &#123;<br>
listen       443 ssl;<br>
server_name  localhost;<br>
<br>
ssl_certificate      cert.pem;<br>
ssl_certificate_key  cert.key;<br>
<br>
ssl_session_cache    shared:SSL:1m;<br>
ssl_session_timeout  5m;<br>
<br>
ssl_ciphers  HIGH:!aNULL:!MD5;<br>
ssl_prefer_server_ciphers  on;<br>
<br>
location / &#123;<br>
    root   html;<br>
    index  index.html index.htm;<br>
&#125;<br>
&#125; <br>
</pre><br>
<h4>7.7、location块</h4>配置请求的路由，以及各种页面的处理情况。主要包括：<br>
<ul><li>请求根目录配置更改</li><li>网站默认首页配置</li><li>location的URI</li></ul><br>
<br>例如：<br>
<pre class="prettyprint">root html; #root是配置服务器的默认网站根目录位置，默认为Nginx安装主目录下的html目录<br>
index index.html index.htm; #配置首页文件的名称<br>
<br>
proxy_pass http://127.0.0.1:88; #反向代理的地址<br>
proxy_redirect off; #是否开启重定向<br>
<h1>后端的Web服务器可以通过X-Forwarded-For获取用户真实IP</h1>proxy_set_header X-Real-IP $remote_addr;<br>
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;<br>
proxy_set_header Host $host;<br>
<h1>以下是一些反向代理的配置，可选。</h1>client_max_body_size 10m; #允许客户端请求的最大单文件字节数<br>
client_body_buffer_size 128k; #缓冲区代理缓冲用户端请求的最大字节数，<br>
proxy_connect_timeout 90; #nginx跟后端服务器连接超时时间（代理连接超时）<br>
proxy_send_timeout 90; #后端服务器数据回传时间（代理发送超时）<br>
proxy_read_timeout 90; #连接成功后，后端服务器响应时间（代理接收超时）<br>
proxy_buffer_size 4k; #设置代理服务器（Nginx）保存用户头信息的缓冲区大小<br>
proxy_buffers 4 32k; #proxy_buffers缓冲区，网页平均在32k以下的设置<br>
proxy_busy_buffers_size 64k; #高负荷下缓冲大小（proxy_buffers*2）<br>
proxy_temp_file_write_size 64k;  #设定缓存文件夹大小<br>
</pre><br>
location的URI：<br>
<br>描述：该指令用于匹配URL<br>
<br>语法：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/4a5974a6e3e3489be5bd32f333f9306d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/4a5974a6e3e3489be5bd32f333f9306d.png" class="img-polaroid" title="33.png" alt="33.png" referrerpolicy="no-referrer"></a>
</div>
<br>
通配符：<br>
<ul><li>=：用于不含正则表达式的uri前，要求请求字符串与uri严格匹配，如果匹配成功，就停止继续向下搜索并立即处理该请求。</li><li>~：用于表示uri包含正则表达式，并且区分大小写。</li><li>~*：用于表示uri包含正则表达式，并且不区分大小写。</li><li>^~：用于不含正则表达式的uri前，要求Nginx服务器找到标识uri和请求字符串匹配度最高的location后，立即使用此location处理请求，而不再使用location块中的正则uri和请求字符串做匹配。</li></ul><br>
<br>注意：如果uri包含正则表达式，则必须要有~ 或者~*标识。<br>
<h3>第八章：Nginx原理分析</h3><h4>8.1、Nginx的线程模型？</h4>Nginx默认采用多进程工作方式，Nginx启动后，会运行一个master进程和多个worker进程。其中master充当整个进程组与用户的交互接口，同时对进程进行监护，管理worker进程来实现重启服务、平滑升级、更换日志文件、配置文件实时生效等功能。worker用来处理基本的网络事件，worker之间是平等的，他们共同竞争来处理来自客户端的请求。<br>
<br>Nginx的进程模型如图所示：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/4aa8312ab1b8aca63897e8df6a5809e8.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/4aa8312ab1b8aca63897e8df6a5809e8.png" class="img-polaroid" title="34.png" alt="34.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>8.2、worker的工作模式？</h4>worker对于连接是采用争抢的模式，谁先抢到就先交给谁处理，如果想要重新更新配置，由于已经抢到任务的worker不会参与争抢，那些空闲的worker就会去争抢连接，拿到连接后会自动更新配置信息，当那些有任务的worker完成任务后，会自动更新配置，这样就实现了无缝热部署。由于每个worker是独立的进程，如果有其中的一个worker出现问题，并不会影响其它worker继续进行争抢，在实现请求的过程，不会造成服务中断，建议worker数和服务器的CPU数相等是最为适宜的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/a0e69a97c248ae3910d08706a3b3afe5.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/a0e69a97c248ae3910d08706a3b3afe5.png" class="img-polaroid" title="35.png" alt="35.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>8.3、如何计算worker连接数？</h4>如果只访问Nginx的静态资源，一个发送请求会占用了woker的2个连接数<br>
而如果是作为反向代理服务器，一个发送请求会占用了woker的4个连接数<br>
<h4>8.4、如何计算最大的并发数？</h4>如果只访问nginx的静态资源，最大并发数量应该是： worker_connections * worker_processes / 2<br>
<br>而如果是作为反向代理服务器，最大并发数量应该是：worker_connections * worker_processes / 4<br>
<br>原文链接：<a href="https://blog.csdn.net/qq_38490457/article/details/108300342" rel="nofollow" target="_blank">https://blog.csdn.net/qq_38490 ... 00342</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            
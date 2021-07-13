
---
title: 'Nginx从基本原理到开发实践'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/ed8f3d85a784c46cb14749230179a6c6.jpg'
author: Dockone
comments: false
date: 2021-07-13 02:21:01
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/ed8f3d85a784c46cb14749230179a6c6.jpg'
---

<div>   
<br><h3>一、前言</h3>Nginx是什么？<br>
<br>Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，在BSD-like 协议下发行。其特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。<br>
<br>​Nginx作为一个高性能的HTTP和反向代理Web服务器，包括三个主要功能：静态服务器（作为Web服务器）、虚拟主机（作为邮件代理服务器）、反向代理(作为服务端的代理，作为负载均衡服务器）。本文以Nginx服务器的三个功能为主线，分为四个部分，分别是：全文第二部分介绍“Nginx三大功能——HTTP服务器”、全文第三部分介绍“Nginx三大功能——虚拟主机”、全文第四部分介绍“Nginx三大功能——负载均衡（反向代理+weight权重）”、全文第五部分介绍“实践——Nginx安装使用”。<br>
<h4>Nginx三个功能的区别</h4><strong>1、HTTP服务器（静态资源服务器/图片服务器）</strong><br>
<br>Nginx作为HTTP服务器：是指在web项目开发时，总是将项目部署在tomcat jetty等应用服务器上，而服务端所需要的资源，文本数据和静态资源路径自然存放在数据库中，而静态资源实体（如图片、音视频等）既不能放在数据库中，又不能放在应用服务器的相关目录下，这个时候我们需要一种用来存放项目所需静态资源的服务器（只要在数据库的字段中存储好静态资源的路径即可），这就是http服务器——Nginx。<br>
<br>为什么称为图片服务器，因为是最常用的静态资源服务器就是图片（虽然Nginx上存放的不一定是图片），以前没有Nginx服务器的时候，使用Apache+Tomcat作为组合，前者存放静态资源，后者存放应用程序，现在变成了 Nginx + Tomcat，Nginx相对于Apache，不仅可以做静态资源存储，还可以使用一个Nginx服务器虚拟出多个服务器（ip port 域名，使一个IP对应多个域名），还可以在服务端作为代理，做负载均衡服务器，将请求转发给Tomcat。<br>
<br><strong>2、反向代理/负载均衡</strong><br>
<br>Nginx反向代理：Nginx作为服务端代理，代表实际应用服务器与客户端交流，将网络请求分发给后台实际服务器。<br>
<br>Nginx负载均衡：Nginx作为服务端代理，根据weight权重将网络请求分发给后台实际服务器。<br>
<br>负载均衡和反向代理的关系：负载均衡是通过反向代理来实现的，负载均衡=反向代理+weight权重<br>
<br><strong>3、虚拟主机</strong><br>
<br>Nginx虚拟主机：Nginx部署在一个物理服务器上，却通过IP、端口、域名对外实现多个访问入口，让客户端以为是多个服务器，这就是虚拟主机（具体是如何实现虚拟的，下文提供解释）。<br>
<br>虚拟主机技术，使一个IP，通过port可以对应多个域名。<br>
<br>虚拟主机和负载均衡的区别又是什么？<br>
<br>Nginx做虚拟主机，将一个服务器当做多个服务器用，通过文件目录来虚拟服务器(主机)，虚拟主机指的是Nginx自己作为服务器存储文件；<br>
<br>Nginx做负载均衡，Nginx作为服务端代理服务器，将网络请求分发到具体的应用服务器（Tomcat或Jetty），根据不同的应用服务器（Tomcat Jetty）的性能，设置weight权重，Nginx本身不作为服务器存储文件。<br>
<br>小结：http服务器是指Nginx自己存储图片等静态文件，虚拟主机是Nginx提供多个入口来存储图片等静态文件，负载均衡是指nginx根据权重weight将网络请求分发给具体的应用服务器，实际项目中三个都会用到。<br>
<h3>二、Nginx三大功能——HTTP服务器</h3>Nginx是一款优秀的静态服务器，在做Java Web开发时，经常将它用来存放静态资源，一般是图片资源，所以又将Nginx称为图片服务器，然后将图片地址存入关系型数据库（一般为MySQL）中。关于Nginx作为静态服务器的配置，且看下面。<br>
<br>配置Nginx——修改Nginx安装目录/conf/nginx.conf（这里是/usr/local/nginx/conf/nginx.conf文件），如下：<br>
<pre class="prettyprint">​​server &#123;<br>
    listen       81; # 监听的端口<br>
    server_name  localhost; # 域名或IP<br>
    location / &#123;      # 访问路径配置<br>
        root   /usr/local/nginx/index; # 根目录<br>
        index  index.html index.htm; # 默认首页<br>
    &#125;<br>
    error_page   500 502 503 504  /50x.html;      # 错误页面<br>
    location = /50x.html &#123;<br>
        root   /usr/local/nginx/html;<br>
    &#125;<br>
&#125; <br>
</pre><br>
现在我们来对这段代码解释，实际上，对于Nginx做服务器，和其他服务器一样，只要搞清“ ip:port、页面、后台目录”三个东西就好了：<br>
<br>指定ip:port是localhost:81，我们直接在Linux计算机的浏览器上输入localhost:81，显示的是index.html/index.htm界面，对应后台目录是Nginx安装目录/index目录（如usr/local/nginx/index）；我们直接在Linux计算机的浏览器上输入localhost:81/50x.html，对应后台目录是Nginx安装目录/html目录（如usr/local/nginx/html）。<br>
<br>关于匹配关系，上面的配置中/表示可以匹配所有，/50x.html表示可以匹配50x.html，优先级关系是优先匹配长的，如localhost:81/50x.html同时满足/和/50x.html，由于优先匹配长的，所以要导向到html目录。如localhost:81/xxx.html仅满足于/，所以导向到index目录。<br>
<br>关于页面优先关系， index、index.html、index.htm；优先关系是从左到右，有index.html就显示index.html，没有就显示index.htm。<br>
<br>如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/ed8f3d85a784c46cb14749230179a6c6.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/ed8f3d85a784c46cb14749230179a6c6.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
附加：关于应用服务器和静态服务器的相关知识：我说软件服务器——软件服务器的前世今生（Web服务器+应用服务器）。<br>
<h3>三、Nginx三大功能——虚拟主机</h3><h4>3.1 虚拟主机</h4>什么是虚拟主机？<br>
<br>虚拟主机是一种特殊的软硬件技术，它可以将网络上的每一台计算机分成多个虚拟主机，每个虚拟主机可以独立对外提供www服务，这样就可以实现一台主机对外提供多个Web服务，每个虚拟主机之间是独立的，互不影响的（看不懂，没关系，一点一点往下面看）。<br>
<br>通过Nginx可以实现虚拟主机的配置，Nginx支持三种类型的虚拟主机配置，分别是：1、基于IP的虚拟主机；2、基于端口的虚拟主机；3、基于域名的虚拟主机。<br>
<h4>3.2 Nginx配置文件的结构</h4><pre class="prettyprint">......<br>
events &#123;<br>
.......<br>
&#125;<br>
http&#123;<br>
.......<br>
server&#123;<br>
.......<br>
&#125;<br>
server&#123;<br>
.......<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
Nginx的/conf/nginx.conf配置中，每个server标签就是一个虚拟主机。 实际上，就是同一机器，用不同的目录虚拟成不同的访问入口。<br>
<br>其中，因IP不同形成的不同的访问入口称为“基于IP的虚拟主机”，因端口不同形成的不同的访问入口称为“基于端口的虚拟主机”，因域名不同形成的不同的访问入口称为“基于域名的虚拟主机”。<br>
<h4>3.3 Nginx三种虚拟主机方式——基于IP的虚拟主机配置</h4>一台Nginx服务器绑定两个IP：192.168.101.3、192.168.101.103，访问不同的IP请求不同的html目录，即：访问<a href="http://192.168.101.3/" rel="nofollow" target="_blank">http://192.168.101.3</a>将访问“html3”目录下的html网页，访问<a href="http://192.168.101.103/" rel="nofollow" target="_blank">http://192.168.101.103</a>将访问“html103”目录下的html网页，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/6bef966a42c9de4d7623c72ac8ba957e.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/6bef966a42c9de4d7623c72ac8ba957e.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
对于上图的解释：<br>
<br>一个物理服务器，提供两个IP地址，分别是192.168.101.3:80和192.168.101.103:80，在外界客户端开来，好像有两个服务器，都可以独立网络请求，因为它们后台是不同的文件目录，分别是/usr/local/nginx/html3和/usr/local/nginx/html103，不会产生任何数据文件干扰。<br>
<br>配置Nginx——修改Nginx安装目录/conf/nginx.conf（这里是/usr/local/nginx/conf/nginx.conf文件），如下：<br>
<pre class="prettyprint">#user  nobody;<br>
worker_processes  1;<br>
<br>
events &#123;<br>
worker_connections  1024;<br>
&#125;<br>
<br>
http &#123;<br>
include       mime.types;<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
<br>
keepalive_timeout  65;<br>
#配置虚拟主机192.168.101.3<br>
server &#123;<br>
#监听的IP和端口，配置192.168.101.3:80<br>
    listen       80;<br>
#虚拟主机名称这里配置IP地址<br>
    server_name  192.168.101.3;<br>
#所有的请求都以/开始，所有的请求都可以匹配此location<br>
    location / &#123;<br>
    #使用root指令指定虚拟主机目录即网页存放目录<br>
    #比如访问http://ip/test.html将找到/usr/local/html3/test.html<br>
    #比如访问http://ip/item/test.html将找到/usr/local/html3/item/test.html<br>
<br>
        root   /usr/local/nginx/html3;<br>
    #指定欢迎页面，按从左到右顺序查找<br>
        index  index.html index.htm;<br>
    &#125;<br>
<br>
&#125;<br>
#配置虚拟主机192.168.101.103<br>
server &#123;<br>
    listen       80;<br>
    server_name  192.168.101.103;<br>
<br>
    location / &#123;<br>
        root   /usr/local/nginx/html103;<br>
        index  index.html index.htm;<br>
    &#125;<br>
<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
<h4>3.4 Nginx三种虚拟主机方式——基于端口的虚拟主机配置</h4>Nginx对外提供80和8080两个端口监听服务，请求80端口则请求html80目录下的html，请求8080端口则请求html8080目录下的html，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/d8ce9bd4d6acd8cbfc2b54167e955ad3.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/d8ce9bd4d6acd8cbfc2b54167e955ad3.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
对于这个图的理解是：<br>
<br>一个物理服务器，提供两个IP地址，分别是192.168.101.3:80和192.168.101.3:8080，在外界客户端开来，好像有两个服务器，都可以独立网络请求，因为它们后台是不同的文件目录，分别是/usr/local/nginx/html80和/usr/local/nginx/html8080，不会产生任何数据文件干扰。<br>
<br>配置Nginx——修改Nginx安装目录/conf/nginx.conf（这里是/usr/local/nginx/conf/nginx.conf文件），如下：<br>
<pre class="prettyprint">#user  nobody;<br>
worker_processes  1;<br>
<br>
events &#123;<br>
worker_connections  1024;<br>
&#125;<br>
<br>
http &#123;<br>
include       mime.types;<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
<br>
keepalive_timeout  65;<br>
#配置虚拟主机<br>
server &#123;<br>
#监听的IP和端口，配置80<br>
    listen       80;<br>
#虚拟主机名称这里配置IP地址<br>
    server_name  192.168.101.3;<br>
#所有的请求都以/开始，所有的请求都可以匹配此location<br>
    location / &#123;<br>
    #使用root指令指定虚拟主机目录即网页存放目录<br>
    #比如访问http://ip/test.html将找到/usr/local/html3/test.html<br>
    #比如访问http://ip/item/test.html将找到/usr/local/html3/item/test.html<br>
<br>
        root   /usr/local/nginx/html80;<br>
    #指定欢迎页面，按从左到右顺序查找<br>
        index  index.html index.htm;<br>
    &#125;<br>
<br>
&#125;<br>
#配置虚拟主机<br>
server &#123;<br>
    listen       8080;<br>
    server_name  192.168.101.3;<br>
<br>
    location / &#123;<br>
        root   /usr/local/nginx/html8080;<br>
        index  index.html index.htm;<br>
    &#125;<br>
<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
<h4>3.5 Nginx三种虚拟主机方式——基于域名的虚拟主机配置</h4>两个域名指向同一台Nginx服务器，用户访问不同的域名显示不同的网页内容。两个域名是aaa.test.com和bbb.test.com，Nginx服务器使用虚拟机192.168.101.3 ，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/9e65c70eec96bada7a64d7cd030eaa2a.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/9e65c70eec96bada7a64d7cd030eaa2a.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
对于这个图的理解是：<br>
<br>一个物理服务器，提供两个域名地址，分别是aaa.test.com和bbb.test.com，在外界客户端开来，好像有两个服务器，都可以独立网络请求，因为它们后台是不同的文件目录，分别是/usr/local/aaa_html和/usr/local/bbb_html，不会产生任何数据文件干扰。<br>
<br>在192.168.101.3上创建/usr/local/aaa_html，此目录为aaa.test.com域名访问的目录；在192.168.101.3上创建/usr/local/bbb_html，此目录为bbb.test.com域名访问的目录。<br>
<br>配置Nginx——修改Nginx安装目录/conf/nginx.conf（这里是/usr/local/nginx/conf/nginx.conf文件），如下：<br>
<pre class="prettyprint">#user  nobody;<br>
worker_processes  1;<br>
<br>
events &#123;<br>
worker_connections  1024;<br>
&#125;<br>
<br>
http &#123;<br>
include       mime.types;<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
<br>
keepalive_timeout  65;<br>
<h1>配置虚拟主机aaa.test.com</h1>server &#123;<br>
    #监听的IP和端口，配置本机IP和端口<br>
    listen 192.168.101.3:80;        <br>
    #虚拟主机名称是aaa.test.com，请求域名aaa.test.com的url将由此server配置解析<br>
    server_name aaa.test.com;    <br>
    #所有的请求都以/开始，所有的请求都可以匹配此location<br>
    location / &#123;<br>
    #使用root指令指定虚拟主机目录即网页存放目录<br>
    #比如访问http://ip/test.html将找到/usr/local/aaa_html/test.html<br>
    #比如访问http://ip/item/test.html将找到/usr/local/aaa_html/item/test.html<br>
            root /usr/local/aaa_html;   <br>
            #指定欢迎页面，按从左到右顺序查找<br>
            index index.html index.htm; <br>
    &#125;<br>
&#125;<br>
<h1>配置虚拟主机bbb.test.com</h1>    server &#123;<br>
    listen 192.168.101.3:80;<br>
    server_name bbb.test.com;<br>
    location / &#123;<br>
            root /usr/local/bbb_html;<br>
            index index.html index.htm;<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
在三种虚拟主机（基于IP的虚拟主机、基于端口的虚拟主机、基于域名的虚拟主机）中，项目开发中使用的最多的是基于域名的虚拟主机。<br>
<br>1、对于基于IP的虚拟主机：由于IP地址本来就稀缺，一个物理服务器配两个IP是不合实际的（毕竟，一个IP比一个服务器贵），所以，基于IP的虚拟主机不常用到，读者了解即可；<br>
<br>2、对于基于端口的虚拟主机：端口倒是不稀缺0-65535（一共65536个，默认是80端口），但是想让用户在浏览器上输入端口是非常不切实际的，所以，基于IP的虚拟主机也不常用到，读者了解即可；<br>
<br>3、对于基于域名的虚拟主机：一个物理服务器/服务器群（一个IP）配置多个域名，是可行的，因为：<br>
<ul><li>一来，域名平均价格比IP便宜的多（即租用多个域名比多个IP便宜，所以基于域名的虚拟主机比基于IP的虚拟主机便宜，注意：这里使用了平均两个字，希望读者不要抬杠）；</li><li>二来，用户可以容易的记得域名，然后在浏览器中输入域名。</li></ul><br>
<br>所以，基于IP的虚拟主机经常用到，读者一定要知道，下面我们将反向代理和负载均衡，在上面的一层会用到虚拟主机，都是基于域名的虚拟主机。<br>
<h3>四、Nginx三大功能——负载均衡（反向代理+weight权重）</h3><h4>4.1 正向代理与反向代理</h4>要搞清楚什么是负载均衡，我们先要搞清楚什么是反向代理，因为负载均衡是在反向代理的基础上加上weight权重得到的。<br>
<br>正向代理：是指客户端的代理，代表客户端向服务端发出网络请求，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/efd0f235b0082ebbc513efcdd8b57231.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/efd0f235b0082ebbc513efcdd8b57231.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
反向代理：是指服务端的代理，代表服务端向客户端发出响应结果，如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/f8ab2ed94e00e5bcb412fa0d8d6aa09b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/f8ab2ed94e00e5bcb412fa0d8d6aa09b.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
正向代理+反向代理，由客户端代理服务器代表Client客户机向服务端发出网络请求，由服务端代理服务器代表Server服务机向客户端发出响应结果。如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/20fcd953f2db4560ecca2eab71ba5439.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/20fcd953f2db4560ecca2eab71ba5439.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
最最最简单的理解，正向代理和反向代理这个知识是计算机网络中的一个知识，由于当前使用的http网络请求时基于请求-响应模式，服务端开启后被动等待（websocket协议服务端也可以发送消息给客户端），由客户端主动发起网络请求（get请求、post请求），服务端提供结果响应，然后客户端再一次主动发起网络请求，服务端再一次提供结果响应<br>
<br>客户端局域网LAN1中的代理服务器代表客户端主机，我们称之为正向代理，正向代理隐藏了客户端，其存在的意义在于 客户端无法直接访问到服务端，但是 代理服务器可以访问到服务端，所以客户端通过代理服务器来访问到服务端。<br>
<br>服务端局域网LAN2中的代理服务器代表服务端主机，我们称之为反向代理，反向代理隐藏了服务端，一个常见的应用就是服务端的负载均衡，其（即负载均衡）存在的意义在于以合理的方式将请求均分到服务端集群各个服务器，是高并发的必备要素。<br>
<br>反向代理和负载均衡：负载均衡是反向代理的一个应用。<br>
<h4>4.2 Nginx实现反向代理</h4>Nginx是如何实现反向代理的，我们一步步来分析。两个Tomcat服务通过Nginx反向代理，本例子使用三台虚拟机进行测试。<br>
<ul><li>Nginx服务器：192.168.101.3</li><li>tomcat1服务器：192.168.101.5</li><li>tomcat2服务器：192.168.101.6</li></ul><br>
<br>如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/cffabd8c622ff9f81dbe84c3560847a2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/cffabd8c622ff9f81dbe84c3560847a2.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置Nginx——修改Nginx安装目录/conf/nginx.conf（这里是/usr/local/nginx/conf/nginx.conf文件），如下：<br>
<pre class="prettyprint">#user  nobody;<br>
worker_processes  1;<br>
<br>
events &#123;<br>
worker_connections  1024;<br>
&#125;<br>
<br>
http &#123;<br>
include       mime.types;<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
<br>
keepalive_timeout  65;<br>
<h1>配置一个代理即tomcat1服务器</h1>upstream tomcat_server1 &#123;<br>
        server 192.168.101.5:8080;<br>
    &#125;<br>
<h1>配置一个代理即tomcat2服务器</h1>    upstream tomcat_server2 &#123;<br>
        server 192.168.101.6:8080;<br>
    &#125;<br>
<h1>配置一个虚拟主机</h1>    server &#123;<br>
    listen 80;<br>
    server_name aaa.test.com;<br>
    location / &#123;<br>
            #域名aaa.test.com的请求全部转发到tomcat_server1即tomcat1服务上<br>
            proxy_pass http://tomcat_server1;<br>
            #欢迎页面，按照从左到右的顺序查找页面<br>
            index index.jsp index.html index.htm;<br>
    &#125;<br>
<br>
&#125;<br>
<br>
server &#123;<br>
    listen 80;<br>
    server_name bbb.test.com;<br>
<br>
    location / &#123;<br>
             #域名bbb.test.com的请求全部转发到tomcat_server2即tomcat2服务上<br>
              proxy_pass http://tomcat_server2;<br>
              index index.jsp index.html index.htm;<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
server标签里面的location标签，里面有一些常用参数，一个个解释：<br>
<br><strong>4.2.1 proxy_pass参数，请求转发</strong><br>
<br>核心：反向代理最重要的参数 proxy_pass，表示将实际请求全部转发到具体服务上。<br>
<br>Nginx可以实现反向代理的功能，Nginx只做请求的转发，后台有多个http服务器提供服务，Nginx的功能就是把请求转发给后面的服务器，决定把请求转发给谁，Nginx提供算法。<br>
<br><strong>4.2.2 proxy_method参数，定义Nginx的请求方式</strong><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/d34af93850be4e9cb5e34936cd338062.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/d34af93850be4e9cb5e34936cd338062.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
浏览器访问192.168.44.181（这是CentOS地址）/user/query，这个到服务端被Nginx挡住，就是localhost:80，转给192.168.44.1:9096（就是本地IDEA启动的Tomcat，本地IP为192.168.44.1，Tomcat端口为9096）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/ecd8087e5fd064d9feb430b6d584c0b2.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/ecd8087e5fd064d9feb430b6d584c0b2.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/582eabba2a045c7e9b5f91ab3bcb14c9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/582eabba2a045c7e9b5f91ab3bcb14c9.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这个nice就是IDEA上启动的Tomcat返回给浏览器的，@RestController = @Controller + @ResponseBody，所以返回的是字符串。<br>
<br><strong>4.2.3 proxy_set_header参数，取到客户端的网络信息</strong><br>
<br>这里实际上进行了两次请求，浏览器发送请求给Nginx，和Nginx发送请求给本地IDEA上的Tomcat，即：<br>
<br>浏览器发送请求给Nginx：192.168.44.181（这是CentOS地址）/user/query，就是到了CentOS上的localhost:80。<br>
<br>Nginx发送请求给本地IDEA上的Tomcat：CentOS上的localhost:80转发到192.168.44.1:9096就是IDEA启动的Tomcat。<br>
<br>所有的，在IDEA的Tomcat上获得的网络请求信息，都是第二次post请求（Nginx发送给本地IDEA上的Tomcat）的，因为第一次get请求是浏览器发送给Nginx的，要想获得第一次get请求的信息，需要先将Nginx收到的浏览器请求的信息存到自定义的变量名里面，然后Nginx发送给Tomcat，这样Tomcat就可以拿到第一次请求的网络信息了。<br>
<br>proxy_set_header自定义变量名（发给Tomcat） $符号拿到Nginx系统内置变量，就是Nginx存放的，第一次请求发送给Nginx的。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/fd1364178882192858e9cf01dcffec57.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/fd1364178882192858e9cf01dcffec57.png" class="img-polaroid" title="12.png" alt="12.png" referrerpolicy="no-referrer"></a>
</div>
<br>
IDEA上Tomcat取出三个变量值。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/4765e19b7e8177c53ef2d60efbf20a4e.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/4765e19b7e8177c53ef2d60efbf20a4e.png" class="img-polaroid" title="13.png" alt="13.png" referrerpolicy="no-referrer"></a>
</div>
<br>
在反向代理的过程中，既可以获得原始网络信息，也可以获得转发的网络信息。<br>
<br><strong>4.2.4 location参数，不同匹配规则和优先级</strong><br>
<br>location /这个是最常用的，优先级最低的，所有如下表，从上往下，优先级越来越低。如果上面的匹配到，下面的就不会再尝试匹配了。<br>
<br>从上到下是：<br>
<br>精准匹配（url要完全匹配上）、前缀匹配（url只要匹配到前面部分）、区分大小写的正则匹配pattern、不区分大小写的正则匹配pattern、前缀匹配（url只要匹配到前面部分），前面五个都没匹配上，就用/：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/2ddc9b359dfaffe8485db10428292605.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/2ddc9b359dfaffe8485db10428292605.png" class="img-polaroid" title="14.png" alt="14.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>4.3 Nignx实现负载均衡，upstream参数</h4>上面讲过，Nginx实现负载均衡是在反向代理的基础上加上一个weight权重，这里一步步分析。Nginx作为负载均衡服务器，用户请求先到达Nginx，再由Nginx根据负载配置将请求转发至Tomcat服务器。<br>
<ul><li>Nginx负载均衡服务器：192.168.101.3</li><li>tomcat1服务器：192.168.101.5</li><li>tomcat2服务器：192.168.101.55</li><li>tomcat3服务器：192.168.101.6</li><li>tomcat4服务器：192.168.101.66</li></ul><br>
<br>如图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/3ca4f4d2654ee98ce6d2d061cc4486ac.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/3ca4f4d2654ee98ce6d2d061cc4486ac.png" class="img-polaroid" title="15.png" alt="15.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置Nginx——修改Nginx安装目录/conf/nginx.conf（这里是/usr/local/nginx/conf/nginx.conf文件），如下：<br>
<pre class="prettyprint">#user  nobody;<br>
worker_processes  1;<br>
<br>
events &#123;<br>
worker_connections  1024;<br>
&#125;<br>
<br>
http &#123;<br>
include       mime.types;<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
<br>
keepalive_timeout  65;<br>
<h1>配置一个代理即tomcat1服务器</h1>upstream tomcat_server1 &#123;<br>
        server 192.168.101.5:8080   weight=1;<br>
        server 192.168.101.55:8080  weight=2;<br>
<br>
    &#125;<br>
<h1>配置一个代理即tomcat2服务器</h1>    upstream tomcat_server2 &#123;<br>
        server 192.168.101.6:8080  weight=2;<br>
server 192.168.101.66:8080  weight=3;<br>
    &#125;<br>
<h1>配置一个虚拟主机</h1>    server &#123;<br>
    listen 80;<br>
    server_name aaa.test.com;<br>
    location / &#123;<br>
            #域名aaa.test.com的请求全部转发到tomcat_server1即tomcat1服务上<br>
            proxy_pass http://tomcat_server1;<br>
            #欢迎页面，按照从左到右的顺序查找页面<br>
            index index.jsp index.html index.htm;<br>
    &#125;<br>
<br>
&#125;<br>
<br>
server &#123;<br>
    listen 80;<br>
    server_name bbb.test.com;<br>
<br>
    location / &#123;<br>
             #域名bbb.test.com的请求全部转发到tomcat_server2即tomcat2服务上<br>
              proxy_pass http://tomcat_server2;<br>
              index index.jsp index.html index.htm;<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
最后，请求aaa.test.com，通过Nginx负载均衡，将请求转发到Tomcat应用服务器。通过观察Tomcat的访问日志或Tomcat访问页面即可知道当前请求由哪个Tomcat服务器受理。<br>
<br>所以，反向代理可能只有一个目标Tomcat服务器，但是负载均衡一定有不止一个目标Tomcat服务器（Nginx只转发到唯一一个目标Tomcat服务器，就不叫负载均衡了），既然有一个多个目标Tomcat服务器，就 引入一个upstream参数，这是负载均衡最重要的参数。<br>
<br>upstream块里面，每个服务器后面可以配置一些参数。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/9e238db2a2d969f673857f47841b3894.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/9e238db2a2d969f673857f47841b3894.jpg" class="img-polaroid" title="16.jpg" alt="16.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/27256267c84ec13a786ba4b936677136.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/27256267c84ec13a786ba4b936677136.jpg" class="img-polaroid" title="17.jpg" alt="17.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
weight和max_conns区别：tweight使用的是比例，max_conns使用的是具体的最大数量，默认无限制。<br>
<br>max_fails和fail_timeout的联系：这两个参数连在一起用，表示某个server（一般是对应Tomcat）失败次数达到max_fails，那么在fail_timeout的时间内不会转发给这个server（即Tomcat）。<br>
<br>backup备用。<br>
<br>down暂时不用。<br>
<br>对于负载均衡，只要知道它的最重要的upstream参数就好，还有就是Nginx的默认的负载均衡算法和常用的负载均衡算法。<br>
<br>wrr就是权重（就是上面的weight）轮询，这是默认的方式。<br>
<br>ip_hash：每个请求只访问Tomcat，解决跨节点session共享问题，分布式登录的时候用到。<br>
<br>leas_conn：考虑两个因素，连接数小，权重大，则优先，如果上一次刚刚分配，本次不分配。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/7fa6cc64650514cc0e081482a11e5488.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/7fa6cc64650514cc0e081482a11e5488.png" class="img-polaroid" title="18.png" alt="18.png" referrerpolicy="no-referrer"></a>
</div>
<br>
哈希算法的参数如何使用，就是配置好，就upstream块里面server全部生效，默认是wrr weight round robin权重轮询。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/947a49291db8baa5e76f303d50f4fba0.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/947a49291db8baa5e76f303d50f4fba0.png" class="img-polaroid" title="19.png" alt="19.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>4.4 Nginx三大功能一起小结</h4>一图小结——Nginx再也不复杂（http服务器+虚拟主机+负载均衡）：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/bf122590effaf3cebffc643d256b58a4.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/bf122590effaf3cebffc643d256b58a4.png" class="img-polaroid" title="20.png" alt="20.png" referrerpolicy="no-referrer"></a>
</div>
<br>
配置Nginx——修改Nginx安装目录/conf/nginx.conf（这里是/usr/local/nginx/conf/nginx.conf文件），如下：<br>
<pre class="prettyprint">​#user  nobody;<br>
worker_processes  1;<br>
<br>
events &#123;<br>
worker_connections  1024;<br>
&#125;<br>
<br>
http &#123;<br>
include       mime.types;<br>
default_type  application/octet-stream;<br>
<br>
sendfile        on;<br>
<br>
keepalive_timeout  65;<br>
<h1>配置一个代理即tomcat1服务器</h1>upstream tomcat_server1 &#123;<br>
        server 192.168.101.5:8080   weight=1;<br>
        server 192.168.101.55:8080  weight=2;<br>
<br>
    &#125;<br>
<h1>配置一个代理即tomcat2服务器</h1>    upstream tomcat_server2 &#123;<br>
        server 192.168.101.6:8080  weight=2;<br>
server 192.168.101.66:8080  weight=3;<br>
    &#125;<br>
<h1>配置两个虚拟主机</h1>    server &#123;<br>
    listen 80;<br>
    server_name aaa.test.com;<br>
    location / &#123;<br>
            #域名aaa.test.com的请求全部转发到tomcat_server1即tomcat1服务上<br>
            proxy_pass http://tomcat_server1;<br>
            #欢迎页面，按照从左到右的顺序查找页面<br>
            index index.jsp index.html index.htm;<br>
    &#125;<br>
<br>
&#125;<br>
<br>
server &#123;<br>
    listen 80;<br>
    server_name bbb.test.com;<br>
<br>
    location / &#123;<br>
             #域名bbb.test.com的请求全部转发到tomcat_server2即tomcat2服务上<br>
              proxy_pass http://tomcat_server2;<br>
              index index.jsp index.html index.htm;<br>
    &#125;<br>
&#125;<br>
# http服务器<br>
server &#123;<br>
    listen       81; # 监听的端口<br>
    server_name  localhost; # 域名或IP<br>
    location / &#123;      # 访问路径配置<br>
        root   /usr/local/nginx/index;# 根目录<br>
        index  index.html index.htm; # 默认首页<br>
    &#125;<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
看到upstream就一定有proxy_pass，upstream + proxy_pass就是用到了负载均衡。<br>
<br>看到proxy_pass就一定要到反向代理。<br>
<br>看到多个server就将一个服务器虚拟出了多个虚拟主机。<br>
<br>至于静态服务器，只要用到了Nginx就会用它来存放图片等静态资源，无法从conf/nginx.conf中看出来。<br>
<h3>五、实践——Nginx安装使用（以CentOS 7.0为例）</h3>Nginx是C语言开发，本节演示CentOS 7.0上安装Nginx。<br>
<h4>5.1 安装好Nginx</h4>步骤一：安装好相关依赖（GCC、PCRE、Zlib、OpenSSL）<br>
<br><strong>GCC</strong><br>
<br>安装Nginx需要先将官网下载的源码进行编译，编译依赖GCC环境，如果没有GCC环境，需要安装gcc：yum install gcc-c++<br>
<br><strong>PCRE</strong><br>
<br>PCRE（Perl Compatible Regular Expressions）是一个Perl库，包括Perl兼容的正则表达式库。Nginx的http模块使用PCRE来解析正则表达式，所以需要在Linux上安装PCRE库：yum install -y pcre-devel<br>
<br>注：pcre-devel是使用PCRE开发的一个二次开发库，Nginx也需要此库。<br>
<br><strong>Zlib</strong><br>
<br>Zlib库提供了很多种压缩和解压缩的方式，Nginx使用Zlib对http包的内容进行gzip，所以需要在Linux上安装Zlib库：yum install -y zlib zlib-devel<br>
<br><strong>OpenSSL</strong><br>
<br>OpenSSL是一个强大的安全套接字层密码库，囊括主要的密码算法、常用的密钥和证书封装管理功能及SSL协议，并提供丰富的应用程序供测试或其它目的使用。<br>
<br>Nginx不仅支持http协议，还支持https（即在SSL协议上传输http），所以需要在Linux安装OpenSSL库：yum install -y zlib zlib-devel<br>
<br>步骤二：下载Linux版本Nginx压缩包<br>
<br>由于各个用户所需要的Nginx版本不一定相同，所有这里不再提供Nginx安装包，用户在到Nginx官网下载。<br>
<br>（本节使用截止2019/12/01最新nginx-1.16.1.tar.gz安装演示，其他版本安装相同）<br>
<br>步骤三：解压并配置Nginx<br>
<br>解压Nginx：tar -zxvf nginx-1.16.1.tar.gz<br>
<br>配置Nginx。<br>
<br>进入解压目录中：cd nginx-1.16.1.tar.gz<br>
<br>配置Nginx：<br>
<pre class="prettyprint">./configure \<br>
<br>
--prefix=/usr/local/nginx \<br>
<br>
--pid-path=/var/run/nginx/nginx.pid \<br>
<br>
--lock-path=/var/lock/nginx.lock \<br>
<br>
--error-log-path=/var/log/nginx/error.log \<br>
<br>
--http-log-path=/var/log/nginx/access.log \<br>
<br>
--with-http_gzip_static_module \<br>
<br>
--http-client-body-temp-path=/var/temp/nginx/client \<br>
<br>
--http-proxy-temp-path=/var/temp/nginx/proxy \<br>
<br>
--http-fastcgi-temp-path=/var/temp/nginx/fastcgi \<br>
<br>
--http-uwsgi-temp-path=/var/temp/nginx/uwsgi \<br>
<br>
--http-scgi-temp-path=/var/temp/nginx/scgi<br>
</pre><br>
注意：此处将临时文件目录指定为/var/temp/nginx，需要在/var下创建temp及Nginx目录，一定要新建这个目录，否则后面无法启动./nginx。<br>
<br>步骤四：编译安装<br>
<br>编译：继续上面的目录下（即刚才配置Nginx的解压目录下）输入命令 make。<br>
<br>安装：继续上面的目录下（即刚才配置Nginx的解压目录下）输入命令 make install。<br>
<br>步骤五：启动Nginx并访问测试成功<br>
<br>启动Nginx：<br>
<pre class="prettyprint">cd /usr/local/nginx/sbin/<br>
<br>
./nginx<br>
</pre><br>
注意：执行./nginx启动Nginx，这里可以-c指定加载的Nginx配置文件，如下：<br>
<pre class="prettyprint">./nginx -c /usr/local/nginx/conf/nginx.conf<br>
</pre><br>
如果不指定-c，Nginx在启动时默认加载conf/nginx.conf文件，此文件的地址也可以在编译安装Nginx时指定./configure的参数（–conf-path=指向配置文件（nginx.conf））。<br>
<br>查询Nginx进程：ps aux|grep nginx，若查到Nginx进程，则已经启动成功，如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210712/ace726457572525d022bb46964cc33ed.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210712/ace726457572525d022bb46964cc33ed.png" class="img-polaroid" title="21.png" alt="21.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>5.2 相关附加操作</h4><strong>附1：关闭Nginx</strong><br>
<br>方式1，快速停止：<br>
<pre class="prettyprint">cd /usr/local/nginx/sbin<br>
<br>
./nginx -s stop<br>
</pre><br>
此方式相当于先查出Nginx进程ID再使用kill命令强制杀掉进程。<br>
<br>方式2，完整停止（建议使用）：<br>
<pre class="prettyprint">cd /usr/local/nginx/sbin<br>
<br>
./nginx -s quit<br>
</pre><br>
此方式停止步骤是待Nginx进程处理任务完毕进行停止。<br>
<br><strong>附2：重启Nginx</strong><br>
<br>方式1，先停止再启动（建议使用）：<br>
<br>对Nginx进行重启相当于先停止Nginx再启动Nginx，即先执行停止命令再执行启动命令。<br>
<br>如下：<br>
<pre class="prettyprint">./nginx -s quit<br>
<br>
./nginx<br>
</pre><br>
方式2，重新加载配置文件：<br>
<br>当Nginx的配置文件nginx.conf修改后，要想让配置生效需要重启Nginx，使用-s reload不用先停止Nginx再启动Nginx即可将配置信息在Nginx中生效，如下：<br>
<pre class="prettyprint">./nginx -s reload<br>
</pre><br>
<strong>附3：设置开机自启动Nginx（这个建设设置，不用每次启动了）</strong><br>
<br>输入vi /etc/init.d/nginx新建编辑文件（输入下面的代码）：<br>
<pre class="prettyprint">#!/bin/bash<br>
# nginx Startup script for the Nginx HTTP Server<br>
# it is v.0.0.2 version.<br>
# chkconfig: - 85 15<br>
# description: Nginx is a high-performance web and proxy server.<br>
#              It has a lot of features, but it's not for everyone.<br>
# processname: nginx<br>
# pidfile: /var/run/nginx.pid<br>
# config: /usr/local/nginx/conf/nginx.conf<br>
nginxd=/usr/local/nginx/sbin/nginx<br>
nginx_config=/usr/local/nginx/conf/nginx.conf<br>
nginx_pid=/var/run/nginx.pid<br>
RETVAL=0<br>
prog="nginx"<br>
# Source function library.<br>
. /etc/rc.d/init.d/functions<br>
# Source networking configuration.<br>
. /etc/sysconfig/network<br>
# Check that networking is up.<br>
[ $&#123;NETWORKING&#125; = "no" ] && exit 0<br>
[ -x $nginxd ] || exit 0<br>
# Start nginx daemons functions.<br>
start() &#123;<br>
if [ -e $nginx_pid ];then<br>
echo "nginx already running...."<br>
exit 1<br>
fi<br>
echo -n $"Starting $prog: "<br>
daemon $nginxd -c $&#123;nginx_config&#125;<br>
RETVAL=$?<br>
echo<br>
[ $RETVAL = 0 ] && touch /var/lock/subsys/nginx<br>
return $RETVAL<br>
&#125;<br>
# Stop nginx daemons functions.<br>
stop() &#123;<br>
    echo -n $"Stopping $prog: "<br>
    killproc $nginxd<br>
    RETVAL=$?<br>
    echo<br>
    [ $RETVAL = 0 ] && rm -f /var/lock/subsys/nginx /var/run/nginx.pid<br>
&#125;<br>
# reload nginx service functions.<br>
reload() &#123;<br>
echo -n $"Reloading $prog: "<br>
#kill -HUP `cat $&#123;nginx_pid&#125;`<br>
killproc $nginxd -HUP<br>
RETVAL=$?<br>
echo<br>
&#125;<br>
# See how we were called.<br>
case "$1" in<br>
start)<br>
    start<br>
    ;;<br>
stop)<br>
    stop<br>
    ;;<br>
reload)<br>
    reload<br>
    ;;<br>
restart)<br>
    stop<br>
    start<br>
    ;;<br>
status)<br>
    status $prog<br>
    RETVAL=$?<br>
    ;;<br>
*)<br>
    echo $"Usage: $prog &#123;start|stop|restart|reload|status|help&#125;"<br>
    exit 1<br>
esac<br>
exit $RETVAL<br>
</pre><br>
输入：wq保存并退出。<br>
<br>输入chmod a+x /etc/init.d/nginx使vi生效：<br>
<pre class="prettyprint">vi /etc/rc.local<br>
</pre><br>
加入一行/etc/init.d/nginx start保存并退出，下次重启会生效。<br>
<br>成功标志 开机启动后，CentOS 7浏览器上localhost成功（当然最小化安装没有浏览器，桌面安装可以用浏览器看一下）。<br>
<br>若是没有成功还是要到cd /etc/usr/local/nginx/sbin ./nginx启动。<br>
<h3>六、尾声</h3>本文先介绍Nginx三大功能原理图与配置文件，然后介绍CentOS 7上安装使用Nginx，希望对读者有用。<br>
<br>原文链接：<a href="https://blog.csdn.net/qq_36963950/article/details/118629611" rel="nofollow" target="_blank">https://blog.csdn.net/qq_36963 ... 29611</a>，作者：毛奇志
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            
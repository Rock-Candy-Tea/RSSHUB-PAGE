
---
title: '彻底搞懂Nginx的五大应用场景'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/c142568e53d39554b3e35e9ca28806fd.png'
author: Dockone
comments: false
date: 2021-08-03 12:11:05
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/c142568e53d39554b3e35e9ca28806fd.png'
---

<div>   
<br><h3>HTTP服务器</h3>Nginx本身也是一个静态资源的服务器，当只有静态资源的时候，就可以使用Nginx来做服务器，如果一个网站只是静态页面的话，那么就可以通过这种方式来实现部署。<br>
<br>1、首先在文档根目录Docroot（/usr/local/var/www）下创建html目录，然后在html中放一个test.html。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210726/c142568e53d39554b3e35e9ca28806fd.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/c142568e53d39554b3e35e9ca28806fd.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
2、配置nginx.conf中的server。<br>
<pre class="prettyprint">user mengday staff;<br>
<br>
http &#123;<br>
server &#123;<br>
    listen       80;<br>
    server_name  localhost;<br>
    client_max_body_size 1024M;<br>
<br>
    # 默认location<br>
    location / &#123;<br>
        root   /usr/local/var/www/html;<br>
        index  index.html index.htm;<br>
    &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
3、访问测试<br>
<ul><li><a href="http://localhost/" rel="nofollow" target="_blank">http://localhost/</a>指向/usr/local/var/www/index.html, index.html是安装Nginx自带的html</li><li><a href="http://localhost/test.html" rel="nofollow" target="_blank">http://localhost/test.html</a>指向/usr/local/var/www/html/test.html</li></ul><br>
<br>注意：如果访问图片出现403 Forbidden错误，可能是因为nginx.conf的第一行user配置不对，默认是#user nobody;是注释的，Linux下改成user root; macos下改成user用户名所在组，然后重新加载配置文件或者重启，再试一下就可以了， 用户名可以通过who am i命令来查看。<br>
<br>4、指令简介<br>
<ul><li>server：用于定义服务，http中可以有多个server块</li><li>listen：指定服务器侦听请求的IP地址和端口，如果省略地址，服务器将侦听所有地址，如果省略端口，则使用标准端口</li><li>server_name：服务名称，用于配置域名</li><li>location：用于配置映射路径uri对应的配置，一个server中可以有多个location，location后面跟一个uri，可以是一个正则表达式, / 表示匹配任意路径, 当客户端访问的路径满足这个uri时就会执行location块里面的代码</li><li>root：根路径，当访问<a href="http://localhost/test.html" rel="nofollow" target="_blank">http://localhost/test.html</a>，“/test.html”会匹配到”/”uri，找到root为/usr/local/var/www/html，用户访问的资源物理地址=root + uri = /usr/local/var/www/html + /test.html=/usr/local/var/www/html/test.html</li><li>index：设置首页，当只访问server_name时后面不跟任何路径是不走root直接走index指令的；如果访问路径中没有指定具体的文件，则返回index设置的资源，如果访问<a href="http://localhost/html/" rel="nofollow" target="_blank">http://localhost/html/</a> 则默认返回index.html</li></ul><br>
<br>5、location uri正则表达式<br>
<ul><li>.：匹配除换行符以外的任意字符</li><li>?：重复0次或1次</li><li>+* 重复1次或更多次</li><li>*：重复0次或更多次</li><li>\d：匹配数字</li><li>^：匹配字符串的开始</li><li>$：匹配字符串的结束</li><li>&#123;n&#125;：重复n次</li><li>&#123;n,&#125;：重复n次或更多次</li><li>[c]：匹配单个字符c</li><li>[a-z]：匹配a-z小写字母的任意一个</li><li>(a|b|c)：属线表示匹配任意一种情况，每种情况使用竖线分隔，一般使用小括号括括住，匹配符合a字符或是b字符或是c字符的字符串</li><li>\反斜杠：用于转义特殊字符</li></ul><br>
<br>小括号()之间匹配的内容，可以在后面通过$1来引用，$2表示的是前面第二个()里的内容。正则里面容易让人困惑的是\转义特殊字符。<br>
<h3>静态服务器</h3>在公司中经常会遇到静态服务器，通常会提供一个上传的功能，其他应用如果需要静态资源就从该静态服务器中获取。<br>
<br>1、在/usr/local/var/www下分别创建images和img目录，分别在每个目录下放一张test.jpg。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210726/83cb5f6c58b2a21f29a59fa858d6f140.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210726/83cb5f6c58b2a21f29a59fa858d6f140.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<pre class="prettyprint">http &#123;<br>
server &#123;<br>
    listen       80;<br>
    server_name  localhost;<br>
<br>
<br>
    set $doc_root /usr/local/var/www;<br>
<br>
    # 默认location<br>
    location / &#123;<br>
        root   /usr/local/var/www/html;<br>
        index  index.html index.htm;<br>
    &#125;<br>
<br>
    location ^~ /images/ &#123;<br>
        root $doc_root;<br>
   &#125;<br>
<br>
   location ~* \.(gif|jpg|jpeg|png|bmp|ico|swf|css|js)$ &#123;<br>
       root $doc_root/img;<br>
   &#125;<br>
&#125;<br>
&#125; <br>
</pre><br>
自定义变量使用set指令，语法 set 变量名值;引用使用变量名值;引用使用变量名; 这里自定义了doc_root变量。<br>
<br>静态服务器location的映射一般有两种方式：<br>
<ul><li>使用路径，如/images/一般图片都会放在某个图片目录下</li><li>使用后缀，如.jpg、.png等后缀匹配模式</li></ul><br>
<br>访问<a href="http://localhost/test.jpg" rel="nofollow" target="_blank">http://localhost/test.jpg</a>会映射到$doc_root/img<br>
<br>访问<a href="http://localhost/images/test.jpg" rel="nofollow" target="_blank">http://localhost/images/test.jpg</a>，当同一个路径满足多个location时，优先匹配优先级高的location，由于^~ 的优先级大于~，所以会走/images/对应的location。<br>
<br>常见的location路径映射路径有以下几种：<br>
<ul><li>=：进行普通字符精确匹配。也就是完全匹配</li><li>^~：前缀匹配。如果匹配成功，则不再匹配其他location</li><li>~：表示执行一个正则匹配，区分大小写</li><li>~*：表示执行一个正则匹配，不区分大小写</li><li>/xxx/：常规字符串路径匹配</li><li>/：通用匹配，任何请求都会匹配到</li></ul><br>
<br><h4>location优先级</h4>当一个路径匹配多个location时究竟哪个location能匹配到时有优先级顺序的，而优先级的顺序于location值的表达式类型有关，和在配置文件中的先后顺序无关。相同类型的表达式，字符串长的会优先匹配。<br>
<br>以下是按优先级排列说明：<br>
<ul><li>等号类型（=）的优先级最高。一旦匹配成功，则不再查找其他匹配项，停止搜索。</li><li>^~类型表达式，不属于正则表达式。一旦匹配成功，则不再查找其他匹配项，停止搜索。</li><li>正则表达式类型（~ ~*）的优先级次之。如果有多个location的正则能匹配的话，则使用正则表达式最长的那个。</li><li>常规字符串匹配类型。按前缀匹配。</li><li>/ 通用匹配，如果没有匹配到，就匹配通用的</li></ul><br>
<br>优先级搜索问题：不同类型的location映射决定是否继续向下搜索。<br>
<ul><li>等号类型、^~类型：一旦匹配上就停止搜索了，不会再匹配其他location了</li><li>正则表达式类型（~ ~*），常规字符串匹配类型/xxx/：匹配到之后，还会继续搜索其他其它location，直到找到优先级最高的，或者找到第一种情况而停止搜索</li></ul><br>
<br>location优先级从高到底：<br>
<br>（location =）>（location 完整路径）>（location ^~ 路径）>（location ~,~* 正则顺序）>（location 部分起始路径）>（/）<br>
<br><pre class="prettyprint">location = / &#123;<br>
# 精确匹配/，主机名后面不能带任何字符串 /<br>
[ configuration A ]<br>
&#125;<br>
location / &#123;<br>
# 匹配所有以 / 开头的请求。<br>
# 但是如果有更长的同类型的表达式，则选择更长的表达式。<br>
# 如果有正则表达式可以匹配，则优先匹配正则表达式。<br>
[ configuration B ]<br>
&#125;<br>
location /documents/ &#123;<br>
# 匹配所有以 /documents/ 开头的请求，匹配符合以后，还要继续往下搜索。<br>
# 但是如果有更长的同类型的表达式，则选择更长的表达式。<br>
# 如果有正则表达式可以匹配，则优先匹配正则表达式。<br>
[ configuration C ]<br>
&#125;<br>
location ^~ /images/ &#123;<br>
# 匹配所有以 /images/ 开头的表达式，如果匹配成功，则停止匹配查找，停止搜索。<br>
# 所以，即便有符合的正则表达式location，也不会被使用<br>
[ configuration D ]<br>
&#125;<br>
<br>
location ~* \.(gif|jpg|jpeg)$ &#123;<br>
# 匹配所有以gif jpg jpeg结尾的请求。<br>
# 但是 以/images/开头的请求，将使用Configuration D，D具有更高的优先级<br>
[ configuration E ]<br>
&#125;<br>
<br>
location /images/ &#123;<br>
# 字符匹配到/images/，还会继续往下搜索<br>
[ configuration F ]<br>
&#125;<br>
<br>
<br>
location = /test.htm &#123;<br>
root   /usr/local/var/www/htm;<br>
index  index.htm;<br>
&#125; <br>
</pre><br>
注意：location的优先级与location配置的位置无关。<br>
<h3>反向代理</h3>反向代理应该是Nginx使用最多的功能了，反向代理（Reverse Proxy）方式是指以代理服务器来接受internet上的连接请求，然后将请求转发给内部网络上的服务器，并将从服务器上得到的结果返回给internet上请求连接的客户端，此时代理服务器对外就表现为一个反向代理服务器。<br>
<br>简单来说就是真实的服务器不能直接被外部网络访问，所以需要一台代理服务器，而代理服务器能被外部网络访问的同时又跟真实服务器在同一个网络环境，当然也可能是同一台服务器，端口不同而已。<br>
<br>反向代理通过proxy_pass指令来实现。<br>
<br>启动一个Java Web项目，端口号为8081：<br>
<pre class="prettyprint">server &#123;<br>
listen       80;<br>
server_name  localhost;<br>
<br>
location / &#123;<br>
    proxy_pass http://localhost:8081;<br>
    proxy_set_header Host $host:$server_port;<br>
    # 设置用户ip地址<br>
     proxy_set_header X-Forwarded-For $remote_addr;<br>
     # 当请求服务器出错去寻找其他服务器<br>
     proxy_next_upstream error timeout invalid_header http_500 http_502 http_503; <br>
&#125;<br>
<br>
&#125;    <br>
</pre><br>
当我们访问localhost的时候，就相当于访问 localhost:8081了。<br>
<h3>负载均衡</h3>负载均衡也是Nginx常用的一个功能，负载均衡其意思就是分摊到多个操作单元上进行执行，例如Web服务器、FTP服务器、企业关键应用服务器和其它关键任务服务器等，从而共同完成工作任务。简单而言就是当有2台或以上服务器时，根据规则随机的将请求分发到指定的服务器上处理，负载均衡配置一般都需要同时配置反向代理，通过反向代理跳转到负载均衡。而Nginx目前支持自带3种负载均衡策略，还有2种常用的第三方策略。<br>
<br>负载均衡通过upstream指令来实现。<br>
<h4>RR（round robin：轮询 默认）</h4>每个请求按时间顺序逐一分配到不同的后端服务器，也就是说第一次请求分配到第一台服务器上，第二次请求分配到第二台服务器上，如果只有两台服务器，第三次请求继续分配到第一台上，这样循环轮询下去，也就是服务器接收请求的比例是1:1， 如果后端服务器down掉，能自动剔除。轮询是默认配置，不需要太多的配置。<br>
<br>同一个项目分别使用8081和8082端口启动项目：<br>
<pre class="prettyprint">upstream web_servers &#123;  <br>
server localhost:8081;  <br>
server localhost:8082;  <br>
&#125;<br>
<br>
server &#123;<br>
listen       80;<br>
server_name  localhost;<br>
#access_log  logs/host.access.log  main;<br>
<br>
<br>
location / &#123;<br>
    proxy_pass http://web_servers;<br>
    # 必须指定Header Host<br>
    proxy_set_header Host $host:$server_port;<br>
&#125;<br>
&#125; <br>
</pre><br>
访问地址仍然可以获得响应<a href="http://localhost/api/user/login?username=zhangsan&password=111111" rel="nofollow" target="_blank">http://localhost/api/user/logi ... 11111</a>，这种方式是轮询的。<br>
<h4>权重</h4>指定轮询几率，weight和访问比率成正比, 也就是服务器接收请求的比例就是各自配置的weight的比例，用于后端服务器性能不均的情况,比如服务器性能差点就少接收点请求，服务器性能好点就多处理点请求。<br>
<pre class="prettyprint">upstream test &#123;<br>
server localhost:8081 weight=1;<br>
server localhost:8082 weight=3;<br>
server localhost:8083 weight=4 backup;<br>
&#125; <br>
</pre><br>
示例是4次请求只有一次被分配到8081上，其他3次分配到8082上。backup是指热备，只有当8081和8082都宕机的情况下才走8083。<br>
<h4>ip_hash</h4>上面的2种方式都有一个问题，那就是下一个请求来的时候请求可能分发到另外一个服务器，当我们的程序不是无状态的时候（采用了session保存数据），这时候就有一个很大的很问题了，比如把登录信息保存到了session中，那么跳转到另外一台服务器的时候就需要重新登录了，所以很多时候我们需要一个客户只访问一个服务器，那么就需要用iphash了，iphash的每个请求按访问ip的hash结果分配，这样每个访客固定访问一个后端服务器，可以解决session的问题。<br>
<pre class="prettyprint">upstream test &#123;<br>
ip_hash;<br>
server localhost:8080;<br>
server localhost:8081;<br>
&#125; <br>
</pre><br>
<h4>fair（第三方）</h4>按后端服务器的响应时间来分配请求，响应时间短的优先分配。这个配置是为了更快的给用户响应。<br>
<pre class="prettyprint">upstream backend &#123;<br>
fair;<br>
server localhost:8080;<br>
server localhost:8081;<br>
&#125; <br>
</pre><br>
<h4>url_hash（第三方）</h4>按访问url的hash结果来分配请求，使每个url定向到同一个后端服务器，后端服务器为缓存时比较有效。 在upstream中加入hash语句，server语句中不能写入weight等其他的参数，hash_method是使用的hash算法。<br>
<pre class="prettyprint">upstream backend &#123;<br>
hash $request_uri;<br>
hash_method crc32;<br>
server localhost:8080;<br>
server localhost:8081;<br>
&#125; <br>
</pre><br>
以上5种负载均衡各自适用不同情况下使用，所以可以根据实际情况选择使用哪种策略模式,不过fair和url_hash需要安装第三方模块才能使用。<br>
<h3>动静分离</h3>动静分离是让动态网站里的动态网页根据一定规则把不变的资源和经常变的资源区分开来，动静资源做好了拆分以后，我们就可以根据静态资源的特点将其做缓存操作，这就是网站静态化处理的核心思路。<br>
<pre class="prettyprint">upstream web_servers &#123;  <br>
   server localhost:8081;  <br>
   server localhost:8082;  <br>
&#125;<br>
<br>
server &#123;<br>
listen       80;<br>
server_name  localhost;<br>
<br>
set $doc_root /usr/local/var/www;<br>
<br>
location ~* \.(gif|jpg|jpeg|png|bmp|ico|swf|css|js)$ &#123;<br>
   root $doc_root/img;<br>
&#125;<br>
<br>
location / &#123;<br>
    proxy_pass http://web_servers;<br>
    # 必须指定Header Host<br>
    proxy_set_header Host $host:$server_port;<br>
&#125;<br>
<br>
error_page 500 502 503 504  /50x.html;  <br>
location = /50x.html &#123;  <br>
    root $doc_root;<br>
&#125;<br>
<br>
&#125; <br>
</pre><br>
<h3>其他</h3><h4>return指令</h4>返回http状态码和可选的第二个参数可以是重定向的URL：<br>
<pre class="prettyprint">location /permanently/moved/url &#123;<br>
return 301 http://www.example.com/moved/here;<br>
&#125; <br>
</pre><br>
<h4>rewrite指令</h4>重写URI请求rewrite，通过使用rewrite指令在请求处理期间多次修改请求URI，该指令具有一个可选参数和两个必需参数。第一个（必需）参数是请求URI必须匹配的正则表达式。第二个参数是用于替换匹配URI的URI。可选的第三个参数是可以停止进一步重写指令的处理或发送重定向（代码301或302）的标志。<br>
<pre class="prettyprint">location /users/ &#123;<br>
rewrite ^/users/(.*)$ /show?user=$1 break;<br>
&#125; <br>
</pre><br>
<h4>error_page指令</h4>使用error_page指令，你可以配置Nginx返回自定义页面以及错误代码，替换响应中的其他错误代码，或将浏览器重定向到其他URI。在以下示例中，error_page指令指定要返回404页面错误代码的页面（/404.html）。<br>
<pre class="prettyprint">error_page 404 /404.html;<br>
</pre><br>
<h4>日志</h4>访问日志：需要开启压缩gzip on，否则不生成日志文件，打开log_format、access_log注释：<br>
<pre class="prettyprint">log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '<br>
                  '$status $body_bytes_sent "$http_referer" '<br>
                  '"$http_user_agent" "$http_x_forwarded_for"';<br>
<br>
access_log  /usr/local/etc/nginx/logs/host.access.log  main;<br>
<br>
gzip  on;<br>
</pre><br>
<h4>deny指令</h4><pre class="prettyprint"># 禁止访问某个目录<br>
location ~* \.(txt|doc)$&#123;<br>
root $doc_root;<br>
deny all;<br>
&#125;    <br>
</pre><br>
<h4>内置变量</h4>Nginx的配置文件中可以使用的内置变量以美元符$开始，也有人叫全局变量。其中，部分预定义的变量的值是可以改变的。<br>
<ul><li>$args：#这个变量等于请求行中的参数，同$query_string</li><li>$content_length：请求头中的Content-length字段。</li><li>$content_type：请求头中的Content-Type字段。</li><li>$document_root：当前请求在root指令中指定的值。</li><li>$host：请求主机头字段，否则为服务器名称。</li><li>$http_user_agent：客户端agent信息</li><li>$http_cookie：客户端cookie信息</li><li>$limit_rate：这个变量可以限制连接速率。</li><li>$request_method：客户端请求的动作，通常为GET或POST。</li><li>$remote_addr：客户端的IP地址。</li><li>$remote_port：客户端的端口。</li><li>$remote_user：已经经过Auth Basic Module验证的用户名。</li><li>$request_filename：当前请求的文件路径，由root或alias指令与URI请求生成。</li><li>$scheme：HTTP方法（如http，https）。</li><li>$server_protocol：请求使用的协议，通常是HTTP/1.0或HTTP/1.1。</li><li>$server_addr：服务器地址，在完成一次系统调用后可以确定这个值。</li><li>$server_name：服务器名称。</li><li>$server_port：请求到达服务器的端口号。</li><li>$request_uri：包含请求参数的原始URI，不包含主机名，如：”/foo/bar.php?arg=baz”。</li><li>$uri：不带请求参数的当前URI，$uri不包含主机名，如”/foo/bar.html”。</li><li>$document_uri：与$uri相同</li></ul><br>
<br>原文链接：<a href="https://blog.csdn.net/vbirdbest/article/details/80913319" rel="nofollow" target="_blank">https://blog.csdn.net/vbirdbes ... 13319</a>，作者：vbirdbest
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                    </ul>
                                                              
</div>
            
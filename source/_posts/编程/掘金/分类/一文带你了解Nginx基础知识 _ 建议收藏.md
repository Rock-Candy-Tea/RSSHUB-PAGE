
---
title: '一文带你了解Nginx基础知识 _ 建议收藏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6485'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 17:23:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=6485'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 概述</h2>
<p>很多人可能或多或少了解过<code>nginx</code>，即使没有使用过<code>nginx</code>，但是可能用<code>Apache</code>搭建过简单的<code>web</code>服务器，用<code>tomcat</code>写过一些简单的动态页面，其实这些功能nginx都可以实现。</p>
<p><code>nginx</code>最重要的三个使用场景个人认为是<code>静态资源服务</code>、<code>反向代理服务</code>和<code>api服务</code>。</p>
<p><code>web</code>请求走进服务以后会先经过<code>nginx</code>再到应用服务，然后再去访问<code>redis</code>或者<code>mysql</code>提供基本的数据功能。</p>
<p>这就有个问题，应用服务因为要求开发效率高，所以他的运行效率是很低的，他的<code>qbs</code>，<code>tps</code>并发都是受限的，所以就需要把很多的应用服务组成集群，向用户提供高可用性。</p>
<p>很多服务构成集群的时候，需要<code>nginx</code>具有反向代理的功能，可以把动态请求传导给对应的应用服务。服务集群一定会带来两个需求，动态的扩容和容灾。</p>
<p>反向代理必须具备负载均衡的功能，其次在链路中，<code>nginx</code>是处在企业内网的边缘节点，随着网络链路的增长，用户体验到的时延会增加。</p>
<p>把一些所有用户看起来不变的，或者在一段时间内看起来不变的动态内容缓存在<code>nginx</code>部分，由<code>nginx</code>直接向用户提供访问，用户的时延就会减少很多。</p>
<p>反向代理衍生出另外的功能叫缓存，他能够加速访问，而很多时候在访问像<code>css</code>或<code>js</code>文件又或者一些小图片是没有必要由应用服务来访问的，他只需要直接由<code>nginx</code>提供访问就可以了这就是<code>nginx</code>的静态资源功能。</p>
<p>应用服务它本身的性能有很大的问题，数据库服务要比应用服务好的多，原因是数据库他的业务场景比较简单，并发性能和<code>tps</code>都要远高于应用服务。由<code>nginx</code>直接去访问数据库或者<code>redis</code>也是不错的选择。</p>
<p>还可以利用<code>nginx</code>强大的并发性能，实现如<code>web</code>防火墙的一些业务功能，这就要求<code>nginx</code>服务有非常强大的业务处理功能，<code>openResty</code>和<code>nginx</code>集成了一些工具库来实现此功能。</p>
<h2 data-id="heading-1">2. 历史背景</h2>
<p>全球化和物联网的快速发展，导致接入互联网中的人与设备的数量都在快速的上升，数据的快速爆炸，对硬件性能提出很高的要求。</p>
<p>摩尔定律表明之前服务跑在<code>1GHZ</code>的<code>CPU</code>上的服务更新到<code>2GHZ</code>的<code>CPU</code>时服务会有两倍的性能提升。</p>
<p>但是到了本世纪初，摩尔定律在单颗<code>CPU</code>的频率上已经失效了，<code>CPU</code>开始向着多核方向发展，当服务器现在是跑在<code>8</code>核<code>CPU</code>上时，一年半以后换到了<code>16</code>核的<code>CPU</code>，服务的性能通常是不会有一倍的提升的。</p>
<p>这些性能主要损耗在操作系统和大量的软件没有做好服务于多核架构的准备，比如说像<code>Apache</code>是低效的，因为他的架构模型里一个进程同一时间，只会处理一个连接，一个请求。只有在这个请求处理完以后才会去处理下一个请求。</p>
<p>它实际上在使用操作系统的进程间切换的特性，因为操作系统微观上是有限的<code>CPU</code>，但是操作系统被设计为同时服务于数百甚至上千的进程。</p>
<p><code>Apache</code>一个进程只能服务于一个连接，这种模式会导致当<code>Apache</code>需要面对几十万，几百万连接的时候，他没有办法去开几百万的进程，而进程间切换的代价成本又太高啦。</p>
<p>当并发的连接数越多，这种无谓的进程间切换引发的性能消耗又会越大。</p>
<p><code>nginx</code>是专门为了这种应用场景而生的，可以处理数百万甚至上千万的并发连接，<code>nginx</code>目前在<code>web</code>市场份额中排行第二，在过去几年他增长极度迅速，在不久的将来<code>nginx</code>在<code>web</code>端的应用将远远超过其他服务器。</p>
<h2 data-id="heading-2">3. nginx的优点</h2>
<p>大部分的程序和服务器随着并发连接数的上升他的<code>RPS</code>数会急剧的下降，这里的原理就像之前所说过的，他的设计架构是有问题的。</p>
<p><code>nginx</code>的第一个优点就是高并发和高性能同时具备的，往往高并发只需要对每一个连接所使用的内存尽量的少就可以达到。</p>
<p>而具有高并发的同时达到高性能，往往需要非常好的设计，那<code>nginx</code>可以达到什么样的标准呢？</p>
<p>比如说现在主流的一些服务器<code>32</code>核<code>64G</code>的内存可以轻松达到数千万的并发链接，如果是处理一些简单的静态资源请求，可以达到一百万的<code>RPS</code>这种级别。</p>
<p>其次<code>nginx</code>的可扩展性非常好，主要在于他的模块化设计非常的稳定，而且<code>nginx</code>的第三方模块的生态圈非常的丰富。甚至于有像<code>TNG</code>,<code>openRestry</code>这种第三方插件。丰富的生态圈为<code>nginx</code>丰富的功能提供了保证。</p>
<p>第三个优点是它的高可靠性，所谓的高可靠性是指<code>nginx</code>可以在服务器上持续不间断的运行数年，而很多<code>web</code>服务器往往运行几周或者几个月就需要做一次重启。</p>
<p>对于<code>nginx</code>这种高并发高性能的反向代理服务器而言，他往往运行在企业内网的边缘节点上，如果企业想提供<code>4个9</code>，<code>5个9</code>，甚至更高的高可用性时，对于<code>nginx</code>持续运行能够<code>down</code>机的时间一年可能只能以秒来计。所以在这种角色中，<code>nginx</code>的高可靠性给提供了非常好的保证。</p>
<p>第四个优点热部署，是指可以在不停止服务的情况下升级<code>nginx</code>，这对于<code>nginx</code>来说非常的重要，因为在<code>nginx</code>可能跑了数百万的并发连接。</p>
<p>如果是普通的服务可能只需<code>kill</code>掉进程再重启的方式就可以处理好，但是对于<code>nginx</code>而言，因为<code>kill</code>掉<code>nginx</code>进程，会导致操作系统为所有的已经建立连接的客户端发送一个<code>tcp</code>中的<code>reset</code>报文。而很多客户端是没有办法很好的处理请求的。</p>
<p>在大并发场景下，一些偶然事件就会导致必然的恶性结果，所以热部署是非常有必要的。</p>
<p>第五个优点是<code>BSD</code>许可证，<code>BSD Listens</code>是指<code>nginx</code>不仅是开源的免费的，而且可以在有定制需要的场景下，去修改<code>nginx</code>源代码，再运行在商业场景下，这是合法的。</p>
<p>以上的优点是<code>nginx</code>最核心的特性。</p>
<h2 data-id="heading-3">4. 主要组成部分</h2>
<p>首先是<code>nginx</code>的可执行文件，它是由<code>nginx</code>自身的框架、官方模块以及各种第三方模块共同构建的文件。他有完整的系统，所有的功能都由他提供。</p>
<p>第二个部分是<code>nginx.conf</code>配置文件，类似于骑车的驾驶员，虽然可执行文件已经提供了许多功能，但这些功能有没有开启，或者开启了以后定义了怎样的行为处理请求，都是由<code>nginx.conf</code>配置文件决定的。</p>
<p><code>nginx</code>的第三个组成部分叫做<code>access.log</code>访问日志，<code>access.log</code>会记录下每一条<code>nginx</code>处理过的<code>http</code>请求信息与响应信息。</p>
<p>第四个组成部分是<code>error.log</code>错误日志，当出现了一些不可预期的问题时，可以通过<code>error.log</code>去把问题定位出来。</p>
<p>这四个部分是相辅相成的。</p>
<p><code>nginx</code>的可执行文件和<code>nginx.conf</code>定义了处理请求的方式。如果想对web服务，做一些运营或者运维的分析，需要对<code>access.log</code>做进一步的分析。如果出现了任何未知的错误，或者与预期的行为不一致时，应该通过<code>error.log</code>去定位根本性的问题。</p>
<h2 data-id="heading-4">5. 版本规则</h2>
<p><code>nginx</code>每发布一个版本的时候会有三个特性，一个是<code>feature</code>，就是他新增了哪些功能，<code>bugfix</code>表示他修复了哪些<code>bug</code>，<code>change</code>表示做了哪些重构。</p>
<p>每一个版本都有<code>mainline</code>主干版本和<code>stable</code>稳定版本。</p>
<p>在<code>nginx</code>的官网点击右下角的<code>download</code>，就可以看到版本号列表，单数版本表示主干版本，会新增很多功能，但不一定稳定。双数版本是稳定版本。</p>
<p><code>CHANGES</code>文件中可以看到每一个版本含有的新增功能，修复的<code>bug</code>，以及做了哪些小的重构。</p>
<p>大概在<code>2009</code>年以后<code>nginx</code>的<code>bugfix</code>数量已经大幅度减少，所以<code>nginx</code>相对已经很稳定了。</p>
<p><code>nginx</code>的开发时间是在<code>2002</code>年，但是他在<code>2004</code>年<code>10</code>月<code>4</code>日推出了第一个版本，在<code>2005年</code>曾经做过一次大的重构。</p>
<p>因为<code>nginx</code>优秀的设计，使得他的生态圈极为丰富，模块的设计，架构的设计都没有再做过大的变动。</p>
<p>在<code>2009</code>年<code>nginx</code>开始支持<code>windows</code>操作系统，<code>2011</code>年<code>1.0</code>正式版本发布，同时<code>nginx</code>的商业公司<code>nginx Plus</code>也成立了，在<code>2015</code>年<code>nginx</code>发布了几个重要的功能。</p>
<p>其中提供<code>stream</code>，<code>四层反向代理</code>，他在功能上完全可以替代传统使用的<code>LVS</code>, 并且具有更丰富的功能。</p>
<h2 data-id="heading-5">6. 版本选择</h2>
<p>免费开源: <code>nginx.org</code></p>
<p>商业版本: <code>nginx.com</code></p>
<p>开源免费的<code>nginx</code>在<code>2002</code>年开始开发，到<code>2004</code>年发布第一个版本，<code>2011</code>年开源版的<code>nginx</code>发布了<code>1.0</code>稳定版，同年<code>nginx</code>的作者成立了一家商业公司，开始推出<code>nginx Plus</code>商业版的<code>nginx</code>。</p>
<p>商业版的<code>nginx</code>在整合第三方模块上还有运营监控以及技术支持上有很多优点，但他有个最大的缺点就是不开源，所以通常在国内会使用<code>nginx.org</code>开源版的。</p>
<p>阿里巴巴也推出了<code>Tengine</code>版本，<code>Tengine</code>的优点就是在阿里巴巴生态下他经历了非常严苛的考验，<code>Tengine</code>之所以会存在也是因为他的很多特性领先于<code>nginx</code>的官方版本。</p>
<p>所以<code>Tengine</code>实际上是修改了<code>nginx</code>官网版本的主干代码，当然框架被修改以后<code>Tengine</code>就遇到了一个明显的问题，没有办法跟着<code>nginx</code>的官方版本同步的升级。<code>Tengine</code>也可以使用<code>nginx</code>的第三方模块。</p>
<p><code>OpenResty</code>的作者章亦春在阿里巴巴的时候开发了<code>Lua</code>语言版本的<code>openResty</code>，因为<code>nginx</code>的第三方模块开发的难度相当大，章亦春把<code>nginx</code>非阻塞事件的一种框架以<code>Lua</code>语言的方式提供给了广大开发者。</p>
<p><code>OenRestry</code>兼具了高性能，以及开发效率高的特点，<code>OpenResty</code>同样有开源版和商业版，目前多使用<code>openresty.org</code>站点下的开源版本。商业版<code>OpenRestry</code>的主要特点是技术支持相对比较好很多。</p>
<p>如果你没有太多的业务诉求，那么使用开源版的<code>nginx</code>就足够了，如果你需要开发<code>Api</code>服务器，或者需要开发<code>web</code>防火墙，<code>openrestry</code>是一个很好的选择。</p>
<h2 data-id="heading-6">7. 编译配置</h2>
<p>安装<code>nginx</code>有两种方法，除了编译外，还可以直接用操作系统上自带的一些工具，比如说<code>yum</code>，<code>apt-get</code>，直接去安装<code>nginx</code>。</p>
<p>但是直接安装<code>nginx</code>有个问题，就是<code>nginx</code>的二进制文件不会把模块直接编译进来，毕竟<code>nginx</code>的官方模块，并不是每一个默认都会开启的。</p>
<p>如果想添加第三方的<code>nginx</code>模块，就必须通过编译<code>nginx</code>的方式。</p>
<p>编译<code>nginx</code>主要分为六个部分，首先需要下载<code>nginx</code>，从<code>nginx.org</code>网站上直接下载就可以。</p>
<p>打开<code>nginx.org</code>在页面中找到右下角<code>donwload</code>，选择<code>Stable</code>版本的下来链接，右键复制链接地址即可，进入到<code>Linux</code>中使用<code>wget</code>进行下载</p>
<pre><code class="hljs language-s copyable" lang="s">cd  /home/nginx
wget http://nginx.org/download/nginx-1.18.0.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载完<code>nginx</code>压缩包以后首先解压压缩包。</p>
<pre><code class="hljs language-s copyable" lang="s">tar -xzf nginx-1.18.0.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着进入解压后的目录通过<code>ll</code>命令查看所有文件。</p>
<pre><code class="hljs language-s copyable" lang="s">cd nginx-1.18.0
ll
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一个目录叫<code>auto</code>目录。</p>
<pre><code class="hljs language-s copyable" lang="s">cd auto
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>auto</code>目录里面有四个子目录，<code>cc</code>是用于编译的，<code>lib</code>库和对操作系统的判断在<code>os</code>里面，其他所有的文件都是为了辅助<code>config</code>脚本执行的时候判定<code>nginx</code>支持哪些模块以及当前的操作系统有什么样的特性可以供给<code>nginx</code>使用。</p>
<p><code>CHANGES文</code>件标记了<code>nginx</code>每一个版本中提供了哪些特性和<code>bugfix</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">cat ../CHANGES
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中会有<code>feature</code>，<code>bugfix</code>，<code>change</code>三种特性在里面。</p>
<p><code>CHANGES.ru</code>文件是俄罗斯语言的<code>CHANGES</code>文件，可能因为作者是个俄罗斯人。</p>
<p><code>conf</code>文件是一个示例文件，就是把<code>nginx</code>安装好以后，为了方便运维配置，会把<code>config</code>里面的示例文件<code>copy</code>到安装目录。</p>
<p><code>configure</code>脚本用来生成中间文件，执行编译前的一个一些配置，也就是记录编译前的设定信息，编译时使用。</p>
<p><code>contrib</code>目录提供了两个脚本和<code>vim</code>工具，也就是让<code>vim</code>打开<code>config</code>配置文件时支持代码高亮。</p>
<p>把<code>contrib</code>目录下<code>vim</code>的所有文件<code>copy</code>到自己的目录中</p>
<pre><code class="hljs language-s copyable" lang="s">cp -r contrib/vim/* ~/.vim/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就可以把<code>nginx</code>语言的语法高亮显示在<code>vim中</code>了。</p>
<p><code>html</code>目录里面提供了两个标准的<code>HTML</code>文件，一个是发现<code>500</code>错误的时候可以重定向到的文件，另一个是默认的<code>nginx</code>的欢迎界面<code>index.html</code>。</p>
<p><code>man</code>文件里则是<code>Linux</code>对<code>nginx</code>的帮助文件，里面标识了最基本的<code>nginx</code>帮助和配置。</p>
<p><code>src</code>目录是<code>nginx</code>的核心源码。</p>
<h2 data-id="heading-7">8. 开始编译</h2>
<p>编译前可以先看一下<code>configure</code>支持哪些参数。</p>
<pre><code class="hljs language-s copyable" lang="s">./configure --help | more
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先就是确定<code>nginx</code>执行中会去找哪些目录下的文件作为辅助文件。比如用动态模块时<code>--modules-path</code>就会产生作用。<code>--lock-path</code>确定<code>nginx.lock</code>文件放在哪里等。</p>
<p>如果没有任何变动的话只需要指定<code>--prefix=PATH</code>就可以了，设定一个安装目录。</p>
<p>第二类参数主要是用来确定使用哪些模块和不使用哪些模块的，前缀通常是<code>--with</code>和<code>--without</code>。</p>
<p>比如说-<code>-with-http_ssl_module</code>或者<code>--with-http_v2_module</code>通常需要主动加<code>--with</code>的时候，意味着模块默认是不会编译进<code>nginx</code>的。</p>
<p>而模块中显示<code>--without</code>比如说<code>--without-http_charset_module</code>意味着默认他会编译进<code>nginx</code>中，加了参数是把他移除默认的<code>nginx</code>的模块中。</p>
<p>第三类参数中指定<code>nginx</code>编译需要的一些特殊的参数，比如说用<code>cc</code>编译的时候需要加一些什么样的优化参数，或者说要打印<code>debug</code>级别的日志(<code>--with-debug</code>)以及需要加一些第三方的模块(<code>--with-zlib-asm=CPU</code>)</p>
<p>这里指定的<code>nginx</code>的安装目录是在<code>/home/nginx</code>目录下。</p>
<pre><code class="hljs language-s copyable" lang="s">./configure --prefix=/home/nginx/nginx/
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有任何报错<code>nginx</code>就已经编译成功了，所有<code>nginx</code>的配置特性以及<code>nginx</code>运行时的目录都会列在最下方。</p>
<p>在<code>config</code>执行完之后，会看到生成了一些中间文件。中间文件会放在<code>objs</code>文件夹下。最重要的是会生成一个文件叫做<code>ngx_modules.c</code>他决定了接下来执行编译时哪些模块会被编译进<code>nginx</code>。可以打开看一下所有被编译进<code>nginx</code>的模块都会列在这里，他们最后会形成一个叫做<code>ngx_modules</code>的数组。</p>
<p>执行<code>make</code>编译。</p>
<pre><code class="hljs language-s copyable" lang="s">make
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译完成以后如果没有任何错误，就可以看见生成了大量的中间文件，以及最终的<code>nginx</code>二进制文件。</p>
<pre><code class="hljs language-s copyable" lang="s">cd objs/
ll
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后进行<code>make install</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装完成之后在<code>--prefix</code>指定的安装目录中可以看到很多目录，<code>nginx</code>的执行文件就在<code>sbin</code>目录下。</p>
<p>决定<code>nginx</code>功能的配置文件在<code>conf</code>下，<code>access.log</code>和<code>error.log</code>在<code>log</code>文件夹下。</p>
<p>可以看到在<code>conf</code>目录下所有文件就是在源代码中<code>conf</code>目录copy过来的，其中的内容也是完全相同的。</p>
<h2 data-id="heading-8">9. 配置语法</h2>
<p><code>nginx</code>可执行文件中已经指定了他包含了哪些模块，但每一个模块都会提供独一无二的配置语法。</p>
<p>这些所有的配置语法，会遵循同样的语法规则。</p>
<p><code>nginx</code>的配置文件是一个<code>ascii</code>的文本文件，主要有两部分组成，<code>指令</code>和<code>指令快</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">http &#123;
    include mime.types;
    upstream thwp &#123;
        server 127.0.0.1:8000;
    &#125;

    server &#123;
        listen 443 http2;
        # nginx配置语法
        limit_req_zone $binary_remote_addr zone=one:10 rate=1r/s;
        location ~* \.(gif|jpg|jpeg)$ &#123;
            proxy_cache my_cache;
            expires 3m;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面<code>http</code>就是一个指令快，<code>include mime.types;</code>就是一条指令。</p>
<p>每条指令以分号结尾，指令和参数间以空格分隔。<code>include mime.types;</code>中<code>include</code>是一个指令名，<code>mime.types</code>是参数中间可以用一个或多个空格分隔。参数可以有多个，比如下面的<code>limit_req_zone</code>有三个参数，多个参数之间也是用空格分隔。</p>
<p>两条指令间是以<code>;</code>作为分隔符的，两条指令放在一行中写也是没有问题的。只不过可读性会变得很差。</p>
<p>第三个指令块是以 <code>&#123;&#125;</code> 组成的，他会将多条指令组织到一起，比如<code>upstream</code>，他把一条指令<code>server</code>放在了<code>thwp</code>指令块下面。</p>
<p><code>server</code>中也放置了<code>listen</code>，<code>limit_req_zone</code>这些指令，他也可以包含其他的指令块，比如说<code>location</code>。</p>
<p>有些指令可以有名字，比如<code>upstream</code>，后面有个<code>thwp</code>作为他的名字。</p>
<p>具体什么样的指令有名字什么样的指令没有名字是由提供指令块的<code>nginx</code>模块来决定的，他也可以决定指令块后面有一个或者说多个参数，或者说没有参数。</p>
<p><code>include</code>语句允许引入多个配置文件以提升可维护性。在例子<code>中mime.types</code>文件中其实里面是含有很多条不同的文件的后缀名与<code>http</code>协议中<code>mime</code>格式的对照关系表。</p>
<p><code>include</code>是导入其他配置模块的意思。</p>
<p><code>#</code>符号可以添加注释，提升可读性，比如在listen后面加了一个<code>nginx</code>配置语法的注释，以描述下面一些配置的表达。</p>
<p>使用<code>$</code>符号可以使用变量，可以看下<code>limit_req_zone</code>这里用了一个参数叫做<code>$binary_remote_addr</code>，这是一个变量描述的是远端的地址。</p>
<p>部分指令的参数是支持正则表达式的，比如<code>location</code>后面可以看到，他可以支持非常复杂的正则表达式，而且可以把正则表达式括号里的内容通过<code>$1</code>,<code>$2</code>,<code>$3</code>的方式取出来。</p>
<p>在<code>nginx</code>的配置文件中当涉及到时间的时候，还有许多表达方式，比如下面的方式:</p>
<pre><code class="hljs language-s copyable" lang="s">ms -> 毫秒
s  -> 秒
m  -> 分钟
h  -> 小时
d  -> 天
w  -> 周
M  -> 月
y  -> 年
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如<code>location</code>中的<code>expires 3m;</code>就表示<code>3分钟</code>后希望<code>cache</code>刷新。</p>
<p>空间也是有单位的，当后面不加任何后缀名时表示字节<code>bytes</code>，加了<code>k</code>或者<code>K</code>表示千字节，<code>m</code>表示兆字节，<code>g</code>表示<code>G</code>字节。</p>
<p><code>http</code>大括号里面所有的指令都是由<code>http</code>模块去解析和执行的，非<code>http</code>模块，比如说像<code>stream</code>或<code>mime</code>是没有办法去解析指令的。</p>
<p><code>upstream</code>表示上游服务，当<code>nginx</code>需要与<code>Tomcat</code>等企业内网的其它服务交互的时候呢，可以定义一个<code>upstream</code>。</p>
<p><code>server</code>对应的一个或一组域名，<code>location</code>是<code>url</code>表达式。</p>
<h2 data-id="heading-9">10. 重载，热部署，日志切割</h2>
<p>需要帮助的时候可以用<code>-?</code> 或者 <code>-h</code>获取帮助信息。</p>
<pre><code class="hljs language-s copyable" lang="s">nginx -?
nginx -h
<span class="copy-code-btn">复制代码</span></code></pre>
<p>默认情况下编译出来的<code>nginx</code>会寻找执行<code>configure</code>命令时指定的配置文件。在命令行中可以指定另一个配置文件用<code>-c 路径</code>。</p>
<p>还能指定一些配置用<code>-g</code>，指令就是在<code>nginx</code>的<code>configure</code>目录里的指令。</p>
<p><code>nginx</code>操作运行中的进程一般是通过发送信号，可以通过<code>linux</code>的<code>kill</code>命令也可以用<code>nginx -s</code>子命令，子命令后可以用<code>stop</code>，<code>quit</code>，<code>reload</code>，<code>reopen</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">nginx -s stop # 停止nginx服务
nginx -s quit # 优雅的停止nginx服务
nginx -s reload # 重载配置文件
nginx -s reopen # 重新开始记录日志文件。
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>-t</code>可以测试一下配置文件是否合法问题。</p>
<p><code>-V</code>是在编译时用<code>configure</code>脚本执行所加的所有参数。</p>
<h3 data-id="heading-10">1. 重载配置文件</h3>
<p>修改<code>nginx</code>配置文件中的一些值，比如说<code>conf/nginx.conf</code>文件中，打开<code>tcp_nopush</code>。</p>
<p>当修改完配置文件以后，可以直接执行<code>nginx -s reload</code>命令<code>nginx</code>是在不停止对客户服务的情况下使用了<code>tcp_nopush</code>新的配置项，非常的简单。</p>
<h3 data-id="heading-11">2. 热部署</h3>
<p><code>nginx</code>在运行的情况下想更换最新版本的<code>nginx</code>，根据之前所说的，<code>nginx</code>编译方法下载一个新的<code>nginx</code>。</p>
<p>把最新版本的<code>nginx</code>编译后的可执行文件<code>nginx</code>，<code>copy</code>到目录中替换掉正在运行的<code>nginx</code>文件。<code>copy</code>完成需要给正在运行的<code>nginx</code>的<code>master</code>进程发送一个信号，告诉他开始进行热部署做一次版本升级，给<code>nginx</code>的<code>master</code>进程发送一个信号，<code>USR2</code>信号。</p>
<pre><code class="hljs language-s copyable" lang="s">kill -USR2 进程号(13195)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>nginx</code>会新启一个<code>master</code>进程使用的正式刚刚复制过来的最新的<code>nginx</code>二进制文件。</p>
<p>旧的<code>worker</code>也在运行，新的master会生成新的<code>worker</code>，他们会平滑的把所有的请求过渡到新的进程中。</p>
<p>新的请求新的连接会进入新的<code>nginx</code>进程中，这时需要向老的<code>nginx</code>进程发送一个信号叫做<code>WINCH</code>，告诉他优雅的关闭所有进程。</p>
<pre><code class="hljs language-s copyable" lang="s">kill -WINCH 13195
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时老的<code>worker</code>进程会优雅的退出，但是老的<code>master</code>进程还在，只是是没有<code>worker</code>进程了。</p>
<p>这说明所有的请求已经全部切换到新的<code>nginx</code>中了，如果需要把新版本退回到老版本，可以向老的进程发送<code>reload</code>命令，让他重新把<code>worker</code>进程拉起来。再把新版本关掉。所以保留<code>master</code>是为了允许做版本回退。</p>
<h3 data-id="heading-12">3. 日志切割</h3>
<p>比如说当前的日志已经很大了。需要把以前的日志备份到另外一个文件中，但是<code>nginx</code>还是正常运行的。</p>
<p>这就要通过<code>reopen</code>命令来做，首先需要把当前正在使用的日志<code>copy</code>一份放在另外的位置.</p>
<pre><code class="hljs language-s copyable" lang="s">mv access_log bak.log
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着执行命令<code>reopen</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">nginx -s reopen
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就重新生成了一个<code>access.log</code>, 原本的<code>log</code>备份成了<code>bak.log</code>,就实现了日志切割。</p>
<p>当然这种方法会非常不好用，实际上往往是每一天，或者是每一周执行一次日至切割，可以先写成一个<code>bash</code>脚本。</p>
<p>在<code>bash</code>脚本中首先把文件复制一下，再执行-<code>s reopen</code>命令，最后把脚本放在<code>crontab</code>中。</p>
<h2 data-id="heading-13">11. 静态资源Web服务器</h2>
<p>编辑<code>conf/nginx.conf</code>文件找到<code>server</code>代码块中，<code>listen</code>配置监听端<code>8080</code>端口，然后需要配置一个<code>location</code>，使用<code>/</code>让所有的请求都访问到<code>www</code>文件夹。</p>
<p>这里需要指定<code>url</code>的后缀与文件的后缀一一对应，有两种用法，<code>root</code>和<code>alias</code>，<code>root</code>是系统的跟目录，所以通常使用<code>alias</code>，<code>alias</code>是<code>nginx</code>的安装目录。</p>
<pre><code class="hljs language-s copyable" lang="s">server &#123;
    listen 8080;
    ...
    location / &#123;
        alias www/;
        ...
    &#125;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>做完配置之后启动<code>nginx</code>在浏览器中访问<code>localhost:8080</code>就可以了。</p>
<pre><code class="hljs language-s copyable" lang="s">nginx -s reload
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">1. 开启gzip</h3>
<p>做完<code>gzip</code>压缩传输的字节数会大幅度减少，所以通常会打开<code>gzip</code>。</p>
<p>首先打开<code>nginx.conf</code>文件，找到<code>http</code>代码块中的<code>gzip</code>相关选项，打开<code>gzip(off -> on)</code>, <code>gzip_min_length</code>是小于多少字节不再执行压缩，因为小于一定的字节<code>http</code>传输直接就可以发送了，压缩反而消耗<code>cpu</code>性能，<code>gzip_comp_level</code>代表压缩级别，<code>gzip_types</code>是针对某些类型的文件才做<code>gzip</code>压缩。</p>
<pre><code class="hljs language-s copyable" lang="s">http &#123;
    ...
    gzip on;
    gzip_min_length 1;
    gzip_comp_level 2;
    gzip_types text/plain applicaton/x-javascript text/css image/png;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置好后重启<code>nginx</code>, 浏览器中查看就会发现，传输的文件已经减少了很多，响应头中多出了<code>Content-encoding: gzip</code>。使用<code>gzip</code>以后整个<code>web</code>服务传输效率会高很多。</p>
<h3 data-id="heading-15">2. 打开目录结构</h3>
<p><code>nginx</code>给提供了一个官方模块叫做<code>autoindex</code>，他可以提供当访问以<code>/</code>结尾的<code>url</code>时，显示目录的结构。使用方法也特别简单，就是<code>autoindex on</code>加入一个指令就可以了。</p>
<pre><code class="hljs language-s copyable" lang="s">location / &#123;
    autoindex on;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>他会把所访问的文件夹内所有文件列出来，当打开一个目录时，可以继续显示目录中的文件，这是一个很好的静态资源帮助功能。</p>
<h3 data-id="heading-16">3. 网速限制</h3>
<p>比如公网带宽是有限的，当有很多并发用户使用带宽时，他们会形成一个争抢关系，可以让用户访问某些大文件的时候来限制他的速度，节省足够的带宽给用户访问一些必要的小文件。</p>
<p>就可以使用<code>set</code>命令，配合一些内置的变量实现这种功能，比如说加上<code>set $limit_rate 1k</code>，限制<code>nginx</code>向客户浏览器发送响应的一个速度。意思是每秒传输多少数据到浏览器中。</p>
<pre><code class="hljs language-s copyable" lang="s">location / &#123;
    set $limit_rate 1k;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">4. 日志</h3>
<p>首先需要设置<code>access</code>日志格式，找到一个指令叫做<code>log_format</code>, 他用来定义日志的格式，这里可以使用变量。</p>
<pre><code class="hljs language-s copyable" lang="s">http &#123;
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
    '$status $body_bytes_sent "$http_referer" '
    '"$http_user_agent" "$http_x_forwarded_for"';
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>$remote_addr</code>为远端的地址，也就是浏览器客户端的<code>ip</code>地址，<code>$time_local</code>表示当时的时间。<code>$status</code>是返回的状态码。格式定义好之后需要定义一个名字，这里是<code>main</code>。</p>
<p>不同的名字可以对不同的域名下，做不同格式的日志记录，或者对不同的<code>url</code>记录不同日志格式。</p>
<p>配置好<code>log_format</code>之后，就可以用<code>access_log</code>指令，配置日志了。<code>access_log</code>所在的代码块决定了日志的位置比如<code>access_log</code>这里放在了<code>server</code>下，也就是所有请求这个路径和端口的请求日志，都会记录到<code>logs/yindong.log</code>文件中，使用的格式就是<code>main</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">server &#123;
    listen 8080;
    access_log logs/yindong.log main;
    location / &#123;
        alias dlib;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置好<code>yindong.log</code>后，所有的请求在完成之后都会记录下一条日志，可以进入logs/yindong.log中查看每一条都是设置的格式。</p>
<h2 data-id="heading-18">12. 反向代理服务</h2>
<p>由于上游服务要处理非常复杂的业务逻辑而且强调开发效率，所以他的性能并不怎么样，使用<code>nginx</code>作为反向代理以后，可以由一台<code>nginx</code>把请求按照负载均衡算法代理分配给多台上游服务器工作。</p>
<p>这就实现了水平扩展的可能，在用户无感知的情况下，添加更多的上游服务器，来提升处理性能，而当上游服务器出现问题的时候，<code>nginx</code>可以自动的把请求从有问题的服务器，转交给正常的服务器。</p>
<p>反向代理需要添加一个<code>upstream</code>，就是上游服务<code>server</code>，访问地址是<code>127.0.0.1:8080</code>如果有很多台上游服务可以依次的放在这里。</p>
<p><code>upstream</code>设置的一批服务叫<code>local</code>。对所有的请求使用<code>proxy_pass</code>一条指令，代理到local里。</p>
<pre><code class="hljs language-s copyable" lang="s">upstream local&#123;
    server 127.0.0.1:8080;
&#125;
server &#123;
    server_name yindong.com;
    listen 80;
    location / &#123;
        proxy_set_header Host $host;
        proxt_set_header X-Real_IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        # 反向代理转发
        proxy_pass http://local;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为反向代理的原因，真实的服务器拿到的信息是经过<code>nginx</code>代理服务器转发的，所以很多信息都不是真实的，比如说<code>域名</code>，<code>ip</code>都是代理服务器发送过来的，所以需要在<code>location</code>中做一些配置处理。</p>
<p>通过<code>proxy_set_header</code>可以把有一些值添加一条新的<code>header</code>发送到上游，比如说叫<code>x-real-ip</code>，然后把他的值设为从<code>tcp</code>链接里面拿到的远端<code>ip</code>地址。</p>
<p><code>$host</code>也是同样的因为用户直接访问的域名，是他在浏览器输入的，既可以让他在上游服务器可以处理域名，也可以由反向代理来处理。</p>
<p>所有这些配置特性都可以在官网中的<code>http_proxy_module</code>找到。</p>
<h3 data-id="heading-19">1. 缓存</h3>
<p>这里有个很重要的特性<code>proxy_cache</code>, 因为当<code>nginx</code>作为反向代理时，通常只有动态的请求，也就是不同的用户访问同一个<code>url</code>看到的内容是不同的，才会交由上游服务处理。</p>
<p>但是有一些内容可能是一段时间不会发生变化的，为了减轻上游服务器的压力，就会让<code>nginx</code>把上游服务返回的内容缓存一段时间，比如缓存一天，在一天之内即使上游服务器对内容的响应发生了变化，也不管，只会去拿缓存住的这段内容向浏览器做出响应。</p>
<p>因为<code>nginx</code>的性能远远领先于上游服务器的性能。所以使用一个特性后，对一些小的站点会有非常大的性能提升。</p>
<p>配置缓存服务器首先要去通过p<code>roxy_cache_path</code>这条指令去设置缓存文件写在哪个目录下。</p>
<p>比如这里是<code>/tmp/nginxcache</code>, 以及这些文件的命名方式，这些文件的关键词<code>key</code>,要放在共享内存中的。这里开了<code>10MB</code>的共享内存，命名为<code>my_cache</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">proxy_cache_patj /tmp/nginxcache levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_temp_path_off;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缓存的使用方法就是在需要做缓存的<code>url</code>路径下，添加<code>proxy_cache</code>, 后面所跟的参数就是刚刚开辟的那个共享内存，在共享内存中所设置的<code>key</code>就是同一个<code>url</code>访问时对不同的用户可能展示的东西是不一样的，所以用户这个变量就要放在<code>key</code>中。</p>
<p>这里做一个非常简单的<code>key</code>，比如说访问的<code>host url</code>可能加了一些参数，这些参数可能已经指明了是哪个用户哪个资源，<code>$host$uri$is_args$args;</code> 这些作为一个整体的<code>key</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">location / &#123;
    proxy_cache my_cache;
    proxy_cache_key $host$uri$is_args$args;
    proxy_cache_valid 200 304 302 1d;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>加完这些参数以后，可以尝试停掉上游服务，然后访问站点，可以发现站点仍然是可以访问的。就是因为被缓存了。</p>
<h2 data-id="heading-20">13. 监控access日志</h2>
<p><code>Access</code>日志记录了<code>nginx</code>非常重要的信息，可以用日志来分析定位问题，也可以用它来分析用户的运营数据，但是如果想实时分析<code>Access.log</code>相对来说还比较困难。</p>
<p>有一款工具叫<code>GoAccess</code>可以以图形化的方式，通过<code>websocket</code>协议实时的把<code>Access.log</code>的变迁反应到浏览器中，方便分析问题。</p>
<p><code>GoAccess</code>的站点是 <code>https://goaccess.io</code>, 以一种非常友好的图形化方式显示。</p>
<p><code>GoAccess</code>使用<code>-o</code>参数生成新的<code>html</code>文件，把当前<code>access.log</code>文件中的内容以html图表的方式展示出来，当<code>access.log</code>变迁的时候<code>GoAccess</code>会新起一个socket进程，通过端口的方式把新的<code>access.log</code>推送到客户端。</p>
<pre><code class="hljs language-s copyable" lang="s">goaccess access.log -o report.html --log-format=COMBINED
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先制定<code>access.log</code>程序制定的位置(<code>yindong.log</code>), 把它输出到<code>../html/report.html</code>文件中，使用的是<code>--real-time-html</code>就是实时更新页面的方式，时间格式<code>--time-format='%H:%M:%S'</code>, 日期格式<code>--date-format='%d/%b/%Y'</code>, 以及日志格式<code>--log-format=COMBINED</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">cd logs
goaccess yindong.log -o ../html/report.html --real-time-html --time-format='%H:%M:%S' --date-format='%d/%b/%Y' --log-format=COMBINED
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>GoAccess</code>的安装可以用<code>yum</code>或者<code>wget</code>，也可以下载源码进行编译。</p>
<p>启动完成之后可以看到一条<code>log</code>叫做<code> WebSocket server ready to accept new client connections</code>, 也就是他已经打开了一个新的<code>websocket</code>监口，当访问<code>report.html</code>的时候，会向进程发起连接, 由进程给推送最新的<code>log</code>变更。</p>
<p>接下来还要在<code>nginx.conf</code>中添加<code>location</code>，当访问<code>/report.html</code>时候用<code>alias</code>重定向到<code>report.html</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">server &#123;
    ...
    location /report.html &#123;
        alias /usr/local/openresty/nginx/html/report.html;
    &#125;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打开<code>localhost:8080/report.html</code>就可以看到效果了。</p>
<p>使用<code>GoAccess.log</code>可以非常直观的看到<code>access.lo</code>g统计信息上的变迁，对分析网站的运营情况非常有帮助，可以看到每个时间点，每一周每一天，甚至不同的国家地区使用不同浏览器和操作系统的人使用站点的一个比例和分布。</p>
<h2 data-id="heading-21">14. SSL安全协议</h2>
<p><code>SSL</code>的全称是<code>Secure Sockets Layer</code>，现在很多时候使用的是<code>TLS</code>也就是<code>Transport Layer Security</code>。可以将<code>TLS</code>看做是<code>SSL</code>的升级版。</p>
<p><code>SSL</code>是网景公司在<code>1995</code>年推出的，后来因为微软把自己的<code>IE浏览器</code>捆绑<code>windows</code>一起卖出导致网景遇到很大的发展困境，网景把<code>SSL</code>协议交给<code>IETF</code>组织。</p>
<p>在<code>1999</code>年，应微软的要求<code>IETF</code>把<code>SSL</code>更名为<code>TLS1.0</code>，在<code>06</code>，<code>08</code>到<code>2018</code>年<code>TLS</code>分别发布了<code>1.1</code>，<code>1.2</code>和<code>1.3</code>协议。</p>
<p>那么<code>TLS</code>协议究竟是怎样保证<code>http</code>的明文消息被加密的呢？</p>
<p>在<code>ISO/OSI</code>七层模型中，应用层是<code>http</code>协议，在应用层之下，表示层也就是<code>TLS</code>所发挥作用的这一层，通过<code>握手</code>，<code>交换密钥</code>，<code>告警</code>，<code>对称加密</code>的方式使<code>http</code>层没有感知的情况下做到了数据的安全加密。</p>
<p>当抓包或者观察服务端配置时，可以看到安全密码的配置，安全密码的配置决定了<code>TLS</code>协议是怎样保证明文被加密的。这里大概有四个组成部分。</p>
<p>第一个组成部分叫做密钥交换，也就是<code>ECDHE</code>，这实际上是一个椭圆曲线加密算法的表达，密钥交换是为了让浏览器和服务器之间怎样各自独立的生成密钥，数据传输时他们会用密钥去加密数据。加解密是需要使用到对方的密钥的所以需要进行交换。</p>
<p>在密钥交换过程中，需要让浏览器和服务器各自去验证对方的身份，而验证身份是需要一个算法的，叫做<code>RSA</code>。</p>
<p>进行数据加密，解密这种通讯的时候，需要用到对称加密算法<code>AES_128——GCM</code>，其中第一个部分<code>AES</code>表达了是怎样一种算法，<code>128</code>表示了<code>AES</code>算法里支持了<code>3</code>种加密强度，使用<code>128</code>位这种一个加密强度。<code>AES</code>中有很多分组模式<code>GCM</code>是一种比较新的分组模式，可以提高多核<code>CPU</code>情况下加密和解密的一个性能。</p>
<p><code>SHA_256</code>是摘要算法，他用来把不定长度的字符串生成固定长度的更短的摘要。</p>
<h2 data-id="heading-22">15. 对称加密、非对称加密</h2>
<p>在对称加密场景中，两个想通讯的人张三和李四，他们共同持有同一把密钥，张三可以把原始明文的文档，通过这一把密钥加密生成一个密文文档，而李四拿到文档以后呢，他可以用这把密钥还原转换为原始的明文文档，而中间的任何人如果没有持有这把密钥，即使他知道了对称加密的算法他也没有办法把密文还原成原始文档。</p>
<p>那么对称加密究竟的实现可以以<code>RC4</code>对称加密的序列算法来描述。</p>
<p>使用异或(<code>xor</code>)操作, 他是一个位操作，比如<code>1</code>和<code>0</code>进行异或得到<code>1</code>，<code>0</code>和<code>1</code>也得到了<code>1</code>，那么相同的<code>1</code>和<code>1</code>或者<code>0</code>和<code>0</code>进行异或操作都会得到<code>0</code>。</p>
<p>在一个场景下<code>1010</code>是共同持有的密钥，<code>0110</code>是明文，张三执行加密的时候就会得到密文<code>1100</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">1 0 1 0 # 密钥
  xor   # 异或操作
0 1 1 0 # 明文
  | |    # 输出
1 1 0 0 # 密文
<span class="copy-code-btn">复制代码</span></code></pre>
<p>异或有一个对称的特性，就是把密文与密钥同样的做异或操作可以得到明文。</p>
<pre><code class="hljs language-s copyable" lang="s">1 0 1 0 # 密钥
  xor   # 异或操作
1 1 0 0 # 密文
  | |    # 输出
0 1 1 0 # 明文
<span class="copy-code-btn">复制代码</span></code></pre>
<p>密文可以用同一把密钥完全还原成了明文，所以对称加密有一个最大的优点就是他的性能非常的好，他只要遍历一次就可以得到最终的密文，解密的过程也是一样，而非对称加密他的性能就会差很多。</p>
<p>非对称加密根据一个数学原理，他会生成一对密钥，这一对密钥中如果称其中一个叫做公开钥匙(<code>公钥</code>)，那么另一个就叫做私有钥匙(<code>私钥</code>)。</p>
<p>公钥和私钥作用就是同一份命名文档如果用公钥加密了那么只有用对应的私钥才能把它解密，同样道理，如果文档用私钥加密了用公钥才能解密。</p>
<p>比如说李四他有一对公钥和私钥，那么他就可以把他的公钥发布给大家，比如张三是其中的一个人，他拿到了李四的公钥，加密操作是怎么做的呢？</p>
<p>张三如果想传递一份原始文档给李四，那么张三就可以拿着李四的公钥对原始文档进行加密，把密文再发送给李四，李四用自己的私钥才能进行解密，其他人即使得到了这份文档也没有办法进行解密。</p>
<pre><code class="hljs language-s copyable" lang="s"> ----------                ----------                  ----------  
|  ------  |  李四的公钥    |  ------  |   李四的私钥     |  ------ | 
|  ------  | -----------> |  -- 密 -- |  ----------->  |  ------ |
|  ------  |    加密       |  ------  |     解密        |  ------ |
 ----------                ----------                  ----------
   原始文档                    加密文档                     原始文档 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>公钥和私钥还有第二种用途，就是身份验证，比如现在有一段信息李四用它的私钥进行了加密，然后把密文发给了张三，只要张三如果可以使用李四的公钥解开这份文档，那么就证明这段密文确实是由李四发出的。因为只有李四有自己的加密私钥，如果是王五加密的文档张三用李四的公钥是解不开的，只有用李四私钥加密的使用李四的公钥才能解开。</p>
<h2 data-id="heading-23">16. SSL证书的公信力</h2>
<p>这里其实还有个问题，李四怎么就知道消息真的是张三发过来的。这里面涉及到一个新的概念叫公信机构。在多方通信的过程中必须有一个公信机构CA，负责颁发证书和把证书过期的。</p>
<p>作为站点的维护者就是证书的订阅人，首先必须申请一个证书，申请证书可能需要登记是谁，属于什么组织，想做什么。</p>
<p>登记机构通过<code>CSR</code>发给<code>CA</code>，<code>CA</code>中心通过后会生成一对公钥和私钥，公钥在<code>CA</code>保存着，公钥私钥证书订阅人拿到之后就会把它部署到自己的<code>web</code>服务器，当浏览器访问站点的时候，服务器会把公钥证书发给浏览器，浏览器需要向<code>CA</code>验证证书是否合法和有效的。如果有效就证明没有被篡改。</p>
<p>由于<code>CA</code>会把过期的证书放在<code>CRL</code>服务器里，服务器会把所有过期的证书形成一条链条所以他的性能非常的差，后来又推出了<code>OCSP</code>程序可以就一个证书去查询是否过期，所以浏览器是可以直接去查询<code>OCSP</code>响应程序的，但<code>OCSP</code>响应程序性能还不是很高。</p>
<p>nginx会有一个<code>OCSP</code>的开关，当打开开关以后会由<code>nginx</code>主动的去<code>OCSP</code>去查询，大量的客户端直接从<code>nginx</code>就可以获取到证书是否有效。</p>
<p>证书一共有<code>3</code>种类型。</p>
<p>第一种叫做域名验证<code>DV</code>证书，也就是说证书只会去验证域名的归属是否正确，申请证书的时候只要域名指向的服务器是正在申请证书的服务器，就可以成功的申请到证书。</p>
<p>第二种证书叫做组织验证<code>OV</code>证书，组织验证就是在申请证书的时候会去验证填写的机构，企业名称是否是正确的，申请<code>OV</code>证书往往需要几天的时间，不像<code>DV</code>证书，基本上实时就可以获取到，<code>OV</code>证书的价格远远高于<code>DV</code>证书，<code>DV</code>证书很多都是免费的。</p>
<p>比<code>OV</code>证书做更严格的是<code>EV</code>证书，大部分浏览器对<code>EV</code>证书显示的非常友好，他会把证书申请时所填写的机构名称在浏览器的地址栏中显示出来。</p>
<p>浏览器在安全角度对<code>DV</code>，<code>OV</code>,，<code>EV</code>证书他的效果是一样的。唯一验证的就是证书链。</p>
<p>如果你点击网站地址栏中的锁头标志，打开证书链的时候，可以发现存在三个级别，目前所有主证书都是由根证书、二级证书、主证书三个证书构成的。</p>
<p>之所以需要三级机构是因为根证书的验证是非常谨慎的，如<code>windows</code>，安卓等操作系统每一年以上才会去更新一次根证书库，所以一个新的根证书<code>CA</code>机构是很难快速的加入到操作系统或者浏览器中的。</p>
<p>大部分浏览器他使用的是操作系统的证书库，只有像<code>firefox</code>这种浏览器会维护自己的根证书库，所以浏览器在验证证书是否有效时，除了验证有没有过期以外，最主要就是在验证根证书是不是有效的，是不是被跟证书库所认可的。</p>
<p><code>nginx</code>在向浏览器发送证书的时候需要发送两个证书，根证书是被操作系统或者浏览器内置的并不需要发送。首先发送站点的主证书，接着会发送二级证书，浏览器会自动去认证二级证书的签发机构，根证书是不是有效的。</p>
<p>浏览器和服务器之间通信时确认对方是信赖的人其实就是验证给站点颁发根证书的发行者是不是有效的。</p>
<h2 data-id="heading-24">17. SSL协议握手时nginx的性能瓶颈</h2>
<p>TLS的通信过程主要想完成四个目的。</p>
<h3 data-id="heading-25">1. 验证对方身份</h3>
<p>浏览器会向服务器发送一个<code>client hello</code>消息。有一浏览器非常多样化，而且版本在不停的变更。所以不同的浏览器所支持的安全套件，加密算法都是不同的。这一步主要是告诉服务器，浏览器支持哪些加密算法。</p>
<h3 data-id="heading-26">2. 对安全套件达成共识</h3>
<p><code>nginx</code>有自己能够支持的加密算法列表，以及他倾向于使用的哪一个加密算法套件，<code>nginx</code>会选择一套他最喜欢的加密套件发送给客户端。</p>
<p>如果想复用<code>session</code>，也就是说<code>nginx</code>打开了<code>session cache</code>，希望在一天内断开链接的客户端不用再次协商密钥，可以直接去复用之前的密钥。</p>
<p><code>server hello</code>信息中主要会发送究竟选择哪一个安全套件。</p>
<h3 data-id="heading-27">3. 传递并生成密钥</h3>
<p><code>nginx</code>会把自己的公钥证书发送给浏览器，公钥证书中包含证书链，浏览器可以找到自己的根证书库，去验证证书是否是有效。</p>
<h3 data-id="heading-28">4. 对数据进行加密通讯</h3>
<p>服务器会发送<code>server hello done</code>，如果之前协商的安全套件是椭圆曲线算法，这时会把椭圆曲线的参数发送给客户端。客户端需要根据椭圆曲线的公共参数，生成自己的私钥后再把公钥发送给服务器。</p>
<p>服务器有了自己的私钥，会把公钥发送给客户端，服务端可以根据自己的私钥和客户端的私钥，共同生成双方加密的密钥。</p>
<p>客户端根据服务器发来的公钥和他自己的私钥也可以生成一个密钥。</p>
<p>服务器和客户端各自生成的密钥是相同的，是由非对称加密算法保证的。接着可以用生成的密钥进行数据加密，进行通信。</p>
<p><code>TLS</code>通信主要在做两件事，第一个是交换密钥，第二个是加密数据，主要的性能消耗也是这两点。</p>
<p>nginx在这里是有性能优化的，主要是他的算法性能，对于小文件，握手是影响<code>QPS</code>性能的主要指标，对于大文件而言，主要考虑对称加密算法的性能比如<code>AES</code>，对称加密算法虽然性能很好，但是对非常大的一个文件，测吞吐量时还是<code>AES</code>的性能比较好的。</p>
<p>当以小文件为主时主要考验的是<code>nginx</code>的非对称加密的性能，比如说<code>RSA</code>，当主要处理大文件时主要考验的是对称加密算法的性能，比如说<code>AES</code>。</p>
<p>面对的场景是小文件比较多时重点应该优化椭圆曲线算法的一些密码强度，看是不是有所降低，当主要面对大的文件处理的时候需要考虑<code>AES</code>算法是不是可以替换为更有效的算法，或者把密码强度调得更小一些。</p>
<h2 data-id="heading-29">18. 用免费SSL证书实现一个HTTPS站点</h2>
<p>首先需要有一个域名比如说<code>yindong.zhiqianduan.com</code>他是一个<code>http</code>的网址。</p>
<p>接着开始安装工具，必须的工具。</p>
<p>如果系统是<code>CentOS</code>，可以使用<code>yum</code>安装，优班图系统可以使用<code>wget</code>工具下载。</p>
<pre><code class="hljs language-s copyable" lang="s">yum install pthon2-certbot-nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装好会提供<code>certbot</code>命令，当后缀加上<code>--nginx</code>的时候就开始为<code>nginx</code>的<code>conf</code>自动执行相应的修改。通常他会默认修改<code>/usr/local/</code>目录下的<code>nginx</code>配置。可以通过<code>--nginx-server-root</code>指定<code>nginx.conf</code>所在的路径。</p>
<p>使用<code>-d</code>指定需要申请证书的域名，比如说<code>yindong.zhiqianduan.com</code>。</p>
<pre><code class="hljs language-s copyable" lang="s">certbot --nginx --nginx-server-root=/usr/local/nginx/conf/ -d yindong.zhiqianduan.com
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先他会去获取一个证书，接着会等待验证，然后把证书部署到<code>nginx.conf</code>文件中。最后提示两个选择，第一不要做任何的重定向，第二做重定向。重定向就是将<code>http</code>的访问<code>302</code>到<code>https</code>从而禁掉不安全的<code>http</code>访问。</p>
<p>选择之后就可以使用<code>https</code>访问<code>yindong.zhiqianduan.com</code>域名了。<code>https://yindong.zhiqianduan.com</code></p>
<p>他是在在<code>server</code>指令块中增加了<code>443</code>端口，让后将公钥证书和私钥证书部署好，并把一些通用的参数通过<code>include</code>加入到配置文件中。</p>
<p>因为<code>ssl</code>中最消耗性能是的握手，所以为了降低握手增加了<code>sessin_cache</code>, 设置<code>1m</code>，可以为大约<code>4000</code>个链接建立服务。也就是说每个<code>http</code>链接握手建立第一次以后如果断开了再次链接，那么在<code>session_timeout</code>时间以内是不用进行再次握手的。可以复用之前的密钥，<code>session_timeout</code>设置了<code>1440m</code>，也就是一天。</p>
<p><code>ssl_protocols</code>表示<code>https</code>支持哪些版本的<code>TLS</code>协议，<code>ssl_prefer_server_ciphers</code>表示<code>nginx</code>开始决定使用哪些协议与浏览器进行通信，他是通过<code>ssl_ciphers</code>中的安全套件，所有的安全套件以分号分隔，是有顺序的，排在前面的会优先被使用。</p>
<p>最后<code>server</code>中的<code>ssl_dhparam</code>是表示加密的时候使用怎样的参数，这些参数会决定网络安全的加密强度。</p>
<h2 data-id="heading-30">19. 基于OpenResty用Lua语言实现简单服务</h2>
<p>在<code>openresty</code>的站点(openresty.org)下载，在源码发布中找到最新版本，复制他的下载链接进行下载。</p>
<pre><code class="hljs language-s copyable" lang="s">wget http://openresty.org/download/openresty-1.13.6.2.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载完成以后解压压缩包，然后进入到源代码目录，可以发现<code>openresty</code>目录和<code>nginx</code>的源代码目录相比少了很多东西，少的这些东西都在<code>bundle</code>目录下，<code>build</code>目录是编译以后生成的一些中间目标文件。</p>
<p>在<code>bundle</code>目录中有很多模块，最核心的是<code>nginx</code>的源代码，也就说当前的<code>OpenResty</code>是基于对应的<code>nginx</code>版本进行的二次开发。</p>
<p>所有<code>nginx</code>对应版本中没有的特性都不可能出现在<code>OpenResty</code>的版本中。</p>
<p>其他的目录又分为两类，第一类是<code>nginx</code>的第三方模块，都是一些<code>C</code>模块，通常会以<code>ngx</code>开头。第二类模块是<code>LUA</code>模块，是<code>lua</code>代码写就的，他需要使用刚刚那些<code>C</code>模块提供的各种功能，在编译的时候主要是在编译<code>C</code>模块。</p>
<pre><code class="hljs language-s copyable" lang="s">./configure --help | more
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过帮助文件可以看到<code>OpenResty</code>和<code>nginx</code>基本没有太大的不同，只不过<code>OpenResty</code>他集成了很多第三方模块，比如<code>http_echo</code>, <code>http_xss</code>等等，这些在<code>nginx</code>的官方版本中是没有的。这些模块很多是<code>OpenResty</code>的作者写的。</p>
<p>最核心的<code>lua_module</code>核心模块通常是不能移除来的，移除来之后整个<code>lua</code>就不能运行了。其他的配置项和官方的<code>nginx</code>基本上是一样的。</p>
<pre><code class="hljs language-s copyable" lang="s">./configure

make install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要将<code>lua</code>代码添加到<code>OpenResty</code>当中首先打开<code>OpenResty</code>的<code>conf</code>文件，在文件中是可以直接添加<code>lua</code>代码的，但是不能直接的把<code>lua</code>的语法放在<code>conf</code>中，因为<code>nginx</code>的解析器配置语法和<code>lua</code>代码是不相同的。</p>
<p>在<code>OpenResty</code>的<code>nginx_lua_module</code>中提供了几条指令，其中有一条叫做<code>content_by_lua</code>, 是在<code>http</code>请求处理的内容生成阶段用<code>lua</code>代码来处理。</p>
<p>增加一个<code>location</code>，当输入<code>/lua</code>的时候，使用<code>lua</code>代码进行处理, 为了使输出的文本能够以浏览器直接显示文本的方式显示，添加一个<code>default_type text/html</code>，在<code>content_by_lua</code>中加一些最简单的命令来演示lua是怎么生效的。</p>
<p>在<code>OpenResty</code>的<code>lua</code>模块中提供了一些<code>API</code>，比如说<code>ngx.say</code>会生成<code>http</code>响应，他是放在<code>http</code>请求的<code>body</code>中的，并不是放在<code>header</code>中的。</p>
<p>可以通过<code>ngx.say</code>语法将内容添加到<code>body</code>中的文本中。这里通过<code>ngx.req.get_headers</code>把用户请求时的<code>http</code>头取出来，然后找出<code>UA</code>，把值返回给浏览器。</p>
<pre><code class="hljs language-s copyable" lang="s">
server &#123;
    server_name yindong.com;
    listen 80;

    location /lua &#123;
        default_type text/html;
        content_by_lua 'ngx.say("User-Agent: ", ngx.req.get_headers()["User-Agent"])';
    &#125;

    location / &#123;
        alias html/yindong/;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问<code>/lua</code>就可以看到效果了。</p>
<p>通过<code>OpenResty</code>的<code>nginx_lua_http</code>模块可以用它提供的<code>API</code>完成很多功能，可以用<code>lua</code>语言本身的一些工具库，把<code>lua</code>语言添加进来参与响应的过程。</p>
<p>可以用<code>lua</code>语言以及相应的提供的工具库直接访问<code>redis</code>，<code>mysql</code>或者<code>tomcat</code>等服务，然后把不同的响应通过程序逻辑组合成相应的内容返回给用户。</p></div>  
</div>
            